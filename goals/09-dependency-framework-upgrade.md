# Dependency / Framework Upgrade

**Use when:** A dependency, framework, language runtime, or toolchain must be upgraded without breaking supported behavior.

```text
/goal Upgrade [DEPENDENCY OR FRAMEWORK] from [CURRENT VERSION] to [TARGET VERSION] across [SCOPE] while preserving [SUPPORTED CONTRACTS]. Establish the actual dependency graph, lockfiles, runtime/toolchain constraints, consumers, generated artifacts, native build/test/release gates, and Git state; reconcile documentation with code and protect unrelated work. Capture the baseline, consult the official migration, release, and security guidance for the exact version path, identify breaking and transitive changes, and choose the smallest safe staged route; avoid unrelated modernization. Upgrade one coherent version boundary at a time, adapt required production code and configuration, regenerate only necessary artifacts, run repository-native targeted and full compatibility checks, inspect lockfile and transitive changes, add regression coverage, and retain a rollback path. Do not disable checks, hide deprecations, or accept unexplained dependency churn merely to make the upgrade pass. Finish only when the target version runs in every supported environment, [COMPATIBILITY GATES] pass with surfaced evidence, and rollback remains viable. Stop for a required product decision, unsupported platform, approval/external blocker, [BUDGET], or two no-progress cycles; do not publish or deploy without explicit approval.
```

**Why it works:** Version upgrades fail at ecosystem boundaries, not only at compilation. The staged path, transitive-change review, compatibility matrix, and rollback requirement keep the upgrade narrow and falsifiable.
