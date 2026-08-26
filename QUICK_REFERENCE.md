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
5. Review the saved shaping history; request another round when needed.
6. Approve the Goal Contract.
7. Let `goal-engine` execute until the evidence passes.
8. Reuse the archived result and shape the next goal.

No placeholder replacement is required in the recommended commands.

## Let the system choose

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Shape or continue | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Add a goal | `/shape-goal New goal: describe the intent` | `$shape-goal New goal: describe the intent` |
| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |
| Deepen a saved goal | `/shape-goal Run another shaping round for goal-id` | `$shape-goal Run another shaping round for goal-id` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |
| Resume | `/shape-goal Resume goal-id` | `$shape-goal Resume goal-id` |

## Zero-friction launch rule

Every recommended goal command performs two phases inside one native `/goal`:

```text
Phase 1: shape-goal discovers inputs, saves questions/answers, and obtains approval
Phase 2: goal-engine implements, verifies, reviews, records, and closes
```

Production edits are forbidden before approval. Shaping alone is never successful completion.

## Saved shaping rounds

Default path:

```text
docs/goals/<goal-id>/SHAPING.md
```

The file preserves:

- Every question actually asked
- The user's answer, verbatim when safe
- Evidence and recommendation
- Normalized contract decision
- Corrections and superseded answers
- Round summaries and readiness
- The round that approved execution

The history is append-only. A correction creates a new entry; it does not erase the earlier answer. Sensitive material is redacted and linked to an approved secure source.

A deepening round reads all previous rounds, selects an unexplored or weak lens, and asks only non-duplicate material questions one at a time. Repeat until the user approves, pauses, or a genuine blocker exists.

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

`shape-goal` searches repository instructions, Git, current/prior goals and shaping histories, PRDs, architecture, scripts, CI, tests, runtime evidence, project harness, connected authoritative systems, and current official documentation before asking.

Questions are:

- Limited to material owner decisions
- Asked one at a time
- Accompanied by evidence and a recommendation
- Saved immediately in the shaping history
- Linked to the input ledger and contract
- Never repeated without materially new evidence

## Multiple goals over time

| Change | Lifecycle action |
|---|---|
| Wording or source reference only | Clarify; append shaping note and keep Goal ID |
| Same outcome, material contract change | Amend; pause, run another shaping round, and approve a new revision |
| Different priority | Reprioritize portfolio |
| Temporary interruption | Pause and preserve shaping/progress resume state |
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
├── SHAPING.md
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
/goal Follow goal-engine to complete GOAL.md using its profile, overlays, project harness, and shaping decision record. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, goal-drift review, or two-cycle stall applies; preserve reusable state and leave a restartable handoff.
```

## Update

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```
