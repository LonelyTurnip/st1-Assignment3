# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Mon 2:30 - 4:30 Group 4 
Members and responsibilities: 
    Aidan - LonelyTurnip - UG
    Alexandria - xereinera - UG
    Archie - Arch2ey - UG
Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason                                                         |
|---|---------------------|-------------------------------------------------------------------------------|
| Patient identity | sesion/domain state | Required for patient registration, lookup, and appointment booking. Must persist for the duration of the session. |
| Appointment history | Session/domain state | Required by FR-07 so cancelled appointments remain available and retrievable. |
| Temporary menu choice | Transient state     | Only needed while processing the user's current menu selection and can be discarded afterwards. |
| Practitioner specialty | Session/domain state | Part of the practitioner record and required for practitioner registration and lookup. |
| Debug print output | Transient state     | Used only for displaying information or troubleshooting and is not stored as application data. |
| Appointment status | Session/domain state | Required to determine whether an appointment is scheduled, cancelled, or completed and to support filtering and validation rules. |

What is intentionally lost on exit? <!-- All SmartCare data is stored in memory for the current session only. When the program exits, patient records, practitioner records, appointments, appointment history, appointment statuses, and any menu state are intentionally discarded because no persistent storage or database is implemented. Temporary interface information such as menu selections and console output is also lost on exit. -->

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs              | Responsibility and validation              | Domain source / existing constraint |
|---|-------------|----------------------|--------------------------------------------|------------------------------|
| appointment_sort_key | Appointment | tuple(datetime, str) | Produce sorting key only; no state changes | Appointment.date_time and appointment_id |
| select_appointments | list[Appointment], practitioner_id:str, status:AppointmentStatus None | list[Appointment]    | Filter and sort appointments without modifying source data | Practitioner IDs, AppointmentStatus enum |
| Service listing | practitioner_id:str, status:AppointmentStatus None | ordered list of appointments | Validate practitioner exists and status is valid | Existing SmartCareDataStore and AppointmentService |
| Console | User menu inputs | Printed output and service calls | Validate user input and recover from errors | Existing service layer rules |

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

| Requirement | Input / session data                    | Operation and responsible component | Expected result or error | Test / evidence |
|---|-----------------------------------------|---|---|---|
|QRY-01 Appointment Sort Key | Appointment object                      |appointment_sort_key() returns (date_time, appointment_id) |Correct ordering key produced |test_appointment_sort_key |
|QRY-02 Practitioner Filter | Appointment list, prctitioner ID        |select_appointments() filters by practitioner |Matching appointments returned only |test_select_appointments_by_practitioner |
|QRY-03 Status Filter | Appointment list, practitioner ID, status |Query function filters by status |Matching status appointments returned |test_select_appointments_by_status |
|QRY-04 Stable Ordering | Appointment list                        |Sort by date/time then appointment ID |Ordered result list returned |test_select_appointments_sorted_by_time_then_id |
|FP-01 Pure Query Processing | Source appointment tlist                |Query returns new list |Original source list unchanged |test_select_appointments_does_not_modify_source |
|FP-02 Empty Result Handling | Known pracitioner with no matches       |Query returns empty list |[] returned |test_select_appointments_empty_result |
|FP-03 Object Identity Preservation | stored appointment objects              |Existing appointment objects returned in new list |Object identity preserved |Workflow tests |
|UI-01 Full Menu Workflow | User menu inputs          |Console calls services and displays results |Registration, booking, cancellation, listing succeed |Manual menu verification |
|UI-02 Invalid Input Recovery | Invalid IDs, dates, menu choices                   |Console catches errors and continues |Error displayed and session retained |Manual menu verification |
|FR-01 Register Patient | Patient ID and name                            |PatientService registers patient |Patient stored or validation error |Existing Stage 6/7 tests |
|FR-02 Patient Search | Patient ID                          |PatientService lookup |Patient returned or error raised |test_find_patient_* tests |
|FR-05 Practitioner Conflict | Practitioner ID and appointment time                         |AppointmentService conflict validation |Double-booking rejected |test_conflict_rule_and_different_practitioner |
|FR-06 Cancel Appointment | Appointment ID                       |AppointmentService cancellation |Status changes to CANCELLED |test_cancel_appointment |
|FR-07 Retain History | Cancelled appointment                   |Lookup and listing functions |Cancelled appointment remains retrievable |Stage 8 regression tests |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: <!-- Empty versus unknown versus invalid, enum conversion, object identity, error handling and unchanged state on rejection

Empty result refers to a valid practitioner who currently has no appointments matching the query. In this case an empty list ([]) is returned.
Unknown practitioner refers to a practitioner ID that does not exist in the data store. A LookupError is raised.
Invalid input refers to values that break the function contract, such as an invalid appointment status filter. A ValueError is raised.
Enum conversion uses the existing AppointmentStatus enum to ensure filtering only occurs against valid appointment states (SCHEDULED, CANCELLED, COMPLETED).
Object identity is preserved because queries return references to the existing Appointment objects stored in memory rather than creating duplicate objects.
Error handling occurs before query execution. Invalid practitioners and invalid status filters are rejected immediately.
Unchanged state on rejection is maintained because failed lookups, invalid filters, rejected bookings, and other validation errors do not modify stored patients, practitioners, or appointments. -->

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
|QRY-01 |queries.py |test_appointment_sort_key() verifies the returned key is (date_time, appointment_id) |Passed |test_queries.py |
|QRY-02 |queries.py |test_select_appointments_by_practitioner() verifies only appointments for the requested practitioner are returned |Passed |test_queries.py |
|QRY-03 |queries.py |test_select_appointments_by_status() verifies filtering by AppointmentStatus.CANCELLED returns only cancelled appointments |Passed |test_queries.py |
|QRY-04 |queries.py |test_select_appointments_sorted_by_time_then_id() verifies appointments are ordered by date/time and then appointment ID where times match |Passed |test_queries.py |
|FP-01 |queries.py |test_select_appointments_does_not_modify_source() verifies the original appointment list remains unchanged after query execution |Passed |test_queries.py |
|FP-02 |queries.py |test_select_appointments_empty_result() verifies a valid practitioner with no matching appointments returns an empty list |Passed |test_queries.py |
|FP-03 |services.py |test_list_practitioner_appointments() verifies returned appointments are the original stored appointment objects |Passed |test_workflows.py |
|SRV-01 |services.py |test_list_practitioner_unknown() verifies an unknown practitioner raises LookupError |Passed |test_workflows.py |
|SRV-02 |services.py |test_list_practitioner_invalid_status() verifies an invalid status filter raises ValueError |Passed |test_workflows.py |
|SRV-03 |services.py |test_list_practitioner_no_matches() verifies a known practitioner with no appointments returns [] |Passed |test_workflows.py |
|FR-07 |services.py, queries.py |test_cancelled_appointments_remain_listable() verifies cancelled appointments remain retrievable and appear in listings |Passed |test_workflows.py |
|QRY-05 |queries.py |Repeated calls using identical inputs return identical outputs |Passed |test_queries.py |
|QRY-06 |queries.py |Already-sorted inputs remain correctly ordered and no unnecessary state changes occur |Passed |test_queries.py |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- select_appointments() is a pure function because:

all required data is supplied through function parameters;
it does not access hidden global state;
it does not modify the supplied appointment list;
it does not modify any Appointment, Patient, or Practitioner objects;
it performs no input/output operations such as print() or input();
it has no side effects;
the same inputs always produce the same outputs.

The function creates a new temporary list, applies filtering rules, and returns a new sorted result using sorted() with the named appointment_sort_key() function. This preserves the source collection and object state. -->
What the tests do and do not establish: <!-- The tests establish that:

practitioner filtering works correctly;
appointment status filtering works correctly;
sorting uses date/time first and appointment ID as the tie-breaker;
equal-time appointments are ordered consistently;
query processing does not modify source lists;
known practitioners with no appointments return an empty list;
unknown practitioners raise LookupError;
invalid status values raise ValueError;
cancelled appointments remain retrievable and listable;
service integration correctly delegates query processing.

The tests do not establish that:

the application is free from all defects;
every possible user input has been tested;
future code changes cannot introduce new faults;
data persists across application restarts, since SmartCare intentionally stores data only for the current session;
all possible combinations of appointments, practitioners, and statuses have been exercised.

The test suite provides strong evidence that the implemented Stage 9 requirements function correctly, but testing can demonstrate the presence of defects rather than prove their complete absence. -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---------------------------------|---|
| UI-01 full menu workflow |Register patient P1, find P1, register practitioner D1, book appointment A1, list appointments, cancel A1, list appointments again, exit program |All operations complete successfully. Appointment is created, found, cancelled and remains visible in appointment listings. Application exits cleanly. | Patient and practitioner records were created successfully. Appointment was booked and retrieved. Cancellation changed status to CANCELLED. Listing continued to display the appointment after cancellation. Exit option terminated the session normally. |Manual console run, final passing workflow execution |
| UI-02 invalid-input recovery |Blank patient ID, duplicate patient ID, unknown practitioner ID, malformed date (2026-15-99 25:00), invalid menu option, repeated cancellation attempt |Application displays an error and continues executing without terminating. Existing stored data remains unchanged. | Appropriate ValueError or LookupError messages were displayed. Application returned to the menu and accepted further input. Existing patients, practitioners and appointments remained unchanged after rejection. |Manual console validation and existing service tests |
| Automated service workflow |Workflow tests covering registration, booking, cancellation, filtering and retained history |Services correctly coordinate domain, datastore and query logic |All workflow tests passed. Appointments were filtered and sorted correctly. Cancelled appointments remained retrievable and listable. Practitioner conflict rules remained enforced. |test_workflows.py and full pytest execution |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.
Registration and Lookup
Before: Patient P1 did not exist.
Action: Register patient P1.
After: Patient lookup successfully returned the registered record.
Subsequent successful action: Appointment booking used the registered patient.

Appointment Booking
Before: No appointment with ID A1.
Action: Book appointment A1.
After: Appointment stored and retrievable.
Subsequent successful action: Appointment listing displayed the new booking.

Practitioner Conflict Rejection
Before: Practitioner D1 had an appointment at the selected time.
Action: Attempt second booking for D1 at the same date/time.
After: ValueError raised and no appointment added.
State Check: Existing appointment list unchanged.
Subsequent successful action: Different practitioner booking at the same time succeeded.

Different-Practitioner Booking
Before: Practitioner D2 available at the same date/time.
Action: Book appointment with D2.
After: Booking succeeded.
State Check: Both appointments remained stored correctly.

Cancellation and Retained History
Before: Appointment status SCHEDULED.
Action: Cancel appointment.
After: Status changed to CANCELLED.
State Check: Appointment still retrievable and visible in practitioner listings.
Subsequent successful action: Appointment history queries returned the cancelled appointment.

Listing and Filtering
Before: Mixed appointment statuses existed.
Action: Filter practitioner appointments by status.
After: Only matching status entries were returned.
State Check: Source appointment collection remained unchanged.

Freed Slot Verification
Before: Practitioner conflict existed because a scheduled appointment occupied the timeslot.
Action: Cancel the appointment.
After: Practitioner no longer had a scheduled booking at that time.
State Check: Appointment history remained stored while the slot was no longer treated as actively scheduled.

Exit
Before: Session contained registered patients, practitioners and appointments.
Action: Select menu option 7.
After: Application terminated successfully.
State Check: Session-only data intentionally discarded on program exit.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- Human design was completed before using GitHub Copilot. The query layer, service-layer validation, menu workflow, appointment filtering behaviour, and testing strategy were designed from the Stage 9 requirements prior to requesting any AI assistance.-->
Actual prompt/context supplied: <!-- Review the implementation of appointment_sort_key(), select_appointments(), list_practitioner_appointments(), and the Stage 9 menu implementation. Verify sorting behaviour, practitioner filtering, status filtering, purity requirements, error handling, retention of cancelled appointments, and separation of responsibilities. Suggest defects or improvements without changing project requirements or introducing additional architecture. -->
Actual response: <!-- Copilot suggested reviewing:
appointment sorting behaviour;
status validation;
handling of unknown practitioners;
separation of query logic from console code;
preservation of source collections during filtering;
verification of cancelled appointment visibility. -->

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

Issues and bounded branches: <!-- debug/stage08; stage09 -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- Human review focused on:
-practitioner conflict detection;
-retained cancelled appointment history;
-query filtering and sorting behaviour;
-menu integration;
-regression test results.
GitHub Copilot suggestions were treated as hypotheses and verified against source code, requirements, and automated tests. Human review decisions were accepted only when supported by evidence from code inspection and test execution. -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- All automated tests passed successfully, including:

Stage 6 functionality tests
Stage 7 testing artefacts
Stage 8 regression tests
Stage 9 query tests
Stage 9 workflow tests

Evidence:
Final pytest execution completed with all tests passing on the Stage 9 branch.
tests\test_queries.py ......                                                 [ 19%]
tests\test_services.py ...........                                           [ 54%]
tests\test_starter.py ........                                               [ 80%]
tests\test_workflows.py ......                                               [100%]

=============================== 31 passed in 0.39s ================================-->
README run instructions and scope/limitations: <!-- Scope limitations:

Session-based storage only.
No database persistence.
Data is intentionally lost when the application exits.
Query functions operate on in-memory collections.
Stage 9 focuses on filtering, sorting, workflow integration, and testing rather than long-term storage. -->
Unresolved issues and support/action: <!-- No known functional defects remain following the final regression run. Future maintenance should continue to use automated regression testing when modifying appointment, query, or workflow functionality. -->
UG common candidate / PG future branch plan: <!-- Current implementation including query functions, practitioner appointment listing, workflow integration, testing suite, and interactive menu. -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
