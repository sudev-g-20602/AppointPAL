# Zoho CRM — Services Module: Admin & Configuration Reference

Sources:
- https://help.zoho.com/portal/en/kb/crm/customize-crm-account/services/articles/managing-services-with-zoho-crm
- Zoho CRM API v8: https://www.zoho.com/crm/developer/docs/api/v8/
Last reviewed: 2026-07-02

---

## Key Fields (API)

Module API name: `Services__s`  
API scope to read: `ZohoCRM.modules.services.READ`

| Field | API key | What the agent uses it for |
|---|---|---|
| Service name | `Service_Name` | Resolving which service was requested |
| Record ID | `id` | Required when creating an appointment (`Service_Name.id`) |
| Location | `Location` | `"Business Address"` or `"Client Address"` — must match the appointment location |
| Job Sheet Required | `Job_Sheet_Required` | `"Yes"` or `"No"` — if Yes, a job sheet is mandatory before completion |
| Members | `Members` | Only users in this list can be assigned as the appointment Owner |

---

## Access and Prerequisites

- Available on **Professional edition or higher**.
- Only CRM administrators can enable the module.
- Users need profile permission to view, create, edit, or delete services.
- If the org uses teamspaces, the module must also be added to the relevant teamspace.

---

## Enable the Services Module

**Path:** Setup > Customization > Modules and Fields > Services

1. Sign in with administrator privileges.
2. Open Setup > Customization > Modules and Fields.
3. Locate and enable the Services module.
4. Add to relevant teamspaces if applicable.

---

## Grant Profile Access

1. Open the Services module.
2. Click More > Module Permission.
3. Select profiles that need access.
4. Save.

---

## Services Layout

Default sections: Service image, Service information, Availability information, Price information, Job sheet information, Description.

Admins can add, remove, and rearrange fields. Examples: car model/wash type for auto businesses, warranty status for repair shops, access instructions for home services.

**Path:** Setup > Customization > Modules and Fields > Services > Standard Layout

---

## Create and Clone Services

**Create:** Services module > + Service > fill in service info, availability, price, job sheet settings, description > Save.

**Clone:** Open existing service > More > Clone > update fields > Save. Use when a new service is mostly similar to an existing one.

**Note:** CRM allows keeping records of discontinued services for historical catalog purposes.

---

## Service Availability Controls

### Mark as Temporarily Unavailable
Hides a service from booking for a defined period.

Supported periods: rest of today, until tomorrow, until end of week, until end of month, until a specific date.

Steps: Services module > select service > More > Mark as Temporarily Unavailable > choose period > Save.

### Mark as Not in Use
Treats the service as unavailable until manually reactivated. Services in this state do not appear during appointment booking.

Steps: Services module > select service > More > Mark as Not in Use > Confirm.

---

## Job Sheets

Captures post-service details: inspection findings, model/serial numbers, warranty, spare parts, completion notes.

**Enable:** Setup > Customization > Modules and Fields > Services > Preferences > enable job sheets > Save.
Once enabled, job sheets apply to all services.

**Customise layout:** Setup > Customization > Modules and Fields > Services > Job Sheet Layout > Edit Layout > add fields > Save.

**Require per service:** On the individual service record, enable **Job sheet required**. When set, the appointment creator is prompted to add a job sheet before saving. The job sheet also opens automatically when the assigned member marks the appointment complete.

---

## Service Preferences (API)

API scope: `ZohoCRM.settings.modules.READ`

| Setting key | Values | Effect |
|---|---|---|
| `job_sheet_enabled` | `true` / `false` | `true` (default) = job sheets are available across the org; must be `true` before any service can mandate a job sheet |

**Note:** Job sheets can only be mandated for completion if this is `true`. This affects the Complete step of an appointment, not the initial booking.
