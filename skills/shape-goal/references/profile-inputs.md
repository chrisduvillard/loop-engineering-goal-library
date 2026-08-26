# Shape Goal: Profile Input Specifications

Use this reference when a zero-friction launcher names a primary execution profile. These are the profile-specific questions that must be resolved in addition to the common Goal Contract fields.

## Common inputs for every goal

Resolve and record:

- One observable outcome and why it is next
- In-scope and out-of-scope boundaries
- Acceptance evidence with exact commands, workflows, measurements, or artifacts where available
- Protected behavior, user work, compatibility, data, and performance characteristics
- Baseline and known exceptions
- Authority and irreversible-action boundaries
- Budget, blocker, approval, stall, and goal-drift exits
- Goal ID, revision, priority, dependencies, state, portfolio, archive, and history paths
- Primary profile, assurance overlays, and project-harness sources

Do not ask the user for facts that repository evidence or connected authoritative sources can answer. Ask only material owner decisions, one at a time, after the evidence search is exhausted.

## 1. Brownfield Continue / Finish

**Use for:** An existing repository has an approved direction, partial implementation, or unfinished milestone and should advance autonomously.

**Required profile inputs**

- Authoritative outcome or next approved milestone
- Priority and dependency order
- Acceptance evidence
- Protected existing behavior and user work

**Suggested overlays:** Select only if required by the contract.

**Execution emphasis**

- Reconcile current state, select the highest-priority dependency-safe gap, and finish the approved outcome rather than merely planning it.
- Select the highest-priority unblocked gap.
- Verify the gap before editing.
- Do not stop at planning, tests, or documentation while required production work remains.

## 2. PRD / Spec Compliance

**Use for:** A product, feature, or repository must be brought into full alignment with documented requirements.

**Required profile inputs**

- Authoritative PRD/specification and version
- In-scope requirements and exclusions
- Contradiction/decision owners
- Final acceptance and regression gates

**Suggested overlays:** Documentation & Knowledge Transfer

**Execution emphasis**

- Build a requirement-to-evidence map, reconcile contradictory requirements, and close every verified in-scope gap.
- Maintain requirement-to-evidence status.
- Never weaken a requirement or verifier.
- Escalate only genuine product contradictions.

## 3. Next Milestone

**Use for:** A roadmap is larger than one run and the next coherent, dependency-safe increment should be completed end to end.

**Required profile inputs**

- Roadmap and current milestone state
- Dependency-safe next milestone
- Milestone acceptance evidence
- Explicit out-of-scope backlog

**Suggested overlays:** Select only if required by the contract.

**Execution emphasis**

- Choose one coherent next milestone, define its evidence, and complete it without unrelated scope expansion.
- Finish one milestone, not the roadmap.
- Avoid opportunistic modernization.
- Deliver production behavior end to end.

## 4. Deep Audit + Remediation

**Use for:** The codebase needs evidence-based discovery and repair of important defects or risks.

**Required profile inputs**

- Audit scope and rubric
- Severity/action threshold
- Verification methods
- Final saturation and regression gates

**Suggested overlays:** Select only if required by the contract.

**Execution emphasis**

- Audit against an explicit rubric and severity bar, verify findings, remediate root causes, and repeat to evidence saturation.
- Treat scanner/reviewer output as hypotheses.
- Rank by severity, confidence, and blast radius.
- Fix verified root causes and add regression coverage.

## 5. QA / Regression / UAT

**Use for:** The actual product surface and realistic user workflows must pass defined acceptance gates.

**Required profile inputs**

- Supported environments and product entry points
- Required user/API/data flows
- Test data, credentials, and lawful access
- Clean-state acceptance and broader gates

**Suggested overlays:** UX & Accessibility

**Execution emphasis**

- Discover the real product surface, build a risk-based flow matrix, reproduce failures, fix root causes, and rerun clean end-to-end evidence.
- Test realistic workflows, not only units.
- Verify failures before fixing.
- Rerun exact failures and affected broader gates.

## 6. Safe Refactor / Modernization

**Use for:** Architecture, dependencies, or internals should change while external behavior and contracts remain stable.

**Required profile inputs**

- Target structure/design
- Public and hidden compatibility contracts
- Characterization baseline
- Rollback/fallback path and parity gates

**Suggested overlays:** Compatibility & Portability

**Execution emphasis**

- Capture behavioral baselines, create safe seams, change incrementally, and prove equivalence with rollback.
- Map consumers and contracts.
- Change one coherent seam at a time.
- Keep rollback until equivalence is proven.

## 7. Release Readiness

**Use for:** A version or milestone must satisfy all release gates without actually being published or deployed.

**Required profile inputs**

- Version or release scope
- Repository-defined release gates
- Release-blocking severity policy
- Production-like checks and rollback evidence

**Suggested overlays:** Reliability & Recovery, Documentation & Knowledge Transfer

**Execution emphasis**

- Turn repository-defined release criteria into evidence, resolve blockers by risk, and verify artifacts, migrations, operations, and rollback together.
- Prepare but do not release.
- Work highest-risk blockers first.
- Verify artifacts, configuration, migrations, docs, and rollback together.

## 8. Incident Recovery / Stabilization

**Use for:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding damage.

**Required profile inputs**

- Incident/failure definition and blast radius
- Recovery target and health gates
- Allowed containment actions
- Evidence sources, rollback, and follow-up owner

**Suggested overlays:** Reliability & Recovery, Operability & Observability

**Execution emphasis**

- Separate containment, restoration, root-cause proof, and prevention while preserving incident evidence.
- Preserve evidence.
- Prefer reversible containment.
- Prove recovery and root cause separately.

## 9. Dependency / Framework Upgrade

**Use for:** A dependency, framework, language runtime, or toolchain must move to a target version without breaking supported behavior.

**Required profile inputs**

- Current and target versions
- Supported environments and consumers
- Official migration/security guidance
- Compatibility gates and rollback

**Suggested overlays:** Compatibility & Portability, Security & Privacy

**Execution emphasis**

- Map the dependency graph, follow official version-path guidance, stage changes, inspect transitive effects, and prove compatibility.
- Upgrade coherent boundaries.
- Inspect lockfiles and generated changes.
- Avoid unrelated modernization.

## 10. Data Migration / Integrity

**Use for:** Stored data, schemas, formats, or backfills must change while preserving correctness, compatibility, and recoverability.

**Required profile inputs**

- Source and target states
- Data invariants and reconciliation queries
- Volume, mixed-version, privacy, and retention constraints
- Idempotency, restart, backup, and rollback

**Suggested overlays:** Data Integrity & Governance, Reliability & Recovery

**Execution emphasis**

- Define invariants and reconciliation first, use expand/backfill/verify/switch/contract phases, and test retry and rollback.
- Define reconciliation before mutation.
- Test interruption/retry/rollback.
- Require approval before destructive cleanup.

## 11. Branch Rescue / Integration

**Use for:** Valuable work is stranded in a stale, divergent, oversized, or conflicting branch and must be recovered safely.

**Required profile inputs**

- Source branch/commits and target branch
- Source intent and relevant requirements
- Slice classification criteria
- Integration, review, and branch-operation authority

**Suggested overlays:** Compatibility & Portability

**Execution emphasis**

- Pin source and target state, classify source slices, port only dependency-complete valid behavior, and account for every decision.
- Protect recovery refs.
- Classify slices as present/obsolete/conflicting/worth porting.
- Never merge wholesale without evidence.

## 12. Measured Optimization / Benchmark

**Use for:** A stable metric must improve under a fixed protocol without regressing required behavior.

**Required profile inputs**

- Primary metric, unit, and current baseline
- Target and practical significance/tolerance
- Fixed workload/dataset/environment/sampling
- Must-pass floors, experiment budget, and rebaseline policy

**Suggested overlays:** Performance & Cost

**Execution emphasis**

- Freeze the benchmark protocol, compare champion and challengers under identical conditions, and retain only meaningful improvements.
- Freeze the protocol before changes.
- Change one hypothesis at a time.
- Keep only reproducible wins without floor regressions.

## 13. Technical Spike / Feasibility

**Use for:** A bounded technical unknown must be resolved before production commitment.

**Required profile inputs**

- Decision question and options
- Decision criteria and evidence
- Time/cost budget
- Isolation, cleanup, and decision owner

**Suggested overlays:** Documentation & Knowledge Transfer

**Execution emphasis**

- Frame one decision question, test the smallest isolated prototypes, compare options, and deliver evidence rather than production code.
- Keep spike code isolated and disposable.
- Do not let prototype become production silently.
- Finish with a decision and explicit conditions.

## 14. Frontend UI / UX / Accessibility

**Use for:** A frontend surface must become coherent, usable, responsive, accessible, and visually polished without regressing behavior.

**Required profile inputs**

- Target screens, journeys, and user groups
- Design references, brand rules, and design system
- Supported browsers, devices, viewports, themes, and input modes
- Visual, interaction, accessibility, content-state, and performance acceptance evidence

**Suggested overlays:** UX & Accessibility, Performance & Cost, Compatibility & Portability

**Execution emphasis**

- Inventory screens and states, reconcile design references and system patterns, test real interactions across supported viewports, and iterate on verified usability and visual gaps.
- Exercise real browser flows and all important states.
- Use screenshots/visual comparison plus functional checks.
- Verify keyboard, focus, semantics, contrast, responsive behavior, loading/error/empty states.

## 15. Documentation Synchronization / Knowledge Transfer

**Use for:** Documentation, examples, runbooks, diagrams, or onboarding material must accurately match current behavior and be usable by its audience.

**Required profile inputs**

- Audiences and documentation surfaces
- Authoritative code/runtime/spec sources
- Supported versions and environments
- Link/build/example checks and freshness policy

**Suggested overlays:** Documentation & Knowledge Transfer

**Execution emphasis**

- Map authoritative behavior to every affected document, execute examples and commands where possible, remove contradictions, and add drift prevention.
- Verify documentation claims against behavior.
- Run commands and examples rather than copying stale text.
- Link decisions to authoritative sources and prevent future drift.

## 16. Security / Privacy Hardening

**Use for:** Security and privacy are the primary outcome: attack surface, authorization, secrets, dependencies, or data handling must be hardened and verified.

**Required profile inputs**

- Assets, actors, trust boundaries, and threat model
- Scope, standards, severity bar, and accepted risk
- Safe testing and disclosure boundaries
- Security/privacy gates, regression tests, and approval owners

**Suggested overlays:** Security & Privacy, Compliance & Auditability

**Execution emphasis**

- Establish assets and trust boundaries, verify attack paths and findings, prioritize by severity and exploitability, remediate root causes, and retest.
- Never exploit or mutate external systems without approval.
- Treat scanner findings as hypotheses.
- Test authorization and data-boundary regressions.

## 17. Reliability / Resilience Hardening

**Use for:** A system must continue or recover correctly under defined failures, load, retries, restarts, and dependency degradation.

**Required profile inputs**

- Critical journeys, SLOs/SLIs, and recovery objectives
- Failure modes, load, and dependency assumptions
- Fault-injection and data-safety boundaries
- Recovery, idempotency, retry, degradation, and observability gates

**Suggested overlays:** Reliability & Recovery, Operability & Observability

**Execution emphasis**

- Define service objectives and failure scenarios, reproduce weaknesses, harden idempotency and recovery, and verify under controlled faults.
- Test failures and recovery, not only happy paths.
- Protect data during retries/restarts.
- Prefer graceful degradation and bounded retries.

## 18. API / Integration Contract Compatibility

**Use for:** APIs, events, schemas, SDKs, or external integrations must remain compatible across producers, consumers, and versions.

**Required profile inputs**

- Providers, consumers, schemas, events, and versions
- Compatibility window and deprecation policy
- Supported environment/version matrix
- Contract tests, schema diff, error/timeout semantics, and rollback

**Suggested overlays:** Compatibility & Portability, Reliability & Recovery

**Execution emphasis**

- Inventory providers and consumers, establish contract baselines, test version combinations, and stage changes with deprecation and rollback.
- Treat undocumented consumers as a risk to investigate.
- Verify positive and negative contract behavior.
- Stage additive changes before removals.

## 19. Observability / Operability

**Use for:** Operators and maintainers must be able to detect, understand, and recover from important failures using useful signals and runbooks.

**Required profile inputs**

- Critical journeys, failure modes, and ownership
- SLIs/SLOs and required logs/metrics/traces
- Alert thresholds, routing, and noise budget
- Health checks, dashboards, runbooks, drills, and evidence retention

**Suggested overlays:** Operability & Observability, Reliability & Recovery

**Execution emphasis**

- Map critical journeys to signals, improve logs/metrics/traces/health checks, tune alerts, create runbooks, and validate diagnosis and recovery.
- Instrument outcomes rather than noise.
- Avoid secrets/high-cardinality leaks.
- Test alerts and runbooks with controlled scenarios.

## 20. Developer Experience / Tooling

**Use for:** Local setup, build, test, debug, CI, or contribution workflows must become faster, clearer, and reproducible.

**Required profile inputs**

- Developer personas and supported platforms
- Clean setup/build/test/debug/contribution journeys
- Baseline time, failure, and complexity metrics
- Success evidence, compatibility, and migration/rollback

**Suggested overlays:** Documentation & Knowledge Transfer, Compatibility & Portability, Performance & Cost

**Execution emphasis**

- Measure developer workflows, remove verified friction, align local and CI behavior, and preserve a reusable project harness.
- Test from clean state.
- Prefer canonical scripts/task runners.
- Make failures actionable and keep local/CI parity.

## 21. Data Quality / Pipeline Assurance

**Use for:** A data pipeline or dataset must satisfy defined freshness, completeness, validity, consistency, lineage, and reconciliation expectations.

**Required profile inputs**

- Datasets, sources, sinks, owners, and lineage
- Freshness/completeness/validity/consistency invariants
- Representative windows and known exceptions
- Reconciliation, anomaly thresholds, monitoring, backfill, and incident gates

**Suggested overlays:** Data Integrity & Governance, Operability & Observability

**Execution emphasis**

- Map sources and transformations, establish measurable data contracts, reproduce quality failures, fix root causes, and add monitoring and reconciliation.
- Verify quality at boundaries and end-to-end.
- Distinguish source defects from transformation defects.
- Add durable checks and lineage evidence.

## 22. Compliance / Audit Readiness

**Use for:** A repository or system must produce implementation evidence for an approved control set without falsely self-certifying legal or regulatory compliance.

**Required profile inputs**

- Approved framework/control set and scope
- Control owners and qualified approvers
- Required evidence, retention, and access rules
- Technical remediation gates and explicit non-technical/legal decisions

**Suggested overlays:** Compliance & Auditability, Security & Privacy, Documentation & Knowledge Transfer

**Execution emphasis**

- Identify the authoritative control framework, map each control to code/config/process/evidence, verify gaps, remediate technical findings, and prepare reviewer-ready evidence.
- Do not invent policy or self-certify.
- Separate technical evidence from legal interpretation.
- Preserve chain of evidence and approval boundaries.

## 23. Test Suite / CI Health

**Use for:** Automated tests and CI must become trustworthy, deterministic, appropriately fast, and consistent with local development.

**Required profile inputs**

- Test and CI topology, owners, supported environments, and required gates
- Flake rate, failure classes, skipped or quarantined coverage, runtime, and feedback targets
- Reproduction protocol, fixtures, caches, services, retries, parallelism, and isolation boundaries
- Local/CI parity, diagnostic quality, completion evidence, and forbidden verifier weakening

**Suggested overlays:** Reliability & Recovery, Documentation & Knowledge Transfer, Performance & Cost

**Execution emphasis**

- Treat the test pipeline as an evidence system, not merely a command that should turn green.
- Reproduce and classify flaky, misleading, slow, skipped, or environment-dependent checks.
- Fix root causes, preserve required coverage, and prove clean local/CI parity repeatedly.

## 24. Infrastructure / Deployment Readiness

**Use for:** Infrastructure, environment configuration, deployment automation, smoke checks, and rollback must be proven ready without silently changing production.

**Required profile inputs**

- Target environments, infrastructure scope, ownership, dependencies, and parity expectations
- Infrastructure-as-code, configuration, secret-reference, artifact, migration, and pipeline sources of truth
- Provisioning validation, smoke/health checks, observability, failure scenarios, and rollback evidence
- Production authority, maintenance/change windows, residual-risk policy, and readiness criteria

**Suggested overlays:** Reliability & Recovery, Operability & Observability, Security & Privacy, Compatibility & Portability

**Execution emphasis**

- Reconcile infrastructure and application assumptions as one deployment surface.
- Validate through approved non-production, ephemeral, dry-run, or simulated environments.
- Prove artifacts, configuration, migrations, health signals, failure handling, and rollback without silently exercising production authority.

## Custom Contract-Driven

Use only when none of the presets matches the dominant loop. Resolve:

- A bounded unit of iteration
- A stable primary verifier or evaluation rubric
- A keep-or-revert rule
- Review and regression obligations
- Objective success, blocker, approval, budget, and stall exits

One unusual goal is not evidence for a new global preset. Promote a recurring custom pattern only after repeated field use proves a distinct loop and verifier.
