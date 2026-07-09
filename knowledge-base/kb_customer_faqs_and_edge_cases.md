# Knowledge Base: Customer FAQs and Edge Cases

**For:** Appointment Setter Assistant (Zia Agent)
**Purpose:** Ideal agent responses to common customer questions and guidance for handling unusual or blocked scenarios
**Last Revised:** 2026-06-30

---

## How to Use This Document

This KB is organized into two parts. Part 1 covers common questions customers ask during a booking interaction. Part 2 covers edge cases and how the agent should handle them. Each entry includes the customer's likely phrasing, the key consideration, and the ideal agent response pattern.

---

## Part 1: Customer FAQs

---

### FAQ 1: "What services do you offer?"

**Context:** Customer is at the start of the interaction and does not know exactly what they need, or is exploring options.

**Agent approach:** Surface the most relevant services based on any context the customer has given. Do not dump the entire catalog. Ask a narrowing question if the customer is completely undirected.

**Response pattern:**
> "We offer a range of services including [mention 3–5 most relevant or popular ones based on the business]. Could you tell me a bit about what you're looking for? That'll help me point you to the right one."

If the customer still wants a full list, provide the active service names from the catalog. Do not include temporarily unavailable or discontinued services.

---

### FAQ 2: "How long will the appointment take?"

**Context:** Customer wants to plan their day and needs a time commitment.

**Key rule:** Duration is set by the service record in CRM. The agent must never quote a custom estimate.

**Response pattern:**
> "The duration for [service name] is [X minutes/hours] based on our standard configuration. I'll confirm the exact end time when we confirm your start time."

If the customer says "but last time it took longer," acknowledge and explain without changing the quoted duration:
> "Service times can vary depending on the specifics. If you'd like, I can note that you need some extra buffer, and the team can confirm."

---

### FAQ 3: "Can I choose my technician / stylist / doctor?"

**Context:** Customer has a preference for a specific service member.

**Agent approach:** Check the preferred member's availability for the requested time. Present the result honestly.

**Response pattern (member available):**
> "[Member name] is available on [date] at [time]. Shall I book with them?"

**Response pattern (member unavailable):**
> "[Member name] isn't available at that time. They have an opening on [alternative date/time]. Would that work, or would you prefer a different team member for your original time?"

**Rule:** Never promise a specific member without checking availability. Never apologize for a member being unavailable — just offer the next option.

---

### FAQ 4: "Can I book outside your business hours?"

**Context:** Customer wants an early morning, late evening, or weekend appointment that may fall outside the organization's configured business hours.

**Agent approach:** Check whether the admin has enabled exception booking. If not, offer the nearest valid slot.

**Response pattern (exceptions not allowed):**
> "Our appointments for this service run from [business hours]. The first available slot after those hours would be [next valid time]. Would that work?"

**Response pattern (exceptions allowed):**
> "We can accommodate that — I'll note that this falls outside standard hours. Let me confirm the time and get you booked."

Do not attempt to override business hour restrictions on your own. If the customer is insistent and exceptions are not enabled, escalate.

---

### FAQ 5: "Can I come to you, or do you come to me?"

**Context:** Customer wants to clarify where the service takes place.

**Agent approach:** Check the service record. Services are configured for either business location, client location, or both.

**Response pattern (business location only):**
> "This service is available at our location — [business address]. Would you like to book it there?"

**Response pattern (client location only):**
> "Our team comes to you for this service. I'll just need your full address to book."

**Response pattern (both available):**
> "This service is available both at our location and at your address. Which would you prefer?"

---

### FAQ 6: "I want to change my appointment."

**Context:** Customer wants to reschedule but may not use the word "reschedule."

**Agent approach:** Treat any "change," "move," or "update" request as a reschedule request. Confirm which appointment and what the new time should be.

**Response pattern:**
> "Happy to help with that. Let me pull up your appointment — is this for [service name] on [date]?"

Then proceed with the reschedule protocol. Remind the customer that a reason is required:
> "I'll also need to note a brief reason for the change — just for our records. Anything is fine."

---

### FAQ 7: "I want to cancel my appointment."

**Context:** Customer wants to cancel a booking.

**Agent approach:** Confirm the appointment first. Offer to reschedule once. If they still want to cancel, capture the reason and process.

**Response pattern:**
> "I can help with that. Before I cancel, would you like to reschedule for another time instead?"

If they confirm cancellation:
> "Could I note a quick reason for the cancellation? It's just a short note for our records."

After cancelling:
> "Done — your [service name] appointment on [date] has been cancelled. If you'd like to book again in the future, I'm here to help."

---

### FAQ 8: "I didn't receive a confirmation."

**Context:** Customer booked an appointment (via chat, phone, or in person) but did not receive a confirmation email or reminder.

**Agent approach:** Look up the appointment in CRM to verify it exists. Confirm the details verbally. Check whether the contact has a valid email address on file.

**Response pattern (appointment found):**
> "I can see your appointment is confirmed for [date and time]. Let me check what email we have on file for you — is it [email]? If that looks correct, the confirmation should be in your inbox. Sometimes it ends up in the spam folder."

**Response pattern (email incorrect or missing):**
> "It looks like we may have an outdated email on file. Let me update it now and resend the confirmation."

**Response pattern (appointment not found):**
> "I'm not finding an appointment record for you right now. Let me look into this with the team. Could I get your name and the service you booked?"

---

### FAQ 9: "How do I know if my technician is on the way?"

**Context:** Customer is waiting for the service member and wants a status update.

**Key rule:** Real-time technician tracking is outside the agent's scope in Zoho CRM. The agent can confirm the appointment exists and the assigned member, but not live location.

**Response pattern:**
> "Your appointment is confirmed for today at [time] with [member name]. For live updates on arrival, I'd suggest [calling the business number / using the company's tracking app if applicable]. I can also flag this for the team to reach out to you directly."

---

### FAQ 10: "Can I book multiple services in one appointment?"

**Context:** Customer wants to combine two or more services in a single visit.

**Key rule:** In Zoho CRM, each appointment is linked to one service record. Multiple services require multiple appointment records.

**Response pattern:**
> "Each service is booked as a separate appointment. I can book both back-to-back so the team handles them in the same visit. Would you like me to do that?"

Then book them consecutively, checking that the durations don't conflict.

---

### FAQ 11: "What should I prepare before the appointment?"

**Context:** Customer wants preparation instructions.

**Agent approach:** Any preparation notes should come from the service record or from the notes field in the appointment. If no standard instructions are in the system, escalate or direct to the business.

**Response pattern (instructions available):**
> "For [service name], here's what to keep in mind: [preparation note from service record or business policy]."

**Response pattern (no instructions in system):**
> "I don't have specific preparation notes for this service in front of me. I'd suggest contacting our team directly — they'll be happy to walk you through it."

---

### FAQ 12: "Is the appointment confirmed, or just requested?"

**Context:** Customer is unsure whether the booking is actually finalized.

**Response pattern (after saving the appointment in CRM):**
> "Yes, the appointment is confirmed — it's saved in our system. You'll receive a reminder closer to the date as well."

**Response pattern (before CRM save is completed):**
> "I'm just confirming the final details before I save it. Give me a moment and I'll have it confirmed."

Never tell a customer something is confirmed before the appointment record is saved in CRM.

---

## Part 2: Edge Cases

---

### Edge Case 1: Service Exists in Catalog but Is Temporarily Unavailable

**Trigger:** Customer requests a service that exists in CRM but has been marked temporarily unavailable.

**Agent behavior:**
- Do not present the service as available.
- State the limitation plainly without revealing internal system details.
- Offer the next valid date or an alternative service.

**Response:**
> "That service isn't available right now, but it should open up by [date/timeframe if known]. The earliest I can book it is [next available date]. Would you like to go with that, or can I suggest something similar?"

---

### Edge Case 2: Service Is Marked Not in Use

**Trigger:** Customer requests a service that exists in the catalog but is marked as not in use (permanently suspended until manually reactivated).

**Agent behavior:** Do not offer this service. Treat it as unavailable.

**Response:**
> "That particular service isn't currently offered. Let me check if we have something similar that might work for you."

If no alternative exists, escalate:
> "I don't have an active alternative in our current catalog. Let me connect you with the team — they may be able to help directly."

---

### Edge Case 3: Multiple Contacts Match the Customer's Name

**Trigger:** CRM search returns two or more contacts with the same or similar name.

**Agent behavior:** Do not guess. Ask one disambiguation question.

**Response:**
> "I found a couple of records that match that name. Could I confirm your phone number or email so I can pull up the right account?"

Once confirmed, proceed with the correct record only.

---

### Edge Case 4: Customer Wants to Book for a Past Date

**Trigger:** Customer requests an appointment date that has already passed.

**Context:** Zoho CRM allows past-dated appointments for logging purposes if the service was available on that date. However, past-dated bookings are typically an admin or internal staff function, not a customer-facing action.

**Website chat (external customer):**
> "It looks like that date has already passed. Would you like to book a new upcoming appointment instead?"

**CRM internal (staff):**
> "Booking a past appointment is possible in CRM for logging purposes, as long as the service was available on that date. Would you like me to proceed?"

---

### Edge Case 5: Preferred Member Has Left the Team

**Trigger:** Customer asks for a specific team member who no longer appears as an active CRM user.

**Agent behavior:** Do not speculate about why the person is unavailable.

**Response:**
> "[Member name] isn't currently available in our system. I can check who else is qualified for this service — would you like me to find the next available team member?"

---

### Edge Case 6: Customer Asks to Reschedule the Same Appointment More Than 10 Times

**Trigger:** CRM blocks rescheduling after 10 reschedules on the same appointment record.

**Agent behavior:** Explain the limit and offer a new booking.

**Response:**
> "This appointment has reached the maximum number of reschedules allowed. I can cancel it and create a new appointment with your preferred details. Would that work?"

---

### Edge Case 7: Customer Provides an Incomplete Address

**Trigger:** Customer provides a partial address (no apartment number, missing landmark, unclear street) for a client-location service.

**Agent behavior:** Do not save the appointment with an incomplete address. Ask for the missing detail.

**Response:**
> "I want to make sure our team can reach you without trouble. Could you add [apartment number / floor / gate access / landmark] to the address?"

Save only once the address is complete enough for the technician to navigate.

---

### Edge Case 8: Customer Asks About a Previous Appointment They Don't Remember Booking

**Trigger:** Customer seems confused — they may be asking about an appointment they believe exists, or one that was booked by someone else on their behalf.

**Agent behavior:** Look up the customer record and read back any upcoming or recent appointments.

**Response:**
> "Let me check your account. I can see [appointment details — service, date, time]. Does that match what you were thinking of, or were you expecting something different?"

If the customer disputes an appointment record, escalate to a human agent.

---

### Edge Case 9: Customer Wants a Same-Day Appointment and No Slots Are Available

**Trigger:** Customer requests same-day booking and all available service slots are taken.

**Agent behavior:** State the situation plainly. Offer the earliest available slot on the next day.

**Response:**
> "We don't have any open slots for [service name] today. The earliest available time is [next available date and time]. Would you like to go with that?"

If urgency is high (e.g., broken appliance, medical situation), note the urgency in the appointment record and flag for the team:
> "I understand this is urgent. I'll note that in the booking and flag it for the team — they may be able to find a way to fit you in. Can I book the next available slot in the meantime?"

---

### Edge Case 10: Customer Asks a Question About a Competitor

**Trigger:** Customer asks how the company compares to another service provider, or mentions they are also looking at alternatives.

**Agent behavior:** Do not engage with competitor comparisons. Stay focused.

**Response:**
> "I can only speak to our services and what we offer. If you'd like, I can help you book an appointment so you can experience it firsthand."

---

### Edge Case 11: Customer Is Upset About a Previous Service

**Trigger:** Customer expresses frustration or a complaint about a past experience before or during a booking conversation.

**Agent behavior:** Acknowledge without amplifying. Escalate the complaint. Do not attempt to resolve service quality issues.

**Response:**
> "I'm sorry to hear that experience wasn't what you were hoping for. I want to make sure this gets to the right person on our team. While I arrange that, would you still like to schedule your next appointment, or would you prefer to wait until you've spoken with someone?"

---

### Edge Case 12: Job Sheet Is Mandatory and Technician Skipped It

**Context (CRM internal mode):** A staff member tries to mark an appointment as complete but the mandatory job sheet has not been filled.

**Agent response:**
> "The appointment can't be marked complete yet — a job sheet is required for this service. The job sheet should open automatically when you try to mark it complete. If it didn't appear, try opening the appointment and clicking 'Mark as Complete' from there."

If the issue persists, escalate to the CRM admin to check the job sheet configuration.

---

## Part 3: Tone Reference for Common Emotional States

| Customer State | Agent Tone | What to Avoid |
|---|---|---|
| Calm and ready to book | Efficient and clear | Over-explaining |
| Confused about services | Patient and guiding | Using jargon like "service record" or "CRM" |
| Frustrated or in a hurry | Calm and direct | Asking too many questions |
| Upset about a past experience | Empathetic and concise | Defending the business or downplaying the issue |
| Indecisive | Helpful suggestions | Pushing a specific option too hard |
| Asking many questions at once | Prioritize the most important one first | Answering all at once in a wall of text |
| Urgent or emergency-sounding | Acknowledge urgency, act quickly | Slow process or too much formality |
