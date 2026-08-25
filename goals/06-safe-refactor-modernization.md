# Safe Refactor / Modernization

**Use when:** Architecture, dependencies, or internals should change while existing contracts remain stable.

```text
/goal Refactor or modernize [SCOPE] to [TARGET DESIGN] while preserving [BEHAVIOR AND CONTRACTS]. Orient from the actual repository and reconcile instructions, architecture, specifications, tests, CI, progress state, and Git history; protect uncommitted and unrelated work. Map consumers, public APIs, data formats, configuration, deployment assumptions, and hidden compatibility constraints. Capture a passing baseline and add characterization coverage for critical behavior that lacks protection. Define incremental seams and a fallback or rollback path, then make one coherent structural change at a time without unrelated feature expansion. After every change, run the same repository-native parity checks; at checkpoints run all affected broader gates, compare behavior and performance, and review the diff. Keep public and external contracts stable unless explicitly authorized, revert changes that worsen the verified state, independently review high-impact changes, and update existing progress or handoff artifacts. Finish only when the target structure is reached and before/after evidence proves equivalence except for explicitly named changes, all required gates pass, and any required rollback path is verified. Stop for an external decision, approval boundary, [BUDGET], or two no-progress cycles. No irreversible or external-system action without explicit approval.
```

**Why it works:** It makes behavioral equivalence a first-class result instead of assuming passing compilation proves safety. Incremental seams and fallback preservation prevent an all-or-nothing rewrite.
