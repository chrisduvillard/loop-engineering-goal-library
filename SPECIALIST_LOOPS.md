# Specialist Goal Profiles

> [!NOTE]
> Generated from canonical files under [`goals/`](goals/) and [`goals/catalog.json`](goals/catalog.json). Edit those sources, then run `python3 scripts/sync_goal_docs.py --write`.

Start with `shape-goal` outside an active `/goal`. It asks one question at a time and returns the exact execution `/goal` after approval.

Distinct loops for unfamiliar codebases, incidents, upgrades, migrations, branch recovery, optimization, feasibility, AI evaluation, and legacy retirement.

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

---

## [AI / LLM Evaluation & Improvement](goals/25-ai-llm-evaluation-improvement.md)

**In simple terms:** Build a trustworthy eval set, classify failures, test one change at a time, and keep only improvements that survive repeated runs.

**Use when:** An AI, agent, retrieval, ranking, or LLM-powered feature must improve under representative evaluations while controlling quality, safety, latency, and cost.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the AI / LLM Evaluation & Improvement profile` | `$shape-goal Use the AI / LLM Evaluation & Improvement profile` |

**Why it works:** It treats nondeterministic AI behavior as an evaluation problem rather than a demo, so prompt, model, retrieval, and workflow changes are kept only when representative repeated evidence improves without breaking safety or operating constraints.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/25-ai-llm-evaluation-improvement.md`](goals/25-ai-llm-evaluation-improvement.md).

---

## [Deprecation / Legacy Sunset](goals/26-deprecation-legacy-sunset.md)

**In simple terms:** Find who still depends on the old path, provide a safe migration, prove adoption, then remove it in controlled stages.

**Use when:** A legacy API, feature, format, service, flag, dependency, or code path must be retired without abandoning active consumers or removing rollback too early.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Deprecation / Legacy Sunset profile` | `$shape-goal Use the Deprecation / Legacy Sunset profile` |

**Why it works:** Retiring a legacy path is not a normal refactor: success depends on consumer discovery, migration adoption, staged warnings, compatibility windows, and evidence-backed removal rather than merely deleting old code.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/26-deprecation-legacy-sunset.md`](goals/26-deprecation-legacy-sunset.md).

---

## [Codebase Onboarding / Knowledge Recovery](goals/30-codebase-onboarding-knowledge-recovery.md)

**In simple terms:** Turn an unfamiliar repository into a verified map that a new maintainer or agent can safely use.

**Use when:** A mature, inherited, or poorly documented codebase must become understandable, runnable, and safe to change before major delivery work begins.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Codebase Onboarding / Knowledge Recovery profile` | `$shape-goal Use the Codebase Onboarding / Knowledge Recovery profile` |

**Why it works:** It makes understanding a testable deliverable. Repository claims must be traced to code or runtime evidence, and the result becomes durable project infrastructure instead of another disposable audit note.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/30-codebase-onboarding-knowledge-recovery.md`](goals/30-codebase-onboarding-knowledge-recovery.md).
