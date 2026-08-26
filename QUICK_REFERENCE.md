# Quick Reference

## Install

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

## Main command

Run `shape-goal` outside an active `/goal`:

| Need | Claude Code | Codex CLI / IDE |
|---|---|---|
| Shape or continue | `/shape-goal Continue this project` | `$shape-goal Continue this project` |
| Use a profile | `/shape-goal Use the profile-name profile` | `$shape-goal Use the profile-name profile` |
| Add another goal | `/shape-goal New goal: describe the intent` | `$shape-goal New goal: describe the intent` |
| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |
| Stress-test clarity | `/shape-goal Stress-test the current goal` | `$shape-goal Stress-test the current goal` |
| Resume | `/shape-goal Resume goal-id` | `$shape-goal Resume goal-id` |
| Review priorities | `/shape-goal Review the goal portfolio` | `$shape-goal Review the goal portfolio` |

## Normal workflow

```text
1. shape-goal investigates the repository
2. it asks one material question and ends the turn
3. you reply normally; no Steer message is required
4. it saves the answer and checks whether it has one clear interpretation
5. it asks as many non-duplicate questions as the risk and ambiguity require
6. it stress-tests assumptions, scenarios, wording, and acceptance evidence
7. you approve, deepen, stress-test, or pause
8. it returns the exact /goal command
9. goal-engine executes autonomously
10. evidence, closeout, and reusable learning are archived
```

## Question rule

After asking a shaping question, the agent must:

- Save the exact proposed question
- End the turn immediately
- Call no more tools
- Start no background work
- Ask no second question
- Save your next reply before continuing

## How many questions?

There is no fixed number. Two questions are enough when the repository already resolves everything else. Many more are correct when choices are high-impact, subjective, conflicting, or irreversible. Approval waits until no material ambiguity or hidden High-/Medium-impact assumption remains.

An ambiguous or partial reply triggers one targeted clarification; the agent must not guess. It also preserves Must versus Preference wording. “You decide” becomes a bounded, recorded delegation with criteria—not permission to expand the outcome or authority.

## If shaping is trapped inside `/goal`

When the UI shows **Pursuing goal** while a question is waiting:

- Codex: `/goal pause` or `/goal clear`, then `$shape-goal Resume goal-id`
- Claude Code: `/goal clear`, then `/shape-goal Resume goal-id`

## Approval and execution

After the contract is approved, `shape-goal` returns a command like:

```text
/goal Follow goal-engine to complete the approved Goal Contract in GOAL.md. Stop only when every acceptance item passes with surfaced evidence, or when a contract-defined blocker, approval boundary, budget, material goal drift, or two-cycle stall applies; preserve reusable state and leave a restartable handoff.
```

## Saved shaping rounds

```text
docs/goals/<goal-id>/SHAPING.md
```

It preserves:

- Exact questions and safe answers
- Evidence and recommendation
- Normalized contract decisions
- Corrections and supersessions
- Round summaries
- Explicit approval record

A deepening round reads all earlier decisions and asks only materially new questions.

## Common profiles

| Need | Profile |
|---|---|
| Finish existing work | Brownfield Continue / Finish |
| Close requirements | PRD / Spec Compliance |
| Deliver the next increment | Next Milestone |
| Find and fix important problems | Deep Audit + Remediation |
| Prove real product workflows | QA / Regression / UAT |
| Modernize without behavior drift | Safe Refactor / Modernization |
| Prepare a release | Release Readiness |
| Recover from a severe failure | Incident Recovery / Stabilization |
| Upgrade a dependency or framework | Dependency / Framework Upgrade |
| Migrate data or schema | Data Migration / Integrity |
| Recover a divergent branch | Branch Rescue / Integration |
| Improve a measurable property | Measured Optimization / Benchmark |
| Resolve a technical unknown | Technical Spike / Feasibility |
| Improve frontend quality | Frontend UI / UX / Accessibility |
| Correct documentation | Documentation Synchronization / Knowledge Transfer |
| Harden security | Security / Privacy Hardening |
| Improve failure recovery | Reliability / Resilience Hardening |
| Evolve APIs safely | API / Integration Contract Compatibility |
| Improve operations | Observability / Operability |
| Improve developer workflows | Developer Experience / Tooling |
| Assure data pipelines | Data Quality / Pipeline Assurance |
| Repair tests and CI | Test Suite / CI Health |
| Prove deployment readiness | Infrastructure / Deployment Readiness |
| Prepare audit evidence | Compliance / Audit Readiness |
| Improve an AI or LLM feature with evals | AI / LLM Evaluation & Improvement |
| Retire a legacy path safely | Deprecation / Legacy Sunset |
| Prepare multiple languages and regions | Internationalization / Localization Readiness |
| Prove backups and disaster recovery | Backup / Restore / Disaster Recovery |
| Make analytics and experiments trustworthy | Product Analytics / Experimentation Integrity |
| Understand an inherited codebase | Codebase Onboarding / Knowledge Recovery |
| Improve public crawlability and discovery | Search / SEO / Web Discoverability |
| None fits | Custom Contract-Driven |

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

Use only when secondary to the primary profile:

- Security & Privacy
- Reliability & Recovery
- Performance & Cost
- UX & Accessibility
- Data Integrity & Governance
- Compatibility & Portability
- Operability & Observability
- Documentation & Knowledge Transfer
- Compliance & Auditability

## Update to the latest version

```bash
npx -y skills@latest update shape-goal goal-engine --global --yes
```

Restart Codex or Claude Code after updating.
