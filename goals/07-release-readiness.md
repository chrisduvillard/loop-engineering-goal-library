# Release Readiness

**Use when:** A version or milestone must converge on all repository-defined release gates without actually publishing it.

```text
/goal Bring [VERSION OR SCOPE] to release-ready—not released—under the repository-defined release criteria. Establish the actual state and reconcile release documentation, specifications, CI, Git history and working changes, open blockers, versioning and changelog, migrations, security, reliability and performance gates, deployment assumptions, and rollback instructions; protect unrelated and uncommitted work. Turn the actual release gates into a concise checklist and capture their baseline. Work the highest-risk unblocked failure first: verify it, make the smallest reversible production fix, add regression protection, run repository-native targeted checks, then rerun clean or production-like full gates at appropriate checkpoints. Use an independent final review and verify every finding; do not hide failures, weaken gates, or expand scope. Update release, progress, and handoff artifacts. Finish only when every required gate passes with surfaced evidence, no release-blocking finding remains, artifacts, documentation, configuration, migrations, and rollback instructions are consistent, and the working tree has no unexplained changes. Do not tag, publish, deploy, merge, push, or alter production without explicit approval. Stop for an external or approval blocker, [BUDGET], or two no-progress cycles; leave a restartable release handoff.
```

**Why it works:** It distinguishes preparing a release from executing irreversible release actions. The loop converges on the repository’s real gates instead of imposing a generic checklist.
