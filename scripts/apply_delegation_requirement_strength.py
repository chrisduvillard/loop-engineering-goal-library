#!/usr/bin/env python3
"""Refine answer handling for delegated judgment and requirement strength."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    source = read(path)
    if source.count(old) != 1:
        raise RuntimeError(f"{path}: expected exactly one match: {old[:90]!r}")
    write(path, source.replace(old, new, 1))


replace_once(
    "skills/shape-goal/references/question-quality.md",
    "7. Can be answered without the user researching repository facts.\n\nSplit compound questions. Do not hide two independent choices behind “and.”\n",
    "7. Can be answered without the user researching repository facts.\n"
    "8. Makes clear that listed options are not exhaustive and the user may answer in their own words.\n\n"
    "Split compound questions. Do not hide two independent choices behind “and.”\n",
)
replace_once(
    "skills/shape-goal/references/question-quality.md",
    "- **Conflicting:** contradicts repository evidence or a prior decision; surface the conflict and ask which authority wins.\n- **Deferred / Blocked:** record the owner or trigger and decide whether the goal excludes the item or cannot become ready.\n\nWhen clarification is needed, quote the shortest faithful interpretation and ask the user to confirm or correct it. Do not silently pick the interpretation that is easiest to implement.\n",
    "- **Conflicting:** contradicts repository evidence or a prior decision; surface the conflict and ask which authority wins.\n"
    "- **Delegated judgment:** the user explicitly asks the agent to decide within stated constraints; record the delegation, selected option, criteria, and rationale.\n"
    "- **Deferred / Blocked:** record the owner or trigger and decide whether the goal excludes the item or cannot become ready.\n\n"
    "When clarification is needed, quote the shortest faithful interpretation and ask the user to confirm or correct it. Do not silently pick the interpretation that is easiest to implement.\n\n"
    "Preserve requirement strength exactly: **Must / hard gate**, **Should**, **Preference**, **Optional**, or **Explicit non-goal**. Do not turn “ideally” into a mandatory acceptance gate or weaken “must” into best effort.\n\n"
    "“You decide” is a real answer only when the delegation boundary is clear. It does not authorize a different product outcome, hidden risk acceptance, destructive action, compatibility removal, legal/compliance judgment, or expanded external-system authority. Ask one boundary question when the delegated decision is still materially unconstrained.\n\n"
    "If a reply voluntarily answers several ledger rows, save each explicit decision and its strength. Do not infer unstated links between them; continue with one unresolved decision at a time.\n",
)
replace_once(
    "skills/shape-goal/references/question-quality.md",
    "- Which assumptions or safe defaults remain\n- What the agent is not authorized to do\n",
    "- Which requirements are hard gates, preferences, optional, or explicit non-goals\n"
    "- Which assumptions, safe defaults, or delegated judgments remain\n"
    "- What the agent is not authorized to do\n",
)
replace_once(
    "skills/shape-goal/references/question-quality.md",
    "- Every material answer passes the answer quality gate.\n",
    "- Every material answer passes the answer quality gate, including preserved requirement strength and bounded delegation.\n",
)

replace_once(
    "skills/shape-goal/SKILL.md",
    "3. Run the answer quality gate: Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.\n4. Normalize only the meaning the user actually supplied; ask a targeted follow-up when multiple material interpretations remain.\n5. Record the contract sections affected, confidence, assumptions, and any superseded decision.\n6. Continue resolving the ledger.\n",
    "3. Run the answer quality gate: Clear, Clear with conditions, Partial, Ambiguous, Conflicting, Delegated judgment, or Deferred / Blocked.\n"
    "4. Preserve requirement strength—Must, Should, Preference, Optional, or Explicit non-goal—and normalize only the meaning the user actually supplied.\n"
    "5. Treat “you decide” as bounded delegation, not permission to change the outcome, risk, compatibility, or authority; ask one boundary question when needed.\n"
    "6. Ask a targeted follow-up when multiple material interpretations remain.\n"
    "7. Record the contract sections affected, confidence, assumptions, delegation, and any superseded decision.\n"
    "8. Continue resolving the ledger.\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "4. On the user's next message, first save the answer, normalize the decision, update the contract impact, and then continue.\n",
    "4. On the user's next message, first save the answer, quality-check its interpretation and requirement strength, update the contract impact, and then continue.\n",
)

replace_once(
    "skills/shape-goal/references/input-resolution.md",
    "3. Classify answer quality as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, or Deferred / Blocked.\n4. Record only the faithful normalized decision, contract impact, confidence, assumption class, and any superseded answer.\n5. When more than one material interpretation remains, save and ask one targeted clarification; never choose silently.\n6. Update the input ledger and contract draft.\n7. Continue only after the answer is safely persisted.\n",
    "3. Classify answer quality as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, Delegated judgment, or Deferred / Blocked.\n"
    "4. Preserve whether each statement is a Must, Should, Preference, Optional item, or Explicit non-goal.\n"
    "5. Treat “you decide” as bounded delegation and record the chosen option, criteria, and rationale; clarify the boundary when outcome, risk, compatibility, or authority remains open.\n"
    "6. Record only the faithful normalized decision, contract impact, confidence, assumption class, delegation, and any superseded answer.\n"
    "7. When more than one material interpretation remains, save and ask one targeted clarification; never choose silently.\n"
    "8. Update the input ledger and contract draft.\n"
    "9. Continue only after the answer is safely persisted.\n",
)

replace_once(
    "skills/shape-goal/templates/shaping-history-template.md",
    "- **Answer quality:** Clear / Clear with conditions / Partial / Ambiguous / Conflicting / Deferred / Blocked\n",
    "- **Answer quality:** Clear / Clear with conditions / Partial / Ambiguous / Conflicting / Delegated judgment / Deferred / Blocked\n"
    "- **Requirement strength:** Must / Should / Preference / Optional / Explicit non-goal\n"
    "- **Delegation:** None / Bounded delegation with [CRITERIA AND LIMITS]\n",
)

replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "| ID | Assumption or term | Class | Impact | Evidence / approval | Treatment |\n|---|---|---|---|---|---|\n| AS1 | [ASSUMPTION OR AMBIGUOUS TERM] | Evidence-backed / Owner-approved / Safe default / Unresolved | High / Medium / Low | [SOURCE OR QUESTION ID] | Keep / Clarify / Exclude / Block |\n",
    "| ID | Assumption or term | Requirement strength | Class | Impact | Evidence / approval | Treatment |\n"
    "|---|---|---|---|---|---|---|\n"
    "| AS1 | [ASSUMPTION OR AMBIGUOUS TERM] | Must / Should / Preference / Optional / Non-goal | Evidence-backed / Owner-approved / Delegated / Safe default / Unresolved | High / Medium / Low | [SOURCE OR QUESTION ID] | Keep / Clarify / Exclude / Block |\n",
)
replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "- [ ] Every answer has one material interpretation or a saved clarification.\n",
    "- [ ] Every answer has one material interpretation or a saved clarification, and its requirement strength is preserved.\n"
    "- [ ] Every delegated judgment has explicit criteria and boundaries.\n",
)

replace_once(
    "skills/shape-goal/agents/openai.yaml",
    "clarify partial or ambiguous replies instead of guessing, stress-test the draft",
    "clarify partial or ambiguous replies instead of guessing, preserve must-versus-preference strength and bound delegated judgment, stress-test the draft",
)

replace_once(
    "CURRENT_IMPLEMENTATION.md",
    "answer quality gate           ambiguous or partial replies are clarified, never guessed\n",
    "answer quality gate           ambiguous or partial replies are clarified, never guessed\n"
    "requirement strength          must, should, preference, optional, or explicit non-goal\n"
    "bounded delegation            “you decide” records criteria and limits instead of blank authority\n",
)
replace_once(
    "CURRENT_IMPLEMENTATION.md",
    "- Ambiguous, partial, or conflicting answers trigger clarification rather than inference.\n",
    "- Ambiguous, partial, or conflicting answers trigger clarification rather than inference.\n"
    "- Requirement strength is preserved, and delegated judgment is explicit, bounded, and reviewable.\n",
)

replace_once(
    "README.md",
    "It stops only when the draft has one material interpretation, no hidden high-impact assumption, and verifiable completion evidence.",
    "It stops only when the draft has one material interpretation, no hidden high- or medium-impact assumption, and verifiable completion evidence. “You decide” is recorded as bounded delegation—not blank authority.",
)

replace_once(
    "QUICK_REFERENCE.md",
    "An ambiguous or partial reply triggers one targeted clarification; the agent must not guess.\n",
    "An ambiguous or partial reply triggers one targeted clarification; the agent must not guess. It also preserves Must versus Preference wording. “You decide” becomes a bounded, recorded delegation with criteria—not permission to expand the outcome or authority.\n",
)

replace_once(
    "CHANGELOG.md",
    "- A risk-weighted assumption register and explicit prohibition on hidden High-/Medium-impact assumptions at approval.\n",
    "- A risk-weighted assumption register and explicit prohibition on hidden High-/Medium-impact assumptions at approval.\n"
    "- Requirement-strength preservation for Must, Should, Preference, Optional, and Explicit non-goal statements.\n"
    "- Bounded delegated judgment: “you decide” records criteria, limits, selection, and rationale instead of becoming blank authority.\n",
)

replace_once(
    "docs/goals/2026-08-26-adaptive-question-clarity/UAT.md",
    "## Scenario 8 — Safe default\n\nA low-impact formatting choice follows a stable repository convention and is reversible. Expected: use a safe default, record its rationale and impact, and surface it in the approval teach-back without asking unnecessarily.\n",
    "## Scenario 8 — Safe default\n\nA low-impact formatting choice follows a stable repository convention and is reversible. Expected: use a safe default, record its rationale and impact, and surface it in the approval teach-back without asking unnecessarily.\n\n"
    "## Scenario 9 — Preference versus hard requirement\n\nThe user says, “I would prefer dark mode, but it is not essential.” Expected: record a Preference, not an acceptance gate, and do not claim failure if the approved goal omits it.\n\n"
    "## Scenario 10 — Delegated judgment\n\nThe user says, “You decide which library to use.” Expected: record bounded delegation within the approved outcome, compatibility, security, cost, and maintenance constraints; choose with evidence and rationale. Do not treat it as authority to change the product outcome or add an external paid service.\n",
)

replace_once(
    "scripts/validate_repository.py",
    '            "Plain-English teach-back",\n            "If this takes two questions",\n',
    '            "Plain-English teach-back",\n            "Delegated judgment",\n            "Must / hard gate",\n            "If this takes two questions",\n',
)

print("Applied delegation and requirement-strength refinement")
