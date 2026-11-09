# Stage 7 Testing and Verification Record

Group/tutorial: Mon 2:30 - 4:30 Group 4 
Members/cohorts: 
    Aidan - LonelyTurnip - UG
    Alexandria - xereinera - UG
    Archie - Arch2ey - UG
    
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion                                                                                    |
|---|---|---|--------------------------------------------------------------------------------------------------|
| FR-01 Register patient | [Reigster a patient with a correct ID and Name] | [Register a patient just a name] | [Assert that a patient record is created and stored only when ID and name are provided]          |
| FR-05 Prevent practitioner conflict | [Try to book an already booked appointment] | [Book an empty appointment] | [Assert that conflicting bookings are rejected while available are successfully booked]          |
| FR-06 Cancel appointment | [Cancel an appointment that has been booked] | [Cancel an appointment that has already been cancled or is not booked] | [Assert that appoitnment status changes to cancelled only for valid appoitnments]                |
| FR-07 Retain cancelled history | [Provide multiple cancelled appointments then view history] | [Attempt to view cancelled appointment history after providing no cancelled appointments] | [Assert that cancelled appoitnments remain accessible in appoitnment history after cancellation] |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Unclear]  Why: [Assert True is unclear on what is assumed to be true.]

`assert appointment is not None`
Judgement: [Strong]  Why: [Assert appointment is not none is strong as it states what element it is asserting and clearly stating what it thinks it should be.]

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong]  Why: [This directly verifies the required behaviour by chacking the exact state change that should occur after cancellation.]

`assert len(results) > 0`
Judgement: [Weak/unclear]  Why: [While this confirms that some result exists, it doesn't verify the correct result was returned.]

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong]  Why: [this verifies that the datastore returns the expected appointment object for the supplied appointment ID]

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 

| [Input]                                          | [Expected Result]                                           | [Supporting Contract]          |
|--------------------------------------------------|-------------------------------------------------------------|--------------------------------|
| [Blank patient ID ("")]                          | [Patient registration rejected]                             | [Patient ID must not be blank] |
| [Whitespace-only patient name (" ")]             | [Registration rejected]                                     | [Patient name must contain valid characters]                     |
| [Practitioner already booked for same date/time] | [Appointment booking rejected]                              | [Practitioners cannot have conflicting appointments]                     |
| [Cancelled appointment booked again]             | [Operation rejected or handled according to business rules] | [Cancelled appointments cannot be reused without explicit rebooking]                     |
| [Transition from CANCELLED to COMPLETED]         | [Invalid transition rejected]                               | [Appointment state transitions must follow the defined workflow]                     | 
| [Duplicate patient ID]                                               | [Registration rejected]                                                          | [Patient IDs must be unique]                             |
| [Null appointment ID]                                               | [Search fails with validation error]                                                          | [Appointment identifiers are required]                             |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | [Only verifies existence, not correctness] | [Verify a patient record contains the expected ID and name] |
| 2 | [Does not validate business rules] | [Verify cancelling a booked appointment changes its status to CANCELLED] |
| 3 | [Verifies nothing about system behaviour] | [Verify a valid patient registration creates a stored patient record] |
| 4 | [SMS functionality is not part of the requirement] | [Verify appointment cancellation is recorded in appointment history] |
| 5 | [Tests an invented requirement] | [Verify invalid appointment cancellation returns the expected error] |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[100% code coverage can coexist with poor software verification. This is because code coverage just refers to the percentage of functions that are executed when running a test. This means that code coverage is only testing to see if functions are getting executed and not if they are producing the expected results. ]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [FR-06 Cancel Appointment]
Acceptance criterion: ["If the user attempts to cancel a valid appointment then the appointment will be modified to be cancelled."]
Behaviour to test: [Appointment status changes from BOOKED to CANCELLED.]
Human-first test idea/categories: [Positive test, state transition verification, status validation.]
Prompt and purpose: [Generate test ideas for validating appointment cancellation behaviour.]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
[Verification checks to see if the program fits the design specifications.]

2. What question does validation answer?
[Validation esnures that the code works properly and is at a usable state for users.]

3. What is a unit test?
[A unit test is creating units that test individual functions to validate if the expected behaviour happens.]

4. What is a pytest fixture?
[A pytest fixture is a defined, reliable, and consistent context for conducting testing.]

5. What is parametrisation in pytest?
[Parametrisation is a testing technique that executes a single function multiple times but with different sets of inputs provided.]

6. What is regression testing?
[Regression testing is testing to ensure that functional and non-functional tests are still providing the expected output after a change. This is to ensure that a change does not break another part of the code.]

7. What does code coverage tell us, and what does it not prove?
[Code coverage tells us the percentage of functions that are executed when running tests. Code coverage does not prove that all those functions are providing the expected outcome.]

8. What makes an assertion weak?
[An assertion is weak when it is unclear what is being asserted.]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[GitHub Copilot should be used to asit with generating test ideas, structures and possible edge cases. However, all generated tests must be reviewed by a human to ensure they accurately trace requirements, verify behaviour, use assertions and don't introduce assumptions or business rules that are not part of the specification.]

10. What is the Stage 7 engineering rule?
[The Stage 7 engineering rule is that every implemented requirement must have traceable tests with meaningful assertions that verify observable behaviour. Tests must be linked to requirements and acceptance criteria, reviewed critically, and executed to provide evidence that the system behaves correctly.]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
