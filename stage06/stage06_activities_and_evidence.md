# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Mon 2:30 - 4:30 Group 4
- Members, GitHub usernames and cohorts:
    Aidan - LonelyTurnip - UG
    Alexandria - xereinera - UG
    Archie - Arch2ey - UG
- Repository URL: https://github.com/LonelyTurnip/st1-Assignment3
- Starting SHA: a6672ff
## A Requirement to issue activities

### FR-02 Patient Search

- Title: [Feature - Patient Search]
- Context: [User looks up a patient using their ID.]
- Requirement: [If the user exists then their information will be returned. If the patient does not exist or the ID is invalid then an error message will return.]
- Acceptance criteria: [Patient can be searched by the ID. If a valid ID is given then the patient will be returned. If the ID is invalid or no patient exists then an error message will be returned.]
- Scope: [Allow users to search for a patient using a unique ID and return details]
- Definition of Done: [Patient search functionality is implemented and tested. Valid IDs return relevant information. Invalid IDs return correct error.]
- Owner: [response]
- Actual issue link: [response]

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: [Feature - Appointment Cancellation]
- Context: [User cancels a booked appointment]
- Requirement: [When the user cancels an appointment, if the appointment exists and is booked then the cancel will get canceled. If the appointment does not exist or is invalid then an error message will be returned.]
- Acceptance criteria: [If the user attempts to cancel a valid appointment then the appointment will be modified to be cancelled. If the user tries to cancel an appointment that has already been cancelled or does not exist then an error message will return.]
- Scope: [Allow users to cancel existing appointments while retaining appointment history.]
- Definition of Done: [Appoitment status chages to cancelled when a valid cancellation occurs. Appointment history remains stored.]
- Owner: [response]
- Actual issue link: [response]

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|----------------|---|
| changes | [Weak]         | [Provides no context for what has been changed in the commit] |
| final version | [Weak]         | [Does not explain why this is the final version. Code is also constantly being changes so stating this is the final version is a bad practice.] |
| Add patient search by ID | [Strong]       | [Explains what has been added in the commit] |
| fix stuff | [Weak]         | [Provides no context on what has been fixed] |
| Prevent cancellation of completed appointments | [Strong]       | [Clearly describes the behaviour change and the problem being addressed.] |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: [The pull request contains changes unrelated to appoitnment cancellation, thus, making the review large and difficult to understand.]
- Responsibility and architecture concerns: [Remaining patient fields and restructuring code may impact other features and violate separation. These changes should be reviewed independently.]
- Testing and review concerns: [Additional changes increase testing requirements and make it harder to determine if failure is caused by the cancellation feature or other modifications.]
- Changes to remove or separate, with reasons: [Rename changes, code restructuring, and dependency additions should be moved into separate pull requests so each change can be reviewed, tested and approved independently of one another]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [What tests passed? What the results of the tests were.]
- Follow-up review question 1: [What parts of the code did you test?]
- Follow-up review question 2: [What parts of the code did you not test?]
- Follow-up review question 3: [What were the results of the tests?]
- Follow-up review question 4: [What was the input and output of the tests?]
- Follow-up review question 5: [Did the tests return the expected output?]
- Additional questions if useful: [Were edge cases tested, such as invalid IDs or missing appointments? Were regression tests performed on existing functionality? Were automated tests, manual tests, or both used? Was test coverage reviewed for the modified code? Were any known limitations or failures identified during testing?]

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | [Either a branch including the work or the name of the person completing the work] |
| Commit message convention | [Short overview of what was added in the commit.] |
| PR size | [One element] |
| Another-member review requirement | [Yes] |
| Merge rule | [Yes] |
| Significant Copilot disclosure rule | [Yes] |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| [issue 1] | [FR-02 Patient Search] | [response] | [Search by valid ID returns patient information. Invalid ID returns an error.] | [Complete] |
| [issue 2] | [FR-06 Appointment Cancellation] | [response] | [Valid booked appointments can be cancelled. Invalid cancellations return errors.] | [Complete] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[A high commit count does not neccissarily show evidence of strong contribtuion. This is because the contents of the commits could be very minimal and only working on a small aspect of the project. An example could be a bunch of small commits changing spelling errors or formatting for one feature. In this scenario, lots of commits have been made but only one feature has been completed.]

## L Stage 6 formative questions

1. What is version control?

[Version control is a practice to help maintain and manage versions and changes of files]

2. Why is a feature branch useful?

[A feature branch is useful because it provides a safe way to test and build code without permanenetly changing the main source code files. This practice ensures that only changes that have passed testing are placed in the main branch.]

3. What makes a commit a good engineering commit?

[A good engineering commit is a concise statement that focuses on one element that has been changed. Good commits will only focus on one implemented feature and provide information on what has been done. Good commits are useful to help in debugging.]

4. What is a pull request?

[A pull request is a way for developers to submit code for it to be reviewed prior to being merged into the main branch.]

5. What is the purpose of code review?

[The purpose of code review is to make sure that it meets specifications and functions properly in the program. It is also so another developer is able to look at the code.]

6. What does a Git diff show?

[Git diff will show the difference between states in repositotries. This means that it will show what lines have been modified.]

7. What is a Definition of Done?

[A Definition of Done is an agreed upon description that outlines what is required in a feature for it meet the requirements of the project.]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[GitHub Copilot should be used as a supporting review tool rather than the final reviewer. Copilot can help identify potential bugs, coding issues, missing tests, or areas requiring attention, but a human reviewer must verify all suggestions and ensure the code meets the project requirements, architecture, and testing standards before approval.]

9. Why should individual contribution not be judged only by commit count?

[Individual contribution should not be judged only by commit count. This is because the contents of the commit could be small changes such as fixing up spelling mistakes in code or rewriting an already finished feature. This means that even though multiple commits are pushed very little has actually changed.]

10. What is the Stage 6 engineering rule?

[The Stage 6 engineering rule is that work must be completed through a structured Git workflow using issues, feature branches, commits, pull requests, code review, testing, and evidence-based approval before changes are merged into the main branch.]

## M Completion and handover

- Starting SHA: [a6672ff]
- Final Stage 6 code SHA: [f810488]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
