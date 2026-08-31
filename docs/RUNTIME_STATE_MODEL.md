# Deterministic runtime state model

Version 0.12.0 introduces a canonical JSON substrate managed by
`skills/goal-engine/scripts/goalctl.py`.

## Three independent dimensions

| Dimension | Values | Meaning |
|---|---|---|
| Goal status | candidate, ready, active, paused, blocked, closed | Lifecycle of the durable goal |
| Run termination | achieved, approval_required, budget_exhausted, stalled, external_blocked, safety_stop, cancelled_by_user, host_failure | Why one execution run stopped |
| Goal outcome | achieved, cancelled, superseded, abandoned | Final disposition, present only for closed goals |

A run that stops for approval, budget, a stall, or an external blocker remains
resumable. It is not archived as a final outcome unless explicitly closed.

## Canonical files

- `.loop/active-goal.json`
- `.loop/goals/<goal-id>/contract.json`
- `.loop/goals/<goal-id>/progress.json`
- `.loop/leases/<goal-id>.json`

`GOAL.md` and `GOAL_PROGRESS.md` are generated views with source hashes. The
JSON files are authoritative.

## Approval fingerprint

`goalctl-v1-sha256` hashes canonical JSON containing the authority-bearing
contract fields. Runtime acceptance statuses and evidence do not alter the
approved authority, while changes to scope, acceptance descriptions, mutation
mode, assurance level, protected paths, or authority boundaries invalidate the
fingerprint.

## Lease behavior

Lease creation uses exclusive file creation. A different unexpired owner blocks
activation. Expired leases are moved aside before a new exclusive acquisition.
A token is required for strict release operations.
