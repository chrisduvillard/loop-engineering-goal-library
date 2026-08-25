# Current Implementation

The original [`FULL_REPORT.md`](FULL_REPORT.md) is the research foundation. The live implementation has evolved through field-oriented design reviews.

## Version `0.4.0`

```text
22 zero-friction goal profiles
+ shape-goal
+ goal-engine
+ profile-specific input specifications
+ assurance overlays
+ reusable Project Harness
+ multi-goal portfolio and immutable closeout history
```

## Zero-friction contract

The first command in every canonical goal file runs unchanged.

```text
Copied /goal
→ shape-goal searches and resolves inputs
→ user approves the Goal Contract
→ goal-engine executes
→ acceptance evidence passes
→ closeout is archived and reusable knowledge is promoted
```

The launcher forbids production changes before approval and forbids successful completion after shaping alone.

## Coverage

### Core

Continuation, requirements compliance, milestone delivery, audit/remediation, QA/UAT, safe refactoring, and release readiness.

### Specialist

Incident recovery, ecosystem upgrades, data migration, branch rescue, measured optimization, and technical feasibility.

### Product and quality

Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, and audit readiness.

Custom Contract-Driven remains the fallback for unusual loops.

## State

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

## Safety

- Repository facts are searched before users are questioned.
- Only material owner decisions are asked.
- Questions are one at a time with evidence and a recommendation.
- One native goal session/worktree executes one dependency-safe leaf contract.
- Profiles and overlays cannot weaken the contract or expand authority.
- Shaping cannot satisfy the enclosing goal.
- Production, destructive, credential, release, security-testing, and legal/compliance boundaries remain explicit.

## Verification

CI validates the catalog, every launcher and fallback, profile input coverage, generated docs, skill metadata, OpenAI host metadata, state schemas, links, package discovery, and deterministic ZIP builds.
