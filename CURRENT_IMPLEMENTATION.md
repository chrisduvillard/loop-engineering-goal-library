# Current Implementation

The original [`FULL_REPORT.md`](FULL_REPORT.md) is the research foundation. The live implementation has evolved through field-oriented design reviews.

## Version `0.5.0`

```text
24 zero-friction goal profiles
+ shape-goal
+ goal-engine
+ profile-specific input specifications
+ append-only shaping questions and answers
+ repeatable deeper shaping rounds
+ assurance overlays
+ reusable Project Harness
+ multi-goal portfolio and immutable closeout history
```

## Zero-friction contract

The first command in every canonical goal file runs unchanged.

```text
Copied /goal
→ shape-goal searches and resolves inputs
→ every asked question and answer is saved
→ user may request deeper non-duplicate shaping rounds
→ user approves the Goal Contract and approval round
→ goal-engine executes
→ acceptance evidence passes
→ shaping, closeout, and reusable knowledge are preserved
```

The launcher forbids production changes before approval and forbids successful completion after shaping alone.

## Coverage

### Core

Continuation, requirements compliance, milestone delivery, audit/remediation, QA/UAT, safe refactoring, and release readiness.

### Specialist

Incident recovery, ecosystem upgrades, data migration, branch rescue, measured optimization, and technical feasibility.

### Product and quality

Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, and audit readiness.

Custom Contract-Driven remains the fallback for unusual loops.

## Shaping history

As soon as a Goal ID exists, the default decision record is:

```text
docs/goals/<goal-id>/SHAPING.md
```

It preserves every asked question, the user's answer, evidence, recommendation, normalized decision, corrections, deferred items, and round summaries. The record is append-only. Sensitive answers are redacted and referenced securely.

The initial round resolves the minimum material decisions required for readiness. A user who is not satisfied can request repeated deeper rounds; each round reads all earlier decisions, selects an unexplored or weak lens, avoids duplicate questions, and updates the contract without erasing history.

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

- Repository facts are searched before users are questioned.
- Only material owner decisions are asked.
- Questions are one at a time with evidence and a recommendation.
- Public repositories never receive confidential strategy or restricted answers verbatim; safe summaries link approved secure evidence.
- Every asked question and answer is saved, unless sensitive content requires a redacted summary and secure reference.
- Corrections append and supersede prior answers rather than rewriting them.
- Production execution begins only from an explicitly approved shaping round.
- One native goal session/worktree executes one dependency-safe leaf contract.
- Profiles and overlays cannot weaken the contract or expand authority.
- Shaping cannot satisfy the enclosing goal.
- Production, destructive, credential, release, security-testing, and legal/compliance boundaries remain explicit.

## Verification

CI validates the catalog, every launcher and fallback, profile input coverage, shaping-history protocol and template, contract/progress/result/history linkage, worked multi-round example, generated docs, skill metadata, OpenAI host metadata, state schemas, links, package discovery, and deterministic ZIP builds.
