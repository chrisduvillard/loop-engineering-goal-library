# Quick Reference

## Install globally

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

## Fastest path

1. Open the repository root in Codex or Claude Code.
2. Choose a profile in [`goals/README.md`](goals/README.md).
3. Copy its first `/goal` command unchanged.
4. Answer only the owner decisions `shape-goal` cannot derive.
5. Approve the Goal Contract.
6. Let `goal-engine` execute until the evidence passes.
7. Reuse the archived result and shape the next goal.

No placeholder replacement is required in the recommended commands.

## Let the system choose

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Continue this project` | `$shape-goal Continue this project` |

## Zero-friction launch rule

Every recommended goal command performs two phases inside one native `/goal`:

```text
Phase 1: shape-goal discovers inputs, asks decisions, and obtains approval
Phase 2: goal-engine implements, verifies, reviews, records, and closes
```

Production edits are forbidden before approval. Shaping alone is never successful completion.

## Common goal choices

| Need | Goal |
|---|---|
| Finish existing approved work | Brownfield Continue / Finish |
| Close requirements | PRD / Spec Compliance |
| Deliver the next roadmap increment | Next Milestone |
| Find and fix important problems | Deep Audit + Remediation |
| Prove real product workflows | QA / Regression / UAT |
| Modernize without behavior drift | Safe Refactor / Modernization |
| Prepare a release | Release Readiness |
| Recover from a severe failure | Incident Recovery / Stabilization |
| Upgrade an ecosystem dependency | Dependency / Framework Upgrade |
| Migrate stored data or schema | Data Migration / Integrity |
| Recover work from a divergent branch | Branch Rescue / Integration |
| Improve a stable metric | Measured Optimization / Benchmark |
| Answer a technical unknown | Technical Spike / Feasibility |
| Improve frontend quality | Frontend UI / UX / Accessibility |
| Correct and verify documentation | Documentation Synchronization / Knowledge Transfer |
| Harden security and privacy | Security / Privacy Hardening |
| Prove failure and recovery behavior | Reliability / Resilience Hardening |
| Evolve APIs or integrations safely | API / Integration Contract Compatibility |
| Improve logs, metrics, alerts, and runbooks | Observability / Operability |
| Improve setup, build, test, or debug workflows | Developer Experience / Tooling |
| Assure pipeline and dataset quality | Data Quality / Pipeline Assurance |
| Prepare technical evidence for an audit | Compliance / Audit Readiness |
| None fits | Custom Contract-Driven |

## How missing inputs are resolved

`shape-goal` searches repository instructions, Git, current/prior goals, PRDs, architecture, scripts, CI, tests, runtime evidence, project harness, connected authoritative systems, and current official documentation before asking.

Questions are:

- Limited to material owner decisions
- Asked one at a time
- Accompanied by evidence and a recommendation
- Recorded in an input ledger and contract
- Never repeated without materially new evidence

## Multiple goals over time

| Change | Lifecycle action |
|---|---|
| Wording or source reference only | Clarify; keep Goal ID |
| Same outcome, material contract change | Amend; pause and approve a new revision |
| Different priority | Reprioritize portfolio |
| Temporary interruption | Pause and preserve resume state |
| Same goal later | Resume |
| Different outcome replaces current | Supersede and create a new Goal ID |
| Goal too broad | Split into dependency-safe children |
| Goal no longer valuable | Cancel with a closeout |
| Terminal result | Close and archive |

One native goal session/worktree executes one dependency-safe leaf contract.

## State and archive

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/PORTFOLIO.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

## Assurance overlays

Add only the proof that matters:

- Security & Privacy
- Reliability & Recovery
- Performance & Cost
- UX & Accessibility
- Data Integrity & Governance
- Compatibility & Portability
- Operability & Observability
- Documentation & Knowledge Transfer
- Compliance & Auditability

Use a dedicated profile when the concern is the primary outcome; use an overlay when it is secondary.

## Ultra-short strict-mode command

When `GOAL.md` is already approved:

```text
/goal Follow goal-engine to complete GOAL.md using its profile, overlays, and project harness. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, goal-drift review, or two-cycle stall applies; preserve reusable state and leave a restartable handoff.
```

## Update

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```
