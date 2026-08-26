# UAT: Interactive shaping on this repository

## Purpose

Verify the corrected user journey against the failure observed during live use: a shaping question must return control to the user instead of continuing inside an autonomous native `/goal`.

## Test surface

This repository itself is the project under test. The shaped objective is the `0.6.0` interactive-first redesign and README rewrite documented in `CONTRACT.md`.

## Scenario A — Normal interactive shaping

1. Start from the repository root with no active native `/goal`.
2. Run:

   ```text
   $shape-goal Continue this project
   ```

3. The skill searches repository evidence and resolves facts without asking the owner to inspect files.
4. When one material owner decision is missing, the skill:
   - creates or resumes `SHAPING.md`;
   - saves the exact proposed question, evidence, options, and recommendation;
   - asks exactly one question;
   - ends the turn immediately;
   - performs no further tool call or background step.
5. The user's next ordinary message is treated as the answer; **Steer is not required**.
6. The answer is saved before another question or contract update.
7. After explicit approval, the skill returns—but does not execute—the exact `/goal` command for `goal-engine`.

**Expected result:** Interactive questions behave like an ordinary conversation and autonomous work has not started.

## Scenario B — Deeper shaping

1. Run `$shape-goal Deepen the current goal`.
2. The skill reads all prior rounds and avoids duplicate questions.
3. It selects one weak or unexplored lens, asks one question, and ends the turn.
4. Earlier answers remain unchanged; corrections append and supersede.

**Expected result:** Additional depth is possible without losing or rewriting earlier decisions.

## Scenario C — Owner decision discovered during autonomous execution

1. Start the approved execution command returned by `shape-goal`.
2. During `goal-engine`, introduce or discover a material change to outcome, scope, evidence, protection, authority, or priority.
3. The engine saves progress and the proposed shaping question.
4. It stops the current native goal as **Approval required**.
5. It does not ask the question and continue looping.
6. The user resumes `shape-goal` outside native `/goal`, approves a revision, and starts a new execution `/goal`.

**Expected result:** Autonomous execution never becomes an interactive interview.

## Scenario D — Advanced profile preflight

1. Open any file under `goals/`.
2. Confirm the interactive `shape-goal` commands are shown first.
3. Run the advanced autonomous preflight only with an already-approved artifact.
4. When an owner decision is missing, the preflight writes one proposed question, stops as **Approval required**, and directs the user back to interactive shaping.

**Expected result:** Advanced compatibility remains, but it cannot recreate the Steer problem.

## Repository-level evidence

The automated repository gates verify the parts that can be tested without launching the external Codex and Claude clients:

- Both skills contain the interaction barrier.
- All 24 profile files expose interactive commands first.
- Every advanced preflight contains the Approval-required stop clauses.
- README and installation guidance teach the interactive-first flow.
- Shaping history remains append-only.
- Agent Skills discovery and deterministic packages pass.

## Honest boundary

This dogfood run validates the repository contract, generated prompts, state artifacts, and CI behavior on the project itself. A full UI-level test that observes the actual Codex and Claude clients pausing after the question remains external host UAT and is tracked before `1.0.0`.
