# Data Migration / Integrity

**Use when:** Stored data or schemas must change while preserving correctness, compatibility, recoverability, and auditability.

```text
/goal Migrate [DATA OR SCHEMA] from [SOURCE STATE] to [TARGET STATE] under [INTEGRITY AND COMPATIBILITY REQUIREMENTS]. First map the authoritative schema, readers and writers, invariants, volumes, retention/privacy constraints, migration history, backup/restore path, repository-native checks, and actual Git/database state; preserve evidence and existing data. Define pre/post reconciliation queries, dry-run behavior, idempotency, restartability, mixed-version compatibility, and rollback before any destructive step. Implement in reversible phases—expand, backfill, verify, switch, then contract where applicable. Test on representative data; compare counts, checksums, relationships, and domain invariants; exercise interruption, retry, rollback, and old/new application combinations; add regression and migration coverage; and independently review high-risk steps. Never mutate production, delete data, or cross an irreversible boundary without explicit approval. Finish only when [MIGRATION GATES] and reconciliation checks pass with surfaced evidence, rollback/recovery is verified, and no unexplained loss, duplication, or corruption remains. Stop for missing access, unclear data ownership, approval/external blocker, [BUDGET], or two no-progress cycles; record the exact resume state.
```

**Why it works:** It treats data correctness and recoverability as the product, not as secondary implementation details. Reconciliation, mixed-version testing, interruption recovery, and explicit irreversible boundaries prevent a technically successful but operationally unsafe migration.
