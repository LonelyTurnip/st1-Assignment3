# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [complete]
Members and UG/PG cohorts: [complete]
Record owner / contribution links for each member: [complete]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason:
- Appointment disappears after cancellation. 
  - Symptom. 
  -This describes an observed behaviour that describes something is wrong without explanations as to why.

- The data-store removal path is probably being called. 
  - Hypothesis/Opinion.
  - This is a possible explanation to the fault but has yet to be supported by evidence. 
  
- The failing test shows store.find_appointment('A1') returns None.
  - Evidence.
  - This is a direct observation from a tests and can be verified.
  
- The service layer is badly designed.
  - Hypothesis/Opinion. 
  - This is a subjective judgement and does not fully explain a fault or provide supporting evidence of that fault. 
  
- Traceback points to smartcare/services.py line 42 in the example.
  - This is an observable fact produced by a runtime environment and can guide future investigation. 

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

[Response and reason: 
Scenario: Cancelled Appointment History

Expected Behaviour
According to FR-07, cancelled appointments must remain in the system and be retrievable after cancellation. Appointment history must be retained.

Observed Behaviour
After cancelling an appointment, attempts to retrieve it resulted in a LookupError because the appointment could no longer be found.

Minimal Reproduction:
1. Register a patient.
2. Register a practitioner.
3. Create an appointment.
4. Cancel the appointment.
5. Call find_appointment() using the appointment ID.
6. Observe that the appointment is no longer returned.

Initial Hypothesis:
The appointment may be removed from the data store during cancellation.

Evidence to Inspect:
  - cancel_appointment() service logic.
  - find_appointment() implementation.
  - Appointment status after cancellation.
  - Current contents of the appointment store.
  - Existing regression tests:
      - test_cancel_appointment
      - test_repeat_cancel_appointment]

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: [The test expecting cancelled appointments to be deleted should be changed because it conflicts with FR-07.
FR-07 explicitly states that cancelled appointment history must be retained. Therefore, the requirement is authoritative and the test is incorrect.
A failing test does not automatically indicate a product defect. If a test contradicts the requirements, the test itself is defective and should be updated.
Similarly, a test expecting different practitioners at the same time to conflict does not match AC-04.2. AC-04.2 allows different practitioners to have appointments at the same time. Therefore, a test that rejects those bookings would also be a test defect rather than a product defect.]

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: [Smells: Long method, Duplicate status strings, Direct collection manipulation, Printing inside application logic, Mixed responsibilities, Excessive 
Rename appt to appointment - Refracting - Improves readability without changing behaviour
Extract a repeated conflict helper - Refracting - Reduces duplication while preserving behaviour
Add rescheduling - Feature - Introduces new behaviour not currently present 
Restore retained cancellation lookup - Repair - Corrects broken behaviour 
Replace a magic status string with the enum - Refracting - Improves maintainability without chaninging behaviour.
Behaviour That Must Remain Unchanged:Appointment booking rules, Practitioner conflict detection, Appointment cancellation behaviour, Lookup operations, Existing test results.
The purpose of refactoring is structural improvement while preserving externally observable behaviour.]

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: [Test: test_conflict_rule_and_different_practitioner
Exception: Failed: DID NOT RAISE <class 'ValueError'>
Expected behaviour: Booking the same practitioner at the same time should raise a ValueError.
Observed behaviour: the second booking was allowed 
Test line: with pytest.raises(ValueError):
Call path: test_conflict_rule_and_different_practitioner
↓
AppointmentService.book_appointment()
↓
SmartCareDataStore.has_practitioner_conflict()
Supporting Requirement: FR-05 Prevent Practitioner Conflict. A practitioner cannot be booked for multiple appointments at the same time.
Ranked Causes: 1. Conflict comparison uses the wrong operator - Directly affects conflict detection logic 2. Conflict method is not being called - Would bypass all conflict checking. 3. Appoitnmnet times are being compared incorrectly - Could prevent matching appoitnments from being detected.
Distinguishing Checks: Wrong comparison operator - Inspect has_practitioner_conflict() logic
Method not called - Add breakpoint/logging before conflict check
time comparison issue - Print both datetime values during evaluation 
A traceback identifies where a failure is detected, not necessarily where the defect originates. Multiple causes can produce the same failure, so additional code inspection and evidence gathering are required before identifying the root cause.]

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: [Changing code immediately after seeing a failure is often a poor debugging strategy because the actual cause of the fault has not yet been identified. Making changes without gathering evidence can introduce additional defects, obscure the original problem, and make diagnosis more difficult. Effective debugging follows a process of observing the failure, reproducing it, forming hypotheses, gathering evidence, identifying the root cause, and then applying the smallest justified fix.]


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [f810488]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [The system allowed the same practitioner to be booked for multiple appointments at the same time.]
- Expected behaviour and requirement: [FR-05 Prevent Practitioner Conflict requires a booking request to be rejected when a practitioner is already scheduled at the requested time.]
- Minimal synthetic reproduction steps: [1. Register practitioner D1. 2. Book appointment A1 for D1 at 9:00 AM. 3. Attempt to book appointment A2 for D1 at 9:00 AM. 4. Observe booking succeeds instead of raising ValueError.]
- Meaningful failing test path/name and exact relevant failure: [tests/test_starter.py
test_conflict_rule_and_different_practitioner
Failed: DID NOT RAISE <class 'ValueError'>]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [Inspection of SmartCareDataStore.has_practitioner_conflict() identified: appointment.practitioner.practitioner_id != practitioner_id. The method was checking for a different practitioner rather than the same practitioner. ]
- Smallest justified fix / diff / why other behaviour is preserved: [Changed != practitioner_id to == practitioner_id. The smallested possible fix because it corrects the comparison without modifying appointment storage, validation logic, or unrelated booking behaviour.]
- Repair SHA / focused verification result: [Verification result: test_conflict_rule_and_different_practitioner PASSED]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [Cancelled appointments could not be retrieved after cancellation.]
- Expected behaviour and requirement: [FR-07 Retain Cancelled History requires cancelled appointments to remain accessible after cancellation.]
- Minimal synthetic reproduction steps: [1. Register patient. 2. Register practitioner. 3. Book appointment A1. 4. Cancel appointment A1. 5. Attempt to retrieve A1. 6. Observe LookupError.]
- Meaningful failing test path/name and exact relevant failure: [tests/test_services.py
test_cancel_appointment
LookupError: Appointment not found
and
tests/test_services.py
test_repeat_cancel_appointment
LookupError: Appointment not found]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [Inspection of find_appointment() identified: and appointment.status.value != "cancelled". This condition prevented cancelled appointments from being returned.]
- Smallest justified fix / diff / why other behaviour is preserved: [Removed the cancellation-status filter from find_appointment(). Lookup functionality now returns appointments regardless of status while preserving cancellation behaviour.]
- Repair SHA / focused verification result: [Verification: test_cancel_appointment PASSED
test_repeat_cancel_appointment PASSED]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [The practitioner conflict validation logic was not correctly identifying appointments with the same practitioner and appointment time. This was plausible because the system allowed a second booking for the same practitioner at the same time, suggesting the conflict detection condition was evaluating incorrectly.]
Evidence intended to inspect / competing explanation / discriminating check: [Evidence to inspect included the implementation of has_practitioner_conflict() in data_store.py. Competing explanations included: the conflict-check method was not being called, appoitnment times were being compared inccorectly, practitioner identifiers were being compared incorrectly. 
Discriminating check: Inspect the logic inside has_practitioner_conflict() and verify whether practitioner IDs are checked for equality or inequality.]
Member and saved sequence/time or commit showing this preceded consultation: [Alexandria - Hypothesis recorded immediately after observing failure: test_conflict_rule_and_different_practitionerbefore code modifications were made.]

### F8-02 human entry
Likely cause and why plausible: [The appointment lookup functionality was excluding cancelled appointments from search results. This was plausible because cancellation succeeded, but subsequent retrieval attempts returned LookupError.]
Evidence intended to inspect / competing explanation / discriminating check: [Evidence to inspect included: find_appointment(), cancellation logic, appointment storage after cancellation
Competing explanations included: cancellation deleting appointments from storage, lookup filtering cancelled appointments, appointment status being corrupted during cancellation.
Discriminating check: Inspect whether cancelled appointments remain present in _appointments after cancellation and verify the filtering conditions used by find_appointment().]
Member and saved sequence/time or commit showing this preceded consultation: [Alexandria - Hypothesis recorded after observing failures in test_cancel_appointment
test_repeat_cancel_appointment before any code changes were applied.]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|--------------------------|-------------------------------|---|
| F8-01 before repair | [2818c55]    | [complete]                     | [complete] |
| F8-01 after repair | [complete]     | [complete]                    | [complete] |
| F8-02 before repair | [2818c55]               | [complete]                    | [complete] |
| F8-02 after repair | [complete]               | [complete]                    | [complete] |
| Full suite after both repairs, before refactor | [complete]               | [complete]                    | [complete] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [The practitioner conflict test uses pytest.raises(ValueError) to verify that duplicate bookings for the same practitioner and time are rejected. If the conflict detection logic is incorrect, no exception is raised and the test fails.
The cancellation tests verify that cancelled appointments remain retrievable and retain the correct status. These tests ensure that cancellation changes state without removing appointment history. Retaining these tests prevents future changes from reintroducing either defect.]
Unrelated failures investigated / resolution: [Not applicable. The only initial issues encountered were Python import/environment issues caused by running tests from an incorrect context. Once the project was run from the correct working directory, the failing tests corresponded directly to the injected Stage 8 faults.]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [One possible diagnosis was that the appointment cancellation process was removing appointments from the data store. This was initially plausible because cancelled appointments could no longer be found. However, there was no direct evidence supporting this claim. Inspection of the code showed that appointments remained stored and that the real issue was the filtering logic inside find_appointment(), which excluded appointments with a cancelled status.]
2. What evidence changed your group's view? [Inspection of SmartCareDataStore.find_appointment() and SmartCareDataStore.has_practitioner_conflict() changed our understanding of the faults. The code review showed that cancelled appointments were being filtered from lookup results and that practitioner conflicts were being checked using an incorrect inequality comparison. This evidence allowed us to identify the actual root causes rather than relying on assumptions.]
3. How did regression tests protect the refactoring? [The regression tests verified that the required behaviour remained unchanged after repairs and refactoring. Tests covering appointment cancellation, retained appointment history, practitioner conflict detection, and lookup functionality ensured that structural improvements did not introduce new defects or break existing functionality.]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [An engineer should reproduce the failure, identify the expected behaviour from the requirements, collect evidence, and form a hypothesis about the cause before making any code changes.]

2. Where should expected behaviour come from during debugging?

Response: [Expected behaviour should come from the project requirements, acceptance criteria, specifications, and documented business rules rather than assumptions.]

3. What is a debugging hypothesis?

Response: [A debugging hypothesis is a proposed explanation for an observed fault that can be tested using evidence gathered from the code, tests, runtime behaviour, and documentation.]

4. What is a regression test and why is it retained?

Response: [A regression test is a test that verifies previously working behaviour continues to function after changes are made. It is retained to prevent old defects from being reintroduced in future updates.]

5. What is meant by root cause?

Response: [The root cause is the underlying defect that directly produces an observed failure. Fixing the root cause removes the defect rather than simply masking its symptoms.]

6. What is refactoring?

Response: [Refactoring is the process of improving the internal structure, readability, or maintainability of code while preserving its externally observable behaviour.]

7. What is a swallowed exception?

Response: [A swallowed exception occurs when an exception is caught and ignored without being properly reported, logged, or handled. This can hide faults and make debugging more difficult.]

8. What is a code smell?

Response: [A code smell is a characteristic of code that suggests a potential design, maintainability, or readability problem. It may not be a bug but often indicates an opportunity for refactoring.]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [GitHub Copilot diagnoses should be treated as hypotheses rather than facts. Each suggestion should be verified against code inspection, test results, requirements, and runtime evidence before being accepted or acted upon.]

10. What is the Stage 8 engineering rule?

Response: [The Stage 8 engineering rule is to follow an evidence-based debugging process: reproduce the fault, identify expected behaviour from requirements, form and test hypotheses, determine the root cause, apply the smallest justified repair, verify the fix with regression tests, and ensure any refactoring preserves behaviour.]

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
