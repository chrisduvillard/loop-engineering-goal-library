# Goal Portfolio: Portfolio Application

**Owner:** Product owner  
**Last reviewed:** 2026-08-25  
**Policy:** One active goal per native `/goal` session/worktree. This example currently has no active goal because import v1.4 is closed.

## Active

_None._

## Ready

| Goal ID | Priority | Outcome | Profile | Assurance overlays | Depends on | Contract | Why next |
|---|---|---|---|---|---|---|---|
| 2026-08-26-import-performance-budget | P2 | The verified import workflow meets the approved large-file latency and memory budget without changing import results | Measured Optimization / Benchmark | Performance & Cost; Data Integrity & Governance | 2026-08-25-portfolio-import-v1-4 | To be shaped | Product behavior is now correct; a fixed benchmark can use the stable fixture and tests created by the completed goal |

## Paused or blocked

_None._

## Candidates

| Candidate | Value | Main uncertainty | Evidence needed | Decision owner |
|---|---|---|---|---|
| Add broker-specific import adapters | Broader coverage | Which brokers matter first | Usage and support data | Product owner |

## Closed history

| Goal ID | Outcome | Result | Reusable outputs |
|---|---|---|---|
| 2026-08-25-portfolio-import-v1-4 | Achieved | [`RESULT.md`](RESULT.md) | XLSX regression tests, date fixture, normalization rule |

## Transition log

| Date | Goal | Transition | Reason | Approved by | Related goal |
|---|---|---|---|---|---|
| 2026-08-25 | 2026-08-25-portfolio-import-v1-4 | Closed | Every acceptance item passed | Product owner | 2026-08-26-import-performance-budget |
| 2026-08-25 | 2026-08-26-import-performance-budget | Ready | Correctness baseline now exists | Product owner | 2026-08-25-portfolio-import-v1-4 |
