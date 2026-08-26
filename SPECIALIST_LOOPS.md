# Specialist `/goal` Library

> [!NOTE]
> Generated from canonical files under [`goals/`](goals/) and [`goals/catalog.json`](goals/catalog.json). Edit those sources, then run `python3 scripts/sync_goal_docs.py --write`.

Six distinct loops for incidents, upgrades, migrations, branch recovery, optimization, and feasibility.

---

## [Incident Recovery / Stabilization](goals/08-incident-recovery.md)

**In simple terms:** Contain damage, restore health, prove the cause, and add prevention.

**Use when:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding damage.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Incident Recovery / Stabilization objective. During shaping, load shape-goal's required-input specification for Incident Recovery / Stabilization; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to separate containment, restoration, root-cause proof, and prevention while preserving incident evidence; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/08-incident-recovery.md`](goals/08-incident-recovery.md).

---

## [Dependency / Framework Upgrade](goals/09-dependency-framework-upgrade.md)

**In simple terms:** Upgrade through safe version steps while checking the full compatibility surface.

**Use when:** A dependency, framework, language runtime, or toolchain must move to a target version without breaking supported behavior.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Dependency / Framework Upgrade objective. During shaping, load shape-goal's required-input specification for Dependency / Framework Upgrade; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to map the dependency graph, follow official version-path guidance, stage changes, inspect transitive effects, and prove compatibility; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/09-dependency-framework-upgrade.md`](goals/09-dependency-framework-upgrade.md).

---

## [Data Migration / Integrity](goals/10-data-migration-integrity.md)

**In simple terms:** Migrate data through reversible phases and prove no unexplained loss, duplication, or corruption.

**Use when:** Stored data, schemas, formats, or backfills must change while preserving correctness, compatibility, and recoverability.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Data Migration / Integrity objective. During shaping, load shape-goal's required-input specification for Data Migration / Integrity; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to define invariants and reconciliation first, use expand/backfill/verify/switch/contract phases, and test retry and rollback; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/10-data-migration-integrity.md`](goals/10-data-migration-integrity.md).

---

## [Branch Rescue / Integration](goals/11-branch-rescue-integration.md)

**In simple terms:** Recover useful behavioral slices without overwriting newer target work.

**Use when:** Valuable work is stranded in a stale, divergent, oversized, or conflicting branch and must be recovered safely.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Branch Rescue / Integration objective. During shaping, load shape-goal's required-input specification for Branch Rescue / Integration; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to pin source and target state, classify source slices, port only dependency-complete valid behavior, and account for every decision; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/11-branch-rescue-integration.md`](goals/11-branch-rescue-integration.md).

---

## [Measured Optimization / Benchmark](goals/12-measured-optimization-benchmark.md)

**In simple terms:** Freeze a baseline, test one challenger at a time, and keep only reproducible wins.

**Use when:** A stable metric must improve under a fixed protocol without regressing required behavior.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Measured Optimization / Benchmark objective. During shaping, load shape-goal's required-input specification for Measured Optimization / Benchmark; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to freeze the benchmark protocol, compare champion and challengers under identical conditions, and retain only meaningful improvements; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/12-measured-optimization-benchmark.md`](goals/12-measured-optimization-benchmark.md).

---

## [Technical Spike / Feasibility](goals/13-technical-spike-feasibility.md)

**In simple terms:** Run an isolated experiment and return a Go, Conditional Go, or No-Go decision.

**Use when:** A bounded technical unknown must be resolved before production commitment.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Technical Spike / Feasibility objective. During shaping, load shape-goal's required-input specification for Technical Spike / Feasibility; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to frame one decision question, test the smallest isolated prototypes, compare options, and deliver evidence rather than production code; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/13-technical-spike-feasibility.md`](goals/13-technical-spike-feasibility.md).
