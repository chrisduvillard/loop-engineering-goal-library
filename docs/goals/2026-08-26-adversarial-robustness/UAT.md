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
