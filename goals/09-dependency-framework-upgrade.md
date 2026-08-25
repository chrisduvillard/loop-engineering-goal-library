# Dependency / Framework Upgrade

**Use when:** A dependency, framework, language runtime, or toolchain must be upgraded without breaking supported behavior.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Dependency / Framework Upgrade profile. Follow official version-path guidance, upgrade through the smallest safe boundaries, inspect transitive changes, preserve rollback, and continue until the target version runs in every supported environment and compatibility gates pass. Stop only for a contract-defined decision, blocker, approval boundary, budget, or two no-progress cycles; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Upgrade [DEPENDENCY OR FRAMEWORK] from [CURRENT VERSION] to [TARGET VERSION] across [SCOPE] while preserving [SUPPORTED CONTRACTS]. Establish the actual dependency graph, lockfiles, runtime/toolchain constraints, consumers, generated artifacts, native build/test/release gates, prior goal archives, and Git state; reconcile documentation with code and protect unrelated work. Capture the baseline, consult official migration, release, and security guidance for the exact version path, identify breaking and transitive changes, and choose the smallest safe staged route; avoid unrelated modernization. Upgrade one coherent version boundary at a time, adapt required production code and configuration, regenerate only necessary artifacts, run repository-native targeted and full compatibility checks, inspect lockfile and transitive changes, add regression coverage, and retain a rollback path. Do not disable checks, hide deprecations, or accept unexplained dependency churn merely to make the upgrade pass. Finish only when the target version runs in every supported environment, [COMPATIBILITY GATES] pass with surfaced evidence, and rollback remains viable. Stop for a required product decision, unsupported platform, approval/external blocker, [BUDGET], or two no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. Do not publish or deploy without explicit approval.
```

**Why it works:** It treats the whole compatibility surface as the unit of success and saves the version path, lockfile evidence, and migration lessons for later upgrades.
