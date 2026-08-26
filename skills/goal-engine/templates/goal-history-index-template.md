# Goal History

This index points to immutable closeout packets and their durable shaping histories. Coordinate non-closed goals in the repository's existing tracker or `docs/goals/PORTFOLIO.md`.

| Goal ID | Rev | Closed | Outcome | Profile | Rounds | Target | Shaping | Result | Related goals | Reusable outputs |
|---|---:|---|---|---|---|---|---|---|---|---|
| [GOAL ID] | [REV] | [DATE] | [OUTCOME] | [PROFILE] | [COUNT / APPROVAL ROUND] | [ONE-LINE TARGET] | `docs/goals/[GOAL ID]/SHAPING.md` | `docs/goals/[GOAL ID]/RESULT.md` | [IDS OR NONE] | [TESTS / DOCS / ADRS / HARNESS / TOOLING] |

## Archive layout

```text
docs/goals/
├── PORTFOLIO.md   optional active/ready/paused coordination
├── INDEX.md       immutable closed history
└── <goal-id>/
    ├── SHAPING.md
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

The shaping history is append-only and preserves every asked question and answer, including later corrections and supersessions. Do not store secrets, credentials, private user data, raw production dumps, exploit-enabling evidence, or unnecessarily large logs. Use redacted summaries and approved secure references when evidence cannot be committed safely.
