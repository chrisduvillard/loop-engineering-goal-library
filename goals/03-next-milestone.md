# Next Milestone

**Use when:** The project has a larger roadmap but only the next coherent, dependency-safe increment should be completed.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Next Milestone profile. Finish the selected milestone end-to-end without expanding into the wider backlog, and continue until its acceptance evidence and affected broader gates pass. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

## Standalone fallback

```text
/goal Complete the next coherent unblocked milestone toward [OBJECTIVE]. Orient from the actual repository and reconcile applicable instructions, specifications, approved plans, progress/handoffs, prior goal archives, tests, CI, and Git state; protect uncommitted and unrelated work. Select the highest-priority dependency-safe milestone that materially advances the objective and can be finished end-to-end without unnecessary scope expansion, then define its acceptance evidence before editing. Implement required production behavior through small reversible changes, run repository-native relevant checks after each meaningful change, add regression coverage, review the diff, and update existing progress state. Do not substitute planning, scaffolding, documentation, or tests for required implementation. Finish when that milestone—not the entire backlog—meets its acceptance criteria and affected broader gates pass with surfaced evidence. Stop only for a genuine external or approval blocker, [BUDGET], or two consecutive no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. No irreversible or external-system action without explicit approval.
```

**Why it works:** It bounds autonomy to one useful delivery unit and retains a reusable record of what the milestone proved, changed, and taught.
