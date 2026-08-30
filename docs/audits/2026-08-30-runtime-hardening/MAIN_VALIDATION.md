# Final clean-main validation

This permanent documentation-only commit intentionally triggers the ordinary
`Validate library` workflow after the one-time release workflow has removed
itself. The workflow therefore evaluates the final repository tree with only
normal read-only CI permissions and no temporary export, remediation, merge, or
release automation present.

The release evidence is recorded in `FINAL_VERIFICATION.md`; live authenticated
Codex and Claude Code trials remain tracked separately in
`docs/HOST_ACCEPTANCE_MATRIX.md`.
