# Specialist Reviewer Team

Use this protocol for broad, high-impact audits when one general reviewer is likely to miss cross-cutting risks. Native subagents are preferred when the host supports them; otherwise run the same reviewer briefs as isolated sequential passes.

## Review team

| Reviewer | Primary attack surface | Required output |
|---|---|---|
| **Contract & State-Machine Reviewer** | Goal lifecycle, approval, revisions, portfolios, leases, locks, stale state, and closeout | Invalid transitions, ambiguous authority, missing invariants, and durable-state gaps |
| **Agent-Control & Interaction Reviewer** | `shape-goal`, `goal-engine`, prompt injection, question boundaries, evaluator evidence, and goal drift | Reproducible ways an agent could guess, loop, broaden authority, or lose user control |
| **Security & Supply-Chain Reviewer** | Workflows, dependencies, archives, paths, symlinks, secrets, permissions, and publishing | Exploit path, impact, containment rule, and regression verifier |
| **Tooling & Portability Reviewer** | Python versions, operating systems, filesystems, encodings, CLI behavior, and deterministic output | Cross-platform failure matrix and minimal compatible remediation |
| **Verification & Mutation Reviewer** | Tests, false confidence, skipped paths, failure injection, property cases, and CI gates | Counterexample, reproduction, missing oracle, and regression test |
| **Documentation & Adoption Reviewer** | README, installation, updates, examples, terminology, generated docs, and maintenance friction | User-visible confusion, drift source, and simpler verified workflow |

Add a domain specialist when the contract involves security, regulated data, accessibility, infrastructure, migrations, financial logic, or another high-risk domain.

## Isolation rules

1. Give each reviewer the approved contract, relevant shaping decisions, repository state, and evidence, not another reviewer's conclusions.
2. Reviews are read-only by default. Do not let multiple reviewers edit the same worktree or shared resource.
3. Treat every finding as a hypothesis until reproduced or independently supported.
4. Do not let a reviewer redefine the product target, weaken acceptance evidence, or expand authority.
5. Use isolated worktrees or non-overlapping ownership when parallel remediation is justified.
6. Preserve existing user and unrelated work.

## Finding format

Every material finding must include:

```text
ID:
Reviewer:
Severity: Critical / High / Medium / Low
Confidence: Confirmed / Strong / Tentative
Affected contract item or invariant:
Evidence:
Reproduction or counterexample:
Impact:
Proposed remediation:
Regression verifier:
Disposition: Open / Accepted / Rejected with reason / Fixed
```

A scanner warning, opinion, or model assertion without evidence is not a confirmed finding.

## Lead consolidation

The lead reviewer must:

1. Deduplicate findings by root cause rather than wording.
2. Resolve disagreements with executable evidence or a clearly recorded owner decision.
3. Rank confirmed findings by severity, likelihood, blast radius, and repair cost.
4. Fix the highest-risk verified issue first with the smallest reversible change.
5. Add regression protection before marking a finding fixed.
6. Ask a fresh reviewer to independently re-check important fixes without the implementer's persuasive narrative.
7. Record residual risks and untested areas instead of claiming exhaustive proof.

## Stop condition

The specialist audit is complete only when:

- every confirmed in-scope finding above the contract's severity threshold is fixed or explicitly accepted by the authorized owner;
- repository-native and affected broader gates pass;
- important fixes receive independent re-review;
- no unexplained audit-created changes remain; and
- findings, evidence, reusable tests, and residual risks are saved in the repository.
