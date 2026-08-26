# Skills, Contracts, and Native Goals

The library separates **interactive decisions** from **autonomous execution**.

```text
shape-goal outside /goal
  - searches evidence
  - asks one owner decision
  - saves the answer
  - ends each question turn
  - supports deeper rounds
        │
        ▼
Shaping history + Goal Contract
  - decision trail
  - one approved outcome
  - proof, protection, authority, exits
        │
        ▼
new native /goal + goal-engine
  - implements
  - verifies
  - reviews
  - records
  - detects drift
        │
        ▼
Closeout + reusable knowledge
```

## Why the split matters

A native `/goal` automatically keeps taking turns until its condition is met. That is excellent for implementation, migrations, audits, testing, and remediation. It is not a smooth place to conduct an interview that must wait for a human reply.

The default architecture is therefore:

```text
Conversation decides what done means.
Native /goal works until done is proven.
```

## Responsibilities

| Layer | Responsibility | Must not do |
|---|---|---|
| Goal catalog | Offer reusable control-loop profiles | Pretend to encode a repository-specific target |
| `shape-goal` | Search evidence, ask one decision per turn, manage shaping rounds and lifecycle, approve the contract | Implement production changes, require Steer, or continue after asking a question |
| Shaping history | Preserve questions, answers, recommendations, corrections, and approval | Erase prior decisions or become a secret store |
| Input specifications | Define what each profile needs | Turn defaults into hidden product decisions |
| Goal Contract | Store one approved outcome, proof, protection, authority, relationships, and exits | Become an unbounded backlog or duplicate the full interview |
| Native `/goal` | Persist autonomous execution toward a known condition | Interview the user or redefine success |
| `goal-engine` | Execute, verify, review, checkpoint, close, and preserve reusable outputs | Absorb unrelated work, weaken evidence, or ask owner questions while looping |
| Assurance overlays | Add cross-cutting proof | Replace the primary profile |
| Project Harness | Preserve verified setup/run/reset/check mechanics | Duplicate stale instructions |
| Portfolio | Coordinate several goals over time | Merge different outcomes into one active goal |
| Closeout archive | Preserve immutable shaping, contract, progress, result, and output links | Become a secret store or raw log dump |

## Interactive input resolution

`shape-goal` loads:

- [`input-resolution.md`](skills/shape-goal/references/input-resolution.md)
- [`profile-inputs.md`](skills/shape-goal/references/profile-inputs.md)
- [`shaping-history.md`](skills/shape-goal/references/shaping-history.md)

It creates an input ledger, searches authoritative evidence, applies only safe reversible defaults, classifies repository visibility, and asks one unresolved material decision at a time with a recommendation.

The question barrier is strict:

```text
prepare → save question → ask → end turn
user replies → save answer → continue
```

No tool calls or background activity occur after a shaping question is asked.

## Durable shaping rounds

Once a Goal ID exists:

```text
docs/goals/<goal-id>/SHAPING.md
```

The history uses stable IDs such as `R1-Q1` and is append-only:

- Prior answers are never silently rewritten.
- Corrections append and supersede earlier decisions.
- Sensitive material is redacted and linked securely.
- Each round records decisions, contract changes, uncertainty, and readiness.
- Approval is saved as an explicit question and answer.

When the user is not satisfied, `shape-goal` reads earlier rounds and runs another non-duplicate deepening round.

## Execution handoff

After approval, `shape-goal` returns an exact command using the real contract reference. The user starts a new native `/goal`; `goal-engine` does not run automatically from the shaping turn.

If a material decision appears during execution, `goal-engine`:

1. Saves progress and the proposed decision.
2. Stops as **Approval required**.
3. Returns the project to interactive `shape-goal`.
4. Resumes only after a revised contract is approved and a new `/goal` is started.

## Profiles and overlays

A profile defines **how work progresses**. An overlay defines **extra proof required**.

Example:

```text
Primary profile: Frontend UI / UX / Accessibility
Overlays:
- Performance & Cost
- Compatibility & Portability
```

Use a dedicated profile when a quality concern is the main outcome. Use its overlay when secondary.

## Multiple goals

```text
Candidate → Ready → Active → Paused / Blocked → Closed
```

One native `/goal` session or worktree executes one dependency-safe leaf contract. Parallel goals require isolated sessions/worktrees and explicit shared-resource coordination.

Lifecycle actions include clarify, amend, reprioritize, pause, resume, supersede, split, merge, cancel, and close. Changes append shaping entries rather than erasing history.

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

Closed evidence is immutable. Later work links back rather than rewriting it.

## Reusable project knowledge

Verified recurring knowledge is promoted to regression tests, ADRs, approved product/architecture documentation, runbooks, the Project Harness, fixtures, scripts, benchmarks, evaluations, and residual-risk documentation.

## Extension rule

Add a global profile only when repeated field use demonstrates a distinct iteration unit, primary verifier, failure mode, keep-or-revert decision, and stop condition.

Use Custom Contract-Driven for unusual one-off loops. Use project-specific overlays or skills for local recurring needs.
