# Specialist `/goal` Extensions

> [!NOTE]
> Generated from the canonical files under [`goals/`](goals/). Edit those files, then run `python3 scripts/sync_goal_docs.py --write`.

Four optional profiles for incidents, ecosystem upgrades, data migrations, and divergent branches. The core library remains the default.

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
