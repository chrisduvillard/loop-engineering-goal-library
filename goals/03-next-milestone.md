# Next Milestone

**Use when:** The project has a larger roadmap but only the next coherent, dependency-safe increment should be completed.

```text
/goal Complete the next coherent unblocked milestone toward [OBJECTIVE]. Orient from the actual repository and reconcile applicable instructions, specifications, approved plans, progress/handoffs, tests, CI, and Git state; protect uncommitted and unrelated work. Select the highest-priority dependency-safe milestone that materially advances the objective and can be finished end-to-end without unnecessary scope expansion, then define its acceptance evidence before editing. Implement the required production behavior through small reversible changes, run repository-native relevant checks after each meaningful change, add regression coverage, review the diff, and update existing progress state. Do not substitute planning, scaffolding, documentation, or tests for required implementation. Finish when that milestone—not the entire backlog—meets its acceptance criteria and affected broader gates pass with surfaced evidence. Stop only for a genuine external or approval blocker, [BUDGET], or two consecutive no-progress cycles; leave a restartable handoff. No irreversible or external-system action without explicit approval.
```

**Why it works:** It constrains autonomy to one meaningful delivery unit without prescribing low-level tasks. The milestone’s evidence contract prevents both premature stopping and uncontrolled backlog expansion.
