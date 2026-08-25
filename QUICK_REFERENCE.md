# Quick Reference

## The 30-second workflow

```bash
npx skills add chrisduvillard/loop-engineering-goal-library --skill '*'
```

| Step | Claude Code | Codex CLI / IDE |
|---|---|---|
| Shape an unclear target | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Start execution | Use the native `/goal` command below | Use the native `/goal` command below |

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

```text
Rough intent → shape-goal → Goal Contract → /goal + goal-engine → Passing evidence
```

---

## What is the target?

A target is not a task breakdown. It is either a verifiable outcome or a pointer to an approved Goal Contract, issue, PRD, milestone, or acceptance checklist.

```text
[Observable outcome] is true for [scope], proven by [acceptance evidence], while [protected behavior] remains intact.
```

Examples:

- `the approved Goal Contract in GOAL.md`
- `all v1.4 requirements in docs/product/import-v2.md`
- `Milestone 3 in PLAN.md with its acceptance flows passing`
- `issue #142 without regressing the existing export workflow`

Use `shape-goal` when the outcome, scope, evidence, protected behavior, or owner decisions are not yet settled.

---

## Skills and goals have different jobs

| Layer | Job |
|---|---|
| `shape-goal` | Decide and persist what “done” means |
| Goal Contract | Hold project-specific truth and authority boundaries |
| Native `/goal` | Keep work running and evaluate the finish condition |
| `goal-engine` | Apply the reusable brownfield execution method and selected profile |

See [`SKILLS_AND_GOALS.md`](SKILLS_AND_GOALS.md) for the architecture.

---

## Recommended Golden Set

Keep these seven execution profiles permanently:

1. **Brownfield Continue / Finish** — default continuation toward an approved outcome.
2. **PRD / Spec Compliance** — requirements-driven convergence.
3. **Next Milestone** — one bounded roadmap increment.
4. **Deep Audit + Remediation** — evidence-based discovery and repair.
5. **QA / Regression / UAT** — actual-product verification.
6. **Safe Refactor / Modernization** — behavior-preserving structural change.
7. **Release Readiness** — convergence on pre-release gates.

For mature products such as Trading-Intel and AuraVoya, **Brownfield Continue / Finish** is the everyday default once the target has been approved.

### Specialist profiles

Use these when the work has a distinct risk model:

1. **Incident Recovery / Stabilization** — containment, recovery, root cause, and prevention.
2. **Dependency / Framework Upgrade** — staged ecosystem changes and compatibility evidence.
3. **Data Migration / Integrity** — reversible transformations, reconciliation, and mixed-version safety.
4. **Branch Rescue / Integration** — recovery of coherent value from divergent branches.

The Goal Contract selects one primary profile. Do not combine profiles when they imply different outcomes; split or reshape the contract instead.

---

## Ultra-short default

When `goal-engine` is installed and `GOAL.md` is already strong:

```text
/goal Follow goal-engine to complete GOAL.md. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, or two-cycle stall applies; leave a restartable handoff.
```

---

## Standalone mode

When the skills are not installed, use the self-contained commands in:

- [`GOAL_LIBRARY.md`](GOAL_LIBRARY.md) — all seven core commands
- [`SPECIALIST_LOOPS.md`](SPECIALIST_LOOPS.md) — four specialist commands
- [`templates/universal-brownfield-goal.md`](templates/universal-brownfield-goal.md) — universal skill-backed and standalone versions
- [`templates/ultra-short-default-goal.md`](templates/ultra-short-default-goal.md) — shortest reliable versions

---

## Brownfield Safety Kernel

```text
First establish the repository’s actual state from applicable instructions, requirements, plans/progress/handoffs, native checks, and Git status/diff/history. Reconcile stale or contradictory artifacts using authority, recency, and executable evidence; protect user, uncommitted, and unrelated work. Make small coherent reversible production changes, verify each with repository-native checks, add regression protection for fixed failures, review important diffs independently, and keep only changes that preserve or improve the baseline. Update existing state artifacts with evidence and the next action. Finish only on passing acceptance evidence; otherwise stop only for a genuine approval/external blocker, exhausted budget, or repeated no-progress, leaving a restartable handoff. Never perform irreversible or external-system actions without explicit approval.
```

The kernel is embedded in `goal-engine`; standalone goals repeat it so they remain self-contained.

---

## Vague task → strong contract

Ask five questions:

1. **Outcome:** What observable state should be true?
2. **Scope:** What is included and excluded?
3. **Evidence:** Which command, workflow, measurement, or artifact proves success?
4. **Protection:** What existing behavior or work must survive?
5. **Exit:** What counts as success, blocker, approval required, exhaustion, or stall?

Transform:

> Improve the project.

Into:

```text
The documented onboarding workflow succeeds for every supported account type, passes its UAT matrix, and does not regress existing sign-in behavior.
```

Then persist it as a Goal Contract and let `goal-engine` choose the next safe action.

> **Never ask an autonomous agent to “make it better.” Give it a state to reach, a check that decides, a boundary it cannot cross, and a record the next iteration can trust.**

---

## Other specialized work

| Area | Recommended profile |
|---|---|
| Bug fixing | **Deep Audit + Remediation**, scoped to one reproducible failure |
| Security | **Deep Audit + Remediation** with a standard and severity threshold |
| Reliability | **Deep Audit + Remediation** or **QA / Regression / UAT** with recovery gates |
| Performance | **Safe Refactor / Modernization** with a fixed baseline benchmark |
| UI/UX | **QA / Regression / UAT** with real browser flows and a stable rubric |
| Technical debt | **Safe Refactor / Modernization** with an objective structural target |
| Documentation sync | **PRD / Spec Compliance** or **Release Readiness**, depending on authority |
