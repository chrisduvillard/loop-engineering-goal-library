# Core Goal Profiles

> [!NOTE]
> Generated from canonical files under [`goals/`](goals/) and [`goals/catalog.json`](goals/catalog.json). Edit those sources, then run `python3 scripts/sync_goal_docs.py --write`.

Start with `shape-goal` outside an active `/goal`. It asks one question at a time and returns the exact execution `/goal` after approval.

Seven default control loops for most long-running brownfield work.

---

## [Brownfield Continue / Finish](goals/01-brownfield-continue-finish.md)

**In simple terms:** Understand the real current state and keep completing the most important unblocked work.

**Use when:** An existing repository has an approved direction, partial implementation, or unfinished milestone and should advance autonomously.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Brownfield Continue / Finish profile` | `$shape-goal Use the Brownfield Continue / Finish profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/01-brownfield-continue-finish.md`](goals/01-brownfield-continue-finish.md).

---

## [PRD / Spec Compliance](goals/02-prd-spec-compliance.md)

**In simple terms:** Compare the real product with its requirements and close every proven gap.

**Use when:** A product, feature, or repository must be brought into full alignment with documented requirements.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the PRD / Spec Compliance profile` | `$shape-goal Use the PRD / Spec Compliance profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/02-prd-spec-compliance.md`](goals/02-prd-spec-compliance.md).

---

## [Next Milestone](goals/03-next-milestone.md)

**In simple terms:** Deliver one useful next milestone without wandering into the whole backlog.

**Use when:** A roadmap is larger than one run and the next coherent, dependency-safe increment should be completed end to end.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Next Milestone profile` | `$shape-goal Use the Next Milestone profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/03-next-milestone.md`](goals/03-next-milestone.md).

---

## [Deep Audit + Remediation](goals/04-deep-audit-remediation.md)

**In simple terms:** Find important problems, prove they are real, fix root causes, and prevent recurrence.

**Use when:** The codebase needs evidence-based discovery and repair of important defects or risks.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Deep Audit + Remediation profile` | `$shape-goal Use the Deep Audit + Remediation profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/04-deep-audit-remediation.md`](goals/04-deep-audit-remediation.md).

---

## [QA / Regression / UAT](goals/05-qa-regression-uat.md)

**In simple terms:** Exercise the real product until required workflows and regression gates pass.

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the QA / Regression / UAT profile` | `$shape-goal Use the QA / Regression / UAT profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/05-qa-regression-uat.md`](goals/05-qa-regression-uat.md).

---

## [Safe Refactor / Modernization](goals/06-safe-refactor-modernization.md)

**In simple terms:** Improve internals while proving users and integrations still see the intended behavior.

**Use when:** Architecture, dependencies, or internals should change while external behavior and contracts remain stable.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Safe Refactor / Modernization profile` | `$shape-goal Use the Safe Refactor / Modernization profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/06-safe-refactor-modernization.md`](goals/06-safe-refactor-modernization.md).

---

## [Release Readiness](goals/07-release-readiness.md)

**In simple terms:** Remove verified release blockers and stop at release-ready.

**Use when:** A version or milestone must satisfy all release gates without actually being published or deployed.

| Claude Code | Codex CLI / IDE |
|---|---|
| `/shape-goal Use the Release Readiness profile` | `$shape-goal Use the Release Readiness profile` |

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Advanced autonomous preflight and self-contained fallback:** [Open `goals/07-release-readiness.md`](goals/07-release-readiness.md).
