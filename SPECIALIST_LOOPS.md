# Specialist Goal Profiles

> [!NOTE]
> Generated from canonical files under [`goals/`](goals/) and [`goals/catalog.json`](goals/catalog.json). Edit those sources, then run `python3 scripts/sync_goal_docs.py --write`.

Start with `shape-goal` outside an active `/goal`. It asks one question at a time and returns the exact execution `/goal` after approval.

Six distinct loops for incidents, upgrades, migrations, branch recovery, optimization, and feasibility.

---

## [Incident Recovery / Stabilization](goals/08-incident-recovery.md)

**In simple terms:** Contain damage, restore health, prove the cause, and add prevention.

**Use when:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding damage.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Incident Recovery / Stabilization profile` | `$shape-goal Use the Incident Recovery / Stabilization profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/08-incident-recovery.md`](goals/08-incident-recovery.md).

---

## [Dependency / Framework Upgrade](goals/09-dependency-framework-upgrade.md)

**In simple terms:** Upgrade through safe version steps while checking the full compatibility surface.

**Use when:** A dependency, framework, language runtime, or toolchain must move to a target version without breaking supported behavior.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Dependency / Framework Upgrade profile` | `$shape-goal Use the Dependency / Framework Upgrade profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/09-dependency-framework-upgrade.md`](goals/09-dependency-framework-upgrade.md).

---

## [Data Migration / Integrity](goals/10-data-migration-integrity.md)

**In simple terms:** Migrate data through reversible phases and prove no unexplained loss, duplication, or corruption.

**Use when:** Stored data, schemas, formats, or backfills must change while preserving correctness, compatibility, and recoverability.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Data Migration / Integrity profile` | `$shape-goal Use the Data Migration / Integrity profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/10-data-migration-integrity.md`](goals/10-data-migration-integrity.md).

---

## [Branch Rescue / Integration](goals/11-branch-rescue-integration.md)

**In simple terms:** Recover useful behavioral slices without overwriting newer target work.

**Use when:** Valuable work is stranded in a stale, divergent, oversized, or conflicting branch and must be recovered safely.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Branch Rescue / Integration profile` | `$shape-goal Use the Branch Rescue / Integration profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/11-branch-rescue-integration.md`](goals/11-branch-rescue-integration.md).

---

## [Measured Optimization / Benchmark](goals/12-measured-optimization-benchmark.md)

**In simple terms:** Freeze a baseline, test one challenger at a time, and keep only reproducible wins.

**Use when:** A stable metric must improve under a fixed protocol without regressing required behavior.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Measured Optimization / Benchmark profile` | `$shape-goal Use the Measured Optimization / Benchmark profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/12-measured-optimization-benchmark.md`](goals/12-measured-optimization-benchmark.md).

---

## [Technical Spike / Feasibility](goals/13-technical-spike-feasibility.md)

**In simple terms:** Run an isolated experiment and return a Go, Conditional Go, or No-Go decision.

**Use when:** A bounded technical unknown must be resolved before production commitment.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Technical Spike / Feasibility profile` | `$shape-goal Use the Technical Spike / Feasibility profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/13-technical-spike-feasibility.md`](goals/13-technical-spike-feasibility.md).
