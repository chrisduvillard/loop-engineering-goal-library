# Branch Rescue / Integration

**Use when:** Valuable work is stranded in a stale, divergent, oversized, or partially conflicting branch and must be recovered safely.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Branch Rescue / Integration profile. Account for every source slice, port only dependency-complete behavior that remains valid, protect newer target work, and continue until selected behavior passes broader gates and the target contains no unexplained changes. Stop for irreconcilable intent or a contract-defined blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Safely recover and integrate valuable work from [SOURCE BRANCH OR COMMITS] into [TARGET BRANCH] while preserving newer target behavior and unrelated work. Establish actual refs/SHAs, clean or dirty state, divergence, target baseline, relevant requirements/issues/PRs/tests, prior goal archives, and source intent from Git history; create a recovery point before changes. Inventory source changes by coherent behavior and classify each slice as already present, obsolete, conflicting, unsafe, or worth porting; verify every classification against current code and executable evidence. Port the smallest dependency-complete slices using the least risky method, resolving conflicts by current contracts and tests rather than taking either side wholesale. After each slice, run repository-native targeted checks, add regression coverage where needed, review the diff, and keep only changes that preserve or improve the target baseline. Never overwrite newer target work or import unrelated source history. Finish only when every source slice is accounted for, all selected behavior passes affected broader gates with surfaced evidence, and the target contains no unexplained changes. Stop for an owner decision on irreconcilable intent, approval/external blocker, [BUDGET], or two no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. Do not merge, push, delete, or rewrite branches without explicit approval.
```

**Why it works:** It treats a branch as behavioral slices, preserves a path matrix, and records reusable integration decisions rather than hiding them in a one-off merge.
