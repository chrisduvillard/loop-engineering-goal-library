# Goal Contract: Portfolio Import v1.4

**Status:** Closed  
**Goal ID:** 2026-08-25-portfolio-import-v1-4  
**Owner:** Product owner  
**Created:** 2026-08-25  
**Last updated:** 2026-08-25  
**Library:** chrisduvillard/loop-engineering-goal-library @ 0.1.0  
**Current branch/SHA:** `codex/portfolio-import-v1-4` / `abc1234`  
**Execution profile:** PRD / Spec Compliance  
**Progress state:** `GOAL_PROGRESS.md`  
**Archive path:** `docs/goals/2026-08-25-portfolio-import-v1-4/`

## Target

> The documented portfolio import v1.4 workflow accepts every supported CSV and XLSX file, produces the approved validation behavior, passes its UAT matrix, and preserves existing portfolio exports.

## Why this is next

The approved v1.4 PRD is the current milestone, CSV import is already stable, and XLSX parsing is the only verified product gap blocking completion.

## In scope

- CSV and XLSX import entry points
- Spreadsheet date normalization
- Validation and user-facing import errors
- Documented import UAT cases
- Regression protection for existing exports

## Out of scope

- New broker integrations
- Import performance optimization
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

- Existing CSV imports
- Existing portfolio export formats
- User-authored working changes outside the import feature
- Public error codes consumed by the frontend

## Baseline and known exceptions

- `python -m pytest tests/imports` — Fail — 4 XLSX date cases failed
- `python scripts/run_import_uat.py` — Fail — 9/12 passed
- `python -m pytest tests/exports` — Pass — 42 passed
- Preserved working changes: `notes/local-investigation.md`
- Known pre-existing failures or accepted risks: none

## Authority boundaries

Explicit approval is required before:

- Merge, push, tag, release, deployment, or production changes
- Destructive data or infrastructure operations
- Credential, billing, account, secret, or external-system changes
- Removing export compatibility or changing public error codes

**Explicitly authorized actions:** local repository edits and repository-native verification only

## Stop and escalation

- **Success:** Every acceptance item passes with surfaced evidence and protected behavior has not regressed.
- **Blocked:** A named external dependency or owner decision prevents progress.
- **Approval required:** The next action crosses an authority boundary.
- **Budget:** 20 serious implementation cycles.
- **Stalled:** Two serious iterations produce neither new evidence nor measurable progress.

## Sources of truth

- `docs/product/portfolio-import-v1.4.md`
- `tests/imports/`
- `tests/exports/`
- `scripts/run_import_uat.py`
- Repository instructions and current Git history

## Execution profile notes

**Primary profile:** PRD / Spec Compliance

Maintain a requirement-to-evidence map. Do not weaken the import PRD or existing export verifiers.

## Reuse and closeout

The closeout packet is stored at `docs/goals/2026-08-25-portfolio-import-v1-4/`.

**Expected reusable outputs:** regression tests, one parser fixture, and one documented normalization rule

## Native `/goal` command

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the PRD / Spec Compliance profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

## Approval record

- 2026-08-25 — Product owner approved this contract, archive path, and authority boundaries.
