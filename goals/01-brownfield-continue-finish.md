# Brownfield Continue / Finish

**Use when:** An existing project has an approved outcome, partial implementation, or unfinished milestone and should advance autonomously.

## Recommended: skill-backed

Use `shape-goal` first when no approved target exists. Then run:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Brownfield Continue / Finish profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

The Goal Contract holds project-specific truth; `goal-engine` supplies the reusable execution loop.

## What does the target mean?

The target is not a task list. It is either a verifiable end state or a pointer such as `GOAL.md`, an approved issue, milestone, PRD, or acceptance checklist.

> **[Observable outcome]** is true for **[scope]**, proven by **[acceptance evidence]**, while **[protected behavior]** remains intact.

When it is unclear:

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

Do not start autonomous execution with an unresolved placeholder.

## Standalone fallback

Use this when `goal-engine` is not installed:

```text
/goal Bring this existing repository to [APPROVED TARGET OR GOAL-CONTRACT PATH]. First establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, prior goal archives, native scripts/CI/tests, and Git status/diff/history. Reconcile stale or conflicting artifacts by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run repository-native relevant checks; review the diff; add regression coverage for fixed failures; keep only changes that preserve or improve the baseline; and update existing progress/handoff state with evidence and the next action. Continue autonomously—do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when the repository answers it. Finish only when every in-scope gap is closed and the approved target's acceptance evidence passes with results surfaced. Stop earlier only for a genuine external/owner-approval blocker, an exhausted contract-defined budget, or two consecutive no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. Never perform destructive, deployment, credential, release, or external-system actions without explicit approval.
```

**Why it works:** It begins from an approved outcome and current evidence, gives the agent authority to choose the next safe action, and preserves both execution state and reusable closeout knowledge.
