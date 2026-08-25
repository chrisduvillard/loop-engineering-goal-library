# Goal History

This index points to durable closeout packets. Keep active state in the repository's existing plan/progress system or in `GOAL.md` and `GOAL_PROGRESS.md`.

| Goal ID | Closed | Outcome | Profile | Target | Result | Reusable outputs |
|---|---|---|---|---|---|---|
| [GOAL ID] | [DATE] | [OUTCOME] | [PROFILE] | [ONE-LINE TARGET] | `docs/goals/[GOAL ID]/RESULT.md` | [TESTS / DOCS / ADRS / TOOLING] |

## Archive layout

```text
docs/goals/
├── INDEX.md
└── <goal-id>/
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

Do not store secrets, credentials, private user data, raw production dumps, or unnecessarily large logs in the archive. Link to approved secure systems when evidence cannot be committed safely.
