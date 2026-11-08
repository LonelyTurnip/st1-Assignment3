# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <!-- complete -->
Members and responsibilities: <!-- complete -->
Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity | | |
| Appointment history | | |
| Temporary menu choice | | |
| Practitioner specialty | | |
| Debug print output | | |
| Appointment status | | |

What is intentionally lost on exit? <!-- response -->

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types                           | Outputs              | Responsibility and validation              | Domain source / existing constraint |
|---|-----------------------------------------------------|----------------------|--------------------------------------------|-------------------------------------|
| appointment_sort_key | Appointment                                         | tuple(datetime, str) | Produce sorting key only; no state changes | Appointment.date_time and appointment_id                                    |
| select_appointments | list[Appointment], practitioner_id:str, status:AppointmentStatus None | list[Appointment]    | Filter and sort appointments without modifying source data | Practitioner IDs, AppointmentStatus enum                                    |
| Service listing | practitioner_id:str, status:AppointmentStatus None  | ordered list of appointments                     | Validate practitioner exists and status is valid | Existing SmartCareDataStore and AppointmentService                                    |
| Console | User menu inputs                                    | Printed output and service calls                     | Validate user input and recover from errors | Existing service layer rules                                    |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: <!-- Patient = patient ID and patient name.
Practitioner = practitioner ID, practitioner name, specialty.
Appointment = appointment ID, patient object, practitioner object, date/time, status.
Appointment objects reference actual Patient and Practitioner objects rather than duplicate data.
Appointment status is restricted to values defined by AppointmentStatus. -->

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason                                                                    |
|---|---|------------------------------------------------------------------------------------------------|
| Appointment.cancel reads input | Domain object performing UI tasks| Input should be handled by console/service layer; domain object only manages state transitions |
| Service prints/reads the menu | Service layer performing UI work| UI belongs in console layer; services coordinate business logic                                |
| Query sorts its source in place | Query mutates supplied data| Queries should be pure and return new lists                                                                                               |
| Store prints Appointment saved | Data store performing presentation tasks| Data store should manage storage only                                                                                               |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: <!-- appointments.sort(key=appointment_sort_key)
Source list is modified.
Sort occurs in place.
Returns None.
Original object remains the same list object.
 
sorted(appointments, key=appointment_sort_key)
Source list remains unchanged.
Returns a new sorted list.
Result is a different list object.

Meaningful mutation check 
before = list(appointments)
select_appointments(appointments, "D1")
assert appointments == before -->

Score-example prediction and explanation of passing the named key: <!-- Why the named key is passed:
sorted(appointments, key=appointment_sort_key)
passes the function itself, allowing Python to compute a consistent ordering using:
(appointment.date_time,
    appointment.appointment_id, 
)
Equal appointment times are resolved using appointment ID as the tie-breaker.-->

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: <!-- Cancellation changes an appointment's status to CANCELLED while retaining the appointment in the system. Deletion would remove the appointment entirely from storage.
Verification should confirm:
- cancelled appointments can still be found using lookup;
- cancelled appointments remain visible in appointment listing;
- status filtering behaves correctly;
- cancellation does not remove appointment history;
- only scheduled appointments participate in practitioner conflict checking. -->

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- response -->

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| | | | | |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: <!-- response -->

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| | | | | |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- response -->
What the tests do and do not establish: <!-- response -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | | | | |
| UI-02 invalid-input recovery | | | | |
| Automated service workflow | | | | |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: <!-- paste or accessible reference -->
Actual response: <!-- accessible reference -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| | | | | | |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- select_appointments() is pure because it depends only on its inputs and does not modify state, perform I/O, or alter the supplied collections. Modifying the source list, printing output, or storing information outside the function would introduce side effects and break purity. -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
