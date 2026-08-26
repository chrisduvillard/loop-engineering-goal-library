# Goal Contract: Adversarial robustness review

**Status:** Ready
**Goal ID:** `2026-08-26-adversarial-robustness`
**Revision:** 1
**Priority:** P0
**Primary profile:** Deep Audit + Remediation
**Shaping history:** `SHAPING.md`
**Approval shaping round:** R1

## Target

The repository rejects destructive, escaping, ambiguous, malformed, and supply-chain-dangerous states with executable evidence while preserving all approved user-facing behavior.

## Acceptance evidence

- Adversarial unit and mutation tests pass on supported Python versions and major runner operating systems.
- Existing repository validation, launcher synchronization, generated documentation, shaping-history checks, skill discovery, and deterministic packaging pass.
- Verified findings have root-cause fixes and regression tests.
- Pull-request and merged-main CI pass.
- Only `main` and the permanent validation workflow remain after closeout.

## Protected behavior

- `shape-goal` remains the interactive main command.
- One question is asked per turn and durable history remains append-only.
- All 31 profiles and 12 assurance overlays remain available.
- `goal-engine` executes only approved contracts and stops on ambiguity.
