# Goal Contract: [NAME]

**Status:** Proposed / Approved / Superseded  
**Owner:** [OWNER]  
**Last updated:** [DATE]  
**Current branch/SHA:** [OPTIONAL]  
**Execution profile:** [PROFILE]  
**Progress state:** [EXISTING ARTIFACT OR `GOAL_PROGRESS.md`]

## Target

> [Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.

## Why this is next

[One short paragraph grounded in repository evidence and current priorities.]

## In scope

- [Required outcome or surface]

## Out of scope

- [Explicit exclusion]

## Acceptance evidence

| ID | Criterion | Verifier or observable evidence | Status |
|---|---|---|---|
| A1 | [MEASURABLE END STATE] | `[EXACT COMMAND]` or [REALISTIC WORKFLOW / ARTIFACT] | Not run |
| A2 | No new failures relative to the recorded baseline | [RELEVANT BROADER GATES] | Not run |
| A3 | Important changes reviewed and unexplained diffs resolved | [REVIEW EVIDENCE] | Not run |

An item becomes **Pass** only when its stated evidence has been produced under the required conditions.

## Protected behavior

- [Existing contract, workflow, compatibility requirement, user work, local modification, or performance characteristic that must survive]

## Baseline and known exceptions

- `[COMMAND OR WORKFLOW]` — Pass / Fail / Blocked / Not run — [RELEVANT RESULT]
- Preserved working changes: [PATHS OR NONE]
- Known pre-existing failures or accepted risks: [LIST OR NONE]

## Authority boundaries

Explicit approval is required before:

- Deployment, publishing, release, merge, push, tag, or production changes unless expressly authorized here
- Destructive data, schema, branch, or infrastructure operations
- Credential, billing, account, secret, or external-system changes
- Removal of a required rollback or recovery path
- [REPOSITORY-SPECIFIC BOUNDARY]

**Explicitly authorized actions:** [NONE OR PRECISE LIST]

## Stop and escalation

- **Success:** Every acceptance item passes with surfaced evidence and protected behavior has not regressed.
- **Blocked:** A named external dependency, credential, hardware resource, lawful-access requirement, or owner decision prevents progress.
- **Approval required:** The next useful action crosses an authority boundary above.
- **Budget:** [TURN, TIME, OR COST BOUND]
- **Stalled:** Two serious iterations produce neither new evidence nor measurable progress.

Blocked, approval-required, budget-exhausted, and stalled outcomes require a restartable handoff and are not success.

## Sources of truth

- [APPROVED ISSUE, PRD, PLAN, MILESTONE, ARCHITECTURE DOCUMENT, TEST SUITE, OR OTHER AUTHORITATIVE SOURCE]

List contradictions that remain relevant and their disposition rather than silently choosing one source.

## Execution profile notes

**Primary profile:** [ONE OF THE CORE OR SPECIALIST PROFILES]

[Only profile-specific constraints that are not already captured above. Do not duplicate the whole profile.]

## Native `/goal` command

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [THIS PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

## Approval record

- [DATE] — [OWNER] approved this contract and its authority boundaries.
