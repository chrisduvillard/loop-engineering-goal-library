# Goal Contract: Specialist codebase audit

**Status:** Ready
**Goal ID:** `2026-08-27-specialist-audit`
**Revision:** 1
**Priority:** P0
**Primary profile:** Deep Audit + Remediation
**Shaping history:** `SHAPING.md`
**Approval shaping round:** R1
**Library target:** `0.11.0`

## Target

Independently audit the complete repository through specialist contract/state, agent-control, security/supply-chain, portability, verification, and documentation lenses; fix every confirmed in-scope Medium-or-higher defect; add regression evidence; merge the reviewed work; and leave no temporary workflow or branch.

## Acceptance evidence

- Six specialist findings are saved and consolidated by root cause.
- Confirmed issues have minimal fixes and regression tests.
- Existing and new tests pass on all configured platforms and Python versions.
- Repository validation, generated docs, shaping-history checks, Skills CLI discovery, and deterministic packaging pass.
- Pull-request and final-main CI pass.
- Only `main` and the permanent read-only validation workflow remain.

## Protected behavior

- `shape-goal` remains the main interactive command.
- One question per turn and explicit approval remain mandatory.
- The 31 profiles and 12 overlays remain available.
- `goal-engine` never guesses a material interpretation or broadens authority.
