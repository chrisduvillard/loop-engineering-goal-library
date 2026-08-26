# Goal Engine: Execution Profiles

Execution profiles are control-loop presets, not project types and not an exhaustive taxonomy. The approved Goal Contract always wins on outcome, scope, acceptance evidence, protected behavior, authority, and stop conditions.

Choose one primary profile when it matches the dominant execution shape. Use a dedicated quality profile when that quality is the primary outcome; use the matching assurance overlay when it is secondary to another goal.

## 1. Brownfield Continue / Finish

**Use for:** An existing repository has an approved direction, partial implementation, or unfinished milestone and should advance autonomously.

- Reconcile current state, select the highest-priority dependency-safe gap, and finish the approved outcome rather than merely planning it.
- Select the highest-priority unblocked gap.
- Verify the gap before editing.
- Do not stop at planning, tests, or documentation while required production work remains.

## 2. PRD / Spec Compliance

**Use for:** A product, feature, or repository must be brought into full alignment with documented requirements.

- Build a requirement-to-evidence map, reconcile contradictory requirements, and close every verified in-scope gap.
- Maintain requirement-to-evidence status.
- Never weaken a requirement or verifier.
- Escalate only genuine product contradictions.

## 3. Next Milestone

**Use for:** A roadmap is larger than one run and the next coherent, dependency-safe increment should be completed end to end.

- Choose one coherent next milestone, define its evidence, and complete it without unrelated scope expansion.
- Finish one milestone, not the roadmap.
- Avoid opportunistic modernization.
- Deliver production behavior end to end.

## 4. Deep Audit + Remediation

**Use for:** The codebase needs evidence-based discovery and repair of important defects or risks.

- Audit against an explicit rubric and severity bar, verify findings, remediate root causes, and repeat to evidence saturation.
- Treat scanner/reviewer output as hypotheses.
- Rank by severity, confidence, and blast radius.
- Fix verified root causes and add regression coverage.

## 5. QA / Regression / UAT

**Use for:** The actual product surface and realistic user workflows must pass defined acceptance gates.

- Discover the real product surface, build a risk-based flow matrix, reproduce failures, fix root causes, and rerun clean end-to-end evidence.
- Test realistic workflows, not only units.
- Verify failures before fixing.
- Rerun exact failures and affected broader gates.

## 6. Safe Refactor / Modernization

**Use for:** Architecture, dependencies, or internals should change while external behavior and contracts remain stable.

- Capture behavioral baselines, create safe seams, change incrementally, and prove equivalence with rollback.
- Map consumers and contracts.
- Change one coherent seam at a time.
- Keep rollback until equivalence is proven.

## 7. Release Readiness

**Use for:** A version or milestone must satisfy all release gates without actually being published or deployed.

- Turn repository-defined release criteria into evidence, resolve blockers by risk, and verify artifacts, migrations, operations, and rollback together.
- Prepare but do not release.
- Work highest-risk blockers first.
- Verify artifacts, configuration, migrations, docs, and rollback together.

## 8. Incident Recovery / Stabilization

**Use for:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding damage.

- Separate containment, restoration, root-cause proof, and prevention while preserving incident evidence.
- Preserve evidence.
- Prefer reversible containment.
- Prove recovery and root cause separately.

## 9. Dependency / Framework Upgrade

**Use for:** A dependency, framework, language runtime, or toolchain must move to a target version without breaking supported behavior.

- Map the dependency graph, follow official version-path guidance, stage changes, inspect transitive effects, and prove compatibility.
- Upgrade coherent boundaries.
- Inspect lockfiles and generated changes.
- Avoid unrelated modernization.

## 10. Data Migration / Integrity

**Use for:** Stored data, schemas, formats, or backfills must change while preserving correctness, compatibility, and recoverability.

- Define invariants and reconciliation first, use expand/backfill/verify/switch/contract phases, and test retry and rollback.
- Define reconciliation before mutation.
- Test interruption/retry/rollback.
- Require approval before destructive cleanup.

## 11. Branch Rescue / Integration

**Use for:** Valuable work is stranded in a stale, divergent, oversized, or conflicting branch and must be recovered safely.

- Pin source and target state, classify source slices, port only dependency-complete valid behavior, and account for every decision.
- Protect recovery refs.
- Classify slices as present/obsolete/conflicting/worth porting.
- Never merge wholesale without evidence.

## 12. Measured Optimization / Benchmark

**Use for:** A stable metric must improve under a fixed protocol without regressing required behavior.

- Freeze the benchmark protocol, compare champion and challengers under identical conditions, and retain only meaningful improvements.
- Freeze the protocol before changes.
- Change one hypothesis at a time.
- Keep only reproducible wins without floor regressions.

## 13. Technical Spike / Feasibility

**Use for:** A bounded technical unknown must be resolved before production commitment.

- Frame one decision question, test the smallest isolated prototypes, compare options, and deliver evidence rather than production code.
- Keep spike code isolated and disposable.
- Do not let prototype become production silently.
- Finish with a decision and explicit conditions.

## 14. Frontend UI / UX / Accessibility

**Use for:** A frontend surface must become coherent, usable, responsive, accessible, and visually polished without regressing behavior.

- Inventory screens and states, reconcile design references and system patterns, test real interactions across supported viewports, and iterate on verified usability and visual gaps.
- Exercise real browser flows and all important states.
- Use screenshots/visual comparison plus functional checks.
- Verify keyboard, focus, semantics, contrast, responsive behavior, loading/error/empty states.

## 15. Documentation Synchronization / Knowledge Transfer

**Use for:** Documentation, examples, runbooks, diagrams, or onboarding material must accurately match current behavior and be usable by its audience.

- Map authoritative behavior to every affected document, execute examples and commands where possible, remove contradictions, and add drift prevention.
- Verify documentation claims against behavior.
- Run commands and examples rather than copying stale text.
- Link decisions to authoritative sources and prevent future drift.

## 16. Security / Privacy Hardening

**Use for:** Security and privacy are the primary outcome: attack surface, authorization, secrets, dependencies, or data handling must be hardened and verified.

- Establish assets and trust boundaries, verify attack paths and findings, prioritize by severity and exploitability, remediate root causes, and retest.
- Never exploit or mutate external systems without approval.
- Treat scanner findings as hypotheses.
- Test authorization and data-boundary regressions.

## 17. Reliability / Resilience Hardening

**Use for:** A system must continue or recover correctly under defined failures, load, retries, restarts, and dependency degradation.

- Define service objectives and failure scenarios, reproduce weaknesses, harden idempotency and recovery, and verify under controlled faults.
- Test failures and recovery, not only happy paths.
- Protect data during retries/restarts.
- Prefer graceful degradation and bounded retries.

## 18. API / Integration Contract Compatibility

**Use for:** APIs, events, schemas, SDKs, or external integrations must remain compatible across producers, consumers, and versions.

- Inventory providers and consumers, establish contract baselines, test version combinations, and stage changes with deprecation and rollback.
- Treat undocumented consumers as a risk to investigate.
- Verify positive and negative contract behavior.
- Stage additive changes before removals.

## 19. Observability / Operability

**Use for:** Operators and maintainers must be able to detect, understand, and recover from important failures using useful signals and runbooks.

- Map critical journeys to signals, improve logs/metrics/traces/health checks, tune alerts, create runbooks, and validate diagnosis and recovery.
- Instrument outcomes rather than noise.
- Avoid secrets/high-cardinality leaks.
- Test alerts and runbooks with controlled scenarios.

## 20. Developer Experience / Tooling

**Use for:** Local setup, build, test, debug, CI, or contribution workflows must become faster, clearer, and reproducible.

- Measure developer workflows, remove verified friction, align local and CI behavior, and preserve a reusable project harness.
- Test from clean state.
- Prefer canonical scripts/task runners.
- Make failures actionable and keep local/CI parity.

## 21. Data Quality / Pipeline Assurance

**Use for:** A data pipeline or dataset must satisfy defined freshness, completeness, validity, consistency, lineage, and reconciliation expectations.

- Map sources and transformations, establish measurable data contracts, reproduce quality failures, fix root causes, and add monitoring and reconciliation.
- Verify quality at boundaries and end-to-end.
- Distinguish source defects from transformation defects.
- Add durable checks and lineage evidence.

## 22. Compliance / Audit Readiness

**Use for:** A repository or system must produce implementation evidence for an approved control set without falsely self-certifying legal or regulatory compliance.

- Identify the authoritative control framework, map each control to code/config/process/evidence, verify gaps, remediate technical findings, and prepare reviewer-ready evidence.
- Do not invent policy or self-certify.
- Separate technical evidence from legal interpretation.
- Preserve chain of evidence and approval boundaries.

## 23. Test Suite / CI Health

**Use for:** Making automated tests and CI reliable evidence rather than a flaky, slow, or misleading gate.

- Map suites, environments, fixtures, services, retries, skips, quarantines, caches, and workflow dependencies.
- Reproduce and classify flakes, false positives/negatives, hidden skips, isolation failures, and local/CI drift.
- Fix root causes without weakening required assertions or silently excluding difficult coverage.
- Finish only after repeated clean runs meet the approved determinism, runtime, diagnostic, coverage, and parity gates.

## 24. Infrastructure / Deployment Readiness

**Use for:** Proving infrastructure and deployment mechanics ready without performing an unauthorized production rollout.

- Reconcile infrastructure-as-code, configuration, artifacts, migrations, application assumptions, and environment differences.
- Validate provisioning and deployment stages in approved non-production, ephemeral, dry-run, or simulated environments.
- Exercise smoke checks, health signals, failure handling, observability, and rollback together.
- Finish at evidence-backed readiness; never provision or mutate production without explicit contract authority.

## 25. AI / LLM Evaluation & Improvement

**Use for:** An AI, agent, retrieval, ranking, or LLM-powered feature must improve under representative evaluations while controlling quality, safety, latency, and cost.

- Freeze a versioned evaluation set, grader/rubric, sampling protocol, and operational floors before changing the system.
- Capture a baseline and failure taxonomy, then test one prompt, model, retrieval, tool, or orchestration hypothesis at a time.
- Repeat nondeterministic runs and compare capability, grounding, safety, latency, cost, and reliability together.
- Keep only reproducible improvements, add discovered failures to regression evals, and version the winning configuration.

## 26. Deprecation / Legacy Sunset

**Use for:** A legacy API, feature, format, service, flag, dependency, or code path must be retired without abandoning active consumers or removing rollback too early.

- Inventory consumers and real usage, including undocumented integrations and long-tail versions.
- Make the replacement production-ready, ship migration tooling and warnings, and measure adoption and error rates.
- Migrate dependency-safe slices and preserve compatibility or rollback through the approved window.
- Remove the legacy surface only after the contract's consumer, telemetry, support, and authority gates pass; then clean up and verify.

## 27. Internationalization / Localization Readiness

**Use for:** A product must work correctly across approved languages, regions, scripts, reading directions, time zones, and local formats.

- Build a supported locale matrix and inventory strings, content, routing, formatting, directionality, fonts, and layout assumptions.
- Centralize messages and locale-aware behavior, define fallbacks, and prevent untranslated or ambiguous states.
- Run pseudo-localization, expansion, RTL, locale-format, browser, visual, and accessibility checks.
- Require qualified human review for linguistic or legal meaning and finish only when every supported locale's evidence passes.

## 28. Backup / Restore / Disaster Recovery

**Use for:** Critical application state must be recoverable within approved recovery objectives, with backups and restore procedures proven by realistic drills.

- Map recovery tiers, critical state, dependencies, owners, RPO/RTO, retention, encryption, and key-recovery assumptions.
- Verify backup freshness and integrity, then restore approved artifacts into an isolated clean environment.
- Reconcile recovered data and application behavior, exercise representative disaster scenarios, and measure recovery objectives.
- Improve automation, monitoring, and runbooks; never claim readiness from backup-job success alone or run destructive production drills without authority.

## 29. Product Analytics / Experimentation Integrity

**Use for:** Product events, funnels, metrics, dashboards, or controlled experiments must become trustworthy enough to support decisions without misleading attribution.

- Map each product decision to versioned metric definitions, event contracts, identity rules, consent, and source-to-report lineage.
- Trace representative events end to end and reconcile loss, duplication, lateness, ordering, joins, and dashboard calculations.
- Validate experiment randomization, assignment persistence, exposure, sample ratios, guardrails, and analysis windows.
- Finish only when the measurement path is reproducible and qualified owners can interpret results without unsupported causal claims.

## 30. Codebase Onboarding / Knowledge Recovery

**Use for:** A mature, inherited, or poorly documented codebase must become understandable, runnable, and safe to change before major delivery work begins.

- Inventory authoritative sources, runtime entry points, architecture boundaries, critical journeys, dependencies, ownership, and supported environments.
- Trace representative user, API, data, and operational flows through code and runtime evidence; verify setup, run, reset, debug, and check commands from clean state.
- Create or update a reviewed Project Harness, architecture map, vocabulary, risk register, and freshness triggers instead of copying stale descriptions.
- Finish when a fresh maintainer can reproduce the critical paths and make safe change decisions without relying on chat history.

## 31. Search / SEO / Web Discoverability

**Use for:** A public website or web application must improve its technical search readiness, rendered metadata, structured data, crawl paths, internal links, and discoverable content quality.

- Build an approved public-route and search-intent matrix, then crawl rendered pages rather than judging source templates alone.
- Verify status codes, redirects, canonical URLs, robots, sitemaps, metadata, structured data, internal links, locale signals, performance, accessibility, and content discoverability together.
- Fix root causes and rerun the same crawler, rendered-HTML, schema, link, and page-quality gates across representative routes.
- Finish at evidence-backed technical readiness; never claim or promise search ranking from repository checks alone.
## Boundary checks for profiles 25–31

Choose these profiles only when their distinctive verifier controls the loop: repeated AI evals, staged legacy retirement, per-locale evidence, clean-room restore drills, trustworthy product/experiment measurement, verified maintainer readiness, or rendered crawl-and-discovery evidence. When the concern is secondary, keep the existing primary profile and add the appropriate assurance overlay.

## Custom Contract-Driven

**Use for:** A measurable engineering outcome whose dominant loop does not fit a preset.

The contract must define:

- One bounded unit of iteration
- One primary verifier or stable evaluation rubric
- A keep-or-revert decision
- Review and regression obligations
- Objective success, blocker, approval, budget, goal-drift, and stall exits

A custom profile is a safe fallback, not permission for vague work. If the same custom pattern recurs across several goals or projects, propose a new profile with field evidence.

## Combining profiles and overlays

Use one primary profile. A secondary profile may contribute one narrow technique when that improves evidence without changing the outcome.

Use assurance overlays for additional proof obligations. Do not combine profiles merely to appear comprehensive. If two profiles imply materially different outcomes, return to `shape-goal` and split or clarify the contract.
