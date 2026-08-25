# Brownfield Continue / Finish

**Use when:** An existing project has an approved outcome, partial implementation, or unfinished milestone and should advance autonomously.

## What does `TARGET` mean?

`TARGET` is **not** a perfect project description or a list of tasks. It is either:

- A verifiable end state: `the v1.4 import workflow passes its acceptance flows without regressing existing exports`
- A pointer to an approved source: `the Goal Contract in GOAL.md`, `issue #142`, `Milestone 3 in PLAN.md`, or `the requirements in docs/product/search-v2.md`

A useful target has this form:

> **[Observable outcome]** is true for **[scope]**, proven by **[acceptance evidence]**, while **[protected behavior]** remains intact.

When you do not yet know the target, run the [`/shape-goal`](../skills/shape-goal/SKILL.md) skill first:

```text
/shape-goal Continue this project
```

It reads the repository, reconciles the actual state, asks only the owner decisions it cannot derive, writes a Goal Contract, selects the right loop, and returns the exact `/goal` command. Do not start an autonomous goal with an unresolved placeholder.

## Command

```text
/goal Bring this existing repository to [APPROVED TARGET OR GOAL-CONTRACT PATH]. First establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile stale or conflicting artifacts by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the repository-native relevant checks; review the diff; add regression coverage for fixed failures; keep only changes that preserve or improve the baseline; and update existing progress/handoff state with evidence and the next action. Continue autonomously—do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when the repository answers it. Finish only when every in-scope gap is closed and the approved target's acceptance evidence passes with results surfaced. Stop earlier only for a genuine external/owner-approval blocker, an exhausted contract-defined budget, or two consecutive no-progress cycles; leave a restartable handoff. Never perform destructive, deployment, credential, release, or external-system actions without explicit approval.
```

**Why it works:** It starts from an approved outcome and current evidence rather than stale assumptions, then gives the agent authority to choose the next safe task. Success, regression, stagnation, and approval boundaries are explicit.
