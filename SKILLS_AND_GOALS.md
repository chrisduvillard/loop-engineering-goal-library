# Skills + Goals + Adaptive Project State

The library separates reusable process, changing project priorities, one executable contract, native persistence, project mechanics, and durable evidence.

```text
Project needs and portfolio
          │
          ▼
shape-goal             chooses, changes, pauses, splits, or resumes the next goal
          │
          ▼
Goal Contract          stores one outcome, revision, proof, relationships, and boundaries
          │
          ▼
native /goal           provides one-session continuation and completion evaluation
          │
          ▼
goal-engine            applies one profile, assurance overlays, and project harness
          │
          ▼
Evidence + archive     closes the goal, preserves learning, and informs what runs next
```

## The layers

| Layer | Responsibility | Must not do |
|---|---|---|
| Goal portfolio or existing tracker | Coordinate candidate, ready, active, paused, blocked, and closed goals; priority and dependencies | Replace individual contracts or silently redefine them |
| `shape-goal` | Inspect evidence, manage lifecycle transitions, assign identity, select profile/overlays, and approve the next contract | Begin production implementation or invent owner decisions |
| Goal Contract | Define one outcome, revision, scope, proof, protection, relationships, authority, harness, and exits | Become a backlog or giant process prompt |
| Native `/goal` | Keep one contract running in one session and evaluate its finish condition | Grant permissions or choose new product direction |
| `goal-engine` | Orient, implement, verify, review, detect drift, checkpoint, close, and preserve reusable outputs | Absorb unrelated work or weaken the contract |
| Project harness | Store verified setup, run, reset, environment, and native-check mechanics reused across goals | Duplicate canonical scripts or preserve stale assumptions as fact |
| Closeout archive | Preserve immutable contract, progress, result, relationships, and links to durable outputs | Become a secret store or raw log dump |

## A project can have many goals

One project may have sequential goals, paused goals, competing candidates, dependency chains, or safely isolated parallel workstreams.

One native `/goal` session or worktree executes one dependency-safe leaf goal. This keeps completion evidence coherent. Parallel goals require separate branches/worktrees, non-overlapping ownership, and explicit coordination of shared resources.

Use an existing issue tracker or roadmap as the portfolio when possible. Otherwise use `docs/goals/PORTFOLIO.md`.

### Lifecycle transitions

- **Clarify:** same semantics and Goal ID; record revision note.
- **Amend:** same outcome, material contract change; pause, approve, increment revision.
- **Reprioritize:** reorder portfolio; contracts remain unchanged.
- **Pause / Resume:** preserve progress, branch/SHA, next action, and resume condition.
- **Supersede:** different outcome replaces prior goal; archive and create a new Goal ID.
- **Split:** create child goals and select one leaf.
- **Merge:** combine only when outcome, evidence, and authority align.
- **Cancel:** close with reason and reusable evidence.

At each checkpoint, `goal-engine` runs a goal-fit gate. A new user need is not automatically scope.

## Thirteen presets are enough as presets—not as an exhaustive taxonomy

The profiles capture common control-loop shapes:

- Completion and convergence
- Requirements compliance
- Milestone delivery
- Audit and remediation
- Product verification
- Behavior-preserving transformation
- Release-gate convergence
- Incident recovery
- Ecosystem upgrades
- Data migration
- Divergent-history integration
- Measured champion-versus-challenger optimization
- Bounded technical feasibility and decision evidence

They intentionally do not duplicate every project domain or quality attribute.

### Assurance overlays

Security, reliability, performance, cost, UX, accessibility, data governance, compatibility, operability, documentation, and compliance are additive proof obligations selected in the contract.

### Custom Contract-Driven fallback

When no preset fits, the contract defines the iteration unit, verifier, keep-or-revert rule, review strategy, and objective stop condition. The [standalone custom fallback](skills/shape-goal/templates/custom-contract-driven-goal.md) preserves the same model without installed skills. A recurring custom pattern may later justify a new preset, but one unusual project should not expand the global taxonomy.

## Reusable project harness

Future goals should not rediscover how to install, run, reset, or verify the same repository. `goal-engine` uses existing instructions and scripts first; when they are fragmented or ambiguous, it creates or refreshes `docs/agent/PROJECT_HARNESS.md`.

The harness remains vendor-neutral and records only verified mechanics. Platform-specific project skills may reference it without becoming the only source of truth.

## Durable state

```text
GOAL.md
GOAL_PROGRESS.md
docs/goals/PORTFOLIO.md   optional when several goals need coordination
docs/goals/INDEX.md
docs/goals/<goal-id>/
├── CONTRACT.md
├── PROGRESS.md
└── RESULT.md
```

Closed evidence is immutable. Later work links to prior goals rather than rewriting their result.

## Separation rule

> **Portfolios coordinate needs. Skills carry method. Contracts carry one project's current truth. Harnesses carry verified mechanics. Native goals carry persistence. Archives carry evidence and reuse.**
