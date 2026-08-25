# Ultra-Short Default `/goal`

Use this when `goal-engine` is installed and the repository already contains an approved `GOAL.md` with strong acceptance evidence.

```text
/goal Follow goal-engine to complete GOAL.md. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, or two-cycle stall applies; leave a restartable handoff.
```

The short command is reliable because reusable safety lives in the skill and project-specific truth lives in the contract.

## No-skill fallback

```text
/goal Finish [APPROVED TARGET OR GOAL-CONTRACT PATH] from the repository’s actual current state. Read and reconcile its instructions, plans/progress/handoffs, tests/CI, and Git state; protect unrelated and uncommitted work. Repeatedly take the highest-priority unblocked gap, make one small reversible production change, verify it with repository-native checks, add regression coverage, review the diff, and update existing progress state. Keep only changes that preserve or improve the baseline. Continue without asking what is next and do not stop at planning, tests, or documentation while implementation remains. Finish only when the target's acceptance evidence passes with surfaced results; stop for a genuine approval/external blocker, exhausted budget, or two no-progress cycles and leave a restartable handoff. No irreversible or external action without approval.
```
