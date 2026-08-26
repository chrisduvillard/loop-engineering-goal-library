# Compliance / Audit Readiness

**Use when:** A repository or system must produce implementation evidence for an approved control set without falsely self-certifying legal or regulatory compliance.

**In simple terms:** Map controls to implementation and evidence, close technical gaps, and leave an auditable package for qualified human review.

## Run unchanged — recommended

Copy this command exactly. It uses `shape-goal` to discover and approve the missing inputs, then `goal-engine` to execute the result.

```text
/goal Use the installed shape-goal and goal-engine skills to discover, approve, and complete this repository's next Compliance / Audit Readiness objective. During shaping, load shape-goal's required-input specification for Compliance / Audit Readiness; exhaustively inspect repository instructions, Git state and history, requirements, architecture, plans, tests and CI, runtime behavior, prior goal state, the project harness, and any connected authoritative sources before asking the user. Resolve every material input from evidence where possible; ask only unresolved owner decisions, one at a time with a recommended answer, and do not make production changes until the user approves a Goal Contract. Then hand off within this same goal to goal-engine to identify the authoritative control framework, map each control to code/config/process/evidence, verify gaps, remediate technical findings, and prepare reviewer-ready evidence; apply relevant assurance overlays, repository-native verification, regression protection, independent review where warranted, durable progress state, and reusable closeout. Do not declare success when shaping is complete. Finish only when every approved acceptance and overlay gate passes with surfaced evidence and protected behavior has not regressed. Stop only for a contract-defined blocker, approval boundary, budget, material goal drift, or two consecutive no-progress cycles.
```

## Inputs the skills resolve

- Approved framework/control set and scope
- Control owners and qualified approvers
- Required evidence, retention, and access rules
- Technical remediation gates and explicit non-technical/legal decisions
- Common contract inputs: outcome, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, goal relationships, state paths, and closeout paths.

**Suggested assurance overlays:** Compliance & Auditability, Security & Privacy, Documentation & Knowledge Transfer

`shape-goal` must search the repository and connected authoritative sources before asking. It asks only material unresolved decisions, one at a time with a recommendation. The active `/goal` is not complete when the contract is shaped; execution and passing evidence are still required.

## Run unchanged — self-contained fallback

Use this command when the skills are unavailable. It reproduces the same shape-then-execute gate without requiring placeholders.

```text
/goal Determine, obtain approval for, and complete this repository's next Compliance / Audit Readiness objective without requiring the user to prefill placeholders. Phase 1 — shape: establish the actual repository state from instructions, Git state/history, requirements, architecture, plans, prior goals, tests/CI, runtime behavior, and available authoritative tools or connected sources. Build an input ledger for the target, scope, exclusions, acceptance evidence, protected behavior, authority boundaries, budget, and the profile-specific inputs described in this goal. Search before asking; when a material decision cannot be derived, ask the user one question at a time, include the evidence and a recommended answer, record the decision, and continue until a concise Goal Contract is approved. Do not edit production before approval, and do not treat contract creation as completion. Phase 2 — execute: identify the authoritative control framework, map each control to code/config/process/evidence, verify gaps, remediate technical findings, and prepare reviewer-ready evidence. In particular, do not invent policy or self-certify; separate technical evidence from legal interpretation; preserve chain of evidence and approval boundaries. Make small coherent reversible changes; use repository-native checks; verify findings before fixing; add regression protection; review important diffs independently when practical; keep only changes that preserve or improve the verified baseline; and persist progress, failed approaches, evidence, reusable outputs, and the next action. Finish only when every approved acceptance and assurance item passes with surfaced evidence and protected behavior remains intact. Stop for a genuine external blocker, required approval, exhausted approved budget, material goal drift, or two consecutive no-progress cycles. At every terminal outcome, preserve a reusable closeout packet containing CONTRACT.md, final PROGRESS.md, and RESULT.md under the repository's goal-history convention, update the portfolio/history, promote durable tests/docs/ADRs/runbooks/fixtures/tooling, and never archive secrets, private data, production dumps, exploit-enabling evidence, or unnecessary large logs. Never perform destructive, deployment, release, credential, billing, or external-system actions without explicit approval.
```

**Why it works:** The user chooses only the kind of outcome. The skills or fallback derive the exact target and proof from the real repository, obtain approval for material decisions, and then keep working until the approved evidence—not agent confidence—says the goal is complete.
