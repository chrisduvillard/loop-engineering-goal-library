# Audit remediation completion

Version 0.11.1 contains the permanent controls approved from the 2026-08-30
full-project audit. All temporary export, transformation, merge, recovery, and
release workflows have been removed before this commit.

This documentation-only commit triggers the repository's ordinary
`Validate library` workflow with its normal read-only permissions against the
final tree. The immutable release is rebuilt from the verified permanent commit.

The project remains labelled beta solely because the authenticated, repeated
Codex and Claude Code host matrix cannot be proven by repository CI. That
boundary is explicit in `docs/HOST_ACCEPTANCE_MATRIX.md` and is not silently
reported as complete.
