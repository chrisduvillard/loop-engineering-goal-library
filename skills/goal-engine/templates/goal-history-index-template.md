# Goal History

This index points to immutable closeout packets. Coordinate non-closed goals in the repository's existing tracker or [`PORTFOLIO.md`](PORTFOLIO.md).

| Goal ID | Revision | Closed | Outcome | Profile | Overlays | Target | Result | Related goals | Reusable outputs |
|---|---:|---|---|---|---|---|---|---|---|
| [GOAL ID] | [REV] | [DATE] | [OUTCOME] | [PROFILE] | [OVERLAYS OR NONE] | [ONE-LINE TARGET] | `docs/goals/[GOAL ID]/RESULT.md` | [IDS OR NONE] | [TESTS / DOCS / ADRS / HARNESS / TOOLING] |

## Archive layout

```text
docs/goals/
├── PORTFOLIO.md   optional active/ready/paused coordination
├── INDEX.md       immutable closed history
└── <goal-id>/
    ├── CONTRACT.md
    ├── PROGRESS.md
    └── RESULT.md
```

Do not store secrets, credentials, private user data, raw production dumps, exploit-enabling evidence, or unnecessarily large logs. Link approved secure systems when evidence cannot be committed safely.
