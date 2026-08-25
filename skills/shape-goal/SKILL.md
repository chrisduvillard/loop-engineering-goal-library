---
name: shape-goal
description: Turn a vague project request, continuation request, issue, PRD, or milestone into an evidence-backed Goal Contract and a copy-ready /goal command. Use before /goal when the target, scope, acceptance evidence, or best loop is unclear.
---

# Shape Goal

Turn rough intent into a safe execution contract. **Shape the work; do not implement production changes.**

A useful target has this form:

> **[Observable outcome]** is true for **[scope]**, proven by **[acceptance evidence]**, while **[protected behavior]** remains intact.

## Required outputs

Produce all four:

1. One approved **Goal Contract**.
2. The most appropriate loop from the repository's goal library.
3. One copy-ready `/goal` command.
4. The path or issue where the contract was persisted.

## 1. Orient before asking

Read the applicable repository evidence first:

- Agent and repository instructions
- Specifications, PRDs, architecture docs, ADRs, and domain glossaries
- Approved plans, milestones, issues, progress files, and handoffs
- Native scripts, tests, CI, release gates, and runtime entry points
- Git status, diff, branch, and relevant history

Establish the actual current state and reconcile contradictions by explicit authority, recency, and executable evidence. Protect uncommitted and unrelated work.

**Facts are the agent's job; decisions are the user's.** Never ask the user for something the repository, tools, or documentation can answer.

## 2. Classify the ambiguity

Choose one path:

### A. One target is strongly supported

Draft the Goal Contract directly. Explain the evidence in a few lines and ask for one approval before persisting it.

### B. Several materially different targets are plausible

Present at most three candidate outcomes. For each, state the supporting evidence, value, scope, and main trade-off. Recommend one, then ask the user to choose **one decision at a time**.

### C. The destination itself is still foggy

Do not manufacture a target. Recommend a broader discovery or wayfinding session first. A `/goal` is premature when product direction, users, or the promised outcome remain undecided.

## 3. Resolve only material decisions

Ask only questions whose answers could materially change the product outcome, scope, acceptance evidence, protected behavior, or authority boundary.

For every question:

- Ask one decision at a time.
- Provide a recommended answer and why.
- Use concrete scenarios when wording is vague.
- Surface conflicts with existing code or documents.
- Do not debate reversible implementation details that the executing agent can safely choose later.

Use `grill-with-docs` or the repository's domain/ADR workflow when terminology or hard-to-reverse design decisions need deeper alignment. Goal shaping is narrower: it defines the execution contract.

## 4. Build the Goal Contract

Use [goal-contract-template.md](goal-contract-template.md). Keep it concise and include:

- One observable outcome
- Why this target is next
- In-scope and out-of-scope boundaries
- Acceptance evidence and exact verifiers where known
- Protected behavior and compatibility constraints
- Approval and irreversible-action boundaries
- Success, blocker, budget, and stalled-loop exits
- The authoritative sources used

A target is not ready when it is merely a task list, a mechanism, an aspiration such as "improve the project," or an entire open-ended backlog.

## 5. Apply the readiness gate

The Goal Contract is ready only when:

- It names one outcome rather than unrelated work.
- A fresh agent can tell what is in and out of scope.
- Completion can be demonstrated by commands, workflows, measurements, or observable artifacts.
- Existing behavior and user work that must survive are named.
- No unresolved owner decision could lead to materially different implementations.
- Stop and escalation conditions are explicit.
- Success cannot be claimed solely from an agent assertion.

## 6. Persist without creating competing state

After approval:

1. Update the existing authoritative issue, milestone, PRD, plan, or goal artifact when one exists.
2. Otherwise create `GOAL.md` at the repository root from the template.
3. Link rather than duplicate detailed requirements.
4. Mark the contract `Approved` and record the current branch/SHA when useful.

If the user requested a read-only session, return the contract in the conversation without writing.

## 7. Select the execution loop

Choose the most specific fit:

- **Brownfield Continue / Finish** — default continuation toward an approved outcome
- **PRD / Spec Compliance** — close documented requirement gaps
- **Next Milestone** — deliver one bounded roadmap increment
- **Deep Audit + Remediation** — discover, prove, and repair important findings
- **QA / Regression / UAT** — make real product workflows pass
- **Safe Refactor / Modernization** — change internals while proving equivalence
- **Release Readiness** — satisfy pre-release gates
- **Incident Recovery**, **Dependency Upgrade**, **Data Migration**, or **Branch Rescue** — use when their distinct risk model applies

## 8. Render the `/goal`

Return one command that references the approved contract instead of repeating it unnecessarily. Adapt the loop-specific clauses, but preserve this shape:

```text
/goal Complete the approved Goal Contract in [PATH OR ISSUE]. Treat its Outcome, Scope, Acceptance evidence, Protected behavior, Authority boundaries, and Stop conditions as binding. Establish the repository's actual state before editing; make small reversible production changes; use repository-native checks; add regression protection for fixed failures; review important changes; and update existing progress or handoff state. Continue autonomously until every acceptance item passes with surfaced evidence. Stop only for a contract-defined blocker, approval boundary, budget, or repeated no-progress, and leave a restartable handoff. Do not perform irreversible or external-system actions without explicit approval.
```

End with:

- **Approved target:** one sentence
- **Contract:** path or issue
- **Selected loop:** name
- **Run:** the copy-ready `/goal`
- **Open decisions:** `None` or a short list
