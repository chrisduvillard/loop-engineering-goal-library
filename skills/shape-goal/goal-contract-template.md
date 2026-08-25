# Goal Contract: [NAME]

**Status:** Proposed / Ready / Active / Paused / Blocked / Closed  
**Outcome:** — / Achieved / Cancelled / Superseded / Approval required / Budget exhausted / Stalled  
**Goal ID:** [ID]  
**Revision:** [INTEGER]  
**Priority:** P0 / P1 / P2 / P3  
**Owner:** [OWNER]  
**Created / updated:** [DATES]  
**Library:** chrisduvillard/loop-engineering-goal-library @ [VERSION OR COMMIT]  
**Launcher:** [GOAL FILE / DIRECT SHAPING / AUTHORITATIVE ISSUE]  
**Input ledger:** [THIS DOCUMENT SECTION / PATH]  
**Branch / worktree / SHA:** [OPTIONAL]  
**Primary profile:** [ONE OF THE CATALOG PROFILES OR CUSTOM CONTRACT-DRIVEN]  
**Assurance overlays:** [LIST OR NONE]  
**Project harness:** [EXISTING SOURCES OR `docs/agent/PROJECT_HARNESS.md`]  
**Parent goal:** [ID OR NONE]  
**Depends on:** [IDS OR NONE]  
**Supersedes:** [ID OR NONE]  
**Portfolio:** [EXISTING TRACKER / `docs/goals/PORTFOLIO.md` / NOT NEEDED]  
**Progress state:** [EXISTING ARTIFACT OR `GOAL_PROGRESS.md`]  
**Archive path:** [EXISTING CONVENTION OR `docs/goals/[GOAL ID]/`]

## Target

> [Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.

## Why this is next

[Short evidence-backed priority and dependency rationale.]

## Input resolution record

| Input | Resolution | Evidence or approved decision |
|---|---|---|
| Outcome | Evidence / Safe default / Owner decision | [SOURCE] |
| Scope and exclusions | ... | ... |
| Acceptance evidence | ... | ... |
| Protected behavior | ... | ... |
| Authority boundaries | ... | ... |
| Profile-specific inputs | ... | ... |

Every material row must be resolved before approval. Searchable repository facts are not user questions.

## In scope

- [REQUIRED OUTCOME OR SURFACE]

## Out of scope

- [EXPLICIT EXCLUSION]

## Acceptance evidence

| ID | Criterion | Verifier or observable evidence | Status |
|---|---|---|---|
| A1 | [MEASURABLE END STATE] | `[EXACT COMMAND]` or [WORKFLOW / ARTIFACT] | Not run |
| A2 | No new failures relative to baseline | [BROADER GATES] | Not run |
| A3 | Important changes reviewed | [REVIEW EVIDENCE] | Not run |

An item becomes **Pass** only after its stated evidence is produced under the required conditions.

## Protected behavior

- [EXISTING CONTRACT, WORKFLOW, COMPATIBILITY, DATA INVARIANT, USER WORK, VISUAL REFERENCE, OR PERFORMANCE FLOOR]

## Baseline and known exceptions

- `[COMMAND OR WORKFLOW]` — Pass / Fail / Blocked / Not run — [RESULT]
- Preserved working changes: [PATHS OR NONE]
- Known pre-existing failures or accepted risks: [LIST OR NONE]

## Execution pattern

### Primary profile

[PROFILE]

### Profile-specific inputs

- [RESOLVED INPUT AND SOURCE]

### Custom Contract-Driven fields

Complete only when no preset fits:

- **Iteration unit:** [BOUNDED CHANGE OR EXPERIMENT]
- **Primary verifier:** [COMMAND / WORKFLOW / MEASUREMENT]
- **Keep-or-revert rule:** [DECISION]
- **Review strategy:** [REVIEW]
- **Stop condition:** [END STATE]

### Assurance overlays

- [OVERLAY] — [CONTRACT-SPECIFIC OBLIGATION]

## Goal relationships and change policy

- Parent / children: [RELATIONSHIPS OR NONE]
- Dependencies: [RELATIONSHIPS OR NONE]
- Related or superseded goals: [RELATIONSHIPS OR NONE]

Keep this Goal ID only while the observable outcome remains the same.

- Clarifications record a revision note.
- Material contract changes pause execution, require approval, and increment revision.
- A different outcome receives a new Goal ID.
- Unrelated requests enter the portfolio rather than this contract.

## Goal-drift review triggers

Re-run `shape-goal` when:

- [PRIORITY / REQUIREMENT / INCIDENT / DEPENDENCY / DATE / CHECKPOINT]

## Authority boundaries

Explicit approval is required before:

- Merge, push, tag, publish, release, deployment, or production mutation unless authorized here
- Destructive data, schema, branch, or infrastructure operations
- Credential, billing, account, secret, or external-system changes
- Removal of a required rollback or recovery path
- Security testing outside approved scope
- Legal, regulatory, privacy, compliance, or risk-acceptance conclusions
- [REPOSITORY-SPECIFIC BOUNDARY]

**Explicitly authorized actions:** [NONE OR PRECISE LIST]

## Stop and escalation

- **Success:** Every acceptance and required overlay item passes with surfaced evidence and protected behavior has not regressed.
- **Blocked:** A named external dependency, credential, hardware resource, lawful-access requirement, or owner decision prevents progress.
- **Approval required:** The next useful action crosses an authority boundary.
- **Budget:** [TURN / TIME / COST / EXPERIMENT BOUND]
- **Stalled:** Two serious iterations produce neither new evidence nor measurable progress.
- **Goal drift:** Pause and return to `shape-goal` when the contract no longer represents the desired outcome.

## Sources of truth

- [APPROVED ISSUE, PRD, PLAN, MILESTONE, ARCHITECTURE, DESIGN FILE, TEST SUITE, RUNBOOK, OR OTHER SOURCE]

Record relevant contradictions and their disposition.

## Reuse and closeout

At terminal closeout preserve:

```text
[ARCHIVE PATH]/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Update goal history and portfolio. Promote verified knowledge to tests, ADRs/docs, runbooks, design references, project harness, fixtures, scripts, benchmarks, or residual-risk records.

Never archive secrets, private user data, production dumps, exploit-enabling evidence, or unnecessary large logs.

**Expected reusable outputs:** [LIST OR NONE]

## Native `/goal` command

Strict two-step mode:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## Revision and approval record

| Revision | Date | Change | Lifecycle decision | Approved by |
|---|---|---|---|---|
| 1 | [DATE] | Initial contract | New | [OWNER] |
