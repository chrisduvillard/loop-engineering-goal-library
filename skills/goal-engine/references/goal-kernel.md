# Goal Kernel

This kernel is the compact, compaction-resistant authority boundary for every
approved native goal.

1. Read the canonical contract and progress state before every serious cycle.
2. Require the recorded goal ID, revision, approval fingerprint, branch, and
   valid lease before modifying repository content.
3. Never silently change the outcome, mutation mode, scope, acceptance proof,
   protected behavior, assurance level, or authority boundaries.
4. Preserve unrelated work and classify pre-existing failures separately.
5. Run the declared verifier before marking an acceptance item `pass`.
6. Never claim `Achieved` while an acceptance item is `fail`, `blocked`, or
   `not_run`, while the verifier failed, or while protected behavior is unknown.
7. Stop with `approval_required` when a material owner decision or authority
   boundary appears. That termination remains resumable.
8. Record evidence, changed paths, remaining risks, and the next action after
   each material cycle.
9. Re-read the complete goal-engine skill after compaction, resume, or uncertain
   state. The kernel remains binding even if skill activation is lost.
