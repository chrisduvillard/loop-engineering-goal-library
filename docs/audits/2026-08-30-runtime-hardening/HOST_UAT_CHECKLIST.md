# Native host UAT checklist

- [ ] Run the tiny clean-repository scenario three times in current Codex.
- [ ] Run the dirty brownfield-repository scenario three times in current Codex.
- [ ] Force context compaction and verify Goal Kernel reload in current Codex.
- [ ] Repeat the same scenarios in current Claude Code.
- [ ] Exercise read-only audit, failed verifier, pause/resume, goal drift,
  destructive migration, and parallel worktree cases on both hosts.
- [ ] Record exact host versions, pass rates, raw evidence, token use, elapsed
  time, unauthorized-write rate, and false-achievement rate.
- [ ] Promote the project beyond beta only when every safety-critical cell passes.
