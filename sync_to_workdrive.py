#!/usr/bin/env python3
"""
Sync changed Markdown files from a Git push to a single (flat) Zoho WorkDrive folder.

Behaviour
---------
* Diffs the push's before/after commits, so only what changed is touched.
* New / modified .md files are uploaded to WORKDRIVE_ROOT_FOLDER_ID.
* Uses `override-name-exist=true`, so an existing filename is replaced in place
  (same file id, shared links stay valid) rather than duplicated.
* MIRROR_DELETES=true: files removed in Git are moved to WorkDrive Trash
  (status 61 -> recoverable from Trash, subject to your retention policy).

Assumes a FLAT layout: all .md files live in one folder, no subdirectories.

Required environment variables (set as GitHub Actions secrets):
    ZOHO_CLIENT_ID
    ZOHO_CLIENT_SECRET
    ZOHO_REFRESH_TOKEN
    WORKDRIVE_ROOT_FOLDER_ID   # the one WorkDrive folder everything syncs into
    BEFORE_SHA                 # provided by the workflow (github.event.before)
    AFTER_SHA                  # provided by the workflow (github.event.after)

Optional (defaults shown; India DC -> use the .in domains):
    ZOHO_ACCOUNTS_DOMAIN=https://accounts.zoho.com
    ZOHO_API_DOMAIN=https://www.zohoapis.com
    MIRROR_DELETES=false
"""

import os
import sys
import subprocess

import requests

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
CLIENT_ID      = os.environ["ZOHO_CLIENT_ID"]
CLIENT_SECRET  = os.environ["ZOHO_CLIENT_SECRET"]
REFRESH_TOKEN  = os.environ["ZOHO_REFRESH_TOKEN"]
FOLDER_ID      = os.environ["WORKDRIVE_ROOT_FOLDER_ID"]

ACCOUNTS_DOMAIN = os.environ.get("ZOHO_ACCOUNTS_DOMAIN", "https://accounts.zoho.com").rstrip("/")
API_DOMAIN      = os.environ.get("ZOHO_API_DOMAIN", "https://www.zohoapis.com").rstrip("/")
MIRROR_DELETES  = os.environ.get("MIRROR_DELETES", "false").lower() == "true"

BEFORE_SHA = os.environ.get("BEFORE_SHA", "").strip()
AFTER_SHA  = os.environ.get("AFTER_SHA", "").strip()

WD_API    = f"{API_DOMAIN}/workdrive/api/v1"
EMPTY_SHA = "0" * 40                       # GitHub's "before" on a first push
JSON_API  = {"Accept": "application/vnd.api+json"}
SYNC_SUFFIXES = (".md",)


# --------------------------------------------------------------------------- #
# Auth
# --------------------------------------------------------------------------- #
def get_access_token() -> str:
    resp = requests.post(
        f"{ACCOUNTS_DOMAIN}/oauth/v2/token",
        params={
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "refresh_token",
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if "access_token" not in data:
        raise RuntimeError(f"Token refresh failed: {data}")
    return data["access_token"]


def auth(token: str) -> dict:
    return {"Authorization": f"Zoho-oauthtoken {token}"}


# --------------------------------------------------------------------------- #
# Git: what changed in this push
# --------------------------------------------------------------------------- #
def _git(*args) -> str:
    return subprocess.check_output(["git", *args], text=True)


def changed_files():
    """Return (upserts, deletes) as lists of repo-relative .md paths."""
    upserts, deletes = [], []

    # First push to a new branch: no "before" -> every tracked .md counts as new.
    if not BEFORE_SHA or BEFORE_SHA == EMPTY_SHA:
        for path in _git("ls-tree", "-r", "--name-only", AFTER_SHA).split("\n"):
            path = path.strip()
            if path.endswith(SYNC_SUFFIXES):
                upserts.append(path)
        return upserts, deletes

    # Normal push: rename-safe, NUL-separated diff.
    tokens = _git("diff", "--name-status", "-z", BEFORE_SHA, AFTER_SHA).split("\0")
    i = 0
    while i < len(tokens):
        status = tokens[i]
        if not status:
            i += 1
            continue
        code = status[0]
        if code in ("R", "C"):                    # status, old, new
            old_path, new_path = tokens[i + 1], tokens[i + 2]
            i += 3
            if new_path.endswith(SYNC_SUFFIXES):
                upserts.append(new_path)
            if code == "R" and old_path.endswith(SYNC_SUFFIXES):
                deletes.append(old_path)           # old name no longer exists
        else:                                     # A / M / D / T: status, path
            path = tokens[i + 1]
            i += 2
            if not path.endswith(SYNC_SUFFIXES):
                continue
            (deletes if code == "D" else upserts).append(path)

    return upserts, deletes


# --------------------------------------------------------------------------- #
# WorkDrive
# --------------------------------------------------------------------------- #
def list_folder(token: str):
    """Yield (name, id, is_folder) for every item directly inside FOLDER_ID."""
    offset, limit = 0, 50
    while True:
        resp = requests.get(
            f"{WD_API}/files/{FOLDER_ID}/files",
            headers={**auth(token), **JSON_API},
            params={"page[limit]": limit, "page[offset]": offset},
            timeout=30,
        )
        resp.raise_for_status()
        items = resp.json().get("data", [])
        if not items:
            break
        for item in items:
            attrs = item.get("attributes", {})
            is_folder = bool(attrs.get("is_folder")) or attrs.get("type") == "folder"
            yield attrs.get("name"), item.get("id"), is_folder
        if len(items) < limit:
            break
        offset += limit


def upload_file(token: str, local_path: str):
    filename = os.path.basename(local_path)
    with open(local_path, "rb") as fh:
        resp = requests.post(
            f"{WD_API}/upload",
            headers=auth(token),                       # requests sets multipart header
            params={
                "parent_id": FOLDER_ID,
                "filename": filename,                  # requests URL-encodes this
                "override-name-exist": "true",         # replace in place, no duplicate
            },
            files={"content": (filename, fh)},
            timeout=120,
        )
    resp.raise_for_status()


def trash_files(token: str, file_ids):
    """Move files to Trash in one batch PATCH (status 61 = trashed, recoverable)."""
    body = {"data": [
        {"attributes": {"status": "61"}, "id": fid, "type": "files"}
        for fid in file_ids
    ]}
    resp = requests.patch(
        f"{WD_API}/files",
        headers={**auth(token), **JSON_API, "Content-Type": "application/json"},
        json=body,
        timeout=30,
    )
    if resp.status_code not in (200, 204):
        resp.raise_for_status()


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    upserts, deletes = changed_files()
    if not upserts and not deletes:
        print("No Markdown changes to sync.")
        return

    token = get_access_token()

    for path in upserts:
        print(f"Uploading {os.path.basename(path)}")
        upload_file(token, path)

    if deletes:
        # One listing gives us a name -> id map for the whole folder.
        name_to_id = {name: fid for name, fid, is_folder in list_folder(token)
                      if not is_folder}
        to_trash, missing = [], []
        for path in deletes:
            fname = os.path.basename(path)
            (to_trash.append(name_to_id[fname]) if fname in name_to_id
             else missing.append(fname))
        if to_trash:
            print(f"Trashing {len(to_trash)} file(s): "
                  f"{', '.join(os.path.basename(p) for p in deletes if os.path.basename(p) not in missing)}")
            trash_files(token, to_trash)
        if missing:
            print(f"Deleted in Git but not found in WorkDrive (skipped): {', '.join(missing)}")

    print("Sync complete.")


if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as exc:
        print(f"HTTP error: {exc}\nResponse: {exc.response.text}", file=sys.stderr)
        sys.exit(1)
