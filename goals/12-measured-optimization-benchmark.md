# Measured Optimization / Benchmark

**Use when:** A measurable property such as latency, throughput, cost, memory, build time, model quality, ranking accuracy, or another stable metric must improve without regressing required behavior.

## Recommended: skill-backed

```text
/goal Follow the installed goal-engine skill to complete the approved Goal Contract in [PATH OR ISSUE]. Use the Measured Optimization / Benchmark profile. Freeze the benchmark protocol and verified baseline, test one coherent challenger at a time, keep only meaningful improvements produced under the same conditions without violating must-pass gates, and continue until the target is reached or the contract-defined experiment budget or stagnation exit applies; preserve a reusable closeout packet.
```

## Standalone fallback

```text
/goal Improve [PRIMARY METRIC] for [SCOPE] from [VERIFIED BASELINE] to [TARGET] under [FIXED BENCHMARK PROTOCOL] while preserving [MUST-PASS BEHAVIOR AND FLOORS]. First establish the actual repository state from applicable instructions, architecture, prior goals, native scripts/CI/tests, benchmarks, runtime entry points, supported environments, and Git status/diff/history; protect user, uncommitted, and unrelated work. Define and freeze the benchmark command, workload or dataset, environment, warm-up and sampling method, variance or tolerance, cost unit, comparison rule, and all must-pass gates; capture a reproducible baseline with enough samples for the metric's noise level. Then repeat: identify one evidence-backed bottleneck or hypothesis; make the smallest coherent reversible challenger; run the same benchmark and relevant repository-native checks; compare it with the current champion using the approved tolerance or significance rule; inspect trade-offs and the diff; keep it only when it materially improves the primary objective without violating any floor or introducing unexplained regressions, otherwise revert only that slice; and record results, failed approaches, reusable benchmarks, and the next hypothesis. Never change the dataset, workload, hardware, metric, thresholds, or measurement conditions merely to manufacture a win; a material protocol change requires an explicit rebaseline and contract approval. Finish only when [TARGET] is achieved reproducibly under the fixed protocol and all acceptance, regression, and assurance gates pass with surfaced evidence. Stop for a contract-defined blocker, approval boundary, exhausted [EXPERIMENT BUDGET], or two consecutive no-progress cycles. At any terminal outcome, preserve a reusable closeout packet under the repository's goal-history convention (default `docs/goals/<goal-id>/`) containing `CONTRACT.md`, final `PROGRESS.md`, and `RESULT.md`; update the history index, promote verified reusable benchmarks/tests/docs/ADRs/runbooks/fixtures/tooling, and exclude secrets, private data, raw production dumps, and unnecessarily large logs. Never deploy, purchase services, change production capacity, or cross another irreversible or external-system boundary without explicit approval.
```

**Why it works:** It uses a fixed champion-versus-challenger loop, so every retained change has comparable evidence and every rejected idea becomes reusable optimization knowledge rather than repeated guesswork.
