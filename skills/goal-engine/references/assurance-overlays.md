# Goal Engine: Assurance Overlays

Execution profiles define the **shape of the loop**. Assurance overlays define **additional proof, review, and authority obligations** that cut across many kinds of work.

Select zero or more overlays in the Goal Contract. Most goals need no more than three. If many overlays are mandatory, the goal may be too broad and should be split.

Overlays are additive. They may strengthen evidence but may not weaken the Goal Contract or primary profile.

## Dedicated profile or overlay?

Use the dedicated profile when the concern is the primary outcome. Use the overlay when it is secondary.

| Primary outcome | Dedicated profile | Use overlay when secondary |
|---|---|---|
| Interface usability and visual quality | Frontend UI / UX / Accessibility | UX & Accessibility |
| Documentation correctness | Documentation Synchronization / Knowledge Transfer | Documentation & Knowledge Transfer |
| Security or privacy hardening | Security / Privacy Hardening | Security & Privacy |
| Failure tolerance and recovery | Reliability / Resilience Hardening | Reliability & Recovery |
| API or integration compatibility | API / Integration Contract Compatibility | Compatibility & Portability |
| Operational visibility and supportability | Observability / Operability | Operability & Observability |
| Developer setup and tooling | Developer Experience / Tooling | Documentation, compatibility, or performance overlays |
| Dataset or pipeline quality | Data Quality / Pipeline Assurance | Data Integrity & Governance |
| Automated test and CI trust | Test Suite / CI Health | Reliability, documentation, or performance overlays |
| Infrastructure and deployment readiness | Infrastructure / Deployment Readiness | Reliability, operability, security, or compatibility overlays |
| Technical audit evidence | Compliance / Audit Readiness | Compliance & Auditability |
| AI behavior and evaluation quality | AI / LLM Evaluation & Improvement | AI Quality & Safety |
| Language and locale support | Internationalization / Localization Readiness | Internationalization & Localization |
| Public web discovery | Search / SEO / Web Discoverability | Search & Discoverability |

## Security & Privacy

**Apply when:** Authentication, authorization, secrets, sensitive data, dependency risk, trust boundaries, or abuse cases are affected but security is not the sole outcome.

Add evidence for:

- Threat boundaries and negative or abuse-path tests
- Authentication and authorization behavior
- Secret handling and data minimization
- Dependency or configuration exposure
- Independent review for high-impact paths
- Explicit approval before production secrets, private data, or exploit-enabling evidence

## Reliability & Recovery

**Apply when:** Availability, retries, concurrency, idempotency, fault handling, recovery, or continuity matters.

Add evidence for:

- Failure modes, timeouts, retries, backoff, and idempotency
- Partial failure and interruption scenarios
- Recovery, rollback, restart, or failover
- Health signals and bounded degraded behavior
- No silent data loss or duplicate side effects

## Performance & Cost

**Apply when:** Latency, throughput, memory, CPU, storage, model usage, external API usage, or infrastructure cost is part of success.

Add evidence for:

- Fixed representative workload and recorded baseline
- Same benchmark conditions before and after
- Target percentile or resource/cost budget
- Champion/challenger keep-or-revert decisions
- No correctness or reliability regression for speed or cost

## UX & Accessibility

**Apply when:** Human-facing workflows, visual design, interaction, accessibility, or comprehension is affected but not the primary goal.

Add evidence for:

- Realistic end-to-end journeys
- Supported viewport, input, keyboard, and assistive-technology behavior
- Empty, loading, error, success, and recovery states
- Screenshots or observable visual artifacts
- Stable rubric and human review for subjective claims

## Data Integrity & Governance

**Apply when:** Stored or derived data, lineage, time semantics, retention, missingness, identity, or domain invariants matter.

Add evidence for:

- Data invariants, lineage, units, timestamps, and identity semantics
- Missing, duplicate, late, partial, and malformed inputs
- Reconciliation, counts, checksums, or domain comparisons
- Retention, minimization, and lawful-access boundaries
- No unexplained loss, corruption, or semantic drift

## Compatibility & Portability

**Apply when:** Public APIs, schemas, configuration, platforms, runtimes, clients, integrations, or old/new versions must coexist.

Add evidence for:

- Supported environment and version matrix
- Backward, forward, or mixed-version behavior
- Public API, data format, and configuration compatibility
- Deprecation and migration paths
- Retained rollback or fallback

## Operability & Observability

**Apply when:** Operators must diagnose, monitor, support, or recover the changed system.

Add evidence for:

- Useful logs, metrics, traces, health checks, and failure signals
- Actionable diagnostics rather than noisy output
- Runbook or recovery instructions
- Alert or dashboard behavior
- Sensitive-data redaction in telemetry

## Documentation & Knowledge Transfer

**Apply when:** Users, operators, maintainers, integrators, or future agents need durable guidance.

Add evidence for:

- User, operator, API, architecture, or migration documentation
- Examples that match verified behavior
- Changelog or decision record
- Removal or correction of stale guidance
- Links to canonical sources instead of duplicated instructions

## Compliance & Auditability

**Apply when:** A policy, control framework, approval trail, regulated workflow, or auditable evidence set is part of the contract.

Add evidence for:

- Requirement-to-control and control-to-evidence mapping
- Required approvals and segregation of duties
- Reproducible timestamps, versions, and artifact references
- Retention and access rules
- Qualified human review for legal, regulatory, or policy conclusions

The agent must never self-certify compliance.

## AI Quality & Safety

**Apply when:** Prompts, models, retrieval, agents, graders, or tool use are affected but AI evaluation is not the primary outcome.

Add evidence for:

- Versioned prompts, models, retrieval sources, tools, eval data, graders, and sampling settings
- Representative, adversarial, and production-like cases with leakage controls
- Repeated trials and stochastic-variation reporting
- Human or domain-expert calibration of model-based graders
- Grounding, refusal, privacy, tool-safety, latency, and cost gates

## Internationalization & Localization

**Apply when:** A change affects language, region, script, time zone, direction, or locale-sensitive data but localization is not the primary outcome.

Add evidence for:

- Supported locale and fallback matrix
- Pseudo-localization, text expansion, and missing-translation behavior
- Date, time-zone, number, currency, unit, plural, and collation behavior
- Encoding, input, keyboard, font, and right-to-left support
- Localized layout, routing, and accessibility checks

## Search & Discoverability

**Apply when:** A change affects public web pages, crawl paths, metadata, structured data, internal links, or discoverable content but search readiness is not the primary outcome.

Add evidence for:

- Public-route, canonical, redirect, robots, and sitemap behavior
- Rendered titles, descriptions, social metadata, headings, and structured data
- Internal links, broken links, duplicate-content rules, and locale signals
- Representative crawl, performance, accessibility, and rendered-page checks
- Honest separation between technical readiness and ranking claims

## Project-specific overlay

When none captures a recurring project concern, define a concise project-specific overlay with:

- Trigger conditions
- Additional acceptance evidence
- Additional review requirements
- Additional authority boundaries

If it recurs across several goals, promote it to a repository-owned document or project skill. Do not add a global overlay from one speculative use case.
