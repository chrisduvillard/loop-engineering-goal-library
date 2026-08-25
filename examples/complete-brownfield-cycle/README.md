# Complete Brownfield Cycle and Goal Portfolio

This fictional example shows one successful goal, its reusable closeout, and a different goal that becomes ready afterward.

```text
Rough request
  → approved Goal Contract
  → checkpointed progress and evidence
  → terminal result and reusable tests
  → portfolio updated with the next distinct goal
```

## Scenario

A mature portfolio application already imports CSV files and exports portfolios. The first outcome completes spreadsheet import v1.4 without regressing exports. After correctness is proven, a separate performance goal becomes ready; it is not silently appended to the completed contract.

## Files

- [`PORTFOLIO.md`](PORTFOLIO.md) — closed, ready, and candidate goals plus their dependencies.
- [`CONTRACT.md`](CONTRACT.md) — the approved target, profile, overlays, scope, proof, and boundaries.
- [`PROGRESS.md`](PROGRESS.md) — baseline, acceptance ledger, completed slices, goal-fit result, and failed approach.
- [`RESULT.md`](RESULT.md) — outcome, evidence, reusable outputs, related next goal, and residual risk.

In a real repository, simple active state would normally be:

```text
GOAL.md
GOAL_PROGRESS.md
```

Multi-goal coordination and closeout would be:

```text
docs/goals/
├── PORTFOLIO.md
├── INDEX.md
└── 2026-08-25-portfolio-import-v1-4/
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

Durable knowledge lives in maintained tests, docs, ADRs, runbooks, fixtures, scripts, and the project harness—not only in the archive.
