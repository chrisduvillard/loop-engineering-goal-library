# Quick Reference

## Recommended Golden Set

Keep these seven loops permanently:

1. **Brownfield Continue / Finish** — default autonomous project loop.
2. **PRD / Spec Compliance** — requirements-driven convergence.
3. **Next Milestone** — bounded roadmap execution.
4. **Deep Audit + Remediation** — evidence-based discovery and repair.
5. **QA / Regression / UAT** — actual-product verification.
6. **Safe Refactor / Modernization** — behavior-preserving structural change.
7. **Release Readiness** — convergence on pre-release gates.

For mature products such as Trading-Intel and AuraVoya, **Brownfield Continue / Finish** is the everyday default—once the target is approved.

---

## What does `TARGET` mean?

A target is not a complete task breakdown. It is either a verifiable end state or a pointer to an approved Goal Contract, issue, PRD, milestone, or acceptance checklist.

```text
[Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.
```

Examples:

- `the approved Goal Contract in GOAL.md`
- `all v1.4 requirements in docs/product/import-v2.md`
- `Milestone 3 in PLAN.md with its acceptance flows passing`
- `issue #142 without regressing the existing export workflow`

When you do not yet know the target, run the [`shape-goal`](skills/shape-goal/SKILL.md) skill before starting `/goal`:

```text
/shape-goal Continue this project
```

It turns rough intent plus repository evidence into an approved Goal Contract, selects the most appropriate loop, and returns the exact copy-ready `/goal` command.

```text
Rough intent → /shape-goal → Goal Contract → /goal → Passing evidence
```

---

## Best Universal Brownfield `/goal`

```text
/goal Bring this existing project to [APPROVED TARGET OR GOAL-CONTRACT PATH]. Before any persistent change, establish the actual state: read applicable repository instructions, specifications/PRDs, architecture, approved plans, progress/handoffs, native scripts/CI/tests, and Git status/diff/history. Reconcile contradictions by authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Derive concrete acceptance evidence from the approved target and repository. Then repeat: select the highest-priority unblocked gap; verify it; make the smallest coherent reversible production change; run the smallest relevant repository-native checks; review the diff; add regression coverage for fixed failures; and keep only changes that preserve or improve the baseline. At checkpoints run broader required gates and independently review important changes. Update existing progress or handoff artifacts with branch/SHA, changes, evidence, remaining gaps, blockers, and the next action. Continue autonomously; do not stop at planning, analysis, documentation, or tests while production work remains, and do not ask what to do next when repository evidence resolves it. Finish only when every in-scope gap is closed and all acceptance gates pass with evidence surfaced. Stop only for a genuine external or owner-approval blocker, an exhausted contract-defined budget, or two consecutive cycles without new evidence or measurable progress; leave a restartable handoff. Never perform destructive, deployment, credential, release, merge, publish, or external-system actions without explicit approval.
```

---

## Ultra-Short Default `/goal`

```text
/goal Finish [APPROVED TARGET OR GOAL-CONTRACT PATH] from the repository’s actual current state. Read and reconcile its instructions, plans/progress/handoffs, tests/CI, and Git state; protect unrelated and uncommitted work. Repeatedly take the highest-priority unblocked gap, make one small reversible production change, verify it with repository-native checks, add regression coverage, review the diff, and update existing progress state. Keep only changes that preserve or improve the baseline. Continue without asking what is next and do not stop at planning, tests, or documentation while implementation remains. Finish only when the target's acceptance evidence passes with surfaced results; stop for a genuine approval/external blocker, exhausted budget, or two no-progress cycles and leave a restartable handoff. No irreversible or external action without approval.
```

---

## Brownfield Safety Kernel

```text
First establish the repository’s actual state from applicable instructions, requirements, plans/progress/handoffs, native checks, and Git status/diff/history. Reconcile stale or contradictory artifacts using authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Make small coherent reversible production changes, verify each with repository-native checks, add regression protection for fixed failures, review important diffs independently, and keep only changes that preserve or improve the baseline. Update existing state artifacts with evidence and the next action. Finish only on passing acceptance evidence; otherwise stop only for a genuine approval/external blocker, exhausted budget, or repeated no-progress, leaving a restartable handoff. Never perform irreversible or external-system actions without explicit approval.
```

---

## Vague Task → Strong Loop

Convert an ordinary request using five questions:

1. **Outcome:** What observable state should be true?
2. **Scope:** Which surfaces are included, and what must remain unchanged?
3. **Verifier:** Which command, workflow, metric, or rubric proves success?
4. **Iteration:** What is one safe change, and when is it kept or reverted?
5. **Exit:** What counts as success, blocker, approval boundary, exhaustion, or stagnation?

Transform:

> Improve the project.

Into:

```text
/goal Improve [SCOPE] from its verified baseline until [MEASURABLE TARGET] passes under [VERIFIER]. Make one small reversible change per cycle, keep only changes that improve the result without regressing repository-native gates, and record the evidence and next action. Stop on target, genuine blocker or approval boundary, exhausted budget, or two no-progress cycles; preserve unrelated work and perform no irreversible action without approval.
```

The central rule:

> Never ask an autonomous agent to “make things better.” Give it a state to reach, a check that decides, a boundary it cannot cross, and a record that lets the next iteration continue safely.

---

## Specialist extensions

These four are useful when the work has a distinct risk model:

1. **Incident Recovery / Stabilization** — containment, recovery, root cause, and prevention.
2. **Dependency / Framework Upgrade** — staged ecosystem changes and compatibility evidence.
3. **Data Migration / Integrity** — reversible transformations, reconciliation, and mixed-version safety.
4. **Branch Rescue / Integration** — evidence-based recovery of coherent work from divergent branches.

See [`SPECIALIST_LOOPS.md`](SPECIALIST_LOOPS.md) for all four copy-ready commands.

---

## Other specialized work

| Area | Recommended treatment |
|---|---|
| Bug fixing | Use **Deep Audit + Remediation** scoped to one bug; use a normal task when it is a single reproduction/fix/check cycle. |
| Security | Use **Deep Audit + Remediation** with a security standard, severity threshold, read-only discovery, and stricter approval boundaries. |
| Reliability | Use **Deep Audit + Remediation** or **QA / Regression / UAT** with failure injection, recovery, idempotency, and observability gates. |
| Performance | Use **Safe Refactor / Modernization** with a fixed benchmark, stable environment, baseline, and champion/challenger keep-or-revert rule. |
| UI/UX | Use **QA / Regression / UAT** with real browser flows, screenshots, supported viewport matrix, accessibility checks, and an explicit design rubric. |
| Technical debt | Use **Safe Refactor / Modernization** with an objective structural target rather than “clean up the code.” |
| Documentation sync | Use **PRD / Spec Compliance** when documentation is authoritative; use **Release Readiness** for version, migration, operational, and release documentation. |
