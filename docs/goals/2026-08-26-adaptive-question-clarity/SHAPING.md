# Shaping History: Adaptive question clarity

**Goal ID:** `2026-08-26-adaptive-question-clarity`
**State:** Approved
**Current round:** R1
**Approval round:** R1
**Shaping depth:** Thorough

## Round R1

### Request and evidence

The owner asked whether the question process could be improved so agents never need to guess, explicitly allowing either two or many questions depending on need. The existing repository already enforced repository-first evidence search, one question per turn, append-only answers, and repeatable deeper rounds. The remaining gap was that “minimum material decisions” did not define answer quality, adaptive depth, hidden assumptions, or a final ambiguity challenge.

### Decisions

- Do not impose a minimum or maximum question count.
- Ask until every material ambiguity is resolved; stop early when evidence makes further questions unnecessary.
- Add a universal clarity matrix, risk-weighted input ledger, assumption register, and answer-quality gate.
- Clarify partial, ambiguous, conditional, or conflicting answers instead of inferring intent.
- Add fresh-reader, counterexample, scenario, verifier, contradiction, traceability, and plain-English teach-back checks before approval.
- Preserve one-question turns and append-only shaping history.
- Add a user-invocable stress-test round.
- Advance the library to `0.9.0`, validate, merge, archive, and clean branches.

### Owner approval

The current request explicitly authorizes the clarity improvements and permits the agent to decide the implementation without another owner question.

**Approval round:** R1
