# Adversarial Robustness Audit

This review treats the library as a small control system and software supply chain: two Agent Skills, 31 goal profiles, generated documents, durable shaping history, deterministic packages, locked tooling, and CI enforcement.

## Framework findings

### Pre-mortem

Assume the library failed badly. The most credible causes were destructive package output, symlink or special-file exfiltration, catalog path traversal, generated-document corruption, silent decision-history rewriting, compromised dependency resolution, prompt injection gaining authority, stale autonomous execution, and CI that covered only one environment.

### First principles

The irreducible properties are trusted provenance, path containment, explicit schemas, deterministic transformations, append-only decisions, bounded authority, observable verification, atomic writes, and fail-closed behavior. Repository prose, logs, issues, web pages, generated artifacts, and model output are evidence to verify—not automatic instruction authority.

### Inversion

To guarantee failure, point packaging at the repository root, follow symlinks, let catalog values choose arbitrary paths, smuggle extra commands into Markdown, reorder or rewrite shaping decisions, weaken workflow permissions, corrupt the dependency lock, or let an expired contract continue. Regression tests now exercise and reject these paths.

### Red team / blue team

The red team attacks filesystems, archives, catalog input, regex boundaries, Markdown markers, shaping-history parsing, workflow permissions, package-lock integrity, prompt-injection boundaries, execution leases, and shared-resource locks. The blue team responds with safe manifests, atomic writes, fingerprints, leases, locks, immutable history, explicit validators, and cross-platform tests.

### Socratic questioning

Claims such as “deterministic,” “append-only,” “safe to package,” “read-only CI,” and “approved contract” now have executable checks. Claims that depend on future hosts or models are recorded as residual risks rather than asserted as guarantees.

### Constraint removal

The suite removes normal safety assumptions and tests repository roots, foreign output directories, malformed schemas, hostile filenames, missing base refs, case-insensitive filesystems, Unicode normalization, generated dependency directories, untrusted instructions, and all supported operating systems.

### Stakeholder mapping

- **Goal owner:** no silent interpretation, authority expansion, or erased decisions.
- **Autonomous agent:** one current approved contract, explicit evidence, and a stop condition when ambiguity returns.
- **Maintainer:** deterministic generators, atomic writes, actionable failures, and durable rationale.
- **Reviewer:** traceable acceptance evidence and immutable shaping history.
- **CI operator:** one read-only workflow, immutable action pins, and locked dependencies.
- **Package consumer:** safe archive names, reproducible bytes, and verified source parity.
- **Future contributor:** mutation tests that explain why each control exists.

### Analogical reasoning

The controls borrow from compiler pipelines, database transactions, archive-extraction hardening, append-only ledgers, software-supply-chain locks, distributed leases, and shared-resource locks. These analogies expose hazards that happy-path testing misses.

## Verified defenses

- Packaging rejects destructive targets, foreign output content, symlinks, special files, path traversal, case-folding or Unicode collisions, invalid semantic versions, corrupt members, source/ZIP divergence, unsafe modes, and nondeterministic metadata.
- Documentation generators validate exact schemas and paths, reject injection-prone text, require exactly two commands, update atomically, and fail on duplicate or reversed markers.
- Shaping-history validation checks new and existing files, ignores fenced decoys and generated directories, rejects duplicate, zero-based, reordered, inserted, removed, or rewritten decisions and approvals, and preserves only explicitly mutable status metadata.
- Repository validation rejects symlinks, NUL bytes, oversized critical files, extra workflows, `.yaml` bypasses, mutable action pins, `write` or `write-all` permissions, malformed catalogs, duplicate frontmatter keys, invalid invocation flags, and lockfile drift.
- The Skills CLI is pinned through a committed lockfile, installed with lifecycle scripts disabled, and invoked from the local locked dependency; every transitive lock entry requires HTTPS registry provenance and SHA-512 integrity.
- `shape-goal` treats repository content as evidence, not instruction authority; `goal-engine` checks approval fingerprints, execution leases, branch/SHA drift, and shared-resource locks before and during work.
- Forty-two adversarial, mutation, property, and regression tests run on Linux, macOS, and Windows with Python 3.9 and 3.13.

## Honest boundary

No finite suite proves all future model, host, filesystem, network, registry, or GitHub behavior. The implemented controls fail closed for deterministic repository-level risks and preserve external behavior as residual risk. Current Codex and Claude Code clients still require field UAT after material host changes.
