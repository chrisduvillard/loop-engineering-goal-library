#!/usr/bin/env python3
"""Apply the adaptive question-depth and clarity-gate upgrade."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    source = read(path)
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one occurrence, found {count}: {old[:100]!r}")
    write(path, source.replace(old, new, 1))


QUESTION_QUALITY = r'''# Shape Goal: Adaptive Question Quality and Clarity Gate

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

Split compound questions. Do not hide two independent choices behind “and.”

## Answer quality gate

Never normalize a reply into a stronger or more specific decision than the user actually made.

Classify each answer:

- **Clear:** one material interpretation; resolve the row.
- **Clear with conditions:** triggers, thresholds, and exceptions are explicit; resolve and record them.
- **Partial:** some of the decision is answered; keep the remainder open.
- **Ambiguous:** more than one material interpretation remains; ask a targeted follow-up.
- **Conflicting:** contradicts repository evidence or a prior decision; surface the conflict and ask which authority wins.
- **Deferred / Blocked:** record the owner or trigger and decide whether the goal excludes the item or cannot become ready.

When clarification is needed, quote the shortest faithful interpretation and ask the user to confirm or correct it. Do not silently pick the interpretation that is easiest to implement.

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
- Which assumptions or safe defaults remain
- What the agent is not authorized to do

Then ask the user to approve, deepen, stress-test, or pause. Approval is valid only after the summary has one material interpretation.

## Clarity gate

The Goal Contract is ready for approval only when:

- No High- or Medium-impact row is unresolved.
- Every material answer passes the answer quality gate.
- Every applicable clarity-matrix row is resolved or marked `Not applicable` with a reason.
- Subjective terms have a rubric, reference, example, or qualified reviewer.
- Acceptance evidence is observable under stated conditions.
- Safe defaults and residual assumptions are visible.
- The fresh-reader and counterexample tests reveal no blocking alternate interpretation.
- The user can correct the plain-English teach-back before explicitly approving.

If this takes two questions, stop after two. If it takes twenty, ask twenty—one per turn, without repetition or guesswork.
'''

write("skills/shape-goal/references/question-quality.md", QUESTION_QUALITY)
write("VERSION", "0.9.0\n")

for skill_path in ("skills/shape-goal/SKILL.md", "skills/goal-engine/SKILL.md"):
    replace_once(skill_path, 'version: "0.8.0"', 'version: "0.9.0"')

replace_once(
    "skills/shape-goal/SKILL.md",
    "- Ask one material owner decision at a time, then **end the turn immediately**.\n",
    "- Ask one material owner decision at a time, then **end the turn immediately**.\n"
    "- Do not optimize for a small question count; ask until no material ambiguity remains.\n"
    "- Never convert an ambiguous, partial, conditional, or conflicting reply into a stronger decision than the user made.\n"
    "- No High- or Medium-impact assumption may survive approval unless it is evidence-backed or explicitly owner-approved.\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |\n",
    "| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |\n"
    "| Stress-test clarity | `/shape-goal Stress-test the current goal` | `$shape-goal Stress-test the current goal` |\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "12. Input ledger showing how every material field was resolved\n",
    "12. Input ledger showing how every material field was resolved\n"
    "13. Assumption register, selected shaping depth, and final clarity-stress-test result\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "Use [references/input-resolution.md](references/input-resolution.md) and build an input ledger covering common contract fields plus the selected profile's fields from [references/profile-inputs.md](references/profile-inputs.md).\n",
    "Use [references/input-resolution.md](references/input-resolution.md), [references/question-quality.md](references/question-quality.md), and build an input ledger covering common contract fields plus the selected profile's fields from [references/profile-inputs.md](references/profile-inputs.md).\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "3. Recommend one answer and explain the trade-off.\n4. Save the exact question before sending it.\n5. Ask only that question.\n6. End the turn immediately.\n",
    "3. Recommend one answer and explain the trade-off.\n"
    "4. State what materially changes based on the answer.\n"
    "5. Ensure the question is atomic rather than bundling independent choices.\n"
    "6. Save the exact question before sending it.\n"
    "7. Ask only that question.\n"
    "8. End the turn immediately.\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "3. Normalize the answer into a contract decision.\n4. Record the contract sections affected and any superseded decision.\n5. Continue resolving the ledger.\n",
    "3. Run the answer quality gate: Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.\n"
    "4. Normalize only the meaning the user actually supplied; ask a targeted follow-up when multiple material interpretations remain.\n"
    "5. Record the contract sections affected, confidence, assumptions, and any superseded decision.\n"
    "6. Continue resolving the ledger.\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "## 4. Run standard or deeper shaping rounds\n\n### Standard round\n",
    "## 4. Run adaptive, standard, deeper, or stress-test shaping rounds\n\n"
    "### Adaptive depth — default\n\n"
    "There is no target question count. Score unresolved items by impact, uncertainty, irreversibility, and confidence; ask the highest-risk decision first and continue until the clarity gate in [references/question-quality.md](references/question-quality.md) passes. Escalate automatically to Thorough or Exhaustive depth for high-risk, subjective, cross-cutting, weakly verified, or irreversible goals.\n\n"
    "### Standard round\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "At round close, append new decisions, contract revisions, remaining uncertainty, readiness, and the recommended next step. Then ask one disposition question and end the turn:\n",
    "### Stress-test round\n\n"
    "Run when the user asks for zero ambiguity, requests a challenge pass, or the contract is high-risk or subjective. Apply the fresh-reader, counterexample, scenario, verifier, contradiction, traceability, assumption, and plain-English teach-back checks from [references/question-quality.md](references/question-quality.md). Turn each material ambiguity into one saved question; do not merely rewrite the contract from your own interpretation.\n\n"
    "At round close, append new decisions, contract revisions, remaining uncertainty, shaping depth, assumption status, clarity-test findings, readiness, and the recommended next step. Then ask one disposition question and end the turn:\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "- Every material input-ledger row is resolved\n",
    "- Every material input-ledger row is resolved\n"
    "- Every material answer passes the answer quality gate\n"
    "- No High- or Medium-impact assumption remains unresolved\n"
    "- Every applicable clarity-matrix row is resolved or marked Not applicable with a reason\n"
    "- A fresh-reader and counterexample review reveals no blocking alternate interpretation\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "Input ledger:\nPortfolio:\n",
    "Input ledger:\nShaping depth / clarity review:\nAssumption register:\nPortfolio:\n",
)

replace_once(
    "skills/goal-engine/SKILL.md",
    "- Material goal drift stops execution as **Approval required** and returns to interactive `shape-goal`; prior decisions remain immutable.\n",
    "- Material goal drift stops execution as **Approval required** and returns to interactive `shape-goal`; prior decisions remain immutable.\n"
    "- If contract wording admits more than one material interpretation during execution, stop as **Approval required** rather than choosing the easiest interpretation.\n",
)

replace_once(
    "skills/shape-goal/agents/openai.yaml",
    '  default_prompt: "Inspect this repository, resolve facts before asking, ask one material owner decision at a time, save the question and answer, end the turn after each question, and produce an explicitly approved Goal Contract plus the exact execution /goal command. Do not start autonomous execution."\n',
    '  default_prompt: "Inspect this repository, resolve facts before asking, adapt the number of one-decision questions to risk and ambiguity, save each question and answer, end the turn after each question, clarify partial or ambiguous replies instead of guessing, stress-test the draft with an assumption register and fresh-reader review, and produce an explicitly approved Goal Contract plus the exact execution /goal command. Do not start autonomous execution."\n',
)

replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "Read [shaping-history.md](shaping-history.md) before asking any user question.\n",
    "Read [shaping-history.md](shaping-history.md) and [question-quality.md](question-quality.md) before asking any user question.\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "| Input | Status | Evidence, decision, or question source |\n|---|---|---|\n| Outcome | Unresolved / Evidence / Safe default / Owner decision | Source or `R1-Q1` |\n| Scope and exclusions | ... | ... |\n| Acceptance evidence | ... | ... |\n| Protected behavior | ... | ... |\n| Authority boundaries | ... | ... |\n| Profile-specific inputs | ... | ... |\n",
    "| Input | Status | Impact | Confidence | Assumption class | Evidence, decision, or question source |\n"
    "|---|---|---|---|---|---|\n"
    "| Outcome | Unresolved / Evidence / Safe default / Owner decision / N/A | High | Unknown | Unresolved | Source or `R1-Q1` |\n"
    "| Users and journey boundary | ... | ... | ... | ... | ... |\n"
    "| Scope and exclusions | ... | ... | ... | ... | ... |\n"
    "| Acceptance evidence | ... | ... | ... | ... | ... |\n"
    "| Protected behavior | ... | ... | ... | ... | ... |\n"
    "| Failure and edge cases | ... | ... | ... | ... | ... |\n"
    "| Data, compatibility, and dependencies | ... | ... | ... | ... | ... |\n"
    "| Authority boundaries | ... | ... | ... | ... | ... |\n"
    "| Ownership and reusable outputs | ... | ... | ... | ... | ... |\n"
    "| Profile-specific inputs | ... | ... | ... | ... | ... |\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "Do not persist an approved contract while a material row remains unresolved. Link every owner-decision row to its saved question-and-answer ID.\n",
    "Do not persist an approved contract while a material row remains unresolved. Link every owner-decision row to its saved question-and-answer ID. Resolve every applicable lens from the universal clarity matrix in [question-quality.md](question-quality.md); `Not applicable` requires a reason.\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "Never default:\n",
    "Record every assumption as Evidence-backed, Owner-approved, Safe reversible default, or Unresolved. Surface safe defaults before approval; High- and Medium-impact unresolved assumptions block readiness.\n\nNever default:\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "2. State the unresolved decision.\n3. Summarize the relevant evidence and conflict.\n4. Present no more than three materially different options.\n5. Recommend one option and explain the trade-off.\n6. Save the exact proposed question in `SHAPING.md`.\n7. Ask one direct question.\n8. **End the turn immediately.** Do not call tools, continue research, ask another question, or begin background work.\n",
    "2. State the unresolved atomic decision and its impact.\n"
    "3. Summarize the relevant evidence and conflict.\n"
    "4. Present no more than three materially different options.\n"
    "5. Recommend one option, explain the trade-off, and state what changes based on the answer.\n"
    "6. Save the exact proposed question in `SHAPING.md`.\n"
    "7. Ask one direct question.\n"
    "8. **End the turn immediately.** Do not call tools, continue research, ask another question, or begin background work.\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "3. Record the normalized decision, contract impact, and any superseded answer.\n4. Update the input ledger and contract draft.\n5. Continue only after the answer is safely persisted.\n",
    "3. Classify answer quality as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.\n"
    "4. Record only the faithful normalized decision, contract impact, confidence, assumption class, and any superseded answer.\n"
    "5. When more than one material interpretation remains, save and ask one targeted clarification; never choose silently.\n"
    "6. Update the input ledger and contract draft.\n"
    "7. Continue only after the answer is safely persisted.\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "## Standard and deeper rounds\n\nThe first round resolves the minimum material decisions required for readiness.\n",
    "## Adaptive, standard, deeper, and stress-test rounds\n\n"
    "There is no minimum or maximum question count. Use Adaptive depth by default and escalate to Thorough or Exhaustive when impact, uncertainty, irreversibility, subjective judgment, or weak evidence requires it. The first round resolves the material decisions required for readiness—not an arbitrary quota.\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "The user may request repeated rounds. Each round must add decision value; repeated questions without new evidence count as no progress.\n",
    "The user may request repeated rounds. Each round must add decision value; repeated questions without new evidence count as no progress. A **stress-test round** challenges the current draft with fresh-reader, counterexample, scenario, verifier, contradiction, traceability, assumption, and plain-English teach-back checks.\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "- Recommended disposition\n",
    "- Selected shaping depth and recommended disposition\n"
    "- Assumption register and clarity-stress-test result\n",
)
replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "Before approval, surface a compact review of outcome, scope, exclusions, evidence, protected behavior, profile, overlays, authority, budget, stop conditions, state paths, and approval round.\n",
    "Before approval, surface a compact plain-English teach-back of outcome, scope, exclusions, evidence, protected behavior, profile, overlays, authority, budget, stop conditions, state paths, shaping depth, assumptions, clarity-test findings, and approval round.\n",
)

replace_once(
    "skills/shape-goal/references/shaping-history.md",
    "- Decision lens and unresolved issue\n",
    "- Decision lens, materiality, uncertainty, irreversibility, and unresolved issue\n",
)
replace_once(
    "skills/shape-goal/references/shaping-history.md",
    "- Normalized decision used by the contract\n- Contract sections affected\n- Status: Proposed, Answered, Deferred, Declined, or Superseded\n",
    "- Answer-quality classification and interpretation confirmation\n"
    "- Normalized decision used by the contract\n"
    "- Confidence and assumption classification\n"
    "- Contract sections affected\n"
    "- Status: Proposed, Answered, Needs clarification, Conflicting, Deferred, Declined, or Superseded\n",
)
replace_once(
    "skills/shape-goal/references/shaping-history.md",
    "## Standard and deepening rounds\n",
    "## Adaptive, standard, deepening, and stress-test rounds\n",
)
replace_once(
    "skills/shape-goal/references/shaping-history.md",
    "A round is a sequence of one-question interactive turns, not a large questionnaire or a background loop.\n",
    "A round is a sequence of one-question interactive turns, not a large questionnaire or a background loop. There is no target question count: the round continues until its material clarity gaps are resolved or explicitly blocked.\n\n"
    "### Stress-test round\n\n"
    "Use a stress-test round when the user requests zero ambiguity or the contract is high-risk, subjective, or easy to misread. Record fresh-reader, counterexample, scenario, verifier, contradiction, traceability, assumption, and plain-English teach-back findings. Every material finding becomes a new saved question rather than an agent-invented correction.\n",
)
replace_once(
    "skills/shape-goal/references/shaping-history.md",
    "Approval is itself recorded as a question and answer. Do not begin production execution until the contract references the approval round.\n",
    "Approval is itself recorded as a question and answer. Do not begin production execution until the contract references the approval round and the clarity gate records no blocking ambiguity or unresolved High-/Medium-impact assumption.\n",
)

replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "**Approval round:** [ROUND ID OR NONE]  \n",
    "**Approval round:** [ROUND ID OR NONE]  \n"
    "**Shaping depth:** Adaptive / Thorough / Exhaustive  \n"
    "**Clarity gate:** Not run / Needs clarification / Pass  \n",
)
replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "| Decision | Current answer | Source | Contract impact | Status |\n|---|---|---|---|---|\n| [DECISION] | [NORMALIZED ANSWER] | [R1-Q1] | [SECTIONS] | Current / Superseded / Deferred |\n",
    "| Decision | Current answer | Impact | Confidence | Assumption class | Source | Contract impact | Status |\n"
    "|---|---|---|---|---|---|---|---|\n"
    "| [DECISION] | [NORMALIZED ANSWER] | High / Medium / Low | Confirmed / Strong / Tentative / Unknown | Evidence / Owner / Safe default / Unresolved | [R1-Q1] | [SECTIONS] | Current / Superseded / Deferred |\n",
)
replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "- **Why this was asked:** [MATERIAL UNCERTAINTY]\n",
    "- **Materiality:** High / Medium / Low; **uncertainty:** High / Medium / Low; **irreversibility:** High / Medium / Low\n"
    "- **Why this was asked:** [MATERIAL UNCERTAINTY]\n",
)
replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "- **Normalized decision:** [DECISION USED BY THE CONTRACT]\n- **Contract impact:** [TARGET / SCOPE / EVIDENCE / PROTECTION / AUTHORITY / EXIT / OTHER]\n",
    "- **Answer quality:** Clear / Clear with conditions / Partial / Ambiguous / Conflicting / Deferred / Blocked\n"
    "- **Interpretation confirmed:** [YES / NO / FOLLOW-UP QUESTION ID]\n"
    "- **Normalized decision:** [DECISION USED BY THE CONTRACT]\n"
    "- **Confidence / assumption class:** [CONFIDENCE + EVIDENCE / OWNER / SAFE DEFAULT / UNRESOLVED]\n"
    "- **Contract impact:** [TARGET / SCOPE / EVIDENCE / PROTECTION / AUTHORITY / EXIT / OTHER]\n",
)
replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "- **Readiness:** Ready for approval / Deeper shaping recommended / Blocked / Paused\n",
    "- **Readiness:** Ready for clarity stress test / Ready for approval / Deeper shaping recommended / Blocked / Paused\n"
    "- **Assumptions:** [REGISTER SUMMARY]\n"
    "- **Clarity findings:** [FRESH-READER / COUNTEREXAMPLE / SCENARIO / VERIFIER / CONTRADICTION / TRACEABILITY]\n",
)
replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "## Approval record\n",
    "## Clarity audit\n\n"
    "| Check | Result | Evidence or follow-up |\n"
    "|---|---|---|\n"
    "| Universal clarity matrix | Pass / Needs clarification | [ROWS / QUESTION IDS] |\n"
    "| Assumption register | Pass / Needs clarification | [SUMMARY] |\n"
    "| Fresh-reader test | Pass / Needs clarification | [REVIEW] |\n"
    "| Counterexample test | Pass / Needs clarification | [LOOPHOLE OR NONE] |\n"
    "| Scenario and verifier test | Pass / Needs clarification | [HAPPY / FAILURE / REGRESSION] |\n"
    "| Plain-English teach-back | Confirmed / Corrected | [QUESTION ID] |\n\n"
    "## Approval record\n",
)

replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "**Approval shaping round:** [ROUND ID OR NONE]  \n",
    "**Approval shaping round:** [ROUND ID OR NONE]  \n"
    "**Shaping depth:** Adaptive / Thorough / Exhaustive  \n"
    "**Clarity gate:** Not run / Needs clarification / Pass  \n",
)
replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "| Input | Resolution | Evidence or approved decision source |\n|---|---|---|\n| Outcome | Evidence / Safe default / Owner decision | [SOURCE OR QUESTION ID] |\n| Scope and exclusions | ... | ... |\n| Acceptance evidence | ... | ... |\n| Protected behavior | ... | ... |\n| Authority boundaries | ... | ... |\n| Profile-specific inputs | ... | ... |\n",
    "| Input | Resolution | Impact | Confidence | Assumption class | Evidence or approved decision source |\n"
    "|---|---|---|---|---|---|\n"
    "| Outcome | Evidence / Safe default / Owner decision / N/A | High | Confirmed / Strong / Tentative / Unknown | Evidence / Owner / Safe default / Unresolved | [SOURCE OR QUESTION ID] |\n"
    "| Users and journey boundary | ... | ... | ... | ... | ... |\n"
    "| Scope and exclusions | ... | ... | ... | ... | ... |\n"
    "| Acceptance evidence | ... | ... | ... | ... | ... |\n"
    "| Protected behavior | ... | ... | ... | ... | ... |\n"
    "| Failure and edge cases | ... | ... | ... | ... | ... |\n"
    "| Data, compatibility, and dependencies | ... | ... | ... | ... | ... |\n"
    "| Authority boundaries | ... | ... | ... | ... | ... |\n"
    "| Ownership and reusable outputs | ... | ... | ... | ... | ... |\n"
    "| Profile-specific inputs | ... | ... | ... | ... | ... |\n",
)
replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "Every material row must be resolved before approval. Searchable repository facts are not user questions.\n",
    "Every material row must be resolved before approval. Searchable repository facts are not user questions. Every applicable universal clarity lens must be resolved or marked Not applicable with a reason.\n\n"
    "## Assumptions and interpretation register\n\n"
    "| ID | Assumption or term | Class | Impact | Evidence / approval | Treatment |\n"
    "|---|---|---|---|---|---|\n"
    "| AS1 | [ASSUMPTION OR AMBIGUOUS TERM] | Evidence-backed / Owner-approved / Safe default / Unresolved | High / Medium / Low | [SOURCE OR QUESTION ID] | Keep / Clarify / Exclude / Block |\n\n"
    "No High- or Medium-impact unresolved assumption may remain. Operationally define subjective terms and surface every safe default before approval.\n",
)
replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "## Protected behavior\n",
    "## Clarity stress test\n\n"
    "| Check | Result | Evidence or decision source |\n"
    "|---|---|---|\n"
    "| Fresh-reader review | Pass / Needs clarification | [REVIEW / QUESTION IDS] |\n"
    "| Counterexample loophole | Closed / Open | [RESULT] |\n"
    "| Happy, failure, and regression scenarios | Pass / N/A / Needs clarification | [SCENARIOS] |\n"
    "| Verifier executability | Pass / Needs clarification | [COMMANDS / ARTIFACTS] |\n"
    "| Contradiction and traceability review | Pass / Needs clarification | [SOURCES] |\n"
    "| Plain-English teach-back | Confirmed / Corrected | [QUESTION ID] |\n\n"
    "## Protected behavior\n",
)
replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "## Revision and approval record\n",
    "## Pre-approval clarity gate\n\n"
    "- [ ] No High- or Medium-impact input or assumption is unresolved.\n"
    "- [ ] Every answer has one material interpretation or a saved clarification.\n"
    "- [ ] Every subjective term has a verifier, rubric, example, reference, or qualified reviewer.\n"
    "- [ ] Fresh-reader and counterexample checks reveal no blocking ambiguity.\n"
    "- [ ] Safe defaults and residual low-impact assumptions are visible in the teach-back.\n"
    "- [ ] The user explicitly approved the plain-English interpretation.\n\n"
    "## Revision and approval record\n",
)

replace_once(
    "skills/shape-goal/references/profile-inputs.md",
    "- Primary profile, assurance overlays, and project-harness sources\n",
    "- Primary profile, assurance overlays, and project-harness sources\n"
    "- Adaptive shaping depth, universal clarity-matrix coverage, answer-quality status, and assumption register\n"
    "- Fresh-reader, counterexample, scenario, verifier, contradiction, traceability, and plain-English teach-back results before approval\n",
)

replace_once(
    "README.md",
    "![Version](https://img.shields.io/badge/version-0.8.0-7C3AED?style=flat-square)",
    "![Version](https://img.shields.io/badge/version-0.9.0-7C3AED?style=flat-square)",
)
replace_once(
    "README.md",
    "After each question, it ends the turn. Your next normal message is the answer—**no Steer message required**.\n",
    "After each question, it ends the turn. Your next normal message is the answer—**no Steer message required**.\n\n"
    "> [!TIP]\n"
    "> **There is no target question count.** It may ask two questions or twenty. It stops only when the draft has one material interpretation, no hidden high-impact assumption, and verifiable completion evidence.\n",
)
replace_once(
    "README.md",
    "Need more depth?\n\n| Claude Code | Codex CLI / IDE |\n|---|---|\n| `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |\n\nEarlier answers stay intact. Each new round asks only materially new questions.\n",
    "Need more depth or a stronger challenge?\n\n"
    "| Need | Claude Code | Codex CLI / IDE |\n"
    "|---|---|---|\n"
    "| Explore new lenses | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |\n"
    "| Challenge ambiguity | `/shape-goal Stress-test the current goal` | `$shape-goal Stress-test the current goal` |\n\n"
    "Earlier answers stay intact. Deepening explores new decisions; stress-testing looks for ambiguous wording, hidden assumptions, weak proof, and alternate interpretations.\n",
)

replace_once(
    "QUICK_REFERENCE.md",
    "| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |\n",
    "| Go deeper | `/shape-goal Deepen the current goal` | `$shape-goal Deepen the current goal` |\n"
    "| Stress-test clarity | `/shape-goal Stress-test the current goal` | `$shape-goal Stress-test the current goal` |\n",
)
replace_once(
    "QUICK_REFERENCE.md",
    "4. it saves the answer and continues\n5. you approve or request a deeper round\n6. it returns the exact /goal command\n7. goal-engine executes autonomously\n8. evidence, closeout, and reusable learning are archived\n",
    "4. it saves the answer and checks whether it has one clear interpretation\n"
    "5. it asks as many non-duplicate questions as the risk and ambiguity require\n"
    "6. it stress-tests assumptions, scenarios, wording, and acceptance evidence\n"
    "7. you approve, deepen, stress-test, or pause\n"
    "8. it returns the exact /goal command\n"
    "9. goal-engine executes autonomously\n"
    "10. evidence, closeout, and reusable learning are archived\n",
)
replace_once(
    "QUICK_REFERENCE.md",
    "## If shaping is trapped inside `/goal`\n",
    "## How many questions?\n\n"
    "There is no fixed number. Two questions are enough when the repository already resolves everything else. Many more are correct when choices are high-impact, subjective, conflicting, or irreversible. Approval waits until no material ambiguity or hidden High-/Medium-impact assumption remains.\n\n"
    "An ambiguous or partial reply triggers one targeted clarification; the agent must not guess.\n\n"
    "## If shaping is trapped inside `/goal`\n",
)

replace_once(
    "SKILLS_AND_GOALS.md",
    "  - asks one owner decision\n  - saves the answer\n",
    "  - asks one owner decision\n  - adapts question depth to risk\n  - validates the answer's meaning\n  - saves the answer\n",
)
replace_once(
    "SKILLS_AND_GOALS.md",
    "- [`input-resolution.md`](skills/shape-goal/references/input-resolution.md)\n",
    "- [`input-resolution.md`](skills/shape-goal/references/input-resolution.md)\n"
    "- [`question-quality.md`](skills/shape-goal/references/question-quality.md)\n",
)
replace_once(
    "SKILLS_AND_GOALS.md",
    "It creates an input ledger, searches authoritative evidence, applies only safe reversible defaults, classifies repository visibility, and asks one unresolved material decision at a time with a recommendation.\n",
    "It creates a risk-weighted input ledger and assumption register, searches authoritative evidence, applies only safe reversible defaults, classifies repository visibility, and asks one unresolved material decision at a time with a recommendation. The number of questions is adaptive: the skill stops only after its answer-quality and clarity gates pass.\n",
)
replace_once(
    "SKILLS_AND_GOALS.md",
    "No tool calls or background activity occur after a shaping question is asked.\n",
    "No tool calls or background activity occur after a shaping question is asked. Before approval, the draft receives fresh-reader, counterexample, scenario, verifier, contradiction, traceability, and plain-English teach-back checks.\n",
)

CURRENT_IMPLEMENTATION = r'''# Current Implementation

[`FULL_REPORT.md`](FULL_REPORT.md) is the historical research foundation. The live implementation is an interactive-first workflow for shaping and then autonomously executing software goals.

## Version `0.9.0`

```text
shape-goal                    main interactive entry point
adaptive question depth       two questions or twenty, based on material ambiguity
answer quality gate           ambiguous or partial replies are clarified, never guessed
clarity stress test           fresh-reader, counterexample, scenario, and verifier review
assumption register           evidence, owner approval, safe defaults, or unresolved
31 execution profiles         reusable loop shapes
12 assurance overlays         extra proof when a concern is secondary
goal-engine                   autonomous brownfield execution
SHAPING.md                    durable questions and answers
Goal Contract                 approved definition of done
Project Harness               reusable project mechanics
Goal Portfolio                multiple goals over time
```

## Primary workflow

```text
shape-goal outside /goal
→ inspect repository evidence
→ score unresolved decisions by impact, uncertainty, and irreversibility
→ ask one atomic material question
→ save and quality-check the answer, then stop the turn
→ repeat, deepen, or stress-test until no material ambiguity remains
→ plain-English teach-back and explicit approval
→ return an exact /goal command
→ goal-engine executes autonomously
→ verify, close out, archive, and reuse
```

The **question barrier** means that `shape-goal` asks once and ends the turn. It never forces the user to steer an active autonomous loop merely to answer.

There is no question quota. A low-risk goal may require two owner decisions; a high-risk, subjective, or irreversible goal may require many more. Approval is blocked while any High- or Medium-impact input or assumption remains unresolved.

## Clarity gate

Before approval, `shape-goal` requires:

- One material interpretation for every answer
- A resolved universal clarity matrix and profile-specific input ledger
- No hidden High-/Medium-impact assumptions
- Operational definitions for subjective terms
- Observable acceptance evidence
- Fresh-reader and counterexample checks with no blocking alternate interpretation
- Scenario, verifier, contradiction, traceability, and plain-English teach-back review as applicable

## Advanced preflight

Each canonical profile contains skill-backed and self-contained `/goal` preflights for environments where an already-approved artifact resolves every owner decision. At the first missing decision they save one recommended question and stop as **Approval required**.

## Coverage

### Core

Continuation, requirements compliance, milestone delivery, audit/remediation, QA/UAT, safe refactoring, and release readiness.

### Specialist

Incident recovery, upgrades, data migration, branch rescue, optimization, feasibility, AI/LLM evaluation, legacy sunset, and codebase onboarding/knowledge recovery.

### Product and quality

Frontend UI/UX/accessibility, documentation, security/privacy, reliability/resilience, API compatibility, observability/operability, developer experience, data quality, test/CI health, infrastructure/deployment readiness, audit readiness, internationalization/localization, backup/restore/disaster recovery, product analytics/experimentation integrity, and search/SEO/web discoverability.

Custom Contract-Driven remains the fallback for unusual loops.

## Safety and reuse

- Facts are discovered before users are questioned.
- One atomic material owner decision is asked per turn.
- The question count adapts to risk rather than a fixed quota.
- Safe questions, answers, corrections, assumptions, and approvals are append-only.
- Ambiguous, partial, or conflicting answers trigger clarification rather than inference.
- Production execution begins only from an explicitly approved, clarity-tested contract.
- Autonomous execution never interviews the user, chooses among ambiguous interpretations, or expands authority.
- Profiles and overlays cannot weaken the contract.
- Reusable knowledge is promoted into tests, ADRs, documentation, runbooks, fixtures, evals, locale/crawl matrices, architecture maps, scripts, benchmarks, design references, and the Project Harness.

## Verification

CI validates the 31-profile catalog, 12 recognized overlays, interactive starts, advanced preflight stop behavior, the 4,000-character native-goal limit, profile input coverage, adaptive-questioning references, shaping-history rules, generated docs, README guidance, skill metadata, links, package discovery, and deterministic ZIP builds.
'''
write("CURRENT_IMPLEMENTATION.md", CURRENT_IMPLEMENTATION)

replace_once(
    "ROADMAP.md",
    "## Implemented through `0.8.0`\n",
    "## Implemented through `0.9.0`\n",
)
replace_once(
    "ROADMAP.md",
    "- A strict question barrier: save one question, ask it, and return control immediately.\n",
    "- A strict question barrier: save one question, ask it, and return control immediately.\n"
    "- Adaptive question depth with no fixed quota, an answer-quality gate, a risk-weighted assumption register, and a pre-approval clarity stress test.\n",
)
replace_once(
    "ROADMAP.md",
    "- Run the comparable flow through Claude Code.\n",
    "- Run the comparable flow through Claude Code.\n"
    "- Field-test adaptive questioning with a two-question low-risk goal and a many-question high-risk goal; verify that ambiguous answers trigger clarification rather than inference.\n"
    "- Field-test the fresh-reader, counterexample, scenario, and plain-English teach-back gates with a subjective UI goal and an irreversible migration goal.\n",
)

CHANGELOG_ENTRY = r'''## [0.9.0] - 2026-08-26

### Added

- Adaptive shaping depth: question count is determined by material ambiguity and risk rather than a fixed minimum or maximum.
- A universal clarity matrix covering outcome, users and journey, scope, evidence, protected behavior, failure cases, data/compatibility, quality obligations, authority, ownership, and profile-specific inputs.
- An answer-quality gate that classifies replies as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.
- A risk-weighted assumption register and explicit prohibition on hidden High-/Medium-impact assumptions at approval.
- A clarity stress test with fresh-reader, counterexample, scenario, verifier, contradiction, traceability, and plain-English teach-back checks.
- A `Stress-test the current goal` command for users who want another challenge pass without losing prior questions or answers.
- Durable dogfood records under `docs/goals/2026-08-26-adaptive-question-clarity/`.

### Changed

- `shape-goal` now asks as few or as many atomic, non-duplicate questions as needed to produce one shared executable interpretation.
- Partial, ambiguous, conditional, or conflicting answers are clarified rather than silently normalized into agent assumptions.
- Goal Contracts and shaping histories now record shaping depth, materiality, confidence, assumption class, answer quality, interpretation confirmation, and clarity-review evidence.
- `goal-engine` stops as Approval required when approved contract wording later admits multiple material interpretations.
- README, quick reference, architecture, current implementation, roadmap, host metadata, validation, and packaged skills now describe and enforce the stronger clarity model.

'''
replace_once(
    "CHANGELOG.md",
    "## [0.8.0] - 2026-08-26\n",
    CHANGELOG_ENTRY + "## [0.8.0] - 2026-08-26\n",
)

# Dogfood records for this change.
write(
    "docs/goals/2026-08-26-adaptive-question-clarity/SHAPING.md",
    r'''# Shaping History: Adaptive question clarity

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
''',
)
write(
    "docs/goals/2026-08-26-adaptive-question-clarity/CONTRACT.md",
    r'''# Goal Contract: Adaptive question clarity

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
''',
)
write(
    "docs/goals/2026-08-26-adaptive-question-clarity/PROGRESS.md",
    r'''# Goal Progress: Adaptive question clarity

**Goal ID:** `2026-08-26-adaptive-question-clarity`  
**Contract revision:** 1  
**State:** Active  
**Branch:** `codex/adaptive-question-clarity`  
**Completed / approval shaping rounds:** R1 / R1

## Verified findings

- The current workflow correctly searches before asking and preserves one-question turns.
- Question count was implicitly “minimum material decisions,” but there was no explicit adaptive-depth rule.
- Ambiguous or partial user replies could be normalized without a formal answer-quality classification.
- Input ledgers did not record impact, confidence, irreversibility, or assumption class.
- Approval did not require a fresh-reader or counterexample test.

## Acceptance ledger

| Item | Status |
|---|---|
| Adaptive question-depth protocol | In progress |
| Answer-quality and assumption gates | In progress |
| Fresh-reader clarity stress test | In progress |
| Templates and documentation | In progress |
| Validator and version `0.9.0` | In progress |
| Branch and PR validation | Pending |
| Merge, closeout, and cleanup | Pending |
''',
)
write(
    "docs/goals/2026-08-26-adaptive-question-clarity/UAT.md",
    r'''# UAT: Adaptive question clarity

## Scenario 1 — Two questions are enough

Repository evidence resolves scope, tests, protected behavior, and authority. Only journey boundary and one acceptance threshold require the owner. Expected: ask exactly those two atomic questions, run the clarity review, and stop asking.

## Scenario 2 — Ambiguous answer

User replies, “support the main browsers.” Expected: classify as Ambiguous, do not guess a browser matrix, save a targeted clarification with a recommendation, and end the turn.

## Scenario 3 — Conditional answer

User says, “keep the old API only if active usage is above 2%.” Expected: record the threshold, measurement source, date/window, and removal trigger before resolving the decision.

## Scenario 4 — High-risk migration

A destructive schema migration has weak rollback evidence and several compatibility consumers. Expected: escalate to Exhaustive depth, ask as many non-duplicate questions as necessary, and block approval while any High-/Medium-impact assumption is unresolved.

## Scenario 5 — Fresh-reader loophole

The draft says “production-ready.” A fresh reviewer can interpret this several ways. Expected: convert the ambiguity into measurable release, reliability, security, operational, and rollback evidence or a targeted owner question.

## Scenario 6 — Counterexample

A result can technically pass tests while omitting an important error journey. Expected: the counterexample and scenario tests expose the loophole, add the missing acceptance evidence, and preserve the regression boundary.

## Scenario 7 — Conflicting answer

A new answer conflicts with an earlier approved compatibility decision. Expected: classify as Conflicting, show both sources, ask which decision supersedes the other, and append rather than rewrite history.

## Scenario 8 — Safe default

A low-impact formatting choice follows a stable repository convention and is reversible. Expected: use a safe default, record its rationale and impact, and surface it in the approval teach-back without asking unnecessarily.
''',
)

# Validator upgrades.
replace_once(
    "scripts/validate_repository.py",
    '        "skills/shape-goal/references/input-resolution.md",\n        "skills/shape-goal/references/profile-inputs.md",\n',
    '        "skills/shape-goal/references/input-resolution.md",\n        "skills/shape-goal/references/question-quality.md",\n        "skills/shape-goal/references/profile-inputs.md",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '            "Version `0.8.0`",\n',
    '            "Version `0.9.0`",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '            "no Steer message required",\n            "Pursuing goal",\n',
    '            "no Steer message required",\n            "There is no target question count",\n            "Stress-test the current goal",\n            "Pursuing goal",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '            "references/input-resolution.md",\n            "references/shaping-history.md",\n',
    '            "references/input-resolution.md",\n            "references/question-quality.md",\n            "no material ambiguity",\n            "answer quality gate",\n            "references/shaping-history.md",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '        "docs/goals/2026-08-26-final-review-readme-onboarding/UAT.md",\n',
    '        "docs/goals/2026-08-26-final-review-readme-onboarding/UAT.md",\n'
    '        "docs/goals/2026-08-26-adaptive-question-clarity/SHAPING.md",\n'
    '        "docs/goals/2026-08-26-adaptive-question-clarity/CONTRACT.md",\n'
    '        "docs/goals/2026-08-26-adaptive-question-clarity/PROGRESS.md",\n'
    '        "docs/goals/2026-08-26-adaptive-question-clarity/UAT.md",\n',
)
needle = '    require_fragments(\n        require("CURRENT_IMPLEMENTATION.md"),\n'
source = read("scripts/validate_repository.py")
if source.count(needle) != 1:
    raise RuntimeError("validator: current implementation anchor missing or duplicated")
clarity_validation = '''    require_fragments(\n        require("skills/shape-goal/references/question-quality.md"),\n        (\n            "No fixed question count",\n            "Answer quality gate",\n            "Assumption register",\n            "Fresh-reader test",\n            "Counterexample test",\n            "Plain-English teach-back",\n            "If this takes two questions",\n        ),\n    )\n'''
write("scripts/validate_repository.py", source.replace(needle, clarity_validation + needle, 1))

# Make sure templates and architecture expose the new protocol.
source = read("scripts/validate_repository.py")
needle = '    readme = require("README.md")\n'
if source.count(needle) != 1:
    raise RuntimeError("validator: README length anchor missing or duplicated")
extra = '''    require_fragments(\n        require("skills/shape-goal/goal-contract-template.md"),\n        (\n            "Assumptions and interpretation register",\n            "Clarity stress test",\n            "Pre-approval clarity gate",\n        ),\n    )\n    require_fragments(\n        require("skills/shape-goal/templates/shaping-history-template.md"),\n        (\n            "Answer quality",\n            "Clarity audit",\n            "Assumption class",\n        ),\n    )\n'''
write("scripts/validate_repository.py", source.replace(needle, extra + needle, 1))

print("Applied adaptive question clarity upgrade")
