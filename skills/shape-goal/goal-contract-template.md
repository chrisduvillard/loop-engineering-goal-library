# Goal Contract: [NAME]

**Status:** Proposed / Ready / Active / Paused / Blocked / Closed  
**Outcome:** — / Achieved / Cancelled / Superseded / Approval required / Budget exhausted / Stalled  
**Goal ID:** [YYYY-MM-DD-SHORT-SLUG OR ISSUE/MILESTONE ID]  
**Revision:** [INTEGER]  
**Priority:** P0 / P1 / P2 / P3  
**Owner:** [OWNER]  
**Created:** [DATE]  
**Last updated:** [DATE]  
**Library:** chrisduvillard/loop-engineering-goal-library @ [VERSION OR SOURCE COMMIT]  
**Current branch/worktree/SHA:** [OPTIONAL]  
**Primary profile:** [PRESET OR CUSTOM CONTRACT-DRIVEN]  
**Assurance overlays:** [LIST OR NONE]  
**Project harness:** [EXISTING SOURCES OR `docs/agent/PROJECT_HARNESS.md`]  
**Parent goal:** [GOAL ID OR NONE]  
**Depends on:** [GOAL IDS OR NONE]  
**Supersedes:** [GOAL ID OR NONE]  
**Portfolio:** [EXISTING TRACKER / `docs/goals/PORTFOLIO.md` / NOT NEEDED]  
**Progress state:** [EXISTING ARTIFACT OR `GOAL_PROGRESS.md`]  
**Archive path:** [EXISTING CONVENTION OR `docs/goals/[GOAL ID]/`]

## Target

> [Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.

## Why this is next

[One short paragraph grounded in repository evidence, priority, dependencies, and current user need.]

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

- [EXISTING CONTRACT, WORKFLOW, COMPATIBILITY, DATA INVARIANT, USER WORK, OR PERFORMANCE CHARACTERISTIC]

## Baseline and known exceptions

- `[COMMAND OR WORKFLOW]` — Pass / Fail / Blocked / Not run — [RESULT]
- Preserved working changes: [PATHS OR NONE]
- Known pre-existing failures or accepted risks: [LIST OR NONE]

## Execution pattern

### Primary profile

[ONE OF THE ELEVEN PRESETS OR CUSTOM CONTRACT-DRIVEN]

For a custom profile, define:

- **Iteration unit:** [BOUNDED CHANGE OR EXPERIMENT]
- **Primary verifier:** [COMMAND / WORKFLOW / MEASUREMENT]
- **Keep-or-revert rule:** [DECISION]
- **Review strategy:** [REVIEW]
- **Stop condition:** [END STATE]

### Assurance overlays

- [OVERLAY] — [CONTRACT-SPECIFIC OBLIGATION]

Use zero or more overlays from `assurance-overlays.md`; do not select overlays merely to appear comprehensive.

## Goal relationships and change policy

- **Parent / children:** [RELATIONSHIPS OR NONE]
- **Dependencies:** [RELATIONSHIPS OR NONE]
- **Related or superseded goals:** [RELATIONSHIPS OR NONE]

Keep this Goal ID only while the observable outcome remains the same.

- Clarifications may update wording and evidence references with a revision-log entry.
- Material changes to scope, evidence, protection, authority, profile, overlays, or exits require approval and a revision increment.
- A different observable outcome receives a new Goal ID.
- New unrelated requests are added to the portfolio rather than silently appended here.

## Goal-drift review triggers

Re-run `shape-goal` when:

- [PRIORITY / REQUIREMENT / INCIDENT / DEPENDENCY / DATE / CHECKPOINT]

## Authority boundaries

Explicit approval is required before:

- Deployment, publishing, release, merge, push, tag, or production changes unless expressly authorized here
- Destructive data, schema, branch, or infrastructure operations
- Credential, billing, account, secret, or external-system changes
- Removal of a required rollback or recovery path
- [REPOSITORY-SPECIFIC BOUNDARY]

**Explicitly authorized actions:** [NONE OR PRECISE LIST]

## Stop and escalation

- **Success:** Every acceptance item and required overlay gate passes with surfaced evidence and protected behavior has not regressed.
- **Blocked:** A named external dependency, credential, hardware resource, lawful-access requirement, or owner decision prevents progress.
- **Approval required:** The next useful action crosses an authority boundary.
- **Budget:** [TURN, TIME, OR COST BOUND]
- **Stalled:** Two serious iterations produce neither new evidence nor measurable progress.
- **Goal drift:** Pause and return to `shape-goal` when the current contract no longer represents the desired outcome.

## Sources of truth

- [APPROVED ISSUE, PRD, PLAN, MILESTONE, ARCHITECTURE DOCUMENT, TEST SUITE, OR OTHER SOURCE]

List relevant contradictions and their disposition rather than silently choosing one source.

## Reuse and closeout

At terminal closeout, preserve:

```text
[ARCHIVE PATH]/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Update the goal history and portfolio. Promote verified knowledge to regression tests, ADRs/docs, runbooks, project harness, fixtures, scripts, or benchmarks.

Do not archive secrets, credentials, private user data, raw production dumps, exploit-enabling evidence, or unnecessary large logs.

**Expected reusable outputs:** [TESTS / FIXTURES / ADRS / RUNBOOKS / HARNESS / COMMANDS / NONE]

## Native `/goal` command

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [THIS PATH OR ISSUE]. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## Revision and approval record

| Revision | Date | Change | Lifecycle decision | Approved by |
|---|---|---|---|---|
| 1 | [DATE] | Initial contract | New | [OWNER] |
