# Goal Shaping History: Zero-Friction Profile Coverage

**Goal ID:** 2026-08-25-zero-friction-profile-coverage  
**Contract:** `CONTRACT.md`  
**Lifecycle state:** Closed  
**Created:** 2026-08-25  
**Last updated:** 2026-08-26  
**Completed rounds:** R1, R2  
**Latest round:** R2  
**Approval round:** R2

## Current decision index

| Decision | Current answer | Source | Contract impact | Status |
|---|---|---|---|---|
| Launcher friction | Recommended commands must run unchanged and let skills resolve inputs | R1-D1 | Target and acceptance | Current |
| Quality coverage | Frontend, documentation, and major project-quality outcomes require direct launchers when they are primary | R1-D2 | Catalog and profiles | Current |
| Question preservation | Every question and answer must be saved in an append-only goal shaping record | R2-D1 | State and closeout | Current |
| Deeper shaping | Users may request repeated non-duplicate shaping rounds before approval or after goal drift | R2-D2 | Skill lifecycle and approval | Current |
| Branch hygiene | Merge the reviewed work to `main` and remove stale working branches | R2-D3 | Delivery and cleanup | Current |

## Round R1 — Zero-friction launchers and profile coverage

**Purpose:** Convert placeholder-based commands into copy-ready launchers and make important product-quality outcomes first-class.  
**Started / completed:** 2026-08-25  
**Lenses covered:** usability, profile coverage, approval safety, validation

### Owner directives

The repository owner explicitly required:

- A deep review of the entire repository.
- Dedicated frontend UI/UX and documentation goals plus broader project-quality coverage.
- Standalone goals linked to `shape-goal` and `goal-engine` so commands run without manual input replacement.
- Repository-first search and owner questions only when the skills cannot derive a decision.

No interactive question was needed in this round because the owner directive and repository evidence resolved the material product decisions.

### Round summary

- **New decisions:** Copy-unchanged launchers, two-skill handoff, dedicated quality profiles, stricter validation.
- **Contract revisions:** Established the zero-friction profile-coverage target.
- **Remaining uncertainty:** How to preserve the shaping interview and support users who want deeper questioning.
- **Readiness:** Ready for implementation, later amended by R2.
- **Next step:** Implement and validate the zero-friction architecture.

## Round R2 — Durable shaping history and deeper interviews

**Purpose:** Preserve all future shaping decisions and allow repeated deeper rounds without losing prior answers.  
**Started / completed:** 2026-08-26  
**Lenses covered:** decision traceability, user satisfaction, state design, closeout, branch hygiene

### Owner directives

The repository owner explicitly required:

- Save all questions and answers used to create a Goal Contract.
- Allow the user to request another batch of questions when not fully satisfied.
- Keep every earlier question and answer while going deeper.
- Merge all reviewed work to `main` and clean stale branches.

No clarification question was required. The repository already had stable Goal IDs, archive paths, contract revisions, and one-question-at-a-time behavior, so the safest extension was an append-only `SHAPING.md` with repeated round IDs and approval-round linkage.

### Evidence and recommendation

- **Evidence:** Existing contracts stored decisions but not the exact asked questions, answers, recommendations, or corrections.
- **Recommendation:** Store `docs/goals/<goal-id>/SHAPING.md` from the moment a Goal ID exists; append rounds and corrections; link the approval round from the contract; preserve the file at closeout.
- **Trade-off:** This adds one small durable artifact per goal but prevents repeated interviews, lost owner rationale, and silent answer rewrites.

### Round summary

- **New decisions:** Append-only shaping history, stable round/question IDs, deeper-round command, safe redaction, approval-round linkage, archive integration.
- **Contract revisions:** Revision 2 adds shaping history to the target and acceptance evidence.
- **Remaining uncertainty:** Live multi-turn behavior still requires field UAT in Codex and Claude Code.
- **Readiness:** Ready for approval and merge after automated validation.
- **Next step:** Validate, merge PR #4, verify `main`, delete stale branches.

## Corrections and supersessions

_None._

## Open and deferred decisions

| Decision | Status | Why unresolved | Owner / trigger | Contract treatment |
|---|---|---|---|---|
| Exact host behavior during repeated deepening rounds | Deferred | Requires live multi-turn field UAT | Pre-1.0 field tests | Tracked in roadmap; does not block repository implementation |
