# Verification plan

The merge gate runs:

```text
python -m compileall -q scripts tests skills/goal-engine/scripts
python -m unittest discover -s tests -v
python scripts/validate_repository.py
python scripts/sync_goal_launchers.py --check
python scripts/sync_goal_docs.py --check
python scripts/validate_shaping_history_diff.py --self-test
python scripts/validate_question_state.py --self-test
python scripts/validate_goal_archives.py --self-test
python scripts/validate_tooling_contract.py --self-test
python skills/goal-engine/scripts/goalctl.py self-test
python scripts/evaluate_behavior.py --self-test
npx --no-install skills add . --list
python scripts/package_skills.py
git diff --check
```

Package tests build all three advertised ZIPs and independently verify that
every package-local Markdown reference resolves within the same archive.

The host acceptance matrix is separate because repository CI cannot prove live
Codex or Claude Code behavior, context compaction, or authenticated native-goal
execution.
