# Current Implementation

[`FULL_REPORT.md`](FULL_REPORT.md) is the historical research foundation. The live implementation is an interactive-first workflow for shaping and then autonomously executing software goals.

## Version `0.8.0`

```text
shape-goal                    main interactive entry point
31 execution profiles        reusable loop shapes
12 assurance overlays        extra proof when a concern is secondary
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

The **question barrier** means that `shape-goal` asks once and ends the turn. It never forces the user to steer an active autonomous loop merely to answer.

## Advanced preflight

Each canonical profile contains skill-backed and self-contained `/goal` preflights for environments where an already-approved artifact resolves every owner decision. At the first missing decision they save one recommended question and stop as **Approval required**.

## Coverage

### Core

Continuation, requirements compliance, milestone delivery, audit/remediation, QA/UAT, safe refactoring, and release readiness.

### Specialist

Incident recovery, upgrades, data migration, branch rescue, optimization, feasibility, AI/LLM evaluation, legacy sunset, and codebase onboarding/knowledge recovery.

### Product and quality

Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, audit readiness, internationalization/localization, backup/restore/disaster recovery, product analytics/experimentation integrity, and search/SEO/web discoverability.

Custom Contract-Driven remains the fallback for unusual loops.

## Safety and reuse

- Facts are discovered before users are questioned.
- One material owner question is asked per turn.
- Safe questions, answers, corrections, and approvals are append-only.
- Production execution begins only from an explicitly approved contract.
- Autonomous execution never interviews the user or expands authority.
- Profiles and overlays cannot weaken the contract.
- Reusable knowledge is promoted into tests, ADRs, documentation, runbooks, fixtures, evals, locale/crawl matrices, architecture maps, scripts, benchmarks, design references, and the Project Harness.

## Verification

CI validates the 31-profile catalog, 12 recognized overlays, interactive starts, advanced preflight stop behavior, the 4,000-character native-goal limit, profile input coverage, shaping-history rules, generated docs, README install/update guidance, skill metadata, links, package discovery, and deterministic ZIP builds.
