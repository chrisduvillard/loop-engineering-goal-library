# Authenticated host UAT tracking

The deterministic repository, package, mutation, lifecycle, concurrency, and
false-completion controls are implemented and verified. The remaining pre-1.0
gate requires authenticated sessions in the native Codex and Claude Code hosts.

Required scenarios and metrics are defined in `docs/HOST_ACCEPTANCE_MATRIX.md`.
Results must record exact host versions, at least three fresh trials per
scenario, raw evidence, failures, and pass rates. This gate is deliberately not
marked complete by repository CI because CI cannot prove native model behavior,
context compaction, or authenticated goal continuation.
