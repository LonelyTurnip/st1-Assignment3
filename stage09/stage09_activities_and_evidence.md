# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <!-- complete -->
Members and responsibilities: <!-- complete -->
Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity | Session/domain state | Needed for operations during the run, but stored only in memory. |
| Appointment history | Session/domain state | Needed to find and list appointments during the run; cancellation retains records until exit. |
| Temporary menu choice | Transient state | Used to select the current operation, not retained as domain data. |
| Practitioner specialty | Session/domain state | A practitioner attribute used during the session. |
| Debug print output | Transient | Diagnostic output is not part of the stored domain model. |
| Appointment status | Session/domain state | It is part of each appointment and changes during the session. |

What is intentionally lost on exit? 
    All in-memory patients, practitioners, appointments, and their statuses. The application does not persist them.

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

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: 
    The query receives the appointment list, practitioner ID, and optional AppointmentStatus explicitly rather than reading a global store. It returns a new sorted list, retaining references to the original appointment objects. The service validates practitioner existence and status before calling the query. Booking must use the actual registered participant objects, and failed operations must not alter stored records.

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
| FR-01–03 registration and lookup | IDs and required participant fields | Domain validates fields; services coordinate registration and lookup through the store | Valid records are stored and found; invalid fields raise ValueError, missing records raise LookupError |
| FR-04–05 booking and conflicts | Appointment ID, registered participant IDs, date/time | Appointment service resolves registered objects, checks duplicates/conflicts, then stores the appointment | Valid booking succeeds; missing participants raise LookupError; duplicate IDs or a scheduled same-practitioner/time conflict raise ValueError |
| FR-06–08 cancellation and history | Appointment ID and stored appointment | Service calls the domain cancellation transition; store retains the object | Scheduled appointment becomes cancelled; unknown appointment raises LookupError; invalid/repeated cancellation raises ValueError without changing status |
| FR-09 / QRY / FP listing | Practitioner ID, optional enum status, appointment list | Service validates; pure query filters and sorts | Unknown practitioner or invalid status is an error; known practitioner with no matches gets an empty list. No status means all statuses |
| UI-01–02 console | Menu choice and operation fields | Console parses input, converts a supplied status to the enum, calls services, displays errors/results | Expected ValueError/LookupError are reported and the menu continues; invalid menu choices are rejected |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection:
    For a rejected operation, capture the store’s records and relevant fields before the call, then compare them after: IDs, list order, participant references, date/time, and status. Follow with a valid operation to show the session remains usable.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| | | | | |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: 
    Purity explanation: appointment_sort_key derives a tuple from one appointment. select_appointments reads its arguments, builds a filtered list, and sorts that new list; it does not print, access a global store, or mutate the supplied list or appointments.
What the tests do and do not establish: 
    The inspected tests contain assertions for those cases, but I have not run them, so don’t report a pass or count based on this review. The visible tests do not individually establish every requested case—for example, repeated calls, fresh-list identity for already-sorted input, every enum status, or unchanged appointment fields after a failed operation. They also don’t demonstrate the full interactive console workflow. Add or run evidence for those before marking them verified.

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

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: 
    Domain objects validate their own data and enforce appointment status transitions. The data store owns the session collections and returns new lists of stored objects. Services coordinate validation, lookups, booking, cancellation, and listing. Pure queries filter and sort without I/O or mutation. The console owns prompts, parsing, and printed output.

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail?  
    Ensuring the services and console use the same session-scoped store, and that appointment history is retained rather than removed on cancellation. That is an integration/data-lifecycle concern, not a sorting detail.  
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? 
    The tests in test_services.py assert that cancellation returns the same appointment, lookup still finds it, and its status is CANCELLED. test_workflows.py asserts a cancelled appointment remains in the default listing. Report these as executed evidence only after running the tests

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? 
    select_appointments() is pure because it depends only on its inputs and does not modify state, perform I/O, or alter the supplied collections. Modifying the source list, printing output, or storing information outside the function would introduce side effects and break purity.
2. Which explicit inputs are needed, and why avoid a global store? 
    The query needs the appointment list, practitioner ID, and optional status: list[Appointment], str, and AppointmentStatus | None. The sort-key function needs one Appointment. Avoiding a global store makes the query’s dependencies explicit, easier to test, and reusable without hidden state.
3. How can a new list reuse Appointment objects safely? 
    select_appointments builds and returns a new list, so sorting or filtering it does not reorder the caller’s list. The returned list contains the same Appointment objects, which is safe here because the query reads them without changing them. Callers should remember that those objects are shared references.
4. Why use a named key, and what breaks equal-time ties?   
    A named key makes the ordering rule explicit and reusable: appointment_sort_key returns (date_time, appointment_id). Passing it as key=appointment_sort_key lets Python call it for each appointment. The ID breaks ties when two appointments have the same time.
5. How do default and explicit status filters differ? 
    With no status (None), the listing includes every status. An explicit AppointmentStatus filters to appointments with that status. In the console, a blank filter means all statuses; a supplied value is converted to the enum.
6. How do empty, unknown practitioner and invalid filter cases differ? 
    A known practitioner with no matching appointments gets an empty list. An unknown practitioner raises LookupError; an invalid status raises ValueError. These are different cases: no results is valid, while the latter two are errors.
7. Which console errors recover, and how is unchanged state checked? 
    The console reports and recovers from expected ValueError and LookupError exceptions, such as invalid fields, unknown records, malformed dates, or booking conflicts; an invalid menu choice also returns to the menu. To check a rejected operation leaves state unchanged, capture the stored records and relevant fields before it, then compare them afterward—including appointment order, status, time, and participants—and confirm a later valid operation still works.
8. What is data integrity for registered participants, conflicts and history? 
    Booking must use the registered Patient and Practitioner objects, not merely new objects with matching IDs. A practitioner conflict is another scheduled appointment for that same practitioner at the same time; a different practitioner does not conflict. Cancellation changes status but retains the appointment, so it remains retrievable and listable, and its slot can be booked again.
9. What is Copilot's review role, and who verifies findings? 
    Copilot can suggest risks or review code against the stated requirements, but its output is not proof of correctness. A human checks each finding against the implementation and tests, then accepts, modifies, or rejects it and records the reason and verification. Don’t claim a review or verification happened unless it did.
10. How do pure functions and OOP responsibilities work together? 
    Pure functions handle collection filtering and ordering without hidden state, I/O, or mutation. OOP objects enforce domain rules and own their state; the store owns session collections, services coordinate workflows, and the console handles user input and output. These responsibilities complement one another rather than compete.



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
