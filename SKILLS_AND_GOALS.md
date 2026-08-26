# Skills + Goals + Zero-Friction Execution

The library separates reusable method, repository-specific truth, durable decision history, native persistence, and completion evidence.

```text
Copied profile launcher
        │
        ▼
shape-goal
  - searches evidence
  - resolves profile inputs
  - asks owner decisions
  - saves every question and answer
  - supports deeper shaping rounds
        │
        ▼
Shaping history
  - append-only rounds
  - evidence + recommendations
  - answers + corrections
  - approval round
        │
        ▼
Goal Contract
  - one outcome
  - proof and protection
  - profile + overlays
  - authority and exits
        │
        ▼
goal-engine inside native /goal
  - implements
  - verifies
  - reviews
  - records
  - detects drift
        │
        ▼
Closeout + reusable knowledge
```

## Why a launcher may begin before the exact target is known

The strictest native-goal pattern shapes the contract first and activates `/goal` second. The zero-friction launchers support a deliberate two-phase meta-goal:

1. Discover, deepen when needed, and approve the exact contract.
2. Execute that contract to passing evidence.

The approval boundary preserves safety. The launcher explicitly forbids production edits during shaping and forbids the evaluator from treating contract creation as completion.

Users who prefer maximum control can always use the strict two-step flow.

## Responsibilities

| Layer | Responsibility | Must not do |
|---|---|---|
| Goal catalog | Offer reusable control-loop choices | Pretend to encode repository-specific targets |
| `shape-goal` | Search evidence, resolve inputs, ask decisions, manage shaping rounds and lifecycle, approve the contract | Implement production changes or invent owner decisions |
| Shaping history | Preserve every asked question, answer, recommendation, correction, and round summary | Become an editable summary that erases prior decisions or a store for secrets |
| Input specifications | Define what each profile needs | Turn defaults into hidden product decisions |
| Goal Contract | Store one approved outcome, proof, protection, authority, relationships, approval round, and exits | Become an unbounded backlog or duplicate the full interview |
| Native `/goal` | Continue the current session toward the condition | Grant extra authority or redefine success |
| `goal-engine` | Execute, verify, review, checkpoint, close, and preserve reusable outputs | Absorb unrelated work, weaken evidence, or reopen settled decisions without new evidence |
| Assurance overlays | Add cross-cutting proof | Replace the primary profile |
| Project Harness | Preserve verified setup/run/reset/check mechanics | Duplicate stale instructions |
| Portfolio | Coordinate several goals over time | Merge different outcomes into one active goal |
| Closeout archive | Preserve immutable shaping, contract, progress, result, and durable-output links | Become a secret store or raw log dump |

## Zero-friction input resolution

The recommended command in every goal file names a profile but no repository-specific placeholder.

`shape-goal` loads:

- [`input-resolution.md`](skills/shape-goal/references/input-resolution.md)
- [`profile-inputs.md`](skills/shape-goal/references/profile-inputs.md)
- [`shaping-history.md`](skills/shape-goal/references/shaping-history.md)

It creates an input ledger, searches all available authoritative sources, applies only safe reversible defaults, and asks one unresolved material decision at a time with a recommendation.

## Durable shaping rounds

Once a Goal ID exists, questions and answers are saved by default in:

```text
docs/goals/<goal-id>/SHAPING.md
```

The history uses stable IDs such as `R1-Q1`. It is append-only:

- Prior answers are never silently rewritten.
- Corrections append and supersede earlier decisions.
- Sensitive material is redacted and linked securely.
- Each round ends with decisions, contract changes, remaining uncertainty, and readiness.
- The contract records which round approved execution.

The first round resolves the minimum material decisions required for readiness. When the user is not satisfied, `shape-goal` reads all previous rounds and runs another non-duplicate deepening round. The user may repeat this until they approve, pause, or reach a genuine blocker.

## Profiles and overlays

A profile defines **how the work progresses**.

An overlay defines **extra proof required**.

Example:

```text
Primary profile: Frontend UI / UX / Accessibility
Overlays:
- Performance & Cost
- Compatibility & Portability
```

When a quality concern is itself the main outcome, use its dedicated profile. When it is secondary to another outcome, add the overlay.

## Multiple goals

A project may have sequential, paused, blocked, competing, or safely parallel goals.

```text
Candidate → Ready → Active → Paused / Blocked → Closed
```

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolated sessions/worktrees and explicit shared-resource coordination.

Lifecycle changes are handled through clarify, amend, reprioritize, pause, resume, supersede, split, merge, cancel, and close. Clarification and amendment append new shaping entries; they do not erase prior answers.

## Durable state

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/PORTFOLIO.md
docs/goals/INDEX.md
docs/goals/<goal-id>/
├── SHAPING.md
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Closed evidence is immutable. Later work links to prior results rather than rewriting them.

## Reusable project knowledge

Verified recurring knowledge is promoted to:

- Regression tests
- ADRs and approved product/architecture documentation
- Runbooks
- Project Harness
- Fixtures and design references
- Scripts and task-runner commands
- Benchmarks and evals
- Residual-risk documentation

The shaping history remains the detailed decision trail. Stable decisions may be promoted to maintained docs or ADRs, but the full interview is not duplicated.

## Extension rule

Add a global profile only when repeated field use demonstrates a distinct:

- Iteration unit
- Primary verifier
- Failure mode
- Keep-or-revert decision
- Stop condition

Use Custom Contract-Driven for unusual one-off loops. Use project-specific overlays or skills for local recurring needs.
