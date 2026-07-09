# Zoho CRM — Appointments Module: Admin & Operations Reference

Sources:
- https://help.zoho.com/portal/en/kb/crm/sales-force-automation/activities/articles/booking-appointments-for-services
- Zoho CRM API v8: https://www.zoho.com/crm/developer/docs/api/v8/
Last reviewed: 2026-07-02

---

## Access and Prerequisites

The Appointments module is added automatically when the Services module is enabled. CRM administrators can access it and grant create, edit, and delete permissions to other profiles.

**Path:** Setup > Customization > Modules and Fields > Appointments > More > Module Permissions

---

## Appointments Layouts

Three layouts exist: **Create**, **Reschedule Appointment**, and **Cancel Appointment**. Admins can add custom fields to any layout (e.g., vehicle photo fields for car wash bookings, custom reschedule reason fields).

**Path:** Setup > Customization > Modules and Fields > Appointments > Standard Layout

---

## Appointment Preferences

Global controls that apply to all appointments. Configure at:
**Path:** Setup > Customization > Modules and Fields > Appointments > Preferences

| Preference | Effect |
|---|---|
| Ask users to mark appointment as completed | Members must manually mark complete; otherwise auto-completes after end time |
| Mandate users to fill job sheet | Job sheet must be submitted before marking complete |
| Allow booking outside service availability | Enables exception bookings beyond the service's configured schedule |
| Allow booking outside business hours | Only available if the above is enabled; shows an alert but allows the booking |
| Create a deal when appointment is completed | Auto-creates a Closed Won deal mapped to the service price and appointment name |

### Deal Creation Config
When enabled: deal defaults to Closed Won, name maps from appointment name, amount from service price, closing date from appointment start date. Admin selects layout, deal owner (admin / creator / assigned member), and account name.

---

## Marking Appointments Complete

If the preference is enabled, members must explicitly mark appointments complete from the list view or detail page. Any user with module access can mark it complete. If the preference is off, appointments auto-complete after the configured end time.

---

## Job Sheets

Job sheets capture post-service details (inspection notes, parts used, warranty, serial numbers). Required when the **Mandate job sheet** preference is on AND the service record has **Job sheet required** enabled. The job sheet opens automatically when a member tries to mark the appointment complete.

**Customise job sheet layout:** Setup > Customization > Modules and Fields > Appointments > Job Sheet Layout > Edit Layout

---

## Create Appointment — API Field Reference

Module API name: `Appointments__s`

### Mandatory Fields

| Field | API key | Notes |
|---|---|---|
| Appointment Name | `Appointment_Name` | Label for the record, e.g. "James - AC Repair" |
| Appointment For — module | `Appointment_For.module.api_name` | API name of the customer's module, e.g. `Contacts` |
| Appointment For — name | `Appointment_For.name` | Customer's display name |
| Appointment For — id | `Appointment_For.id` | Customer's CRM record id |
| Service Name — name | `Service_Name.name` | Exact service name from the Services module |
| Service Name — id | `Service_Name.id` | Service record id from Get Services |
| Start Time | `Appointment_Start_Time` | ISO 8601 format; must be in the future for Scheduled status |
| Owner | `Owner` | Provider's CRM user id; **must be a member of the chosen service** |
| Location | `Location` | `"Client Address"` or `"Business Address"` — must match the service |
| Address | `Address` | Required only when Location is `"Client Address"` |

### Optional Fields

| Field | API key | Notes |
|---|---|---|
| Additional Information | `Additional_Information` | Extra detail about the customer's needs |
| Reminder unit | `Remind_At.unit` | Integer 0–100; supply with period |
| Reminder period | `Remind_At.period` | `"minutes"`, `"hours"`, or `"days"` |
| Status | `Status` | Defaults to `Scheduled`; do not set past-time with Scheduled |

**Note:** There is no end-time field. The API stores only `Appointment_Start_Time`; displayed end time is calculated from the service duration and shown to the user, not written to CRM.

---

## Update Appointment — Reschedule, Cancel, Complete

The appointment `id` is always required for any update.

### Reschedule
- Provide a new `Appointment_Start_Time` that is in the future.
- Optionally add a reschedule reason (`By Customer` or `By Team`) and a note.
- Reason and notes are **mandatory** per business rule.

### Cancel
- Set `Status` to `"Cancelled"` — mandatory.
- Optionally add a cancellation reason and note.
- Reason and notes are **mandatory** per business rule.

### Complete
- Set `Status` to `"Completed"`.
- Can only be set after the appointment's end time.
- If the org mandates job sheets (`show_job_sheet` preference on), a job sheet name and description become mandatory before completing.

### Hard Restrictions
- Cannot reschedule or change status of a **Cancelled** or **Completed** appointment — create a new one instead.
- `Scheduled` status cannot be assigned to a past time.
- `Completed` / `Overdue` can only be set after the appointment time has ended.

---

## Rescheduling and Cancellation — CRM Mechanics

- Reason and notes are **mandatory** for both actions.
- An email notification is sent to the appointment owner on reschedule/cancel (not sent if the user acts on their own appointment).
- Maximum **10 reschedules** per appointment record; rescheduling history is visible from the detail page.
- Appointments can be rescheduled or backdated to past dates.
- Actions available from: Appointments list view or appointment detail page.

---

## Appointment For Field — Adding Modules

The **Appointment For** field is a multi-module lookup. Contacts is included by default. Additional customer-facing modules (Leads, Clients, etc.) can be added.

**Path:** Setup > Customization > Modules and Fields > Appointments > Standard Layout > Appointment For field > More > Edit Properties

---

## Notifications and Reminders

- Members receive email and pop-up notifications when an appointment is assigned.
- Users can opt out of assignment notifications via CRM Calendar > Options > Preferences > "Notify me when an appointment is assigned."
- Users do not receive email notifications when they create an appointment for themselves.
- Reminders can be set during booking or in CRM Calendar preferences.

---

## Provider Availability — User Unavailability

Availability is determined by checking when a provider is **not** available. Each user can have unavailability windows (leave, blocked time) defined by a `from` and `to` time in ISO 8601 format.

**Key fields:** `from`, `to`, `comments`, `user.name`, `user.id`, `id`

**Access rule:** Admin users can see all users' unavailability; non-admin users can only see their own.

**Booking rule:** A provider can be booked for a slot only if that slot falls entirely outside all of their unavailability windows. When the user says "any provider," the agent picks a service member with no unavailability covering the requested time.

**API scope to read unavailability:** `ZohoCRM.settings.users_unavailability.READ`

---

## Appointment Preferences — API Reference

API scope: `ZohoCRM.settings.modules.READ`

| Setting key | Effect |
|---|---|
| `allow_booking_outside_service_availability` | If `false`, start time must fall within the service's availability window |
| `allow_booking_outside_businesshours` | If `false`, time must be within business hours (only configurable when the above is `true`) |
| `when_duration_exceeds` | `ask_provider` = manual completion required; otherwise auto-completes after end time |
| `show_job_sheet` | Job sheet mandatory to complete (requires manual-complete mode) |
| `when_appointment_completed` | Whether completing an appointment auto-creates a deal |

**Deal auto-creation mapping (system-defined, cannot be remapped):** Amount → service Price; Closing Date → Appointment Start Time; Deal Name → Appointment Name; Status → Closed Won.

---

## API Scope Reference

| Action | Scope |
|---|---|
| Read appointments | `ZohoCRM.modules.appointments.READ` |
| Create appointment | `ZohoCRM.modules.appointments.CREATE` |
| Update / reschedule / cancel | `ZohoCRM.modules.appointments.UPDATE` |
| Read services | `ZohoCRM.modules.services.READ` |
| Read appointment preferences | `ZohoCRM.settings.modules.READ` |
| Read service preferences | `ZohoCRM.settings.modules.READ` |
| Read user unavailability | `ZohoCRM.settings.users_unavailability.READ` |

**Edition note:** Zia Agents require Enterprise or Ultimate. Confirm your edition before building tools.

---

## Reporting and Dashboards

**Common reports:** appointments per service, reschedules/cancellations by month, deals won from completed appointments, appointments grouped by cancellation reason.

**Common dashboards:** appointments per member, monthly creation trends, service popularity (quadrant analysis), cohort trends over time.

**Path:** Reports tab > Add > choose Services / Appointments / Deals as primary module → add child modules → set relationship (Inclusive/Exclusive).
