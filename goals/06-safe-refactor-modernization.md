# Safe Refactor / Modernization

**Use when:** Architecture, dependencies, or internals should change while existing contracts remain stable.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Safe Refactor / Modernization profile. Work through incremental seams, compare against the captured baseline, retain rollback, and continue until the target structure is reached with behavioral-equivalence evidence and all gates passing. Stop only for a contract-defined decision, blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Refactor or modernize [SCOPE] to [TARGET DESIGN] while preserving [BEHAVIOR AND CONTRACTS]. Orient from the actual repository and reconcile instructions, architecture, specifications, tests, CI, progress state, prior goal archives, and Git history; protect uncommitted and unrelated work. Map consumers, public APIs, data formats, configuration, deployment assumptions, and hidden compatibility constraints. Capture a passing baseline and add characterization coverage for critical behavior that lacks protection. Define incremental seams and a fallback or rollback path, then make one coherent structural change at a time without unrelated feature expansion. After every change, run the same repository-native parity checks; at checkpoints run all affected broader gates, compare behavior and performance, and review the diff. Keep public and external contracts stable unless explicitly authorized, revert changes that worsen the verified state, independently review high-impact changes, and update existing progress or handoff artifacts. Finish only when the target structure is reached and before/after evidence proves equivalence except for explicitly named changes, all required gates pass, and any required rollback path is verified. Stop for an external decision, approval boundary, [BUDGET], or two no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. No irreversible or external-system action without explicit approval.
```

**Why it works:** Behavioral equivalence, incremental seams, rollback, and an archived parity record keep modernization falsifiable and reusable.
