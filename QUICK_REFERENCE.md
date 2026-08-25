# Quick Reference

## Choose the right loop

### Seven core loops

| Loop | Use it for |
|---|---|
| [**Brownfield Continue / Finish**](goals/01-brownfield-continue-finish.md) | Default autonomous continuation of an existing project |
| [**PRD / Spec Compliance**](goals/02-prd-spec-compliance.md) | Requirements-driven convergence |
| [**Next Milestone**](goals/03-next-milestone.md) | One bounded, dependency-safe delivery increment |
| [**Deep Audit + Remediation**](goals/04-deep-audit-remediation.md) | Evidence-based discovery and root-cause repair |
| [**QA / Regression / UAT**](goals/05-qa-regression-uat.md) | Actual-product and workflow verification |
| [**Safe Refactor / Modernization**](goals/06-safe-refactor-modernization.md) | Behavior-preserving structural change |
| [**Release Readiness**](goals/07-release-readiness.md) | Convergence on pre-release gates |

For mature products such as Trading-Intel and AuraVoya, **Brownfield Continue / Finish** is the everyday default.

### Optional specialist extensions

| Loop | Use it for |
|---|---|
| [**Incident Recovery / Stabilization**](goals/08-incident-recovery.md) | Separating containment, restoration, root cause, and prevention |
| [**Dependency / Framework Upgrade**](goals/09-dependency-framework-upgrade.md) | Staged version upgrades with compatibility and rollback evidence |
| [**Data Migration / Integrity**](goals/10-data-migration-integrity.md) | Reversible data changes with reconciliation and recovery checks |
| [**Branch Rescue / Integration**](goals/11-branch-rescue-integration.md) | Recovering coherent work without overwriting a newer target branch |

---

## Best Universal Brownfield `/goal`

```text
/goal Bring this existing project to [TARGET]. Before any persistent change, establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile contradictions by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Derive concrete acceptance evidence from the target and repository. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the smallest relevant repository-native checks; review the diff; add regression coverage for fixed failures; and keep only changes that preserve or improve the baseline. At checkpoints run broader required gates and independently review important changes. Update existing progress or handoff artifacts with branch/SHA, changes, evidence, remaining gaps, blockers, and the next action. Continue autonomously; do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when repository evidence resolves it. Finish only when every in-scope gap is closed and all acceptance gates pass with evidence surfaced. Stop only for a genuine external or owner-approval blocker, an exhausted [BUDGET], or two consecutive cycles without new evidence or measurable progress; leave a restartable handoff. Never perform destructive, deployment, credential, release, merge, publish, or external-system actions without explicit approval.
```

---

## Ultra-Short Default `/goal`

```text
/goal Finish [TARGET] from the repository’s actual current state. Read and reconcile its instructions, plans/progress/handoffs, tests/CI, and Git state; protect unrelated and uncommitted work. Repeatedly take the highest-priority unblocked gap, make one small reversible production change, verify it with repository-native checks, add regression coverage, review the diff, and update existing progress state. Keep only changes that preserve or improve the baseline. Continue without asking what is next and do not stop at planning, tests, or documentation while implementation remains. Finish only when [ACCEPTANCE] passes with surfaced evidence; stop for a genuine approval/external blocker, exhausted budget, or two no-progress cycles and leave a restartable handoff. No irreversible or external action without approval.
```

---

## Brownfield Safety Kernel

```text
First establish the repository’s actual state from applicable instructions, requirements, plans/progress/handoffs, native checks, and Git status/diff/history. Reconcile stale or contradictory artifacts using authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Make small coherent reversible production changes, verify each with repository-native checks, add regression protection for fixed failures, review important diffs independently, and keep only changes that preserve or improve the baseline. Update existing state artifacts with evidence and the next action. Finish only on passing acceptance evidence; otherwise stop only for a genuine approval/external blocker, exhausted budget, or repeated no-progress, leaving a restartable handoff. Never perform irreversible or external-system actions without explicit approval.
```

---

## Vague task → strong loop

Ask five questions:

1. **Outcome:** What observable state should be true?
2. **Scope:** What is included, and what must remain unchanged?
3. **Verifier:** Which command, workflow, metric, or rubric proves success?
4. **Iteration:** What is one safe change, and when is it kept or reverted?
5. **Exit:** What counts as success, blocker, approval boundary, exhaustion, or stagnation?

Transform:

> Improve the project.

Into:

```text
/goal Improve [SCOPE] from its verified baseline until [MEASURABLE TARGET] passes under [VERIFIER]. Make one small reversible change per cycle, keep only changes that improve the result without regressing repository-native gates, and record the evidence and next action. Stop on target, genuine blocker or approval boundary, exhausted budget, or two no-progress cycles; preserve unrelated work and perform no irreversible action without approval.
```

> Give the agent a state to reach, a check that decides, a boundary it cannot cross, and a record the next iteration can trust.

---

## Configure a core loop instead of inventing another

| Area | Recommended treatment |
|---|---|
| Bug fixing | Scope **Deep Audit + Remediation** to one reproducible bug |
| Security | Add a security standard, severity threshold, read-only discovery, and stricter approval boundaries |
| Reliability | Add failure injection, recovery, idempotency, and observability gates |
| Performance | Add a fixed benchmark, stable environment, baseline, and keep-or-revert rule |
| UI/UX | Add real browser flows, screenshots, viewport coverage, accessibility checks, and a design rubric |
| Technical debt | Give **Safe Refactor** an objective structural target rather than “clean up” |
| Documentation sync | Use **PRD / Spec Compliance** or **Release Readiness**, depending on authority |
