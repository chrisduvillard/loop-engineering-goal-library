# Goal Engine: State and Evidence

Use the repository's existing plan, progress, issue, milestone, or handoff format when it can represent the state below. Do **not** create a competing source of truth merely because this template exists.

When no suitable artifact exists, create `GOAL_PROGRESS.md` beside `GOAL.md`.

## Minimal progress state

```markdown
# Goal Progress: [CONTRACT NAME]

**Contract:** [PATH OR ISSUE]  
**Profile:** [EXECUTION PROFILE]  
**Branch/SHA:** [BRANCH] / [SHA]  
**Last checkpoint:** [DATE OR SESSION]

## Baseline

- `[COMMAND OR WORKFLOW]` — Pass / Fail / Blocked / Not run — [RELEVANT RESULT]
- Preserved working changes: [PATHS OR NONE]
- Known pre-existing failures: [LIST OR NONE]

## Acceptance ledger

| ID | Acceptance item | Verifier | Status | Evidence |
|---|---|---|---|---|
| A1 | [CRITERION] | `[COMMAND OR FLOW]` | Not run | — |

## Completed changes

- [PRODUCTION CHANGE] — [EVIDENCE]

## Failed or reverted approaches

- [APPROACH] — [WHY IT FAILED OR WAS REVERTED]

## Open contradictions and risks

- [CONTRADICTION OR RISK] — [CURRENT DISPOSITION]

## Blockers and approvals

- [BLOCKER OR APPROVAL NEEDED] — [OWNER / EXTERNAL DEPENDENCY]

## Next action

[ONE HIGHEST-PRIORITY UNBLOCKED ACTION]
```

## Evidence quality

Prefer evidence in this order:

1. Deterministic repository-native commands with exact results
2. Reproduction or realistic runtime workflow
3. Integration, E2E, UAT, security, performance, or migration evidence
4. Reviewed diff tied to the contract
5. Stable rubric-based evaluation for subjective properties
6. Code inspection or agent judgment only as supporting context

An acceptance item is **Pass** only when its stated verifier has run successfully under the required conditions. “Implemented,” “reviewed,” or “looks correct” is not a verifier.

## Baseline discipline

- Record pre-existing failures before changing them.
- Do not hide regressions by redefining the baseline after edits.
- If a verifier must change because the requirement changed, obtain the contract-required approval and explain the before/after semantics.
- A narrower targeted check may guide an iteration; the contract's broader final gates still determine completion.

## Keep-or-revert rule

Keep a change only when it:

- Advances at least one contract acceptance item or removes a verified blocker
- Preserves protected behavior
- Does not introduce unexplained new failures
- Has a coherent, reviewable diff

Otherwise revert only the agent-authored slice when safe. Never discard unrelated or user-authored work.

## No-progress accounting

Count a serious cycle as progress only when it produces at least one of:

- New verified evidence
- A smaller reproducible failure
- A changed and testable hypothesis
- A closed acceptance gap
- A newly proven external blocker or approval boundary

Record no-progress cycles explicitly. Reset the count only when one of those outcomes occurs.

## Checkpoint update

At each meaningful checkpoint, surface and persist:

```text
Profile:
Current gap:
Change made:
Verifier and result:
Acceptance items changed:
Regression status:
Review status:
No-progress count:
Remaining highest-priority gap:
Blocker or approval needed:
```

## Completion packet

```markdown
## Goal closeout

**Outcome:** Achieved / Blocked / Approval required / Budget exhausted / Stalled

### Acceptance evidence

| ID | Status | Evidence |
|---|---|---|

### Delivered behavior

- [CHANGE]

### Regression and review status

- [CHECKS, PROTECTED BEHAVIOR, AND REVIEW]

### Residual risk

- [BOUNDED RISK OR NONE]

### Restart information

- State artifact: [PATH OR ISSUE]
- Branch/SHA: [BRANCH] / [SHA]
- Next action: [ONLY WHEN NOT ACHIEVED]
```
