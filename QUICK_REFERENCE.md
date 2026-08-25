# Quick Reference

## Install globally

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

## Common actions

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Shape or continue | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Add a goal | `/shape-goal New goal: [INTENT]` | `$shape-goal New goal: [INTENT]` |
| Change direction | `/shape-goal Change current goal: [NEED]` | `$shape-goal Change current goal: [NEED]` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |
| Resume | `/shape-goal Resume [GOAL ID]` | `$shape-goal Resume [GOAL ID]` |

## Start execution

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## Multiple goals over time

A project may have many goals. Use one dependency-safe contract per native `/goal` session or worktree.

| New need | Correct transition |
|---|---|
| Wording or evidence reference only | Clarify; same Goal ID, revision log |
| Same outcome, material scope/evidence change | Amend; pause, approve, increment revision |
| Different priority | Reprioritize portfolio; do not rewrite contracts |
| Temporary interruption | Pause; preserve progress and resume condition |
| Same goal later | Resume from preserved state |
| Different outcome replaces current | Supersede; archive old, create new Goal ID |
| Goal is too broad | Split into child goals; execute one leaf |
| Goal no longer has value | Cancel with reason and closeout evidence |

Use the existing issue tracker or roadmap when possible. Otherwise create `docs/goals/PORTFOLIO.md` from the [portfolio template](skills/shape-goal/templates/goal-portfolio-template.md).

## Coverage model

The eleven standalone goals are presets, not a ceiling:

```text
Primary execution profile
+ Assurance overlays
+ Project harness
+ Custom Contract-Driven fallback
```

### Primary profiles

| Work | Profile |
|---|---|
| Continue existing work | Brownfield Continue / Finish |
| Close requirements | PRD / Spec Compliance |
| Deliver one roadmap increment | Next Milestone |
| Find and repair important problems | Deep Audit + Remediation |
| Exercise real workflows | QA / Regression / UAT |
| Change internals without behavior drift | Safe Refactor / Modernization |
| Remove release blockers | Release Readiness |
| Recover a degraded system | Incident Recovery / Stabilization |
| Upgrade a dependency/framework/runtime | Dependency / Framework Upgrade |
| Transform schema or stored data | Data Migration / Integrity |
| Recover divergent branch value | Branch Rescue / Integration |
| None fits | Custom Contract-Driven |

### Assurance overlays

Add only what the target needs:

- Security & Privacy
- Reliability & Recovery
- Performance & Cost
- UX & Accessibility
- Data Integrity & Governance
- Compatibility & Portability
- Operability & Observability
- Documentation & Knowledge Transfer
- Compliance & Auditability

See [`assurance-overlays.md`](skills/goal-engine/references/assurance-overlays.md).

## Save reusable project mechanics

Use existing instructions and scripts. When setup/run/verify knowledge is repeatedly rediscovered, create or refresh `docs/agent/PROJECT_HARNESS.md` from the [Project Harness template](skills/goal-engine/templates/project-harness-template.md).

## State and archive

```text
GOAL.md                    current approved contract
GOAL_PROGRESS.md           mutable execution evidence
docs/goals/PORTFOLIO.md    optional multi-goal coordination
docs/goals/INDEX.md        closed-goal history
docs/goals/<goal-id>/      CONTRACT.md + PROGRESS.md + RESULT.md
```

Never commit secrets, credentials, private data, raw production dumps, exploit-enabling evidence, or unnecessary large logs.

## Ultra-short default

```text
/goal Follow goal-engine to complete GOAL.md using its profile, overlays, and project harness. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, goal-drift review, or two-cycle stall applies; preserve reusable state and leave a restartable handoff.
```

## Standalone custom fallback

When none of the eleven presets fits and the skills are not installed, use [`custom-contract-driven-goal.md`](skills/shape-goal/templates/custom-contract-driven-goal.md). It requires the contract to define a bounded iteration, verifier, keep-or-revert rule, review strategy, and stop condition.

## Update

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```
