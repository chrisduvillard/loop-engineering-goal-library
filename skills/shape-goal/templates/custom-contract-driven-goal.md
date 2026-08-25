# Custom Contract-Driven `/goal`

**Use when:** The target is measurable, but none of the thirteen execution presets matches the dominant control loop.

Do not use this as an escape hatch for a vague request. The approved Goal Contract must define:

- One bounded unit of iteration
- One primary verifier or stable evaluation rubric
- One keep-or-revert rule
- A review and regression strategy
- Objective success, blocker, approval, budget, and stall exits

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE] using its Custom Contract-Driven execution pattern, assurance overlays, and project harness. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. At checkpoints, detect material goal drift instead of silently expanding scope. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve reusable state and leave a restartable handoff.
```

## Standalone fallback

Use this when `goal-engine` is not installed:

```text
/goal Complete the approved Goal Contract in [PATH OR ISSUE] using the custom loop defined there. Before editing, establish the actual repository state from applicable instructions, requirements, architecture, plans, prior goals, native scripts/CI/tests, runtime behavior, and Git status/diff/history; reconcile contradictions and protect user, uncommitted, and unrelated work. Confirm the contract defines one bounded iteration unit, a primary verifier, a keep-or-revert rule, a review strategy, assurance obligations, and objective stop conditions; if any is materially unresolved, stop for goal shaping rather than inventing it. Then repeat: select the highest-priority dependency-safe gap; verify it is real; perform one contract-defined reversible iteration; run the same primary verifier under the required conditions; apply the keep-or-revert rule; add regression protection for corrected failures; run relevant broader and assurance checks; review the diff; and record evidence, failed approaches, reusable discoveries, goal fit, and the next action. Do not silently absorb a different outcome or weaken the verifier. Finish only when every acceptance and assurance item passes with surfaced evidence and protected behavior remains intact. Stop for a contract-defined blocker, approval boundary, exhausted budget, material goal drift, or two consecutive no-progress cycles; preserve a reusable closeout packet and restartable handoff. Never perform irreversible, deployment, credential, release, destructive, or external-system actions without explicit approval, and never archive secrets, private data, raw production dumps, exploit-enabling evidence, or unnecessary large logs.
```

**Why it works:** It preserves the universal brownfield safety loop while allowing the contract to define an unusual iteration and evaluation pattern. The custom pattern remains falsifiable, bounded, reviewable, and reusable without expanding the global preset taxonomy from a one-off project.
