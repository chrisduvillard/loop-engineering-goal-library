# Best Universal Brownfield `/goal`

Use this when you want the library to determine and complete the next appropriate existing-project outcome without filling any placeholders.

## Run unchanged — zero-friction

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Brownfield Continue / Finish objective. During shaping, load shape-goal's required-input specification for Brownfield Continue / Finish; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to reconstruct the real current state, select the highest-priority dependency-safe unblocked gap, and complete the approved outcome end to end rather than stopping at plans or partial artifacts; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Strict two-step mode

Use this when an approved `GOAL.md` already exists:

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use its selected execution profile, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

The zero-friction command lets `shape-goal` resolve the project-specific contract first. The strict command skips shaping only because the contract is already approved.
