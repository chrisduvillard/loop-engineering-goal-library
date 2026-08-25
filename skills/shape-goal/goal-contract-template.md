# Goal Contract: [NAME]

**Status:** Proposed  
**Owner:** [OWNER]  
**Last updated:** [DATE]  
**Current branch/SHA:** [OPTIONAL]

## Target

> [Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.

## Why this is next

[One short paragraph grounded in repository evidence and current priorities.]

## In scope

- [Required outcome or surface]

## Out of scope

- [Explicit exclusion]

## Acceptance evidence

- [ ] [Exact command, workflow, measurement, or observable artifact]
- [ ] No new failures relative to the recorded baseline
- [ ] Important changes reviewed and unexplained diffs resolved

## Protected behavior

- [Existing contract, workflow, compatibility requirement, user work, or local modification that must survive]

## Authority boundaries

Explicit approval is required before:

- Deployment, publishing, release, merge, or production changes
- Destructive data or infrastructure operations
- Credential, billing, account, or external-system changes
- [Repository-specific boundary]

## Stop and escalation

- **Success:** Every acceptance item passes with surfaced evidence.
- **Blocked:** A named external dependency, credential, hardware resource, lawful-access requirement, or owner decision prevents progress.
- **Budget:** [TURN, TIME, OR COST BOUND]
- **Stalled:** Two serious iterations produce neither new evidence nor measurable progress.

Blocked, budget-exhausted, and stalled outcomes require a restartable handoff and are not success.

## Sources of truth

- [Approved issue, PRD, plan, milestone, architecture document, test suite, or other authoritative source]

## Baseline and known exceptions

- [Relevant current check results, pre-existing failures, unresolved contradictions, or accepted risks]

## Selected loop

[Brownfield Continue / Finish, PRD / Spec Compliance, Next Milestone, Deep Audit + Remediation, QA / Regression / UAT, Safe Refactor / Modernization, Release Readiness, or a specialist loop]
