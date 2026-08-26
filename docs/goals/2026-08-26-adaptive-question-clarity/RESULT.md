# Goal Result: Adaptive question clarity

**Goal ID:** `2026-08-26-adaptive-question-clarity`
**Contract revision:** 1
**Outcome:** Achieved
**Closed:** 2026-08-26
**Profile:** PRD / Spec Compliance
**Shaping history:** `SHAPING.md`
**Completed / approval shaping rounds:** R1 / R1
**Pull request:** [#9](https://github.com/chrisduvillard/loop-engineering-goal-library/pull/9)
**Merge commit:** `541f6736c604aa26bc70f99a5a6b03d1cc6df9fd`

## Delivered behavior

- `shape-goal` now uses adaptive question depth rather than a fixed question count. Two questions are enough when evidence is strong; many more are required when material ambiguity remains.
- Unresolved decisions are prioritized by impact, uncertainty, irreversibility, and confidence.
- A universal clarity matrix covers outcome, users and journey boundaries, scope, acceptance evidence, protected behavior, failure paths, data and compatibility, quality obligations, authority, ownership, and profile-specific inputs.
- Answers are classified as Clear, Clear with conditions, Partial, Ambiguous, Conflicting, Delegated judgment, or Deferred / Blocked.
- Partial, ambiguous, or conflicting replies trigger a targeted follow-up instead of an inferred decision.
- Requirement strength is preserved as Must, Should, Preference, Optional, or Explicit non-goal.
- “You decide” is treated as bounded delegation with recorded criteria and rationale rather than unrestricted authority.
- High- and Medium-impact assumptions must be evidence-backed or explicitly owner-approved before execution.
- Before approval, the contract receives fresh-reader, counterexample, scenario, verifier, contradiction, traceability, assumption, and plain-English teach-back checks.
- Users can invoke another challenge pass with `Stress-test the current goal` while retaining all prior questions and answers.
- `goal-engine` stops as Approval required when an approved contract later admits more than one material interpretation.

## Verification evidence

The review branch, pull request, and merged `main` passed:

```text
python scripts/sync_goal_launchers.py --check
python scripts/sync_goal_docs.py --check
python scripts/validate_shaping_history_diff.py --self-test --base-ref origin/main
python scripts/validate_repository.py
python scripts/package_skills.py
npx -y skills@1.5.23 add . --list
```

Verified outcomes include:

- Version `0.9.0` across both skills and repository metadata
- Both Agent Skills discovered by the real Skills CLI
- All 31 profile launchers and advanced preflights retained
- Adaptive-questioning reference, contract fields, shaping fields, and validator checks present
- Append-only shaping history preserved
- No unresolved command placeholders or oversized native-goal commands
- Generated documents synchronized and local Markdown links resolved
- Deterministic `0.9.0` ZIP packages generated
- Pull-request CI and merged-main CI completed successfully

## Protected behavior retained

- `shape-goal` remains the main interactive command.
- One question is asked per turn, then the turn ends immediately.
- The user replies normally without Steer.
- All safe questions, answers, corrections, delegations, and approvals remain durable and append-only.
- Production work starts only after explicit Goal Contract approval.
- `goal-engine` never interviews the user during autonomous execution.
- Existing 31 profiles, 12 assurance overlays, Goal Portfolio, Project Harness, closeout, and authority boundaries remain intact.

## Reusable outputs

- `skills/shape-goal/references/question-quality.md`
- Adaptive input-ledger and assumption-register rules
- Updated Goal Contract and shaping-history templates
- Stress-test command and clarity-gate workflow
- UAT scenarios for short, long, ambiguous, conditional, conflicting, delegated, and high-risk shaping
- Updated README, quick reference, architecture, implementation guide, roadmap, changelog, validation, and `0.9.0` packages

## Residual risk

The repository mechanically enforces the new protocol and documents representative scenarios. Real client behavior should still be field-tested in current Codex and Claude Code sessions, especially for long multi-question interviews, context compaction, fresh-reader subagent review, and user corrections after a decision echo.
