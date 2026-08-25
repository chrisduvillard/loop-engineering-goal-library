# Specialist `/goal` Extensions

These four profiles are worth keeping because incidents, ecosystem upgrades, data changes, and divergent branches have distinct failure modes that a generic loop can easily miss.

## Recommended: skills + native goal

After `shape-goal` has approved the target and selected one of these specialist profiles, run:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

The commands below are **standalone fallbacks** for environments where `goal-engine` is not installed.

---

## Incident Recovery / Stabilization

**Use when:** A severe regression or production-like incident must be contained, diagnosed, and recovered without compounding the damage.

```text
/goal Stabilize and recover [SYSTEM OR SCOPE] from [INCIDENT OR FAILURE] to [RECOVERY TARGET]. First preserve evidence and establish the actual state from incident reports, logs, metrics, traces, recent deploys/config/data changes, repository instructions/runbooks, native tests/CI, and Git status/history; protect unrelated work and do not alter production or external systems without explicit approval. Separate containment, restoration, root cause, and prevention. Reproduce or otherwise verify the failure, map its blast radius, and identify the safest reversible mitigation. Then iterate: test one evidence-backed hypothesis, make the smallest reversible change, run repository-native targeted checks and realistic recovery scenarios, compare health with the pre-incident baseline, and keep only proven improvements. Add regression and observability coverage, independently review high-risk fixes, and record the timeline, evidence, decisions, and residual risk. Finish only when [RECOVERY GATES] pass, the failure is no longer reproducible under the defined conditions, and rollback/recovery is verified. Stop for an approval or external blocker, unresolved safety uncertainty, [BUDGET], or two no-progress cycles; leave an actionable incident handoff.
```

**Why it works:** It prevents the common mistake of mixing emergency containment with speculative cleanup. Recovery, root cause, and prevention each require their own evidence before the incident can be considered closed.

---

## Dependency / Framework Upgrade

**Use when:** A dependency, framework, language runtime, or toolchain must be upgraded without breaking supported behavior.

```text
/goal Upgrade [DEPENDENCY OR FRAMEWORK] from [CURRENT VERSION] to [TARGET VERSION] across [SCOPE] while preserving [SUPPORTED CONTRACTS]. Establish the actual dependency graph, lockfiles, runtime/toolchain constraints, consumers, generated artifacts, native build/test/release gates, and Git state; reconcile documentation with code and protect unrelated work. Capture the baseline, consult the official migration, release, and security guidance for the exact version path, identify breaking and transitive changes, and choose the smallest safe staged route; avoid unrelated modernization. Upgrade one coherent version boundary at a time, adapt required production code and configuration, regenerate only necessary artifacts, run repository-native targeted and full compatibility checks, inspect lockfile and transitive changes, add regression coverage, and retain a rollback path. Do not disable checks, hide deprecations, or accept unexplained dependency churn merely to make the upgrade pass. Finish only when the target version runs in every supported environment, [COMPATIBILITY GATES] pass with surfaced evidence, and rollback remains viable. Stop for a required product decision, unsupported platform, approval/external blocker, [BUDGET], or two no-progress cycles; do not publish or deploy without explicit approval.
```

**Why it works:** Version upgrades fail at ecosystem boundaries, not only at compilation. The staged path, transitive-change review, compatibility matrix, and rollback requirement keep the upgrade narrow and falsifiable.

---

## Data Migration / Integrity

**Use when:** Stored data or schemas must change while preserving correctness, compatibility, recoverability, and auditability.

```text
/goal Migrate [DATA OR SCHEMA] from [SOURCE STATE] to [TARGET STATE] under [INTEGRITY AND COMPATIBILITY REQUIREMENTS]. First map the authoritative schema, readers and writers, invariants, volumes, retention/privacy constraints, migration history, backup/restore path, repository-native checks, and actual Git/database state; preserve evidence and existing data. Define pre/post reconciliation queries, dry-run behavior, idempotency, restartability, mixed-version compatibility, and rollback before any destructive step. Implement in reversible phases—expand, backfill, verify, switch, then contract where applicable. Test on representative data; compare counts, checksums, relationships, and domain invariants; exercise interruption, retry, rollback, and old/new application combinations; add regression and migration coverage; and independently review high-risk steps. Never mutate production, delete data, or cross an irreversible boundary without explicit approval. Finish only when [MIGRATION GATES] and reconciliation checks pass with surfaced evidence, rollback/recovery is verified, and no unexplained loss, duplication, or corruption remains. Stop for missing access, unclear data ownership, approval/external blocker, [BUDGET], or two no-progress cycles; record the exact resume state.
```

**Why it works:** It treats data correctness and recoverability as the product, not as secondary implementation details. Reconciliation, mixed-version testing, interruption recovery, and explicit irreversible boundaries prevent a technically successful but operationally unsafe migration.

---

## Branch Rescue / Integration

**Use when:** Valuable work is stranded in a stale, divergent, oversized, or partially conflicting branch and must be recovered safely.

```text
/goal Safely recover and integrate the valuable work from [SOURCE BRANCH OR COMMITS] into [TARGET BRANCH] while preserving newer target behavior and unrelated work. Establish the actual refs/SHAs, clean or dirty state, divergence, target baseline, relevant requirements/issues/PRs/tests, and source intent from Git history; create a recovery point before changes. Inventory source changes by coherent behavior and classify each slice as already present, obsolete, conflicting, unsafe, or worth porting; verify every classification against current code and executable evidence. Port the smallest dependency-complete slices using the least risky method, resolving conflicts by current contracts and tests rather than taking either side wholesale. After each slice, run repository-native targeted checks, add regression coverage where needed, review the diff, and keep only changes that preserve or improve the target baseline. Never overwrite newer target work or import unrelated source history. Finish only when every source slice is accounted for, all selected behavior passes affected broader gates with surfaced evidence, and the target contains no unexplained changes. Stop for an owner decision on irreconcilable intent, approval/external blocker, [BUDGET], or two no-progress cycles; leave a path matrix and restartable handoff. Do not merge, push, delete, or rewrite branches without explicit approval.
```

**Why it works:** It treats a branch as a collection of behavioral slices rather than an all-or-nothing merge candidate. The accounting matrix preserves useful intent while protecting newer work and making every discarded or ported change explainable.
