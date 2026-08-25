# Roadmap

The repository is intentionally small. New abstractions should be added only after real use proves that they remove more friction than they create.

## Before `1.0.0`

- Run one complete brownfield cycle in a live Codex `/goal` session.
- Run the same contract shape in a live Claude Code `/goal` session.
- Compare evaluator behavior, compaction, evidence visibility, and resume quality.
- Test global install, update, reinstall, and ZIP upload paths on macOS.
- Choose an explicit repository and skill license. **Recommended:** MIT for maximum reuse with attribution.
- Create the first tagged GitHub release with packaged skill ZIPs and checksums.

## Evidence-gated candidates

### `reshape-goal`

Add only when field use shows that superseding or narrowing an active Goal Contract is common enough to deserve a dedicated workflow. Until then, rerun `shape-goal`, preserve the prior contract, and record the supersession.

### Goal-history search or summarization

Add only when several archived goals exist and manual navigation through `docs/goals/INDEX.md` becomes inconvenient.

### Per-profile skills

Do not add unless profile routing through `goal-engine` repeatedly fails. Eleven separate skills would duplicate the safety kernel and increase discovery ambiguity.

## Not planned

- A custom replacement for native `/goal`.
- A proprietary state database when repository artifacts are sufficient.
- Automatic deployment, release, destructive migration, or credential authority.
