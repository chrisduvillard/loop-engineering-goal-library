# Goal Engine: Assurance Overlays

Execution profiles define the **shape of the loop**. Assurance overlays define **additional proof and review obligations** that cut across many kinds of work.

Select zero or more overlays in the Goal Contract. Most goals need no more than three. If many overlays are mandatory, the goal may be too broad and should be split.

Overlays are additive. They may strengthen evidence, review, or authority boundaries, but may not weaken the Goal Contract or primary profile.

## Security & Privacy

**Apply when:** Authentication, authorization, secrets, sensitive data, dependency risk, trust boundaries, or abuse cases are affected.

Add evidence for:

- Threat boundaries and negative or abuse-path tests
- Authentication and authorization behavior
- Secret handling and data minimization
- Dependency or configuration exposure as applicable
- Independent review for high-impact paths
- Explicit approval before handling production secrets, private data, or exploit-enabling evidence

## Reliability & Recovery

**Apply when:** Availability, retries, concurrency, idempotency, fault handling, recovery, or operational continuity matters.

Add evidence for:

- Failure modes, timeouts, retries, backoff, and idempotency
- Partial failure and interruption scenarios
- Recovery, rollback, restart, or failover behavior
- Health signals and bounded degraded behavior
- No silent data loss or duplicate side effects

## Performance & Cost

**Apply when:** Latency, throughput, memory, CPU, storage, model usage, external API usage, or infrastructure cost is part of success.

Add evidence for:

- A fixed representative workload and recorded baseline
- The same benchmark conditions before and after
- Target percentile or resource/cost budget
- Champion/challenger keep-or-revert decisions
- No correctness or reliability regression in exchange for speed or cost

## UX & Accessibility

**Apply when:** Human-facing workflows, visual design, interaction, accessibility, or user comprehension is affected.

Add evidence for:

- Realistic end-to-end user journeys
- Supported viewport, input, keyboard, and assistive-technology behavior
- Clear empty, loading, error, and recovery states
- Screenshots or observable artifacts where useful
- A stable rubric and human review for subjective claims

## Data Integrity & Governance

**Apply when:** Stored or derived data, lineage, time semantics, retention, missingness, identity, or domain invariants matter.

Add evidence for:

- Data invariants, lineage, units, timestamps, and identity semantics
- Missing, duplicate, late, partial, and malformed inputs
- Reconciliation, counts, checksums, or domain-level comparisons
- Retention, minimization, and lawful-access boundaries where applicable
- No unexplained loss, corruption, or semantic drift

## Compatibility & Portability

**Apply when:** Public APIs, schemas, configuration, platforms, runtimes, clients, integrations, or old/new versions must coexist.

Add evidence for:

- Supported environment and version matrix
- Backward, forward, or mixed-version behavior as required
- Public API, data format, and configuration compatibility
- Deprecation and migration paths
- A retained rollback or fallback where the contract requires one

## Operability & Observability

**Apply when:** Operators must diagnose, monitor, support, or recover the changed system.

Add evidence for:

- Useful logs, metrics, traces, health checks, and failure signals
- Actionable diagnostics rather than noisy output
- Runbook or recovery instructions for new operational behavior
- Alert or dashboard behavior when in scope
- Sensitive-data redaction in telemetry and evidence

## Documentation & Knowledge Transfer

**Apply when:** Users, operators, maintainers, integrators, or future agents need durable guidance.

Add evidence for:

- User, operator, API, architecture, or migration documentation as applicable
- Examples that match the verified behavior
- Changelog or decision record when required
- Removal or correction of stale contradictory guidance
- Links to canonical sources instead of duplicated instructions

## Compliance & Auditability

**Apply when:** A policy, control framework, approval trail, regulated workflow, or auditable evidence set is part of the contract.

Add evidence for:

- Requirement-to-control and control-to-evidence mapping
- Required approvals and segregation of duties
- Reproducible timestamps, versions, and artifact references
- Retention and access rules for evidence
- Explicit human review for legal, regulatory, or policy conclusions; the agent must not self-certify compliance

## Project-specific overlay

When none of the overlays captures a recurring project concern, define a concise project-specific overlay in the Goal Contract with:

- Trigger conditions
- Additional acceptance evidence
- Additional review requirements
- Additional authority boundaries

If the same overlay is reused across several goals, promote it to a repository-owned document or project skill. Do not add a global library overlay from one speculative use case.
