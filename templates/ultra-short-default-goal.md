# Ultra-Short Default `/goal`

Use this when an established repository already contains a reliable **approved target**, instructions, plans, progress files, and native checks. The target may be a concise outcome or a pointer to an approved Goal Contract, issue, PRD, or milestone. Use [`/shape-goal`](../skills/shape-goal/SKILL.md) first when it is unclear.

```text
/goal Finish [APPROVED TARGET OR GOAL-CONTRACT PATH] from the repository’s actual current state. Read and reconcile its instructions, plans/progress/handoffs, tests/CI, and Git state; protect unrelated and uncommitted work. Repeatedly take the highest-priority unblocked gap, make one small reversible production change, verify it with repository-native checks, add regression coverage, review the diff, and update existing progress state. Keep only changes that preserve or improve the baseline. Continue without asking what is next and do not stop at planning, tests, or documentation while implementation remains. Finish only when the target's acceptance evidence passes with surfaced results; stop for a genuine approval/external blocker, exhausted budget, or two no-progress cycles and leave a restartable handoff. No irreversible or external action without approval.
```
