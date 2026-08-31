# Current Implementation

[`FULL_REPORT.md`](FULL_REPORT.md) is the historical research foundation. The live implementation is an interactive-first workflow for shaping and then autonomously executing software goals.

## Version `0.12.0`

```text
shape-goal                    main interactive entry point
adaptive question depth       two questions or twenty, based on material ambiguity
answer quality gate           ambiguous or partial replies are clarified, never guessed
requirement strength          must, should, preference, optional, or explicit non-goal
bounded delegation            “you decide” records criteria and limits instead of blank authority
clarity stress test           fresh-reader, counterexample, scenario, and verifier review
assumption register           evidence, owner approval, safe defaults, or unresolved
31 execution profiles         reusable loop shapes
12 assurance overlays         extra proof when a concern is secondary
specialist reviewer team      six isolated audit roles with evidence-based consolidation
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
→ score unresolved decisions by impact, uncertainty, and irreversibility
→ ask one atomic material question
→ save and quality-check the answer, then stop the turn
→ repeat, deepen, or stress-test until no material ambiguity remains
→ plain-English teach-back and explicit approval
→ return an exact /goal command
→ goal-engine executes autonomously
→ verify, close out, archive, and reuse
```

The **question barrier** means that `shape-goal` asks once and ends the turn. It never forces the user to steer an active autonomous loop merely to answer.

There is no question quota. A low-risk goal may require two owner decisions; a high-risk, subjective, or irreversible goal may require many more. Approval is blocked while any High- or Medium-impact input or assumption remains unresolved.

## Clarity gate

Before approval, `shape-goal` requires:

- One material interpretation for every answer
- A resolved universal clarity matrix and profile-specific input ledger
- No hidden High-/Medium-impact assumptions
- Operational definitions for subjective terms
- Observable acceptance evidence
- Fresh-reader and counterexample checks with no blocking alternate interpretation
- Scenario, verifier, contradiction, traceability, and plain-English teach-back review as applicable

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
- One atomic material owner decision is asked per turn.
- The question count adapts to risk rather than a fixed quota.
- Safe questions, answers, corrections, assumptions, and approvals are append-only.
- Ambiguous, partial, or conflicting answers trigger clarification rather than inference.
- Requirement strength is preserved, and delegated judgment is explicit, bounded, and reviewable.
- Production execution begins only from an explicitly approved, clarity-tested contract.
- Autonomous execution never interviews the user, chooses among ambiguous interpretations, or expands authority.
- Profiles and overlays cannot weaken the contract.
- Reusable knowledge is promoted into tests, ADRs, documentation, runbooks, fixtures, evals, locale/crawl matrices, architecture maps, scripts, benchmarks, design references, and the Project Harness.

## Adversarial robustness

The repository now includes cross-platform unit, mutation, property, archive, path, history, workflow, and malformed-input tests. Generators and packagers fail closed, use atomic replacement, and reject symlinks, path escapes, hidden command counts, and destructive output choices. See [`docs/ROBUSTNESS_AUDIT.md`](docs/ROBUSTNESS_AUDIT.md).

## Specialist review

High-impact audits can use six isolated reviewer roles covering contract/state, agent control, security/supply chain, portability, verification, and documentation/adoption. Findings use one evidence schema, remain hypotheses until reproduced, and important fixes receive independent re-review. See [`skills/goal-engine/references/specialist-reviewers.md`](skills/goal-engine/references/specialist-reviewers.md).

## Verification

CI validates the canonical profile catalog, recognized overlays, interactive starts, advanced preflight stop behavior, the 4,000-character native-goal limit, profile input coverage, adaptive questioning, append-only history, question-state transitions, closed-goal archives, locked tooling, generated docs, skill metadata, links, discovery, and deterministic ZIP builds across Linux, macOS, and Windows.

## 0.12.0 deterministic control layer

The implementation now includes canonical JSON state, approval fingerprints,
atomic leases, generated state views, mutation-mode enforcement, separate
lifecycle and termination concepts, assurance levels, a compaction-resistant
Goal Kernel, held-out verification guidance, and deterministic behavioral
invariant scoring. Live host UAT remains pending and is documented as a beta
release gate rather than implied by repository tests.
