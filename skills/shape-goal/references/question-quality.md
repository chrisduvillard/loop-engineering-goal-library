# Shape Goal: Adaptive Question Quality and Clarity Gate

The goal is not to ask few questions. The goal is to reach **one shared, executable interpretation** without making the agent guess.

> **No fixed question count:** two questions may be enough when repository evidence is strong. Twenty may be necessary when the outcome is subjective, high-risk, cross-cutting, or irreversible. Stop only when the clarity gate passes.

## What counts as material ambiguity

A material ambiguity exists when two reasonable users or agents could read the same draft and take meaningfully different actions while both believing they complied.

A decision is material when it can change any of the following:

- User-visible or business outcome
- Journey boundary, scope, exclusions, or priority
- Acceptance evidence or success threshold
- Protected behavior, compatibility, data, privacy, security, or performance
- Dependency, migration, rollout, recovery, ownership, or maintenance expectations
- Authority, irreversible actions, budget, stop conditions, or risk acceptance

Do not optimize for a short interview. Do not ask questions merely to appear thorough. Ask until every material ambiguity is resolved, safely defaulted, explicitly deferred, or declared blocking.

## Adaptive shaping depth

Use **Adaptive** depth by default. Escalate automatically when risk or uncertainty requires it.

| Depth | Use when | Required review |
|---|---|---|
| Adaptive | Normal default; repository evidence is reasonably strong | Resolve all material ledger rows and run a compact clarity review |
| Thorough | Several plausible interpretations, subjective quality, multiple journeys, weak tests, or important compatibility/data concerns | Cover every applicable clarity lens, scenario walkthrough, and fresh-reader test |
| Exhaustive | Irreversible migration, security/privacy, compliance, production authority, major architecture, substantial cost, or high blast radius | Independent fresh-reader review, explicit assumption sign-off, counterexample test, and all applicable scenarios |

Depth is a quality decision, not a question quota. Record the selected depth and rationale.

## Universal clarity matrix

Every row must be resolved by repository evidence, an owner answer, an explicit safe default, or `Not applicable` with a reason. Omission is not resolution.

| Lens | What must be unambiguous |
|---|---|
| Outcome and value | What becomes true, for whom, and why it matters now |
| Users and journey | Target users, entry point, journey start/end, and supported environments |
| Scope and non-goals | Included surfaces, excluded work, dependencies, and follow-on goals |
| Acceptance evidence | Exact observable proof, conditions, thresholds, examples, and required reviewers |
| Protected behavior | Existing workflows, data, compatibility, user work, visual references, and performance floors |
| Failure and edge cases | Negative paths, partial failure, recovery, empty/loading/error states, and unacceptable outcomes |
| Data and compatibility | Identity, time, units, formats, versions, migrations, retention, and consumer expectations |
| Quality obligations | Security, privacy, reliability, performance, cost, UX, accessibility, operations, and documentation as applicable |
| Authority and risk | Destructive, production, release, credential, billing, legal, security-testing, and external-system boundaries |
| Ownership and longevity | Owners, support expectations, maintainability, freshness triggers, and reusable outputs |
| Profile-specific inputs | Every required field from the selected execution profile |

## Question priority

For each unresolved item, record:

- **Impact:** High / Medium / Low
- **Uncertainty:** High / Medium / Low
- **Irreversibility:** High / Medium / Low
- **Confidence:** Confirmed / Strong / Tentative / Unknown

Ask the highest-risk unresolved decision first. A low-impact, reversible choice may use a recorded safe default. A High- or Medium-impact unresolved assumption may not survive approval.

## Atomic question gate

One question must resolve one decision.

A strong question:

1. Names the decision needed.
2. Explains why it changes the contract.
3. Summarizes the evidence and any conflict.
4. Offers at most three materially different options when useful.
5. Recommends one option and explains the trade-off.
6. States what will change based on the answer.
7. Can be answered without the user researching repository facts.
8. Makes clear that listed options are not exhaustive and the user may answer in their own words.

Split compound questions. Do not hide two independent choices behind “and.”

## Answer quality gate

Never normalize a reply into a stronger or more specific decision than the user actually made.

Classify each answer:

- **Clear:** one material interpretation; resolve the row.
- **Clear with conditions:** triggers, thresholds, and exceptions are explicit; resolve and record them.
- **Partial:** some of the decision is answered; keep the remainder open.
- **Ambiguous:** more than one material interpretation remains; ask a targeted follow-up.
- **Conflicting:** contradicts repository evidence or a prior decision; surface the conflict and ask which authority wins.
- **Delegated judgment:** the user explicitly asks the agent to decide within stated constraints; record the delegation, selected option, criteria, and rationale.
- **Deferred / Blocked:** record the owner or trigger and decide whether the goal excludes the item or cannot become ready.

When clarification is needed, quote the shortest faithful interpretation and ask the user to confirm or correct it. Do not silently pick the interpretation that is easiest to implement.

Preserve requirement strength exactly: **Must / hard gate**, **Should**, **Preference**, **Optional**, or **Explicit non-goal**. Do not turn “ideally” into a mandatory acceptance gate or weaken “must” into best effort.

“You decide” is a real answer only when the delegation boundary is clear. It does not authorize a different product outcome, hidden risk acceptance, destructive action, compatibility removal, legal/compliance judgment, or expanded external-system authority. Ask one boundary question when the delegated decision is still materially unconstrained.

If a reply voluntarily answers several ledger rows, save each explicit decision and its strength. Do not infer unstated links between them; continue with one unresolved decision at a time.

## Ambiguous-language lint

Operationally define or link to an authoritative reference for terms such as:

```text
good, better, best, complete, all, production-ready, secure, safe, fast,
scalable, clean, modern, intuitive, user-friendly, robust, reliable,
correct, supported, compatible, polished, optimized, high quality
```

The word itself is not forbidden. The contract must say how it will be observed or judged.

## Assumption register

Every assumption must be one of:

- **Evidence-backed** — linked to an authoritative source or executable observation.
- **Owner-approved** — linked to a shaping question and answer.
- **Safe reversible default** — low-risk, repository-consistent, and explicitly surfaced before approval.
- **Unresolved** — cannot be used for execution.

Surface all safe defaults and residual low-impact assumptions in the approval summary. No hidden assumption may determine success, scope, protection, or authority.

## Clarity stress test before approval

Run these checks against the draft contract:

1. **Fresh-reader test:** where practical, give a fresh reviewer or subagent only the draft contract and referenced sources—not the persuasive chat history. Ask what it could misunderstand.
2. **Counterexample test:** describe a result that technically satisfies the wording but would disappoint the user. Tighten the contract until that loophole is closed.
3. **Scenario test:** walk through at least one happy path, one important failure or edge path, and one protected regression boundary when applicable.
4. **Verifier test:** confirm that every acceptance item can actually be run, observed, or reviewed under stated conditions.
5. **Contradiction test:** compare the draft with prior answers, authoritative artifacts, runtime behavior, and current Git state.
6. **Traceability test:** every material contract statement links to evidence, a question ID, or an explicit safe default.

For a simple low-risk goal, a concise self-review may be enough. For high-risk or subjective work, use an independent reviewer where the host supports it.

## Plain-English teach-back

Before the approval question, summarize in plain English:

- What will be true when finished
- What is included and excluded
- How completion will be proved
- What must not regress
- Which requirements are hard gates, preferences, optional, or explicit non-goals
- Which assumptions, safe defaults, or delegated judgments remain
- What the agent is not authorized to do

Then ask the user to approve, deepen, stress-test, or pause. Approval is valid only after the summary has one material interpretation.

## Clarity gate

The Goal Contract is ready for approval only when:

- No High- or Medium-impact row is unresolved.
- Every material answer passes the answer quality gate, including preserved requirement strength and bounded delegation.
- Every applicable clarity-matrix row is resolved or marked `Not applicable` with a reason.
- Subjective terms have a rubric, reference, example, or qualified reviewer.
- Acceptance evidence is observable under stated conditions.
- Safe defaults and residual assumptions are visible.
- The fresh-reader and counterexample tests reveal no blocking alternate interpretation.
- The user can correct the plain-English teach-back before explicitly approving.

If this takes two questions, stop after two. If it takes twenty, ask twenty—one per turn, without repetition or guesswork.
