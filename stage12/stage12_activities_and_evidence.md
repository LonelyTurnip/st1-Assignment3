# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Mon 2:30 - 4:30 Group 4
Members and UG/PG applicability: 
    Aidan - LonelyTurnip - UG
    Alexandria - xereinera - UG
    Archie - Arch2ey - UG


## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2S
Common starting SHA / branch / applicable members: 528589eb133a550eee1f1a4533cdb44c492baa62 / origin/stage12 / all members (UG)
PG starting SHA / branch / applicable members or not applicable: Not applicable. UG-only group, Stages 10 and 11 not undertaken
Working-state review and approved integration: [response]
Protected common candidate and PG differences: The common candidate is the only candidate; there are no PG differences
Feature freeze / owner / verifier: [response]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [Release with conditions. Because of the tests passing the program has been shown to be functional. Prior to release, the README setup needs to be completed to ensure users can install the program. The dependency should also be reviewed to check for potential issues that could arise from the dependency. The limitation in the program should be documents in the README so users are aware of the limitation. Once these three conditions have been met, the program should be ready for release.]

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | [User can view cancellation history] | [response] | [response] | [response] | [response] |
| Architecture responsibilities are appropriate | [Each function is responsbile for one thing and does not negatively impact any other function] | [response] | [response] | [response] | [response] |
| Rescheduling is safe — PG only | [response] | [response] | [response] | [response] | [response] |
| AI use is responsible — common recheck / PG assurance | [response] | [response] | [response] | [response] | [response] |
| System is maintainable | [System can be scaled and each function is easily identifiable in case of debugging.] | [response] | [response] | [response] | [response] |
| FR-01–03 register/find and validation | [FR1 and FR2 are both functional with verifiable test results] | [response] | [response] | [response] | [response] |
| FR-04–05 booking/conflict rules | [FR4 and FR5 are both functional with verifiable test results] | [response] | [response] | [response] | [response] |
| FR-06–08 cancellation/history/find | [FR6 and FR8 are both functional with verifiable test results] | [response] | [response] | [response] | [response] |
| FR-09 and QRY/FP listing/filter/order/purity | [response] | [response] | [response] | [response] | [response] |
| UI full console sequence and error recovery | [Console UI is implemented and all functions are connect properly with verifiable tests proving each console option works.] | [response] | [response] | [response] | [response] |
| Session-only scope / FR-10 retired | [response] | [response] | [response] | [response] | [response] |
| PG RES and assurance integration | [response] | [response] | [response] | [response] | [response] |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [response] | [response] | [response] | [response] | [response] |
| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |
| Affected focused checks after correction | [response] | [response] | [response] | [response] | [response] |
| Full integrated recheck | [response] | [response] | [response] | [response] | [response] |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [Register a Patient and Register 2 practitioners. Run find patient and find practitioner. Input: 1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 3, D2, Dan Wilson, General Practitioner, 2, P1, 4, D1, 4, D2] | [The program will register the patient and practitioners and return their information when called.] | [Program succesfully registers the patient and practitioners and returns their information when called.] | [response] |
| Valid booking | [Register a patient and practitioner and use information to book an appointment. Input: 1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 5, A1, P1, D1, 2026-10-10 10:00] | [Program will succesfully book an appointment.] | [Program succesfully books an appointment for patient 1 with practitioner 1] | [response] |
| Same practitioner exact-time conflict rejected | [Try to book a second appointment using the same practitioner at the same time as a previously booked appointment] | [Input: 1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 5, A1, P1, D1, 2026-10-10 10:00, 5, A2, P1, D1, 2026-10-10 10:00] | [Program returned Error: Practitioner already has a scheduled appointment at this time. Program continues to run] | [response] |
| Different practitioner same time allowed | [Try to book an appointment with a different practitioner at the same time as an appointment booked with first practitioner. Input: 1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 3, D2, Dan Wilson, General Practitioner, 2, P1, 4, D1, 4, D2, 5, A1, P1, D1, 2026-10-10 10:00, 5, A2, P1, D2, 2026-10-10 10:00] | [Appointment will be succesfully booked] | [Program succesfully books appointment at same time as previous appointment booking but with different practitioner] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [Cancel a scheduled appointment and then find the cancelled appointment. Input: 1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 3, D2, Dan Wilson, General Practitioner, 2, P1, 4, D1, 4, D2, 5, A1, P1, D1, 2026-10-10 10:00, 5, A2, P1, D2, 2026-10-10 10:00, 6, A1, 7, A1] | [The appointment will succesfully be cancelled and when find appointment is called it will still return a value.] | [Program succesfully cancels a scheduled appointment and then retains that information to return the appointment when called in find appointment.] | [response] |
| Invalid/repeated cancellation rejected | [Cancel an appointment that has already been cancelled. Input:1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 3, D2, Dan Wilson, General Practitioner, 2, P1, 4, D1, 4, D2, 5, A1, P1, D1, 2026-10-10 10:00, 5, A2, P1, D2, 2026-10-10 10:00, 6, A1, 6, A1] | [Program will return a message saying that cancelled appointments cannot be cancelled.] | [Program returns Error message: Only SCHEDULED appointments may be cancelled.] | [response] |
| Default all-status listing | [A practitioner will be given multiple appointments and then then list practitioner appointments will be called. Input: Input:1, P1, John Smith, 3, D1, Greg Stevens, General Practitioner, 3, D2, Dan Wilson, General Practitioner, 2, P1, 4, D1, 4, D2, 5, A1, P1, D1, 2026-10-10 10:00, 5, A2, P1, D1, 2026-10-14 10:00, 5, A3, P1, D1, 2026-10-18 10:00] | [When find practitioner appointments is called a list of all appointments for that practitioner will be returned] | [A list of all appointments registered to that practitioner were returned.] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [response] | [response] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [response] | [response] | [response] | [response] |
| Session-only limitation and normal exit | [response] | [response] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [response] | [response] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [response] | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: Not Applicable
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [A release candidate is a version of the program that contains all features in a stable state that could be release as the final version. A release candidate can not turn into the full release version if any major bugs come up while testsing.]

2. What is feature freeze and why is it used? [A feature freeze is the point in the product development lifecycle where major changes or additional features are reduced or even stopped. A feature freeze is used to help reach a release stage through reducing major changes made.]

3. What is regression testing in a release context? [Regression testing is a form of testing to make sure that new additions to the source code do not iinadvertently break any other features in the program. It ensures that any changes made to the source code does not break the program.]

4. What is a known limitation? [A known limitation is a flaw, missing feature or constraint that is known by the developers that is yet to be implemented in the current version.]

5. What is technical debt? [Technical debt describes the cost of maintaining software. This is usually brought up when deciding if an issue should be solved with an easy to implement solution that could cause problems later on or solving the issue with a solution that takes more time to develop but ensures fewer problems in the future.]

6. What are release notes? [Release notes are a document released along side a program release or update. Release notes explain what features the program has and the purpose of the program. When release notes are released with an update, the release notes will explain what has been changed from the prior version.]

7. What is software maintenance? [Software maintenance is the practice of updating, modifying and optimising code after it has been released. This practice is used to improve the program performance and fix any bugs not found or fixed prior to release.]

8. What is the purpose of the individual demonstration/viva? [The purpose of the individual demonstration/viva is to showcase individual understanding and contribution on the project.]

9. What should the final responsible-AI check establish before release? [The final responsible-AI check before release should establish that AI-generated decisions should be communicated, function as intended and code generated is safe for release.]

10. What is the main course conclusion about AI and the role of the software engineer? [The main course conclusion about AI and the role of the software engineer is that AI can be used an effective tool when used properly and guided by a software engineer in the production of code for a program. AI does not fully replace the role of a software engineer as there still needs to be a code review conducted prior to AI written code being approved.]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [Even though AI can write code, software engineers are still required in the production of software. This is because there are certain tasks that AI cannot effectively complete without assitance from software engineers. Software engineers are still required to create guidelines and prompts to help guide the AI to succesfully create propper code. Software engineers are also still needed to ensure the quality of code meets the standard required and also that the program has no major flaws or security risks. Software engineers still need the ability to read code and understand the logic behind algorithms so they can modify code provided by AI.]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | Not Applicable |
| PG responsible-AI risk/remediation or supported no finding | Not Applicable |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
