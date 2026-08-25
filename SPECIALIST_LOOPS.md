# Specialist `/goal` Extensions

> [!NOTE]
> Generated from the canonical files under [`goals/`](goals/). Edit those files, then run `python3 scripts/sync_goal_docs.py --write`.

Six optional profiles for incidents, ecosystem upgrades, data migrations, divergent branches, measured optimization, and technical feasibility. The core library remains the default.

---

## [Incident Recovery / Stabilization](goals/08-incident-recovery.md)

**Use when:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding the damage.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Incident Recovery / Stabilization profile. Preserve evidence; separate containment, restoration, root cause, and prevention; and continue until recovery gates pass, the failure is no longer reproducible under defined conditions, and rollback/recovery is verified. Stop for unresolved safety uncertainty or a contract-defined blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

**Why it works:** It prevents emergency work from becoming speculative cleanup and retains the incident timeline, proof, and prevention assets for the next response.

**Standalone fallback:** [Open the complete profile](goals/08-incident-recovery.md).

---

## [Dependency / Framework Upgrade](goals/09-dependency-framework-upgrade.md)

**Use when:** A dependency, framework, language runtime, or toolchain must be upgraded without breaking supported behavior.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Dependency / Framework Upgrade profile. Follow official version-path guidance, upgrade through the smallest safe boundaries, inspect transitive changes, preserve rollback, and continue until the target version runs in every supported environment and compatibility gates pass. Stop only for a contract-defined decision, blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

**Why it works:** It treats the whole compatibility surface as the unit of success and saves the version path, lockfile evidence, and migration lessons for later upgrades.

**Standalone fallback:** [Open the complete profile](goals/09-dependency-framework-upgrade.md).

---

## [Data Migration / Integrity](goals/10-data-migration-integrity.md)

**Use when:** Stored data or schemas must change while preserving correctness, compatibility, recoverability, and auditability.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Data Migration / Integrity profile. Define reconciliation, idempotency, restartability, mixed-version compatibility, and rollback before any destructive boundary, then continue through reversible phases until migration and reconciliation gates pass with no unexplained loss, duplication, or corruption. Stop for a contract-defined blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

**Why it works:** Data integrity and recoverability become explicit acceptance evidence, and the archived reconciliation plan makes future migrations safer.

**Standalone fallback:** [Open the complete profile](goals/10-data-migration-integrity.md).

---

## [Branch Rescue / Integration](goals/11-branch-rescue-integration.md)

**Use when:** Valuable work is stranded in a stale, divergent, oversized, or partially conflicting branch and must be recovered safely.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Branch Rescue / Integration profile. Account for every source slice, port only dependency-complete behavior that remains valid, protect newer target work, and continue until selected behavior passes broader gates and the target contains no unexplained changes. Stop for irreconcilable intent or a contract-defined blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

**Why it works:** It treats a branch as behavioral slices, preserves a path matrix, and records reusable integration decisions rather than hiding them in a one-off merge.

**Standalone fallback:** [Open the complete profile](goals/11-branch-rescue-integration.md).

---

## [Measured Optimization / Benchmark](goals/12-measured-optimization-benchmark.md)

**Use when:** A measurable property such as latency, throughput, cost, memory, build time, model quality, ranking accuracy, or another stable metric must improve without regressing required behavior.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Measured Optimization / Benchmark profile. Freeze the benchmark protocol and verified baseline, test one coherent challenger at a time, keep only meaningful improvements produced under the same conditions without violating must-pass gates, and continue until the target is reached or the contract-defined experiment budget or stagnation exit applies; preserve a reusable closeout packet.
```

**Why it works:** It uses a fixed champion-versus-challenger loop, so every retained change has comparable evidence and every rejected idea becomes reusable optimization knowledge rather than repeated guesswork.

**Standalone fallback:** [Open the complete profile](goals/12-measured-optimization-benchmark.md).

---

## [Technical Spike / Feasibility](goals/13-technical-spike-feasibility.md)

**Use when:** A bounded technical unknown must be answered before committing to a production implementation, architecture, vendor, migration, or other costly or risky direction.

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Technical Spike / Feasibility profile. Keep the investigation isolated, define the decision questions and Go / Conditional Go / No-Go criteria before experimenting, test the smallest representative prototype under realistic constraints, and continue until every question has an evidence-backed answer and a follow-on recommendation; preserve a reusable closeout packet and do not silently turn the spike into production implementation.
```

**Why it works:** It treats knowledge and a decision—not prototype volume—as the deliverable, keeps exploratory code from leaking into production, and saves the evidence needed to shape the next goal confidently.

**Standalone fallback:** [Open the complete profile](goals/13-technical-spike-feasibility.md).
