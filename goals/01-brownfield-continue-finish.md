# Brownfield Continue / Finish

**Use when:** An existing project has plans, partial implementation, or an unfinished target and should advance autonomously.

```text
/goal Bring this existing repository to [TARGET]. First establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile stale or conflicting artifacts by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the repository-native relevant checks; review the diff; add regression coverage for fixed failures; keep only changes that preserve or improve the baseline; and update existing progress/handoff state with evidence and the next action. Continue autonomously—do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when the repository answers it. Finish only when every in-scope gap is closed and [ACCEPTANCE EVIDENCE] passes with results surfaced. Stop earlier only for a genuine external/owner-approval blocker, an exhausted [BUDGET], or two consecutive no-progress cycles; leave a restartable handoff. Never perform destructive, deployment, credential, release, or external-system actions without explicit approval.
```

**Why it works:** It starts from evidence rather than stale assumptions and gives the agent authority to choose the next safe task. Success, regression, stagnation, and approval boundaries are all explicit.
