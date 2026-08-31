# Behavioral evaluation

`scripts/evaluate_behavior.py` scores recorded host runs against safety-critical
invariants. It rejects unauthorized writes in read-only and propose-patch modes,
pre-approval edits, protected-work loss, false completion, unhandled goal drift,
missing kernel reload after compaction, and missing independent verification for
High assurance work.

Run the deterministic evaluator self-test with:

```bash
python scripts/evaluate_behavior.py --self-test
```

Score a recorded JSON result with:

```bash
python scripts/evaluate_behavior.py path/to/result.json
```

Compare the current release, the previous release, a no-skill baseline, and any
simplified candidate. Non-deterministic host runs require repeated trials and
reported pass rates rather than a single successful demonstration.
