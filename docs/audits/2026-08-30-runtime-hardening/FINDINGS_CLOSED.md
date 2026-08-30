# Findings closed by 0.11.1

| Audit finding | Implemented control |
|---|---|
| Standalone packages had broken cross-skill references | Vendored transitive assets plus archive closure validation |
| Audit wording could authorize remediation accidentally | Explicit mutation mode with read-only audit default |
| Interactive shaping could be invoked implicitly | Explicit-only shaping metadata |
| Runtime state depended too heavily on prose | Canonical JSON state and `goalctl` transitions |
| Approval evidence was not canonical | Versioned SHA-256 approval fingerprint |
| Concurrent goals lacked deterministic ownership | Atomic expiring leases |
| Completion could rely on agent confidence | Verifier and acceptance-based false-completion guard |
| Compaction could lose the full skill | Compact binding Goal Kernel |
| Lifecycle and stop reasons were conflated | Separate goal status, run termination, and final outcome |
| Verification lacked behavioral scoring | Behavioral evaluator and host acceptance matrix |
| Repository had no explicit reuse license | MIT license |
| Security reporting was undefined | `SECURITY.md` and safety-critical `CODEOWNERS` |
| Distribution was not plugin-ready | Claude Code plugin metadata and combined skill bundle |

Live-host acceptance is intentionally tracked as a release gate rather than
marked closed without evidence.
