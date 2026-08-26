# Core `/goal` Library

> [!NOTE]
> Generated from canonical files under [`goals/`](goals/) and [`goals/catalog.json`](goals/catalog.json). Edit those sources, then run `python3 scripts/sync_goal_docs.py --write`.

Seven default control loops for most long-running brownfield work.

---

## [Brownfield Continue / Finish](goals/01-brownfield-continue-finish.md)

**In simple terms:** Understand the real current state and keep completing the most important unblocked work.

**Use when:** An existing repository has an approved direction, partial implementation, or unfinished milestone and should advance autonomously.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Brownfield Continue / Finish objective. During shaping, load shape-goal's required-input specification for Brownfield Continue / Finish; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to reconcile current state, select the highest-priority dependency-safe gap, and finish the approved outcome rather than merely planning it; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/01-brownfield-continue-finish.md`](goals/01-brownfield-continue-finish.md).

---

## [PRD / Spec Compliance](goals/02-prd-spec-compliance.md)

**In simple terms:** Compare the real product with its requirements and close every proven gap.

**Use when:** A product, feature, or repository must be brought into full alignment with documented requirements.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next PRD / Spec Compliance objective. During shaping, load shape-goal's required-input specification for PRD / Spec Compliance; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to build a requirement-to-evidence map, reconcile contradictory requirements, and close every verified in-scope gap; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/02-prd-spec-compliance.md`](goals/02-prd-spec-compliance.md).

---

## [Next Milestone](goals/03-next-milestone.md)

**In simple terms:** Deliver one useful next milestone without wandering into the whole backlog.

**Use when:** A roadmap is larger than one run and the next coherent, dependency-safe increment should be completed end to end.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Next Milestone objective. During shaping, load shape-goal's required-input specification for Next Milestone; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to choose one coherent next milestone, define its evidence, and complete it without unrelated scope expansion; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/03-next-milestone.md`](goals/03-next-milestone.md).

---

## [Deep Audit + Remediation](goals/04-deep-audit-remediation.md)

**In simple terms:** Find important problems, prove they are real, fix root causes, and prevent recurrence.

**Use when:** The codebase needs evidence-based discovery and repair of important defects or risks.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Deep Audit + Remediation objective. During shaping, load shape-goal's required-input specification for Deep Audit + Remediation; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to audit against an explicit rubric and severity bar, verify findings, remediate root causes, and repeat to evidence saturation; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/04-deep-audit-remediation.md`](goals/04-deep-audit-remediation.md).

---

## [QA / Regression / UAT](goals/05-qa-regression-uat.md)

**In simple terms:** Exercise the real product until required workflows and regression gates pass.

**Use when:** The actual product surface and realistic user workflows must pass defined acceptance gates.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next QA / Regression / UAT objective. During shaping, load shape-goal's required-input specification for QA / Regression / UAT; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to discover the real product surface, build a risk-based flow matrix, reproduce failures, fix root causes, and rerun clean end-to-end evidence; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/05-qa-regression-uat.md`](goals/05-qa-regression-uat.md).

---

## [Safe Refactor / Modernization](goals/06-safe-refactor-modernization.md)

**In simple terms:** Improve internals while proving users and integrations still see the intended behavior.

**Use when:** Architecture, dependencies, or internals should change while external behavior and contracts remain stable.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Safe Refactor / Modernization objective. During shaping, load shape-goal's required-input specification for Safe Refactor / Modernization; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to capture behavioral baselines, create safe seams, change incrementally, and prove equivalence with rollback; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/06-safe-refactor-modernization.md`](goals/06-safe-refactor-modernization.md).

---

## [Release Readiness](goals/07-release-readiness.md)

**In simple terms:** Remove verified release blockers and stop at release-ready.

**Use when:** A version or milestone must satisfy all release gates without actually being published or deployed.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Release Readiness objective. During shaping, load shape-goal's required-input specification for Release Readiness; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Create or resume an append-only `SHAPING.md` under the resolved goal archive; after every answer, save the exact question, safe user answer, evidence, recommendation, normalized decision, and contract impact, and append corrections or supersessions instead of rewriting history. At each shaping-round close, let the user approve, request another deeper non-duplicate round, or pause; deeper rounds must read all prior rounds first. Then hand off within this same goal to goal-engine to turn repository-defined release criteria into evidence, resolve blockers by risk, and verify artifacts, migrations, operations, and rollback together; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.

**Full profile and self-contained fallback:** [Open `goals/07-release-readiness.md`](goals/07-release-readiness.md).
