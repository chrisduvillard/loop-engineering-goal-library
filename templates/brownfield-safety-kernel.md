# Brownfield Safety Kernel

This is the minimal reusable paragraph that should appear in almost every brownfield loop.

```text
First establish the repository’s actual state from applicable instructions, requirements, plans/progress/handoffs, native checks, and Git status/diff/history. Reconcile stale or contradictory artifacts using authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Make small coherent reversible production changes, verify each with repository-native checks, add regression protection for fixed failures, review important diffs independently, and keep only changes that preserve or improve the baseline. Update existing state artifacts with evidence and the next action. Finish only on passing acceptance evidence; otherwise stop only for a genuine approval/external blocker, exhausted budget, or repeated no-progress, leaving a restartable handoff. Never perform irreversible or external-system actions without explicit approval.
```

## Irreducible ideas

1. Orient from actual state.
2. Reconcile rather than blindly trust.
3. Protect existing work and behavior.
4. Change incrementally and reversibly.
5. Use native, stable verification.
6. Require evidence and regression protection.
7. Persist state and the next action.
8. Bound stagnation and authority.
