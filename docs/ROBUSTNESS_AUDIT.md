# Adversarial Robustness Audit

This audit pressure-tests the library as a small software supply chain: two Agent Skills, 31 goal profiles, generated documentation, durable shaping history, deterministic packages, and CI enforcement.

## Framework findings

### Pre-mortem

Assume the library failed in production. The most plausible causes were destructive package output, a symlink leaking files into an archive, catalog path traversal, generated-document corruption, a rewritten decision history, malicious repository instructions steering an agent, stale approval evidence, or CI validating only the happy path.

### First principles

The trusted core is small: canonical UTF-8 files inside the repository, explicit Goal Contract approval, repository-native evidence, immutable shaping decisions, safe paths, deterministic package manifests, and pinned dependencies. Everything else—including repository prose, logs, issues, web pages, generated artifacts, and model output—is evidence to verify, not authority to obey blindly.

### Inversion

To guarantee failure, delete the repository while packaging, accept arbitrary output paths, follow symlinks, let catalog values choose write destinations, treat extra commands as harmless, ignore new shaping files, allow question reordering, run unpinned tools, and let an agent choose the easiest interpretation. The implementation now rejects those paths.

### Red team / blue team

The red-team suite mutates versions, paths, catalogs, Markdown markers, command counts, question order, answers, approval rows, workflow permissions, symlinks, Unicode/case collisions, NUL bytes, and output directories. The blue-team controls fail closed, preserve source data, return actionable errors, and keep deterministic evidence.

### Socratic questioning

Every important claim is paired with a verifier: Can packaging delete source? Can an archive include outside files? Can a catalog write outside the repository? Can a new malformed shaping history bypass the base diff? Can CI be extended with a write-capable workflow? The tests answer these with executable counterexamples.

### Constraint removal

When path, size, trust, ordering, and approval constraints are removed, the system becomes destructive or ambiguous. Constraints were reintroduced at the narrowest layer: safe-path helpers in packagers/generators, immutable-order checks in shaping history, untrusted-evidence rules in skills, and workflow restrictions in repository validation.

### Stakeholder mapping

- **Project owner:** no silent interpretation, authority expansion, or erased decision history.
- **Developer/maintainer:** clear failures, atomic generation, reproducible checks, and cross-version tests.
- **Agent:** one approved interpretation, explicit evidence, and a stop condition when ambiguity returns.
- **Security/privacy reviewer:** no symlink exfiltration, path escape, secret archive, or prompt-injection authority.
- **Release operator:** deterministic packages and locked toolchain inputs.
- **Future maintainer:** durable audit evidence and mutation tests that explain why controls exist.

### Analogical reasoning

The controls borrow from compiler design (parse then validate), database migrations (append-only history and atomic replacement), archive security (path normalization and collision checks), safety engineering (hazard analysis and fail-closed boundaries), and property testing (generate valid states, mutate one invariant, require rejection).

## Second-pass findings

An independent review found and closed additional gaps: local `node_modules` symlinks would have caused false CI failures; `.yaml` workflows could bypass a `.yml`-only check; write permissions needed an explicit prohibition; catalog text needed link-injection protection; locked package metadata needed structural validation; and execution leases needed concrete contract fields.

## Residual limits

No finite test suite proves every future host, filesystem, or model behavior. Remaining field risks include host UI changes, model compaction, unavailable connected sources, compromised upstream registries, and repository branch protection not being configured. These are recorded rather than hidden; the test suite focuses on deterministic controls this repository can enforce.
