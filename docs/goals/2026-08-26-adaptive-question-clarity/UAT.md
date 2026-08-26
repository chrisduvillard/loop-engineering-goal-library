# UAT: Adaptive question clarity

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
