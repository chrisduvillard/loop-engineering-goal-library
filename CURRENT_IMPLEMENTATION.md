# Current Implementation

[`FULL_REPORT.md`](FULL_REPORT.md) is the historical research foundation. The live implementation is an interactive-first workflow for shaping and then autonomously executing software goals.

## Version `0.7.0`

```text
shape-goal                    main interactive entry point
29 execution profiles        reusable loop shapes
goal-engine                   autonomous brownfield execution
SHAPING.md                    durable questions and answers
Goal Contract                 approved definition of done
Project Harness               reusable project mechanics
Goal Portfolio                multiple goals over time
```

## Primary workflow

```text
shape-goal outside /goal
→ inspect repository evidence
→ ask one material question
→ save the answer and stop the turn
→ repeat or deepen
→ approve the Goal Contract
→ return an exact /goal command
→ goal-engine executes autonomously
→ verify, close out, archive, and reuse
```

This separation is intentional. Shaping is interactive; native `/goal` loops automatically continue between turns and are therefore reserved for execution after the target and proof are approved.

## Advanced preflight

Each canonical profile still contains two `/goal` preflights for exceptional environments:

- Skill-backed autonomous preflight
- Self-contained autonomous preflight

They continue only when an already-approved artifact resolves every owner decision. At the first unresolved decision they save one recommended question and stop as **Approval required** rather than asking and continuing inside the active goal.

## Coverage

### Core

Continuation, requirements compliance, milestone delivery, audit/remediation, QA/UAT, safe refactoring, and release readiness.

### Specialist

Incident recovery, ecosystem upgrades, data migration, branch rescue, measured optimization, technical feasibility, AI/LLM evaluation, and legacy sunset.

### Product and quality

Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, audit readiness, internationalization/localization, backup/restore/disaster recovery, and product analytics/experimentation integrity.

Custom Contract-Driven remains the fallback for unusual loops.

## Shaping history

As soon as a Goal ID exists, the default decision record is:

```text
docs/goals/<goal-id>/SHAPING.md
```

It preserves every asked question, safe user answer, evidence, recommendation, normalized decision, correction, deferred item, approval, and round summary. The record is append-only. Sensitive answers are redacted and referenced securely.

The question barrier is explicit:

1. Search before asking.
2. Save one exact question.
3. Ask it.
4. End the turn immediately.
5. Save the user's next reply before continuing.

A user can request repeated deeper rounds without losing earlier decisions.

## State

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

## Safety

- Facts are discovered before users are questioned.
- Only material owner decisions are asked.
- Questions are one at a time with evidence and a recommendation.
- No question is asked inside an active autonomous goal unless that goal will stop immediately.
- Public repositories never receive confidential strategy or restricted answers verbatim.
- Corrections append and supersede rather than rewriting history.
- Production execution begins only from an explicitly approved shaping round.
- One native goal session or worktree executes one dependency-safe leaf contract.
- Profiles and overlays cannot weaken the contract or expand authority.
- Production, destructive, credential, release, security-testing, and legal/compliance boundaries remain explicit.

## Verification

CI validates the 29-profile catalog, interactive start commands, advanced preflight stop behavior, the 4,000-character native-goal limit, profile input coverage, shaping-history append-only rules, contract/progress/result linkage, generated docs, skill metadata, links, package discovery, and deterministic ZIP builds.
