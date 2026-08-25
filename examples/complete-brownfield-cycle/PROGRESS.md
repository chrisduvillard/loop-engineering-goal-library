# Goal Progress: Portfolio Import v1.4

**Goal ID:** 2026-08-25-portfolio-import-v1-4  
**Contract:** `GOAL.md`  
**Library:** chrisduvillard/loop-engineering-goal-library @ 0.1.0  
**Profile:** PRD / Spec Compliance  
**Branch/SHA:** `codex/portfolio-import-v1-4` / `def5678`  
**Last checkpoint:** 2026-08-25 closeout  
**No-progress count:** 0

## Baseline

- `python -m pytest tests/imports` — Fail — 64 passed, 4 failed
- `python scripts/run_import_uat.py` — Fail — 9/12 flows passed
- `python -m pytest tests/exports` — Pass — 42 passed
- Preserved working changes: `notes/local-investigation.md`
- Known pre-existing failures: none

## Acceptance ledger

| ID | Acceptance item | Verifier | Status | Evidence |
|---|---|---|---|---|
| A1 | Import tests pass | `python -m pytest tests/imports` | Pass | 68 passed |
| A2 | Import UAT passes | `python scripts/run_import_uat.py` | Pass | 12/12 flows passed |
| A3 | Exports do not regress | `python -m pytest tests/exports` | Pass | 42 passed |
| A4 | Full repository gates pass | `make verify` | Pass | exit 0 |
| A5 | Important changes reviewed | Independent diff review | Pass | no unexplained changes |

## Completed changes

- Normalized spreadsheet serial dates at the XLSX parser boundary.
- Preserved CSV parsing behavior.
- Added a workbook fixture covering date, blank, and malformed cells.
- Added regression coverage in `tests/imports/test_spreadsheet_dates.py`.
- Documented the normalization rule in `docs/product/portfolio-import-v1.4.md`.

## Failed or reverted approaches

- Global post-parse date coercion — reverted because it changed valid CSV string fields and widened the blast radius.

## Open contradictions and risks

- None.

## Blockers and approvals

- None.

## Next action

Archive the closeout packet and update the goal-history index. No production deployment or merge is authorized by this contract.
