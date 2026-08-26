# Complete Brownfield Cycle, Shaping History, and Goal Portfolio

This fictional example shows two shaping rounds, one approved goal, its reusable closeout, and a different goal that becomes ready afterward.

```text
Rough request
  → evidence-backed questions and saved answers
  → approved Goal Contract
  → checkpointed progress and evidence
  → terminal result and reusable tests
  → portfolio updated with the next distinct goal
```

## Scenario

A mature portfolio application already imports CSV files and exports portfolios. The first shaping round defines the supported formats and compatibility boundary. A second, deeper round resolves spreadsheet date semantics and separates performance work from correctness. The approved goal completes spreadsheet import v1.4 without regressing exports. After correctness is proven, a separate **Measured Optimization / Benchmark** goal becomes ready to improve latency and memory against the new stable baseline; it is not silently appended to the completed contract.

## Files

- [`SHAPING.md`](SHAPING.md) — every question, answer, recommendation, decision, and round summary.
- [`PORTFOLIO.md`](PORTFOLIO.md) — closed, ready, and candidate goals plus their dependencies.
- [`CONTRACT.md`](CONTRACT.md) — the approved target, approval round, profile, overlays, scope, proof, and boundaries.
- [`PROGRESS.md`](PROGRESS.md) — baseline, acceptance ledger, completed slices, goal-fit result, and failed approach.
- [`RESULT.md`](RESULT.md) — outcome, evidence, shaping decision trace, reusable outputs, related next goal, and residual risk.

In a real repository, simple active state would normally be:

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/<goal-id>/SHAPING.md
```

Multi-goal coordination and closeout would be:

```text
docs/goals/
├── PORTFOLIO.md
├── INDEX.md
└── 2026-08-25-portfolio-import-v1-4/
    ├── SHAPING.md
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

Durable knowledge lives in maintained tests, docs, ADRs, runbooks, fixtures, scripts, benchmarks, and the project harness—not only in the archive. The shaping history remains the append-only record of what the user was asked, what they answered, and how the contract evolved.
