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
**Shaping history:** [EXISTING DECISION LOG OR `docs/goals/[GOAL ID]/SHAPING.md`]
**Completed shaping rounds:** [COUNT / IDS]
**Last shaping round:** [ROUND ID]
**Approval shaping round:** [ROUND ID OR NONE]
**Approval fingerprint:** [GOAL ID + REVISION + APPROVAL ROUND + APPROVED SOURCE SHA/HASH]
**Execution lease:** Not acquired / [SESSION OR WORKTREE + OWNER + ACQUIRED + EXPIRY OR RENEWAL]
**Shaping depth:** Adaptive / Thorough / Exhaustive
**Clarity gate:** Not run / Needs clarification / Pass
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

## Shaping history and decision trace

- **History path:** [PATH]
- **Current decision source:** [ROUND / QUESTION IDS]
- **Open or deferred decisions:** [LIST OR NONE]
- **Corrections or superseded answers:** [IDS OR NONE]
- **Approval basis:** [ROUND SUMMARY AND APPROVER]

The detailed questions, answers, evidence, recommendations, and corrections live in the shaping history. Do not duplicate the full interview here.

## Input resolution record

| Input | Resolution | Impact | Confidence | Assumption class | Evidence or approved decision source |
|---|---|---|---|---|---|
| Outcome | Evidence / Safe default / Owner decision / N/A | High | Confirmed / Strong / Tentative / Unknown | Evidence / Owner / Safe default / Unresolved | [SOURCE OR QUESTION ID] |
| Users and journey boundary | ... | ... | ... | ... | ... |
| Scope and exclusions | ... | ... | ... | ... | ... |
| Acceptance evidence | ... | ... | ... | ... | ... |
| Protected behavior | ... | ... | ... | ... | ... |
| Failure and edge cases | ... | ... | ... | ... | ... |
| Data, compatibility, and dependencies | ... | ... | ... | ... | ... |
| Authority boundaries | ... | ... | ... | ... | ... |
| Ownership and reusable outputs | ... | ... | ... | ... | ... |
| Profile-specific inputs | ... | ... | ... | ... | ... |

Every material row must be resolved before approval. Searchable repository facts are not user questions. Every applicable universal clarity lens must be resolved or marked Not applicable with a reason.

## Assumptions and interpretation register

| ID | Assumption or term | Requirement strength | Class | Impact | Evidence / approval | Treatment |
|---|---|---|---|---|---|---|
| AS1 | [ASSUMPTION OR AMBIGUOUS TERM] | Must / Should / Preference / Optional / Non-goal | Evidence-backed / Owner-approved / Delegated / Safe default / Unresolved | High / Medium / Low | [SOURCE OR QUESTION ID] | Keep / Clarify / Exclude / Block |

No High- or Medium-impact unresolved assumption may remain. Operationally define subjective terms and surface every safe default before approval.

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

## Clarity stress test

| Check | Result | Evidence or decision source |
|---|---|---|
| Fresh-reader review | Pass / Needs clarification | [REVIEW / QUESTION IDS] |
| Counterexample loophole | Closed / Open | [RESULT] |
| Happy, failure, and regression scenarios | Pass / N/A / Needs clarification | [SCENARIOS] |
| Verifier executability | Pass / Needs clarification | [COMMANDS / ARTIFACTS] |
| Contradiction and traceability review | Pass / Needs clarification | [SOURCES] |
| Plain-English teach-back | Confirmed / Corrected | [QUESTION ID] |

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

- Clarifications append a shaping entry and revision note.
- Material contract changes pause execution, require a new shaping round and approval, and increment revision.
- A different outcome receives a new Goal ID.
- Unrelated requests enter the portfolio rather than this contract.
- Prior questions and answers remain immutable; corrections append and supersede them.

## Goal-drift review triggers

Re-run `shape-goal` and append a new shaping round when:

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
- **Shaping not accepted:** Preserve the draft and history; run another round or pause rather than beginning production work.

## Sources of truth

- [APPROVED ISSUE, PRD, PLAN, MILESTONE, ARCHITECTURE, DESIGN FILE, TEST SUITE, RUNBOOK, OR OTHER SOURCE]

Record relevant contradictions and their disposition.

## Reuse and closeout

At terminal closeout preserve:

```text
[ARCHIVE PATH]/
├── SHAPING.md
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Update goal history and portfolio. Promote verified knowledge to tests, ADRs/docs, runbooks, design references, project harness, fixtures, scripts, benchmarks, or residual-risk records.

Never archive secrets, private user data, production dumps, exploit-enabling evidence, or unnecessary large logs. Redact sensitive shaping answers and link approved secure evidence instead.

**Expected reusable outputs:** [LIST OR NONE]

## Native `/goal` command

Strict two-step mode:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, project harness, and shaping decision record. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## Pre-approval clarity gate

- [ ] No High- or Medium-impact input or assumption is unresolved.
- [ ] Every answer has one material interpretation or a saved clarification, and its requirement strength is preserved.
- [ ] Every delegated judgment has explicit criteria and boundaries.
- [ ] Every subjective term has a verifier, rubric, example, reference, or qualified reviewer.
- [ ] Fresh-reader and counterexample checks reveal no blocking ambiguity.
- [ ] Safe defaults and residual low-impact assumptions are visible in the teach-back.
- [ ] The user explicitly approved the plain-English interpretation.

## Revision and approval record

| Revision | Date | Change | Lifecycle decision | Shaping round | Approved by |
|---|---|---|---|---|---|
| 1 | [DATE] | Initial contract | New | [ROUND ID] | [OWNER] |

## Execution controls

- Mutation mode: `read_only` | `propose_patch` | `apply_verified_fixes`
- Assurance level: `lite` | `standard` | `high`
- Canonical state: `.loop/goals/<goal-id>/contract.json`
- Approval fingerprint algorithm: `goalctl-v1-sha256`
- Generated human view: `GOAL.md` (do not edit directly)
- Private shaping journal: `.loop/private/<goal-id>/` (ignored and never committed)

`read_only` is the default for review, audit, assessment, inspection, and
evaluation requests. Remediation requires separate explicit authorization.

## State and termination model

- Goal status: `candidate` | `ready` | `active` | `paused` | `blocked` | `closed`
- Run termination: `achieved` | `approval_required` | `budget_exhausted` |
  `stalled` | `external_blocked` | `safety_stop` | `cancelled_by_user` |
  `host_failure`
- Final goal outcome: `achieved` | `cancelled` | `superseded` | `abandoned`

A run termination is not automatically a final goal outcome. A goal with
`approval_required`, `budget_exhausted`, `stalled`, or `external_blocked`
remains resumable unless it is explicitly closed.
