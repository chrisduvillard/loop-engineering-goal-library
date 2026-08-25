# Best Universal Brownfield `/goal`

Use this after the target has been approved in `GOAL.md`, an issue, PRD, or milestone.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

This is the strongest reusable default: the Goal Contract holds project truth, `goal-engine` holds the complete brownfield execution method, and native `/goal` provides durable continuation and evaluation.

When the target is unclear, use `shape-goal` first:

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

## Standalone fallback

Use this when the skills are not installed:

```text
/goal Bring this existing project to [APPROVED TARGET OR GOAL-CONTRACT PATH]. Before any persistent change, establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile contradictions by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Derive concrete acceptance evidence from the approved target and repository. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the smallest relevant repository-native checks; review the diff; add regression coverage for fixed failures; and keep only changes that preserve or improve the baseline. At checkpoints run broader required gates and independently review important changes. Update existing progress or handoff artifacts with branch/SHA, changes, evidence, remaining gaps, blockers, and the next action. Continue autonomously; do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when repository evidence resolves it. Finish only when every in-scope gap is closed and all acceptance gates pass with evidence surfaced. Stop only for a genuine external or owner-approval blocker, an exhausted contract-defined budget, or two consecutive cycles without new evidence or measurable progress; leave a restartable handoff. Never perform destructive, deployment, credential, release, merge, publish, or external-system actions without explicit approval.
```
