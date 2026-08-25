# Skills + Goals

The strongest workflow combines them, but does not confuse their roles.

```text
Rough intent
    │
    ▼
shape-goal skill        decides what done means
    │
    ▼
Goal Contract           stores project-specific truth
    │
    ▼
native /goal            provides durable continuation and evaluation
    │
    ▼
goal-engine skill       supplies the safe execution method
    │
    ▼
Passing evidence        proves the target was reached
```

## The four layers

| Layer | Responsibility | Must not do |
|---|---|---|
| **`shape-goal` skill** | Read the repository, resolve material ambiguity, select an execution profile, and write an approved Goal Contract | Begin production implementation or invent owner decisions |
| **Goal Contract** | Define the outcome, scope, acceptance evidence, protected behavior, authority, and stopping conditions | Contain a giant generic process prompt or duplicate every source document |
| **Native `/goal`** | Keep work running across turns and evaluate the completion condition | Supply all repository methodology or grant extra permissions |
| **`goal-engine` skill** | Orient, reconcile, implement, verify, review, record state, detect stalls, and apply the selected profile | Redefine the approved target or weaken its verifier |

## Why not make every `/goal` a separate skill?

Eleven near-duplicate skills would:

- Crowd skill discovery and increase trigger ambiguity
- Duplicate the brownfield safety kernel
- Drift as common rules evolve
- Force users to choose a process before the target is understood
- Confuse a reusable method with a project-specific completion condition

Instead, `goal-engine` is one execution skill with **eleven profiles**. The Goal Contract selects one primary profile. The long standalone `/goal` commands remain available for environments where the skills are not installed.

## Recommended workflow

### 1. Install both skills

```bash
npx skills add chrisduvillard/loop-engineering-goal-library --skill '*'
```

### 2. Shape the target

**Claude Code**

```text
/shape-goal Continue this project
```

**Codex CLI or IDE**

```text
$shape-goal Continue this project
```

The output is an approved `GOAL.md` or an updated authoritative issue/spec, plus a selected execution profile.

### 3. Start the native goal

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the execution profile named in the contract. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; leave a restartable handoff.
```

The wording is vendor-neutral. The host can implicitly load `goal-engine` because the command names it and matches its description.

## When the target is already clear

Skip `shape-goal` only when an approved issue, PRD section, milestone, or Goal Contract already defines:

- One observable outcome
- Scope and exclusions
- Acceptance evidence
- Protected behavior
- Authority boundaries
- Stop conditions

Then point the native goal directly at that artifact.

## When the skills are not installed

Use the standalone commands under [`goals/`](goals/). They embed the execution discipline directly in the `/goal` condition, making them longer but self-contained.

## Separation rule

> **Skills carry reusable process. Contracts carry project truth. Native goals carry persistence. Evidence carries the right to say “done.”**
