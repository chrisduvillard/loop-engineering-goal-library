# Remaining validation boundary

The following cannot be proven by repository CI alone:

- authenticated native Codex `/goal` continuation after forced compaction;
- authenticated Claude Code continuation and plugin discovery across supported
  host versions;
- repeated model-behavior pass rates across fresh sessions;
- production deployment behavior in a third-party target repository.

These are retained in `docs/HOST_ACCEPTANCE_MATRIX.md` as explicit beta gates.
They must be executed in the real hosts and reported with exact host versions,
trial counts, failures, and raw evidence before a 1.0 production-ready claim.
