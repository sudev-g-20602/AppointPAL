#!/usr/bin/env python3
"""
Sync changed docs from a Git push to Zoho WorkDrive, mirroring the repo's folder tree.

Behaviour
---------
* Diffs the push's before/after commits, so only what changed is touched.
* Recreates your repo's nested folder structure inside WorkDrive (find-or-create,
  results cached so each folder is listed at most once per run).
* New / modified files are uploaded with `override-name-exist=true`, so an existing
  filename is replaced in place (same file id, shared links stay valid).
* MIRROR_DELETES=true: files removed in Git are moved to WorkDrive Trash
  (status 61 -> recoverable from Trash, subject to your retention policy).

Which files sync: SYNC_SUFFIXES below. Currently .md + .yaml/.yml. To sync only
Markdown, set SYNC_SUFFIXES = (".md",). Anything not matching (e.g. the .py script
itself) is ignored, so empty tooling folders are never created in WorkDrive.

Required environment variables (set as GitHub Actions secrets):
    ZOHO_CLIENT_ID
    ZOHO_CLIENT_SECRET
    ZOHO_REFRESH_TOKEN
    WORKDRIVE_ROOT_FOLDER_ID   # the WorkDrive folder that maps to your repo root
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
from collections import defaultdict

import requests

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
CLIENT_ID      = os.environ["ZOHO_CLIENT_ID"]
CLIENT_SECRET  = os.environ["ZOHO_CLIENT_SECRET"]
REFRESH_TOKEN  = os.environ["ZOHO_REFRESH_TOKEN"]
ROOT_FOLDER_ID = os.environ["WORKDRIVE_ROOT_FOLDER_ID"]

ACCOUNTS_DOMAIN = os.environ.get("ZOHO_ACCOUNTS_DOMAIN", "https://accounts.zoho.com").rstrip("/")
API_DOMAIN      = os.environ.get("ZOHO_API_DOMAIN", "https://www.zohoapis.com").rstrip("/")
MIRROR_DELETES  = os.environ.get("MIRROR_DELETES", "false").lower() == "true"

BEFORE_SHA = os.environ.get("BEFORE_SHA", "").strip()
AFTER_SHA  = os.environ.get("AFTER_SHA", "").strip()

WD_API    = f"{API_DOMAIN}/workdrive/api/v1"
EMPTY_SHA = "0" * 40                       # GitHub's "before" on a first push
JSON_API  = {"Accept": "application/vnd.api+json"}

# Files to sync. Add/remove extensions here.
SYNC_SUFFIXES = (".md", ".yaml", ".yml")

# Cache: repo-relative dir ("" = root) -> WorkDrive folder id.
_folder_cache = {"": ROOT_FOLDER_ID}


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
    """Return (upserts, deletes) as lists of repo-relative paths we care about."""
    upserts, deletes = [], []

    # First push to a new branch: no "before" -> every tracked file counts as new.
    if not BEFORE_SHA or BEFORE_SHA == EMPTY_SHA:
        for path in _git("ls-tree", "-r", "--name-only", AFTER_SHA).split("\n"):
            path = path.strip()
            if path.endswith(SYNC_SUFFIXES):
                upserts.append(path)
        return upserts, deletes

    tokens = _git("diff", "--name-status", "-z", BEFORE_SHA, AFTER_SHA).split("\0")
    i = 0
    while i < len(tokens):
        status = tokens[i]
        if not status:
            i += 1
            continue
        code = status[0]
        if code in ("R", "C"):                     # status, old, new
            old_path, new_path = tokens[i + 1], tokens[i + 2]
            i += 3
            if new_path.endswith(SYNC_SUFFIXES):
                upserts.append(new_path)
            if code == "R" and old_path.endswith(SYNC_SUFFIXES):
                deletes.append(old_path)
        else:                                      # A / M / D / T: status, path
            path = tokens[i + 1]
            i += 2
            if not path.endswith(SYNC_SUFFIXES):
                continue
            (deletes if code == "D" else upserts).append(path)

    return upserts, deletes


# --------------------------------------------------------------------------- #
# WorkDrive: folders
# --------------------------------------------------------------------------- #
def list_children(token: str, folder_id: str):
    """Yield (name, id, is_folder) for every item directly inside folder_id."""
    offset, limit = 0, 50
    while True:
        resp = requests.get(
            f"{WD_API}/files/{folder_id}/files",
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


def find_child_folder(token: str, parent_id: str, name: str):
    for child_name, child_id, is_folder in list_children(token, parent_id):
        if is_folder and child_name == name:
            return child_id
    return None


def create_folder(token: str, parent_id: str, name: str) -> str:
    body = {"data": {"attributes": {"name": name, "parent_id": parent_id}, "type": "files"}}
    resp = requests.post(
        f"{WD_API}/files",
        headers={**auth(token), **JSON_API, "Content-Type": "application/json"},
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["data"]["id"]


def resolve_dir(token: str, rel_dir: str, create: bool = True):
    """
    Map a repo-relative directory (e.g. 'knowledge-base') to a WorkDrive folder id.
    With create=False, return None if any segment doesn't exist yet.
    """
    rel_dir = rel_dir.strip("/")
    if rel_dir in _folder_cache:
        return _folder_cache[rel_dir]

    parent_id, walked = ROOT_FOLDER_ID, ""
    for segment in rel_dir.split("/"):
        walked = f"{walked}/{segment}".strip("/")
        if walked in _folder_cache:
            parent_id = _folder_cache[walked]
            continue
        child = find_child_folder(token, parent_id, segment)
        if child is None:
            if not create:
                return None
            child = create_folder(token, parent_id, segment)
        _folder_cache[walked] = child
        parent_id = child
    return parent_id


# --------------------------------------------------------------------------- #
# WorkDrive: upload + trash
# --------------------------------------------------------------------------- #
def upload_file(token: str, local_path: str, parent_id: str):
    filename = os.path.basename(local_path)
    with open(local_path, "rb") as fh:
        resp = requests.post(
            f"{WD_API}/upload",
            headers=auth(token),                       # requests sets multipart header
            params={
                "parent_id": parent_id,
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
        print("No changes to sync.")
        return

    token = get_access_token()

    for path in upserts:
        parent_id = resolve_dir(token, os.path.dirname(path), create=True)
        print(f"Uploading {path}")
        upload_file(token, path, parent_id)

    if MIRROR_DELETES and deletes:
        # Group deletes by directory so each WorkDrive folder is listed once.
        by_dir = defaultdict(list)
        for path in deletes:
            by_dir[os.path.dirname(path)].append(os.path.basename(path))

        trash_ids, missing = [], []
        for rel_dir, names in by_dir.items():
            folder_id = resolve_dir(token, rel_dir, create=False)
            if folder_id is None:
                missing.extend(names)
                continue
            name_to_id = {n: i for n, i, is_f in list_children(token, folder_id)
                          if not is_f}
            for name in names:
                (trash_ids.append(name_to_id[name]) if name in name_to_id
                 else missing.append(name))
        if trash_ids:
            print(f"Trashing {len(trash_ids)} file(s)")
            trash_files(token, trash_ids)
        if missing:
            print(f"Deleted in Git but not found in WorkDrive (skipped): "
                  f"{', '.join(missing)}")
    elif deletes:
        print(f"{len(deletes)} file(s) deleted in Git, left untouched in WorkDrive "
              f"(MIRROR_DELETES is off).")

    print("Sync complete.")


if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as exc:
        print(f"HTTP error: {exc}\nResponse: {exc.response.text}", file=sys.stderr)
        sys.exit(1)