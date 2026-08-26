# Goal Catalog

Interactive-first profiles. Start with `shape-goal`; each linked file also contains advanced autonomous preflight commands.

| ID | Goal | Category | In simple terms |
|---:|---|---|---|
| 01 | [Brownfield Continue / Finish](01-brownfield-continue-finish.md) | Core goals | Understand the real current state and keep completing the most important unblocked work. |
| 02 | [PRD / Spec Compliance](02-prd-spec-compliance.md) | Core goals | Compare the real product with its requirements and close every proven gap. |
| 03 | [Next Milestone](03-next-milestone.md) | Core goals | Deliver one useful next milestone without wandering into the whole backlog. |
| 04 | [Deep Audit + Remediation](04-deep-audit-remediation.md) | Core goals | Find important problems, prove they are real, fix root causes, and prevent recurrence. |
| 05 | [QA / Regression / UAT](05-qa-regression-uat.md) | Core goals | Exercise the real product until required workflows and regression gates pass. |
| 06 | [Safe Refactor / Modernization](06-safe-refactor-modernization.md) | Core goals | Improve internals while proving users and integrations still see the intended behavior. |
| 07 | [Release Readiness](07-release-readiness.md) | Core goals | Remove verified release blockers and stop at release-ready. |
| 08 | [Incident Recovery / Stabilization](08-incident-recovery.md) | Specialist goals | Contain damage, restore health, prove the cause, and add prevention. |
| 09 | [Dependency / Framework Upgrade](09-dependency-framework-upgrade.md) | Specialist goals | Upgrade through safe version steps while checking the full compatibility surface. |
| 10 | [Data Migration / Integrity](10-data-migration-integrity.md) | Specialist goals | Migrate data through reversible phases and prove no unexplained loss, duplication, or corruption. |
| 11 | [Branch Rescue / Integration](11-branch-rescue-integration.md) | Specialist goals | Recover useful behavioral slices without overwriting newer target work. |
| 12 | [Measured Optimization / Benchmark](12-measured-optimization-benchmark.md) | Specialist goals | Freeze a baseline, test one challenger at a time, and keep only reproducible wins. |
| 13 | [Technical Spike / Feasibility](13-technical-spike-feasibility.md) | Specialist goals | Run an isolated experiment and return a Go, Conditional Go, or No-Go decision. |
| 14 | [Frontend UI / UX / Accessibility](14-frontend-ui-ux-accessibility.md) | Product and quality goals | Improve the real interface through browser-based user journeys, visual evidence, and accessibility checks. |
| 15 | [Documentation Synchronization / Knowledge Transfer](15-documentation-synchronization.md) | Product and quality goals | Find documentation drift, verify examples and commands, and make the maintained knowledge trustworthy. |
| 16 | [Security / Privacy Hardening](16-security-privacy-hardening.md) | Product and quality goals | Threat-model the scoped system, prove actionable findings, remediate safely, and add lasting protection. |
| 17 | [Reliability / Resilience Hardening](17-reliability-resilience-hardening.md) | Product and quality goals | Model failure modes, inject safe faults, improve recovery, and prove reliability objectives. |
| 18 | [API / Integration Contract Compatibility](18-api-integration-contract-compatibility.md) | Product and quality goals | Map contracts and consumers, prove compatibility, and evolve interfaces without hidden breakage. |
| 19 | [Observability / Operability](19-observability-operability.md) | Product and quality goals | Make system health visible and actionable, then prove it with drills. |
| 20 | [Developer Experience / Tooling](20-developer-experience-tooling.md) | Product and quality goals | Make the common developer path work from clean state with clear commands and actionable failures. |
| 21 | [Data Quality / Pipeline Assurance](21-data-quality-pipeline-assurance.md) | Product and quality goals | Define data invariants, test the real pipeline, correct root causes, and make quality continuously observable. |
| 22 | [Compliance / Audit Readiness](22-compliance-audit-readiness.md) | Product and quality goals | Map controls to implementation and evidence, close technical gaps, and leave an auditable package for qualified human review. |
| 23 | [Test Suite / CI Health](23-test-suite-ci-health.md) | Product and quality goals | Find flaky, misleading, slow, skipped, or environment-dependent checks and turn the test pipeline into reliable evidence. |
| 24 | [Infrastructure / Deployment Readiness](24-infrastructure-deployment-readiness.md) | Product and quality goals | Verify that the system can be provisioned and deployed consistently, diagnosed after rollout, and safely rolled back before a human authorizes production change. |
| 25 | [AI / LLM Evaluation & Improvement](25-ai-llm-evaluation-improvement.md) | Specialist goals | Build a trustworthy eval set, classify failures, test one change at a time, and keep only improvements that survive repeated runs. |
| 26 | [Deprecation / Legacy Sunset](26-deprecation-legacy-sunset.md) | Specialist goals | Find who still depends on the old path, provide a safe migration, prove adoption, then remove it in controlled stages. |
| 27 | [Internationalization / Localization Readiness](27-internationalization-localization-readiness.md) | Product and quality goals | Find hard-coded locale assumptions, build a locale matrix, test translated and right-to-left experiences, and prove every supported locale works. |
| 28 | [Backup / Restore / Disaster Recovery](28-backup-restore-disaster-recovery.md) | Product and quality goals | Define what must survive, create trustworthy backups, restore them in a clean environment, and prove recovery meets the agreed targets. |
| 29 | [Product Analytics / Experimentation Integrity](29-product-analytics-experimentation-integrity.md) | Product and quality goals | Define the events and metrics, verify collection end to end, test experiment assignment, and prove the numbers mean what the team thinks they mean. |

The machine-readable source is [`catalog.json`](catalog.json).
