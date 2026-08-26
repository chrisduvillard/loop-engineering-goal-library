# Custom Contract-Driven Goal

**Use when:** The desired outcome is measurable, but none of the catalog's primary profiles matches the dominant control loop.

**In simple terms:** Let `shape-goal` discover the unusual loop, make it measurable and bounded, obtain approval, and then return the exact execution `/goal`.

## Recommended — interactive shaping

Run this outside an active `/goal`:

| Host | Command |
|---|---|
| Claude Code | `/shape-goal Use a Custom Contract-Driven profile` |
| Codex CLI / IDE | `$shape-goal Use a Custom Contract-Driven profile` |

`shape-goal` proves that no existing profile cleanly fits, resolves the iteration and verification model, asks one material question per turn, and returns the execution command only after approval.

## Inputs the skill resolves

- Why no existing primary profile fits
- One observable outcome
- One bounded iteration unit
- One primary verifier or stable rubric
- Keep-or-revert rule
- Review and regression strategy
- Scope, exclusions, protected behavior, authority, budget, and stopping logic
- Durable state and closeout paths

## Advanced — autonomous preflight

Use only when an approved repository artifact already resolves every owner decision.

```text
/goal Use the installed shape-goal and goal-engine skills to discover and complete this repository's next measurable engineering objective whose dominant execution loop does not fit an existing catalog profile. Search repository and connected authoritative evidence first and prove that no standard profile cleanly fits. Continue inside this /goal only when an already-approved Goal Contract or authoritative artifact resolves the outcome, scope, exclusions, evidence, protection, authority, budget, bounded iteration unit, primary verifier, keep-or-revert rule, review strategy, and stop conditions. Otherwise create or resume SHAPING.md, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to resume shape-goal outside /goal; do not ask the question or take another autonomous turn. After approval, use goal-engine to run small reversible iterations, apply the same verifier, keep or revert by evidence, run repository-native and assurance checks, review important changes, preserve reusable state, and finish only when every approved gate passes without protected-behavior regression. Never perform destructive, production, deployment, release, credential, billing, or external-system actions without explicit approval.
```

## Advanced — self-contained preflight

Use only when the skills are unavailable and no owner interaction is expected.

```text
/goal Determine and complete this repository's next measurable engineering objective whose dominant loop does not fit an existing catalog profile, without requiring the user to prefill placeholders. Search repository and authoritative evidence first and prove that no standard profile fits. Continue only when an existing approved artifact resolves one outcome, scope, exclusions, evidence, protected behavior, authority, budget, bounded iteration unit, primary verifier, keep-or-revert rule, review strategy, regression obligations, and objective exits. Otherwise create or resume SHAPING.md, save the unresolved decision and one recommended question, stop as Approval required, and tell the user to continue shaping outside /goal; do not ask the question or take another autonomous turn. Once approved, repeat the bounded iteration, run the same verifier, apply the keep-or-revert rule, run repository-native and assurance checks, review the diff, preserve progress and failed approaches, and finish only when every gate passes with surfaced evidence. Preserve a reusable closeout packet with SHAPING.md, CONTRACT.md, PROGRESS.md, and RESULT.md. Never perform destructive, production, deployment, release, credential, billing, or external-system actions without explicit approval.
```

**Why it works:** It preserves the universal brownfield safety system while allowing an unusual iteration and evaluation pattern to remain explicit, falsifiable, bounded, reviewable, and reusable.
