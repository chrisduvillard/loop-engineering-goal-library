# Complete Brownfield Cycle Example

This fictional example shows the durable artifacts produced by one successful `shape-goal` → native `/goal` → `goal-engine` cycle.

```text
Rough request
  → approved Goal Contract
  → checkpointed progress and evidence
  → terminal result
  → reusable tests and lessons
```

## Scenario

A mature portfolio application already imports CSV files and exports portfolios. The next approved outcome is to complete spreadsheet import v1.4 without regressing exports.

## Files

- [`CONTRACT.md`](CONTRACT.md) — the approved target, scope, evidence, protections, and authority boundaries.
- [`PROGRESS.md`](PROGRESS.md) — the final acceptance ledger, baseline, delivered slices, and failed approach.
- [`RESULT.md`](RESULT.md) — the terminal outcome, evidence, reusable outputs, lessons, and residual risk.

In a real repository, the active files would normally be:

```text
GOAL.md
GOAL_PROGRESS.md
```

At closeout they would be snapshotted under:

```text
docs/goals/2026-08-25-portfolio-import-v1-4/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

The history index would link the result, while durable knowledge would live in the maintained product, tests, ADRs, runbooks, fixtures, or scripts—not only in this archive.
