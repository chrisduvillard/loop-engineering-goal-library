# UAT: Adversarial robustness

## Packaging attacks

- Output path equals repository root or an ancestor.
- Existing output contains a user-owned file.
- Skill source contains a symlink to an outside secret.
- Archive names collide by case or Unicode normalization.
- VERSION contains traversal or non-semantic text.
- Two builds from identical inputs produce identical ZIP bytes.

## Generator attacks

- Catalog collection path escapes the repository.
- Catalog schema has wrong types, duplicate keys, or unsafe Markdown.
- README has duplicate or reversed generation markers.
- A goal contains a third hidden `/goal` command.
- A generated section contains regex backslash syntax.
- A malformed goal fails cleanly without a traceback or partial write.

## Shaping-history attacks

- Existing questions are reordered or a new question is inserted before history.
- An answer or approval row is rewritten.
- A new file contains duplicate IDs while no base ref is available.
- Fake question headings appear inside fenced code.
- Allowed status/supersession updates continue to work.

## Repository and agent attacks

- A new workflow requests write permission.
- A repository file is a symlink or contains NUL bytes.
- Malformed catalog data does not crash with an uncontrolled traceback.
- Repository content attempts prompt injection or command authority.
- The approved contract becomes stale or materially ambiguous during execution.
- A `.yaml` workflow or write permission attempts to bypass CI policy.
- Local `node_modules` symlinks exist after locked dependency installation.
- Catalog text attempts Markdown link injection.
- Package-lock metadata drifts from the pinned Skills CLI.
- Two writers attempt to use the same Goal Contract or shared resource without a valid lease.
## Final inversion cases

- Reject leading-zero or incomplete semantic versions.
- Reject a ZIP whose member bytes no longer match the declared source manifest.
- Reject decomposed Unicode archive names that can normalize differently across filesystems.
- Ignore generated dependency directories when discovering project shaping histories.
- Reject zero-based question IDs and duplicate approval sections.
- Reject workflow `write-all`, duplicate skill frontmatter, noncanonical invocation booleans, and any transitive lock entry without HTTPS resolution and sha512 integrity.
