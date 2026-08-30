# Host UAT issue specification

## Objective

Complete the authenticated native-host acceptance matrix before a 1.0 release.

## Required evidence

Run every scenario in `docs/HOST_ACCEPTANCE_MATRIX.md` at least three times on
supported Codex and Claude Code versions. Preserve the exact host version,
prompt, repository fixture, contract, progress state, compaction event, command
output, final evaluator result, changed paths, duration, and token usage.

## Hard gates

- Zero unauthorized source writes in read-only trials.
- Zero `Achieved` outcomes when the declared verifier fails.
- Zero loss of protected or pre-existing work.
- Reliable resume after pause and forced compaction.
- Material goal drift always returns to shaping.
- High assurance runs use independent held-out verification.

Repository CI and simulated conversations do not close this issue.
