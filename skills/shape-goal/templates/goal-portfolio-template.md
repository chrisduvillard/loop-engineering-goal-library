# Goal Portfolio

Use the repository's existing issue tracker, roadmap, milestone system, or project board when it already represents the fields below. Create `docs/goals/PORTFOLIO.md` only when the project has more than one non-closed goal and no suitable authoritative tracker.

**Project:** [NAME]  
**Owner:** [OWNER]  
**Last reviewed:** [DATE]  
**Authoritative tracker:** [THIS FILE OR EXISTING SYSTEM]  
**Policy:** One active goal per native `/goal` session or worktree. Parallel goals require isolated branches/worktrees, non-overlapping ownership, and explicit dependency handling.

## Active

| Goal ID | Priority | Outcome | Profile | Assurance overlays | Branch/worktree | Contract | Progress | Depends on | Review trigger |
|---|---|---|---|---|---|---|---|---|---|
| [ID] | P0 / P1 / P2 / P3 | [ONE-LINE OUTCOME] | [PROFILE] | [OVERLAYS OR NONE] | [REF] | [PATH/ISSUE] | [PATH/ISSUE] | [IDS OR NONE] | [EVENT/DATE] |

## Ready

| Goal ID | Priority | Outcome | Profile | Assurance overlays | Depends on | Contract | Why next |
|---|---|---|---|---|---|---|---|
| [ID] | P0 / P1 / P2 / P3 | [ONE-LINE OUTCOME] | [PROFILE] | [OVERLAYS OR NONE] | [IDS OR NONE] | [PATH/ISSUE] | [EVIDENCE] |

## Paused or blocked

| Goal ID | State | Reason | Preserved progress | Resume condition | Next review |
|---|---|---|---|---|---|
| [ID] | Paused / Blocked | [REASON] | [PATH/ISSUE] | [CONDITION] | [DATE/EVENT] |

## Candidates

| Candidate | Value | Main uncertainty | Evidence needed | Decision owner |
|---|---|---|---|---|
| [ROUGH INTENT] | [VALUE] | [UNCERTAINTY] | [DISCOVERY] | [OWNER] |

## Closed history

See [`INDEX.md`](INDEX.md) or the repository's existing goal-history index for achieved, cancelled, superseded, stalled, blocked, and budget-exhausted closeout packets.

## Transition log

| Date | Goal | Transition | Reason | Approved by | Related goal |
|---|---|---|---|---|---|
| [DATE] | [ID] | Clarified / Amended / Reprioritized / Paused / Resumed / Split / Merged / Superseded / Cancelled / Closed | [REASON] | [OWNER] | [ID OR NONE] |

## Rules

- Priority changes reorder work; they do not silently rewrite Goal Contracts.
- Keep the same Goal ID only when the observable outcome remains the same.
- A material change to scope, evidence, protected behavior, authority, or stop conditions requires an approved contract revision.
- A different observable outcome gets a new Goal ID and an explicit relationship to the prior goal.
- Do not append an unrelated request to the active contract merely because it arrived during execution.
- A parent goal may coordinate child goals, but only a dependency-safe leaf goal should run in one native `/goal` session.
- Parallel work must not share mutable files or external resources without explicit coordination.
- Closed goals remain immutable evidence; later work links to them rather than rewriting their result.
