# Skills + Goals + Reusable State

The strongest workflow combines reusable skills, a project-specific contract, native goal persistence, and a durable closeout archive without confusing their roles.

```text
Rough intent
    │
    ▼
shape-goal skill             decides what done means
    │
    ▼
Goal Contract                stores project-specific truth
    │
    ▼
native /goal                 provides continuation and evaluation
    │
    ▼
goal-engine skill            supplies safe execution discipline
    │
    ▼
Passing or bounded outcome   produces terminal evidence
    │
    ▼
Reusable closeout archive    preserves the contract, progress, result, and lessons
```

## The five layers

| Layer | Responsibility | Must not do |
|---|---|---|
| **`shape-goal`** | Read the repository, resolve material ambiguity, assign a Goal ID, select a profile, and persist the contract and state paths | Begin production implementation or invent owner decisions |
| **Goal Contract** | Define outcome, scope, acceptance evidence, protected behavior, authority, stopping, library version, and archive paths | Contain a giant generic process prompt or duplicate every source document |
| **Native `/goal`** | Keep work running across turns and evaluate the completion condition | Supply all methodology or grant extra permissions |
| **`goal-engine`** | Orient, reconcile, implement, verify, review, checkpoint, detect stalls, and apply the selected profile | Redefine the target or weaken its verifier |
| **Reusable closeout archive** | Preserve terminal evidence and link durable tests, ADRs, docs, runbooks, fixtures, scripts, and lessons | Become a secret store, raw log dump, or substitute for maintained product artifacts |

## Recommended lifecycle

### 1. Install globally

```bash
npx -y skills@latest add chrisduvillard/loop-engineering-goal-library \
  --skill '*' --global --agent codex --agent claude-code --yes
```

### 2. Shape

```text
Claude Code: /shape-goal Continue this project
Codex:       $shape-goal Continue this project
```

`shape-goal` checks for an existing active goal before creating state. It resumes, supersedes, or closes deliberately rather than overwriting history.

### 3. Execute

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in GOAL.md. Use the selected execution profile. Continue until every acceptance item passes with surfaced evidence and no protected behavior regresses. Stop only for a contract-defined blocker, approval boundary, budget, or two consecutive no-progress cycles; preserve a reusable closeout packet and leave a restartable handoff.
```

### 4. Checkpoint

Use the repository's existing progress system when possible. Otherwise:

```text
GOAL.md
GOAL_PROGRESS.md
```

The mutable progress state records the baseline, acceptance ledger, completed changes, failed or reverted approaches, blockers, no-progress count, and next action.

### 5. Close and reuse

Every terminal outcome is archived:

```text
docs/goals/
├── INDEX.md
└── <goal-id>/
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

A goal may end as Achieved, Blocked, Approval required, Budget exhausted, Stalled, or Superseded. Only Achieved is success, but every outcome can preserve useful evidence.

Verified learning moves to its maintained home:

- fixed failures → regression tests
- product or architecture decisions → approved docs or ADRs
- operational knowledge → runbooks
- reusable workflows → tests or scripts
- representative data → maintained fixtures
- important limitations → residual-risk documentation

## Why not make every profile a skill?

Eleven near-duplicate skills would:

- Crowd discovery and increase trigger ambiguity
- Duplicate the brownfield safety kernel
- Drift as common rules evolve
- Force users to choose a process before the target is understood
- Confuse reusable method with project-specific completion conditions

Instead, `goal-engine` has eleven execution profiles. The Goal Contract selects one primary profile. Canonical files under [`goals/`](goals/) remain standalone fallbacks, and consolidated libraries are generated automatically.

## Reproducibility

Every Goal Contract records:

- Stable Goal ID
- Library source and skill version or source commit
- Contract, progress, archive, and history-index paths
- Execution profile
- Baseline and acceptance verifiers
- Approval and stopping boundaries

The repository itself records:

- [`VERSION`](VERSION)
- [`CHANGELOG.md`](CHANGELOG.md)
- deterministic skill ZIP packages and checksums
- CI validation and Agent Skills CLI discovery
- a [complete example cycle](examples/complete-brownfield-cycle/)

## Separation rule

> **Skills carry reusable process. Contracts carry project truth. Native goals carry persistence. Archives carry reusable evidence.**
