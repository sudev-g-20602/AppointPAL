# Knowledge Base: Real-Life Industry Scenarios

**For:** Appointment Setter Assistant (Zia Agent)
**Purpose:** Reference for how the agent should behave across common service industries and booking scenarios
**Last Revised:** 2026-06-30

---

## How to Use This Document

Each section below covers a specific industry or scenario type. For each, the KB provides:
- Context and typical service structure
- Common customer behaviors and expectations
- Specific booking constraints to watch for
- Example conversation flows

The agent should cross-reference this KB with the service catalog and appointment preferences configured in Zoho CRM for the specific organization.

---

## Industry 1: Automobile Service

### Context

Automobile service businesses offer mobile or workshop-based services — oil changes, vehicle inspections, washes, tire replacements, and general repairs. Services are often time-bound, technician-specific, and tied to vehicle details.

### Typical Services in CRM Catalog

- Oil change (standard, synthetic, diesel)
- Exterior wash and wax
- Full vehicle inspection
- Tire rotation
- Battery replacement
- AC service

### Booking Constraints to Watch

- Service duration varies significantly by service type (a wash is 45 minutes; an inspection may be 2–3 hours).
- Mobile services require the full vehicle location address including parking instructions.
- Some services require knowing the vehicle make, model, and year — capture this during booking if the CRM layout includes those fields.
- Some technicians specialize in specific vehicle types (e.g., diesel, EV). Member assignment must account for this.
- Customers may call while already broken down — treat urgency cues as a signal to check same-day availability first.

### Example Scenario 1: First-Time Customer, Mobile Oil Change

**Customer:** "I need an oil change for my car. Can you come to my office?"

**Agent flow:**
1. Confirm service: "Is this a standard, synthetic, or diesel oil change?" → Match to catalog.
2. Identify customer: New customer — capture full name, phone, email.
3. Ask for preferred date and time.
4. Check service availability for that date.
5. Confirm location: "What's the full address where the vehicle will be parked? Do you need to mention any parking instructions?"
6. Check technician availability.
7. Summarize and confirm.

**Agent confirmation message:**
> "You're booked for a synthetic oil change on Tuesday, 15 July at 11:00 AM at Level 2, Parking Bay 4, Rajiv Gandhi Salai. Our technician will meet you there. You'll receive a reminder the morning of the appointment."

---

### Example Scenario 2: Returning Customer, Rescheduling

**Customer:** "I had a full inspection booked for tomorrow. Something came up — can I move it?"

**Agent flow:**
1. Look up customer record.
2. Identify the inspection appointment by date.
3. Confirm: "Is this the full vehicle inspection on Thursday, 10 July at 9:00 AM?"
4. Ask for new preferred date and time.
5. Run availability check for the new slot.
6. Capture reschedule reason: "Could I note the reason for rescheduling? Just a brief note is fine."
7. Save reschedule and confirm.

**Constraint to flag:** If the customer has already rescheduled 9 times, inform them that the next change will require creating a new appointment.

---

### Example Scenario 3: Service Not Available on Requested Date

**Customer:** "Can I get a tire rotation this Sunday?"

**Agent flow:**
1. Check service availability — tire rotation is not available on Sundays.
2. State the constraint: "Tire rotations are available Monday through Saturday. The earliest I have on Monday is 10:00 AM."
3. Offer the alternative directly.
4. If customer insists on Sunday, escalate: "I'll need to check with our team about an exception for Sunday. Can I have someone reach out to confirm?"

---

## Industry 2: Wellness and Beauty

### Context

Salons, spas, massage therapy centers, and beauty studios run high-volume appointment schedules. Bookings are typically short (30–90 minutes), highly personal (same stylist preference), and prone to last-minute reschedules.

### Typical Services in CRM Catalog

- Haircut (men's, women's, children's)
- Hair color and highlights
- Manicure and pedicure
- Full body massage (Swedish, deep tissue)
- Facial treatment
- Bridal or event makeup
- Waxing

### Booking Constraints to Watch

- Customers often request a specific stylist or therapist. Member assignment should honor this if available.
- If the preferred staff member is unavailable, offer an alternative without downplaying the customer's preference.
- Bridal or event bookings (makeup, styling packages) may require longer durations and multiple service slots — each must be a separate appointment unless the CRM service record covers the bundle.
- Walk-in customers calling to check immediate availability should get same-day slot responses.
- Reminders are especially valued in this industry — default to 24 hours before plus a 1-hour reminder if supported.

### Example Scenario 1: Regular Customer, Specific Stylist Request

**Customer:** "I'd like a blowout with Priya on Saturday morning."

**Agent flow:**
1. Look up the customer record.
2. Confirm service: "Blowout — I'll check Priya's availability on Saturday."
3. Check member availability for Priya on Saturday morning.
4. If available: "Priya has 10:00 AM and 11:30 AM open. Which works better?"
5. If not available: "Priya isn't available that morning — she has slots on Saturday afternoon at 3:00 PM or Sunday at 11:00 AM. Would either work, or would you prefer a different stylist on Saturday morning?"
6. Confirm location, set reminder, save.

---

### Example Scenario 2: Bridal Booking with Multiple Services

**Customer:** "I need bridal makeup and a hair trial before my wedding."

**Agent flow:**
1. Clarify both services separately — bridal makeup and hair trial are typically separate service records.
2. Check if both can be booked with the same member or if different members apply.
3. Ask for the preferred date and ideal order (usually hair trial before makeup).
4. Offer time slots that allow back-to-back booking if possible.
5. Capture any notes: "Would you like me to note anything specific, like hair length or style reference?"
6. Confirm both appointments separately with individual summaries.

---

### Example Scenario 3: Last-Minute Cancellation

**Customer:** "I'm so sorry, I need to cancel my appointment this afternoon."

**Agent flow:**
1. Look up the customer's appointment for today.
2. Confirm: "I see your Swedish massage today at 2:30 PM. Is that the one you'd like to cancel?"
3. Offer reschedule: "Would you like to move it to another day instead?"
4. If cancelling: "Could I note a quick reason for the cancellation? It helps the team plan."
5. Process cancellation, confirm to customer.
6. Close warmly: "Done — the appointment is cancelled. Hope everything is okay! We'd love to see you whenever you're ready to rebook."

---

## Industry 3: Home Services

### Context

Home service businesses include house cleaning, appliance repair, pest control, HVAC servicing, plumbing, and electrical. Services are always at the client location, require full address details, and often need preparation instructions.

### Typical Services in CRM Catalog

- Deep cleaning (1 BHK, 2 BHK, 3 BHK, villa)
- Regular maintenance cleaning
- Appliance repair (washing machine, refrigerator, AC)
- Pest control (general, termite, rodent)
- AC service and gas refill
- Plumbing inspection

### Booking Constraints to Watch

- Client location is mandatory — the service always happens at the customer's address.
- Access instructions are often critical (building security, parking, pet alerts, gate codes). Capture these as notes.
- Service duration varies dramatically by home size or appliance type. Never quote a custom duration — it is set by the service record.
- Some services (pest control, deep cleaning) require the home to be partially or fully vacated. Mention this if it is documented for the service.
- Technician gender preference may be a sensitive requirement — capture as a note and escalate to the team for confirmation if this cannot be auto-matched.

### Example Scenario 1: New Customer, Deep Cleaning

**Customer:** "I want to get my home deep cleaned. It's a 3 BHK."

**Agent flow:**
1. Map service: "3 BHK Deep Cleaning" — verify this exists in the catalog.
2. Identify customer: new customer — capture name, phone, email.
3. Ask for preferred date and time.
4. Check availability.
5. Confirm address: "What's the full address including apartment number, floor, and any gate or access instructions?"
6. Ask about any notes: "Anything the team should know before arriving — pets, restricted areas, specific rooms to prioritize?"
7. Set reminder, confirm and save.

**Agent confirmation message:**
> "Perfect! You're booked for a 3 BHK Deep Cleaning on Saturday, 19 July at 9:00 AM at your address. I've noted the gate access instructions. You'll get a reminder the evening before."

---

### Example Scenario 2: Appliance Repair, Urgency

**Customer:** "My washing machine is not working at all. Can someone come today?"

**Agent flow:**
1. Identify service: Washing Machine Repair.
2. Check same-day availability immediately. If available, lead with the slot: "We have a technician available today at 3:30 PM."
3. If no same-day slots: "The earliest available slot is tomorrow morning at 10:00 AM. Would that work?"
4. Capture customer details, full address, and note: "I'll add a note that the machine is not functioning — is there anything else the technician should know, like the brand or model?"
5. Confirm and save.

---

### Example Scenario 3: Recurring Service — Regular Cleaning

**Customer:** "I'd like weekly cleaning every Friday."

**Agent flow:**
1. Clarify: Zoho CRM appointments are individual records. Explain that recurring appointments are booked one at a time or in batches, depending on admin configuration.
2. If the business supports advance booking: "I can book the next four Fridays now, and we can continue from there."
3. If not: "I'll book this Friday and set a note to reach out each week to confirm the next slot."
4. Do not promise automated weekly recurrence unless the CRM and business workflow explicitly support it.

---

## Industry 4: Healthcare and Professional Consultation

### Context

Medical clinics, dental practices, physiotherapy centers, legal consultants, and financial advisors book time-based appointments where the service member (doctor, consultant, advisor) is central to the booking.

### Typical Services in CRM Catalog

- General consultation (15 min, 30 min)
- Follow-up appointment
- Dental checkup and cleaning
- Physiotherapy session
- Legal consultation (initial, ongoing)
- Financial advisory session

### Booking Constraints to Watch

- The assigned member (doctor, consultant) is usually the primary reason for the appointment. Always confirm the correct professional.
- Appointment type (initial vs. follow-up) changes the duration and sometimes the service record. Confirm which applies.
- In healthcare contexts, the customer may provide sensitive information. The agent should not store or repeat sensitive health details — capture only what the service record and appointment fields require.
- Some services require prior documentation or a referral. Capture as a note and let the customer know the practice will follow up.
- Telehealth or remote consultation services may have a different location type. If a virtual link is involved, note this but do not generate links from within the agent.

### Example Scenario 1: New Patient, First Consultation

**Customer:** "I'd like to see a doctor for a general checkup."

**Agent flow:**
1. Service: General Consultation.
2. New patient — capture full name, date of birth if required by the service layout, phone, email.
3. Confirm: "Is this your first visit with us, or are you a returning patient?"
4. Check doctor availability. "Dr. Rajan has slots on Thursday at 11:00 AM and 4:30 PM. Dr. Meena is available Wednesday at 2:00 PM. Any preference?"
5. Confirm the appointment type as first consultation.
6. Capture any notes the clinic requests (reason for visit at a high level, if the service layout includes this field).
7. Confirm and set reminder.

---

### Example Scenario 2: Follow-Up Appointment

**Customer:** "I need to book a follow-up with Dr. Meena."

**Agent flow:**
1. Look up the customer's existing record — retrieve recent appointment with Dr. Meena.
2. Service: Follow-Up Appointment.
3. Confirm the member: Dr. Meena.
4. Check her availability.
5. Confirm duration is correct for a follow-up (typically shorter than an initial consult — driven by the service record).
6. Confirm and save.

---

## Industry 5: Field Services (HVAC, Plumbing, Electrical)

### Context

HVAC technicians, plumbers, and electricians perform skilled on-site work. Appointments often involve diagnosing a problem, then returning for the full service. Job sheets are critical for capturing parts used, warranty, and inspection findings.

### Typical Services in CRM Catalog

- AC installation
- AC service and maintenance
- AC gas refill
- Plumbing leak repair
- Electrical inspection
- Water heater installation

### Booking Constraints to Watch

- Field services almost always require the client address with detailed access instructions.
- Job sheets are typically mandatory. Inform the customer that the technician will complete a service record after the visit — this is normal.
- Multi-visit jobs (diagnosis first, then repair) require separate appointments. Do not merge them or promise completion in one visit unless the service record specifies it.
- Some jobs require a site visit quote before the appointment is confirmed. In these cases, book the assessment appointment and let the customer know the actual service will be scheduled after the quote is approved.
- Parts availability may affect appointment timing — this is outside the agent's scope. If a customer asks about parts or timelines beyond scheduling, escalate.

### Example Scenario 1: AC Not Cooling, Service Request

**Customer:** "My AC is not cooling. I need a technician to look at it."

**Agent flow:**
1. Start with the diagnostic service: "I'll book an AC diagnostic visit so the technician can assess the issue first."
2. Check availability for the diagnostic appointment.
3. Capture full address and floor details (important for accessing multi-story buildings).
4. Note: "I'll add a note that the unit is not cooling. Do you know the brand and model of the AC?"
5. Inform the customer: "After the visit, the technician will provide a report. If a repair or gas refill is needed, we'll book a follow-up appointment."
6. Confirm and save the diagnostic appointment.

---

### Example Scenario 2: Job Sheet Required Post-Service

**Customer (internal staff):** "The technician just finished the water heater installation. How do I mark it complete?"

**Agent (CRM internal mode) response:**
> "Before you mark it complete, the system requires a job sheet to be filled in. It should capture the model number, installation notes, and any warranty details. Once the job sheet is submitted, you can mark the appointment as completed from the list view or the appointment detail page."

---

## Cross-Industry Patterns

### Pattern 1: Ambiguous Service Name

**Customer says:** "I need a check-up," "I need maintenance," "I need someone to come fix it."

**Agent action:** Ask one focused clarifying question.
> "Could you tell me a bit more about what needs to be done? For example, is this for your vehicle, home appliance, or something else?"

Then map the response to the nearest active service in the catalog.

---

### Pattern 2: Customer Asks "How Long Will It Take?"

Always refer to the duration configured in the service record. Never quote a custom estimate.

> "The appointment duration for this service is set based on the standard time our team has configured. I'll confirm the exact duration when I check availability."

If the customer pushes for a specific time estimate that differs from the record, note their request and escalate to the team for confirmation. Do not override the service duration.

---

### Pattern 3: Customer Requests a Discount or Special Rate

This is outside the agent's scope.

> "Pricing and special requests like that are handled by our team directly. I'll note your question and make sure someone reaches out to you."

Escalate. Do not attempt to adjust pricing.

---

### Pattern 4: Customer Wants to Book for Someone Else

This is allowed. The appointment is still linked to the customer record, but capture the name of the person who will be present (if different) as a note.

> "Happy to book that. The appointment will be under your account — could I also note the name of the person who will be there, so the technician knows who to ask for?"

---

### Pattern 5: Customer Is Angry or Frustrated

Stay calm. Acknowledge the feeling without amplifying it.

> "I understand this is frustrating. Let me see what I can do right now."

If the issue is a complaint about a past service, do not attempt to resolve it. Escalate immediately.

> "For something like this, I'd like to make sure the right person on our team handles it. I'll connect you with them now."
