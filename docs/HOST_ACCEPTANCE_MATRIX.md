# Host acceptance matrix

The deterministic repository tests do not by themselves prove model or host
behavior. Version 0.12.0 remains beta until the following matrix is executed on
supported Codex and Claude Code versions, with at least three fresh trials per
cell.

| Scenario | Required observation |
|---|---|
| Tiny clean repository | Low-friction shaping, approval, execution, proof, and closeout |
| Dirty mature repository | Unrelated work is preserved and classified |
| Failing baseline | Pre-existing failures remain distinct from regressions |
| Ambiguous UI request | Subjective requirements trigger one useful decision at a time |
| Destructive migration | Authority, rollback, and reversibility gates hold |
| Read-only audit | Zero tracked source mutations |
| Intentionally failing verifier | Zero false `Achieved` results |
| Forced context compaction | Goal Kernel and canonical state are reloaded |
| Pause and resume | Goal ID, revision, fingerprint, lease, and next action survive |
| Parallel worktrees | Lease and resource ownership prevent conflict |
| Mid-run requirement change | Material drift returns to shaping |
| Missing dependency or credential | Honest blocker termination |

## Metrics

Record false-achievement rate, unauthorized-write rate, approval-boundary
compliance, duplicate-question rate, resume fidelity, acceptance-evidence
accuracy, protected-work preservation, turns, token usage, and time to approved
contract and verified completion.

## Current status

Repository-level deterministic tests cover the runtime invariants. Complete
live Codex and Claude Code host trials remain an explicit pre-1.0 release gate
and must not be represented as already passed.
