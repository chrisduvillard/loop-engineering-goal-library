# Goal Contract: Adaptive question clarity

**Status:** Ready
**Goal ID:** `2026-08-26-adaptive-question-clarity`
**Revision:** 1
**Priority:** P0
**Library target:** `0.9.0`
**Primary profile:** PRD / Spec Compliance
**Shaping history:** `SHAPING.md`
**Approval shaping round:** R1
**Shaping depth:** Thorough

## Target

The shaping workflow asks as few or as many questions as necessary to reach one unambiguous, verifiable Goal Contract; ambiguous answers and hidden material assumptions cannot silently become execution instructions.

## In scope

- Adaptive question depth and risk priority
- Universal clarity matrix
- Atomic-question and answer-quality gates
- Assumption register
- Fresh-reader and counterexample stress testing
- Scenario, verifier, contradiction, traceability, and teach-back checks
- Durable templates, README/quick-reference guidance, validation, versioning, packaging, and dogfood records

## Out of scope

- Replacing native `/goal`
- Asking several questions in one turn
- Forcing exhaustive questions when repository evidence already resolves the goal
- Creating another execution profile

## Acceptance evidence

- Repository validation passes.
- Launcher and generated-document synchronization pass.
- Skills CLI discovers both skills.
- Deterministic `0.9.0` packages build.
- README states that question count is adaptive.
- An ambiguous answer is explicitly required to trigger clarification.
- A fresh-reader clarity stress test and assumption gate are required before approval.
- Pull-request and merged-main CI pass.
- Only `main` remains after merge.

## Protected behavior

- `shape-goal` remains the main interactive command.
- One question is asked per turn and the turn ends immediately.
- All safe questions, answers, corrections, and approvals remain append-only.
- Production execution starts only after explicit approval.
- `goal-engine` does not interview the user while autonomous execution is active.
