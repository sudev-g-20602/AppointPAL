# Zia Agents — Use Case Submission

**Agent name:** AppointPal

**Agent tagline:** Turns booking emails, website chats, and staff requests into confirmed Zoho CRM appointments — automatically, without double-booking, dropping a request, or ever inventing a detail.

---

## Use case

**What problem does the agent solve? / What does it do?**

Appointment-driven service businesses — home services, automobile workshops, salons and spas, clinics, and field-service teams (HVAC, plumbing, electrical) — lose bookings to slow, manual scheduling. For every request, a human has to read the message, find the right customer record, check the live service catalog, verify that a qualified technician is actually free, avoid double-booking, create the appointment with all mandatory fields, tag it, and send a confirmation. Doing this by hand across email, a website chat widget, and internal staff requests is slow, inconsistent, and does not scale.

**AppointPal** is a Zia Agent built on Zoho CRM that books, reschedules, and cancels service appointments across three channels while enforcing every business rule. It runs in three modes from a single shared booking domain:

- **Email (autonomous):** reads an inbound customer email and, with no human confirming each step, either books the appointment and replies to confirm, asks once for anything genuinely missing, reschedules an existing appointment, or escalates to a Task — always exactly one outcome per email.
- **Website chatbot (conversational):** a warm, customer-facing assistant that never exposes any internal system, collects name and email up front, and confirms before every write. New visitors are captured as a Lead with their preferences, not a direct booking.
- **CRM internal (staff assistant):** a colleague-style assistant for sales reps and coordinators, where a human confirms each write; adds two-layer availability checks, enabling fast-paced appointment bookings for staffs.

The core promise across all three: the CRM is the single source of truth, services are always fetched live, providers must be eligible and available, times must be in the future, and no genuine request is ever silently dropped.

**One business scenario**

A home-services company receives this email from an existing customer:

> "Hi, could you book me a Car cleaning appointment for Friday, July 10th at 02:00 PM? Any available technician is fine. My address is 42 Lake View Street, Chennai. Regards, Sudev G"

AppointPal reads the email, matches the sender to their Contact record, confirms "Car cleaning" against the live Services catalog, resolves "any technician" to a qualified member who is actually free at 2:00 PM (checking both leave windows and existing appointments), creates the appointment at the client's address, tags it `Zia Agent - AppointPal`, and replies in the same thread with a confirmation signed `Zia Agent - AppointPal` — all without a human touching it.

**Quick examples of inputs**

- Email: *"Book me an AC repair next Monday at 10 am, my address is 12 Anna Nagar."*
- Website chat: *"Is Priya free Saturday morning for a blowout?"*
- Staff (in CRM): *"Book James for AC Repair on Thursday 2 PM with Alex."*
- Reschedule: *"Something came up — can we move my cleaning to Friday?"*
- Human handoff: *"I'd rather not deal with a bot — can someone call me?"* → escalates to a Task for the record owner.

---

## Walkthrough

AppointPal runs one shared booking engine behind three channel-specific front doors.

**Shared booking engine (all modes)**

1. **Identify the customer** — search across all modules linked to the Appointment-For field (Contacts by default), resolving one confirmed record; never guess, never duplicate.
2. **Confirm the service live** — always fetch the current active list from the Services module; map the request to a real record; never use a service name from memory.
3. **Resolve the provider and check availability** — the assigned member (Owner) must be a member of the chosen service, and must pass a two-layer availability check: no overlapping unavailability window AND no conflicting existing appointment.
4. **Validate** — future start time, location type matching the service (Business vs Client Address), and a full address captured for client-location services.
5. **Create the appointment** with all mandatory fields, then **tag it** `Zia Agent - AppointPal` (get → create if absent → associate), then **notify** the customer.

**Email mode (autonomous)** — *First,* it reads the triggering email (resolving the CRM internal message-id, not the raw RFC-822 id) and extracts every stated detail into a structured table. *Then,* it classifies the email into exactly one type — human-handoff, new booking, reply to a pending ask, reschedule, or neither — and runs the required-to-book checklist against the extracted details. *Finally,* it produces exactly one outcome: auto-book + confirm, one missing-details ask (max two per request), a reschedule via a minimal update, or escalation to a Task. Because each email is a fresh, stateless run, the customer's email thread itself serves as the memory.

**Website chatbot mode** — *First,* it greets the visitor and collects their name and email before anything else. *Then,* it handles their request (browse services, check availability, book, view, reschedule, cancel) in warm, plain language, never revealing Zoho/CRM/records/leads, and confirming before every write. *Finally,* it books (returning visitor) or registers the request as a Lead with all preferences in the Notes field (new visitor).

**CRM internal mode** — *First,* the staff user names a customer and service; the agent looks them up, surfaces history, and suggests returning-customer shortcuts. *Then,* it runs the two-layer availability check and reads back a plain summary. *Finally,* on the staff user's explicit confirmation it creates/reschedules/cancels the appointment (reasons mandatory for reschedule/cancel), tags it, and sends the relevant customer email template — signed with the staff member's own name.

---

## Overview

| | |
|----------|----------|
| **Purpose** | Automates end-to-end appointment scheduling — booking, rescheduling, and cancelling — across inbound email, a website chat widget, and internal CRM staff, enforcing every business rule so no request is dropped, duplicated, or double-booked. |
| **Products** | Zoho CRM (Services module `Services__s` and Appointments module `Appointments__s`); Zia Agent Studio. Email path additionally requires the org mailbox integrated with CRM via IMAP/POP3. |
| **Best suited for** | Appointment-driven service businesses: home services (cleaning, appliance/pest/HVAC), automobile service, wellness & beauty (salons, spas), healthcare & professional consultation, and field services (HVAC, plumbing, electrical). |
| **Complexity** | High — three deployment modes, a fully autonomous email path with stateless thread reconstruction, two-layer availability checking, strict anti-fabrication validation, and idempotent writes with tagging and escalation. |
| **Deployment mode** | Connection-based (Zoho CRM connection). The autonomous path is email-triggered; the chatbot runs as a website chat widget; the staff assistant runs inside CRM. |
| **Trigger** | Incoming customer email (autonomous path); chat message from a website visitor (chatbot); staff invocation inside CRM (chat/button). |
| **Tools** | System tools only — no custom tools. **Search Customer**, **List Services**, **Get Service History**, **Check Availability (user unavailability)**, **Get Emails of a Record**, **View Email (crm_getSpecificCrmEmailContent)**, **Send Mail**, **Create Appointment**, **Update Appointment (reschedule/cancel)**, **Get Tags**, **Create Tag**, **Associate Tags**, **Create Task (crm_insertTaskRecord)**. |
| **Knowledge Base** | `instructor_appointment_setter_agent.md` (master spec), `kb_email_booking_path.md`, `kb_website_chatbot_agent.md`, `kb_crm_staff_agent.md`, `zoho_crm_managing_services_kb.md`, `zoho_crm_booking_appointments_kb.md`, `kb_customer_faqs_and_edge_cases.md`, `kb_industry_scenarios.md`. |
| **Model Configuration** | OpenAI model, configured in Zia Agent Studio. *(Confirm exact model/version before submission.)* |
| **Constraints** | CRM is the source of truth (never invents customers, services, members, or availability); services fetched live every run; provider must be a member of the chosen service and pass availability checks; location must match the service; Scheduled start time must be in the future; one member per appointment; duration is fixed by the service; no duplicate contacts or appointments; the email path never cancels (always a Task) and sends at most two ask emails with one outcome per run; out of scope — pricing, discounts, refunds, complaints, post-service disputes (all escalate). |

---

## Configuration

### Pre-requisites

- Upload all eight Knowledge Base files listed in the Overview to the agent.
- Zoho CRM edition: **Enterprise or Ultimate** (required for Zia Agents), with the **Services module enabled** (Professional or higher for Services; the Appointments module is added automatically with it).
- Create a Zoho CRM connection with the scopes listed below and test each tool as ready.
- For the autonomous email path: integrate the org mailbox with CRM via **IMAP/POP3** so received emails and replies sync to the contact's Emails related list (the native non-integrated setup can send but cannot track replies).
- Confirm a single allowed/configured outbound **From address** for Send Mail before going live.

**Connection scopes**

- `ZohoCRM.modules.appointments.READ`, `.CREATE`, `.UPDATE`
- `ZohoCRM.modules.services.READ`
- `ZohoCRM.modules.contacts.READ`, `.CREATE` (and other Appointment-For module scopes, e.g. `ZohoCRM.modules.leads.CREATE`)
- `ZohoCRM.modules.emails.READ`
- `ZohoCRM.send_mail.Contacts.CREATE` (and `ZohoCRM.send_mail.{module}.CREATE` as needed)
- `ZohoCRM.settings.users_unavailability.READ`
- `ZohoCRM.settings.modules.READ` (appointment/service preferences)
- `ZohoCRM.settings.tags.READ`, `.CREATE`
- Activities/Tasks create access

### Agent Instructions

The full agent instructions are defined in `instructor_appointment_setter_agent.md` (included with this submission). Summary of the operative instruction set:

**Identity.** A Zia-powered AI agent for scheduling, rescheduling, and cancelling service appointments in Zoho CRM — warm, professional, efficient. Sole function: move customers from inquiry to confirmed appointment with minimum friction while following all business rules. Does not handle complaints, pricing, refunds, or disputes — those escalate.

**Path selection.**
- *Email trigger:* follow `kb_email_booking_path.md` exclusively — auto-book when complete, ask when a detail is missing, escalate to a Task when unresolvable, with no human confirming each step. Auto-created appointments get `Additional_Information = "Auto-booked from email by AppointPal"` and tag `Zia Agent - AppointPal` (the same tag is applied to agent-created Tasks). Every customer email ends with the signature `Zia Agent - AppointPal`. Reschedules use the reschedule flow; cancellations and human-handoff requests always become a Task; max two ask emails; one outcome per email.
- *Website chat:* follow `kb_website_chatbot_agent.md` — collect name + email first, never mention any internal system, fetch services live, and register new visitors as a Lead (never call it a "lead" to the visitor).
- *CRM internal:* direct and efficient for staff; look up availability, pre-fill from records, confirm required fields, never override admin settings or assign non-member providers.

**Conversation flow (10 steps).** Greet & detect intent → identify the customer (search all Appointment-For modules) → suggest last service for returning customers → confirm the service live → suggest last member (returning) → check service availability → confirm date/time → confirm location → confirm service member (eligibility + availability) → reminders & confirmation summary → create the appointment → close.

**Protocols.** Rescheduling (identify, new time, availability re-check, mandatory reason, confirm, save; max 10 reschedules) and Cancellation (identify, offer reschedule once, mandatory reason, process).

**Behavioral guardrails (11).** No appointment is confirmed until all required fields pass; availability is a hard constraint absent an admin exception; CRM is the source of truth; reschedule/cancel reasons mandatory; one member per appointment; duration fixed by service; never create duplicate contacts; Owner must be a service member; Scheduled start must be in the future; location must match the service type; services must always be fetched live.

*(Full text of all sections — identity, both flows, required-information checklist, CRM actions table, escalation rules, communication rules, appointment statuses, error/validation reference, and quick reference — is in the accompanying `instructor_appointment_setter_agent.md`.)*

### Knowledge Base

The agent's knowledge base is the eight source files below, all included with this submission. Each is summarized here; the complete `.md` text accompanies the submission package.

**1. `instructor_appointment_setter_agent.md` — Master spec.** Agent identity and scope; email-trigger routing; deployment-mode rules (website chat, CRM staff); detail-extraction rule; the 10-step conversation flow; rescheduling and cancellation protocols; required-information checklist; CRM actions table; escalation rules; communication rules; appointment statuses; behavioral guardrails; and an error/validation reference.

**2. `kb_email_booking_path.md` — Autonomous email path (governs email runs).** Mailbox IMAP/POP3 prerequisite; how CRM email APIs work (Send Mail, Get Emails of a Record, View Email); the critical message-id rule (the trigger carries an RFC-822 `<…@domain>` id, but the View Email tool needs the 64-char hex CRM internal id resolved from the Get Emails list, with the contact's Owner ID as `user_id`); statelessness (the thread is the memory); Step 1 read → Step 2 classify (human-handoff / new booking / pending reply / reschedule / neither) → Step 3 resolve contact → Step 4 mandatory extraction table (with a worked example proving stated details must not be re-asked) → Step 5 required-to-book checklist; the three mutually-exclusive Outcomes (A auto-book + confirm, B one ask email with a pre-send guard, C escalate to Task); reschedule flow with minimal-payload rules and error handling; email-sending constraints; appointment field rules; email-path hard limits; risk controls; tool reference; common errors and fixes; and API scope reference.

**3. `kb_website_chatbot_agent.md` — Website chatbot path.** Persona and purpose; language rules (what to say instead of internal terms); opening the conversation (name + email first); visitor identification; conversation flows for service search, availability, booking (Path A returning visitor / Path B new visitor → Lead), viewing, rescheduling, cancelling; handling common visitor situations; escalation to a human; visitor data-privacy rules; a "what the chatbot never does" list; and three customer email templates (confirmed / rescheduled / cancelled) with silent failure handling.

**4. `kb_crm_staff_agent.md` — CRM internal staff path.** Identity/scope for authenticated staff; domain model; customer/contact lookup; live services; provider selection with the two-layer availability check (unavailability windows + existing-appointment overlap); fetching/viewing appointments and idempotency; the step-by-step booking flow; rescheduling (mandatory reason + double-check) and cancellation flows; appointment statuses; job sheets and preferences; cloning; notifications; API and scope references; an error reference; the required-to-book checklist; and three customer email templates signed with the staff user's name.

**5. `zoho_crm_managing_services_kb.md` — Services module admin reference.** Key API fields (`Service_Name`, `id`, `Location`, `Job_Sheet_Required`, Members); access prerequisites; enabling the module and granting profile access; layout; create/clone; availability controls (Temporarily Unavailable / Not in Use); job sheets; and service preferences.

**6. `zoho_crm_booking_appointments_kb.md` — Appointments module admin/operations reference.** Access; the three layouts (Create / Reschedule / Cancel); appointment preferences (outside-availability, outside-business-hours, job-sheet, deal-on-completion); marking complete; job sheets; the Create Appointment API field reference; update/reschedule/cancel/complete mechanics and hard restrictions; the Appointment-For multi-module lookup; notifications and reminders; user-unavailability model; preferences API; scopes; and reporting/dashboards.

**7. `kb_customer_faqs_and_edge_cases.md` — Behavioral reference.** Twelve common customer FAQs with ideal response patterns; twelve edge cases (temporarily-unavailable and not-in-use services, duplicate matches, past dates, departed members, reschedule-limit, incomplete addresses, disputed appointments, no same-day slots, competitor questions, past-service complaints, mandatory job sheets); and a tone reference for common emotional states.

**8. `kb_industry_scenarios.md` — Industry playbook.** Context, typical services, booking constraints, and example flows for five industries — automobile service, wellness & beauty, home services, healthcare & professional consultation, and field services — plus cross-industry patterns (ambiguous service names, duration questions, discount requests, booking for someone else, angry customers).

**Workdrive link : [AppointPal_Knowledge_Base](https://workdrive.zoho.in/folder/5p3ayc5ebe604415044d3b47eb112be19b24f)**

### Custom tools

None. AppointPal uses Zoho CRM system tools only (see the Tools row in the Overview). No custom tool YAML or Python functions are required.

### Custom Guardrails

**Do's**
- Always fetch services live from the Services module before every booking; treat the CRM record as the only valid source.
- Always resolve exactly one customer record before acting; create a new record only after searching, and never create duplicates.
- Always confirm the provider is a member of the chosen service and passes the two-layer availability check (no unavailability window + no overlapping appointment) before booking or rescheduling.
- Always extract every stated detail from the email body into the structured table before running the checklist; ask only for items genuinely missing.
- Follow each path's signature convention — email path: `Zia Agent - AppointPal`; website chatbot: `AppointPal (AI Assistant)`; CRM staff: the staff member's own name — and tag every agent-created appointment and Task so all agent activity is auditable, creating the tag if absent (per module).
- Always confirm before every write in staff and chatbot modes; always ensure every genuine email request ends in exactly one outcome — an appointment or a Task, never neither.

**Don'ts**
- Never invent or guess a customer, service, member, availability, date, or address; never book on details the customer did not state.
- Never run the required-to-book checklist before extracting the email body (the cause of spurious ask emails); never re-ask for a detail the customer already provided.
- Never cancel an appointment from the email path — cancellations and human-handoff requests always become a Task.
- Never assign a provider who is not a member of the service, book a past time, or use a location type the service does not support.
- Never send more than one email per inbound message or more than two ask emails per request; never send more than one outcome per run.
- Never reveal Zoho/CRM/modules/records/leads/tags or any internal identifier to a website visitor; never expose another person's data.
- Never resend untouched fields (Location, Address, Service) in a reschedule update; never change a service via reschedule (that is a new booking).

---

## Invocation

- **Deployment:** A Zia Agent running on Zoho CRM via a CRM connection, operating in three modes from one shared booking domain.
- **Integration Details:** Zoho CRM (Services + Appointments modules); the org mailbox integrated with CRM via IMAP/POP3 for inbound/outbound email on contact records; a website chat surface for the chatbot mode.
- **External Tools Used:** None beyond Zoho CRM system tools and Zia Agent Studio — no custom serverless/Catalyst code.
- **How Users Interact With It:** Customers email the business or chat via the website widget; internal staff invoke the assistant inside CRM.
- **How It's Triggered:** An incoming customer email (autonomous path); a website chat message (chatbot); staff invocation inside CRM (staff assistant).
- **Where It's Deployed:** Zoho CRM (staff + email paths) and the company website (chatbot).

---

## Observability

- **Logs and execution history:** Every run produces a run summary recording the outcome and reason — including silent no-ops (unknown sender, non-booking email, mismatched-sender reply). Every agent-created appointment and Task carries the `Zia Agent - AppointPal` tag and, for appointments, an `Additional_Information` stamp, enabling after-the-fact filtering and audit of exactly what the agent created.
- **Error handling:** Documented error/fix tables in each KB (invalid provider, location mismatch, past time, missing address, message-id format, `DEPENDENT_FIELD_*` on reschedule, tag limits, Send Mail From-address, etc.). Retries are limited to one per action and only with a changed payload; identical retries are forbidden. Fail-safe ordering creates the escalation Task the moment an action fails without a usable fallback, so an outcome always survives — and a successful write whose confirmation email failed still produces a Task so the customer is reached.
- **Monitoring and metrics:** Recommended reports/dashboards from the Appointments KB — appointments per service, reschedules/cancellations by month, appointments per member, and creation trends — plus filtering by the agent tag to measure agent-created volume and escalation rate.
- **Debugging:** Common-errors tables map each failure to its cause and fix; the email path documents the exact message-id and `user_id` pitfalls; the extraction-before-checklist worked example makes the most common failure mode reproducible and testable.

### Supporting Code

None. AppointPal is implemented entirely within Zia Agent Studio using Zoho CRM system tools and the knowledge base; there are no backend functions, Catalyst/serverless code, middleware, or helper scripts.

---

*Single-agent submission. AppointPal operates as one agent across three deployment modes governed by a shared booking domain; no multi-agent setup is used.*
