# Goal Progress: Adversarial robustness review

**Goal ID:** `2026-08-26-adversarial-robustness`
**Contract revision:** 1
**State:** Active
**Branch:** `codex/adversarial-robustness-review`

## Verified attack surfaces

- Destructive output-directory handling
- Symlink and archive-path exfiltration
- Case and Unicode extraction collisions
- Catalog path traversal and malformed schema
- Markdown marker and replacement corruption
- Extra or malformed goal commands
- New-file, reordering, fencing, and mutation gaps in shaping history
- Write-capable workflow injection, symlinks, NUL text, and malformed input crashes
- Prompt-injection and stale-contract trust boundaries

## Next action

Run the complete adversarial suite, fix any remaining failures, review the diff, open a pull request, merge after CI, archive the result, and clean the branch.
