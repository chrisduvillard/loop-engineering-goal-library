# Goal Contract: Portfolio Import v1.4

**Status:** Closed  
**Outcome:** Achieved  
**Goal ID:** 2026-08-25-portfolio-import-v1-4  
**Revision:** 1  
**Priority:** P1  
**Owner:** Product owner  
**Created:** 2026-08-25  
**Last updated:** 2026-08-25  
**Library:** chrisduvillard/loop-engineering-goal-library @ 0.2.0  
**Current branch/worktree/SHA:** `codex/portfolio-import-v1-4` / isolated worktree / `def5678`  
**Primary profile:** PRD / Spec Compliance  
**Assurance overlays:** Data Integrity & Governance; Compatibility & Portability  
**Project harness:** `docs/agent/PROJECT_HARNESS.md`  
**Parent goal:** none  
**Depends on:** none  
**Supersedes:** none  
**Portfolio:** `docs/goals/PORTFOLIO.md`  
**Progress state:** `GOAL_PROGRESS.md`  
**Archive path:** `docs/goals/2026-08-25-portfolio-import-v1-4/`

## Target

> The documented portfolio import v1.4 workflow accepts every supported CSV and XLSX file, produces the approved validation behavior, passes its UAT matrix, and preserves existing portfolio exports.

## Why this is next

The approved v1.4 PRD is the current P1 milestone, CSV import is stable, and XLSX parsing is the only verified product gap blocking completion.

## In scope

- CSV and XLSX import entry points
- Spreadsheet date normalization
- Validation and user-facing import errors
- Documented import UAT cases
- Regression protection for existing exports

## Out of scope

- Broker adapters
- Performance optimization
- Redesign outside the import workflow
- Production deployment or release

## Acceptance evidence

| ID | Criterion | Verifier or observable evidence | Status |
|---|---|---|---|
| A1 | Import unit and integration behavior passes | `python -m pytest tests/imports` | Pass |
| A2 | Every approved import workflow succeeds from clean state | `python scripts/run_import_uat.py` | Pass |
| A3 | Existing exports remain unchanged | `python -m pytest tests/exports` | Pass |
| A4 | Repository-wide gates remain green | `make verify` | Pass |
| A5 | Important changes reviewed and unexplained diffs resolved | Independent diff review | Pass |

## Protected behavior

- Existing CSV imports and portfolio exports
- Public error codes consumed by the frontend
- User-authored working changes outside the feature

## Baseline and known exceptions

- `python -m pytest tests/imports` — Fail — 64 passed, 4 failed
- `python scripts/run_import_uat.py` — Fail — 9/12 passed
- `python -m pytest tests/exports` — Pass — 42 passed
- Preserved working changes: `notes/local-investigation.md`
- Known exceptions: none

## Execution pattern

### Primary profile

PRD / Spec Compliance — maintain a requirement-to-evidence map and never weaken the PRD or export verifiers.

### Assurance overlays

- Data Integrity & Governance — verify date semantics, malformed/blank cells, and no unexplained data drift.
- Compatibility & Portability — preserve CSV, export formats, and public error codes.

## Goal relationships and change policy

- Parent / children: none
- Dependencies: none
- Related goal: `2026-08-26-import-performance-budget` follows this goal but is a different outcome.

Performance work is explicitly out of scope and receives a new Goal ID rather than being appended here.

## Goal-drift review triggers

Re-run `shape-goal` if the PRD changes, a production incident interrupts the work, or performance becomes a higher priority before correctness is complete.

## Authority boundaries

Explicit approval is required before merge, push, tag, release, deployment, destructive operations, credential changes, removal of export compatibility, or changes to public error codes.

**Explicitly authorized actions:** local repository edits and repository-native verification only

## Stop and escalation

- Success: every acceptance and overlay item passes.
- Blocked: named external dependency or owner decision.
- Approval required: authority boundary crossed.
- Budget: 20 serious implementation cycles.
- Stalled: two no-progress cycles.
- Goal drift: pause and reshape rather than silently expand scope.

## Sources of truth

- `docs/product/portfolio-import-v1.4.md`
- `tests/imports/`
- `tests/exports/`
- `scripts/run_import_uat.py`
- Repository instructions and Git history

## Reuse and closeout

Archive: `docs/goals/2026-08-25-portfolio-import-v1-4/`

**Expected reusable outputs:** regression tests, parser fixture, normalization rule, and verified harness commands

## Native `/goal` command

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its PRD / Spec Compliance profile, Data Integrity & Governance and Compatibility & Portability overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## Revision and approval record

| Revision | Date | Change | Lifecycle decision | Approved by |
|---|---|---|---|---|
| 1 | 2026-08-25 | Initial contract | New | Product owner |
