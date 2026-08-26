#!/usr/bin/env python3
"""Apply second-pass adversarial refinements found during independent diff review."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    if source.count(old) != 1:
        raise RuntimeError(f"{path}: expected one occurrence, found {source.count(old)} for {old!r}")
    target.write_text(source.replace(old, new, 1), encoding="utf-8")


# Prevent link/table injection through catalog-controlled text and preserve normal file modes.
replace_once(
    "scripts/sync_goal_docs.py",
    '    if any(char in value for char in ("|", "<", ">", "`")):\n',
    '    if any(char in value for char in ("|", "<", ">", "`", "[", "]", "(", ")")):\n',
)
replace_once(
    "scripts/sync_goal_docs.py",
    '        with os.fdopen(handle, "w", encoding="utf-8", newline="\\n") as stream:\n            stream.write(content)\n        os.replace(temp, path)\n',
    '        with os.fdopen(handle, "w", encoding="utf-8", newline="\\n") as stream:\n            stream.write(content)\n        os.chmod(temp, 0o644)\n        os.replace(temp, path)\n',
)
replace_once(
    "scripts/sync_goal_launchers.py",
    '    if any(char in title for char in ("|", "<", ">", "`")):\n',
    '    if any(char in title for char in ("|", "<", ">", "`", "[", "]", "(", ")")):\n',
)
replace_once(
    "scripts/sync_goal_launchers.py",
    '        with os.fdopen(handle, "w", encoding="utf-8", newline="\\n") as stream:\n            stream.write(content)\n        os.replace(temp, path)\n',
    '        with os.fdopen(handle, "w", encoding="utf-8", newline="\\n") as stream:\n            stream.write(content)\n        os.chmod(temp, 0o644)\n        os.replace(temp, path)\n',
)

# Make the approval fingerprint and execution lease concrete rather than aspirational.
replace_once(
    "skills/shape-goal/goal-contract-template.md",
    "**Approval shaping round:** [ROUND ID OR NONE]  \n",
    "**Approval shaping round:** [ROUND ID OR NONE]  \n**Approval fingerprint:** [GOAL ID + REVISION + APPROVAL ROUND + APPROVED SOURCE SHA/HASH]  \n**Execution lease:** Not acquired / [SESSION OR WORKTREE + OWNER + ACQUIRED + EXPIRY OR RENEWAL]  \n",
)
replace_once(
    "skills/goal-engine/templates/goal-progress-template.md",
    "**Branch/worktree/SHA:** [BRANCH] / [WORKTREE] / [SHA]  \n",
    "**Branch/worktree/SHA:** [BRANCH] / [WORKTREE] / [SHA]  \n**Approval fingerprint:** [GOAL ID + REVISION + APPROVAL ROUND + APPROVED SOURCE SHA/HASH]  \n**Execution lease:** [OWNER / SESSION / WORKTREE / ACQUIRED / RENEWED / EXPIRES]  \n**Shared-resource locks:** [PATHS / SERVICES / ENVIRONMENTS / NONE]  \n",
)
replace_once(
    "skills/goal-engine/SKILL.md",
    "2. Confirm the contract names its approval shaping round.\n3. Surface the exact outcome and acceptance evidence for the native evaluator.\n4. Continue execution; do not treat shaping as completion.\n",
    "2. Confirm the Goal ID, revision, approval round, approval fingerprint, branch/worktree, and current source SHA still match the approved handoff.\n3. Acquire or renew one execution lease in progress state; stop when another live writer or shared-resource lock conflicts.\n4. Surface the exact outcome and acceptance evidence for the native evaluator.\n5. Continue execution; do not treat shaping as completion.\n",
)
replace_once(
    "skills/goal-engine/SKILL.md",
    "8. Progress, archive, history, library version, and authority boundaries\n",
    "8. Approval fingerprint, execution lease, shared-resource locks, progress, archive, history, library version, and authority boundaries\n",
)
replace_once(
    "skills/shape-goal/SKILL.md",
    "- The approval shaping round is recorded\n- The contract is explicitly approved\n",
    "- The approval shaping round and approval fingerprint are recorded\n- The execution-lease and shared-resource-lock policy is explicit when concurrent work is possible\n- The contract is explicitly approved\n",
)

# Repository validator: ignore local generated environments, inspect both workflow extensions,
# forbid write permissions, validate the npm lock contract, and require trust-boundary language.
replace_once(
    "scripts/validate_repository.py",
    "from pathlib import PurePath\nfrom pathlib import Path\n",
    "from pathlib import Path\n",
)
replace_once(
    "scripts/validate_repository.py",
    '        if ".git" in path.parts or "dist" in path.parts or "__pycache__" in path.parts:\n            continue\n',
    '        if any(part in {".git", "dist", "build", "node_modules", "__pycache__", ".venv", "venv", ".tox", ".nox", ".pytest_cache", ".mypy_cache", ".ruff_cache"} for part in path.parts):\n            continue\n',
)
replace_once(
    "scripts/validate_repository.py",
    '    workflows = sorted(workflow_dir.glob("*.yml")) if workflow_dir.exists() else []\n',
    '    workflows = sorted(set(workflow_dir.glob("*.yml")) | set(workflow_dir.glob("*.yaml"))) if workflow_dir.exists() else []\n',
)
replace_once(
    "scripts/validate_repository.py",
    '    source = workflow.read_text(encoding="utf-8")\n    for line in source.splitlines():\n',
    '    source = workflow.read_text(encoding="utf-8")\n    if "contents: read" not in source:\n        fail(".github/workflows/validate.yml: contents permission must remain read-only")\n    if re.search(r"^\\s*[A-Za-z-]+:\\s*write\\s*$", source, flags=re.MULTILINE):\n        fail(".github/workflows/validate.yml: write permission is forbidden")\n    for line in source.splitlines():\n',
)
replace_once(
    "scripts/validate_repository.py",
    '        "python -m unittest discover -s tests -v",\n        "npm ci --ignore-scripts",\n        "npx --no-install skills",\n',
    '        "python -m unittest discover -s tests -v",\n',
)
replace_once(
    "scripts/validate_repository.py",
    "def validate_scripts_and_ci() -> None:\n",
    '''def validate_package_manifest() -> None:
    try:
        package = json.loads(text("package.json"))
        lock = json.loads(text("package-lock.json"))
    except (json.JSONDecodeError, TypeError) as error:
        fail(f"npm package metadata is invalid: {error}")
        return
    expected = "1.5.23"
    if package.get("name") != "loop-engineering-goal-library" or package.get("private") is not True:
        fail("package.json must remain the private loop-engineering-goal-library package")
    if package.get("devDependencies", {}).get("skills") != expected:
        fail(f"package.json must pin skills exactly to {expected}")
    if lock.get("lockfileVersion") != 3:
        fail("package-lock.json must use lockfileVersion 3")
    packages = lock.get("packages")
    if not isinstance(packages, dict):
        fail("package-lock.json packages must be an object")
        return
    root_package = packages.get("", {})
    skills_package = packages.get("node_modules/skills", {})
    if root_package.get("devDependencies", {}).get("skills") != expected:
        fail("package-lock.json root dependency does not match package.json")
    if skills_package.get("version") != expected or not skills_package.get("integrity"):
        fail("package-lock.json must pin skills 1.5.23 with an integrity hash")


def validate_scripts_and_ci() -> None:
''',
)
replace_once(
    "scripts/validate_repository.py",
    "    validate_tree_hygiene()\n    validate_scripts_and_ci()\n",
    "    validate_tree_hygiene()\n    validate_package_manifest()\n    validate_scripts_and_ci()\n",
)
replace_once(
    "scripts/validate_repository.py",
    '            "references/shaping-history.md",\n',
    '            "prompt-injection",\n            "without symlink traversal",\n            "references/shaping-history.md",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '            "goal-fit gate",\n            "shaping history",\n',
    '            "goal-fit gate",\n            "prompt-injection",\n            "execution lease",\n            "shaping history",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '            "Pre-approval clarity gate",\n',
    '            "Pre-approval clarity gate",\n            "Approval fingerprint",\n            "Execution lease",\n',
)

# Expand attack tests for the second-pass findings.
replace_once(
    "tests/test_adversarial_robustness.py",
    '''    def test_malformed_catalog_fails_without_traceback(self):
''',
    '''    def test_catalog_link_injection_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            catalog_path = repo / "goals" / "catalog.json"
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog["goals"][0]["simple"] = "safe](https://attacker.example)"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--write")
            self.assertNotEqual(result.returncode, 0)

    def test_malformed_catalog_fails_without_traceback(self):
''',
)
replace_once(
    "tests/test_adversarial_robustness.py",
    '''    def test_repository_validator_rejects_symlink(self):
''',
    '''    def test_repository_validator_rejects_yaml_workflow(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            evil = repo / ".github" / "workflows" / "evil.yaml"
            evil.write_text("name: evil\\non: push\\njobs: {}\\n", encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("workflow", result.stdout.lower())

    def test_repository_validator_rejects_write_permission(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            workflow = repo / ".github" / "workflows" / "validate.yml"
            workflow.write_text(workflow.read_text(encoding="utf-8").replace("contents: read", "contents: write"), encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("write permission", result.stdout.lower())

    def test_repository_validator_ignores_local_node_modules(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            bin_dir = repo / "node_modules" / ".bin"
            bin_dir.mkdir(parents=True)
            target = repo / "node_modules" / "tool"
            target.write_text("tool", encoding="utf-8")
            link = bin_dir / "tool"
            try:
                os.symlink(target, link)
            except OSError:
                link.write_text("shim", encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_repository_validator_rejects_package_lock_drift(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            lock_path = repo / "package-lock.json"
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            lock["packages"]["node_modules/skills"]["version"] = "9.9.9"
            lock_path.write_text(json.dumps(lock), encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("package-lock", result.stdout.lower())

    def test_repository_validator_rejects_symlink(self):
''',
)

# Record the verified second-pass lessons.
replace_once(
    "docs/ROBUSTNESS_AUDIT.md",
    "## Residual limits\n",
    "## Second-pass findings\n\nAn independent review found and closed additional gaps: local `node_modules` symlinks would have caused false CI failures; `.yaml` workflows could bypass a `.yml`-only check; write permissions needed an explicit prohibition; catalog text needed link-injection protection; locked package metadata needed structural validation; and execution leases needed concrete contract fields.\n\n## Residual limits\n",
)
replace_once(
    "docs/goals/2026-08-26-adversarial-robustness/UAT.md",
    "- The approved contract becomes stale or materially ambiguous during execution.\n",
    "- The approved contract becomes stale or materially ambiguous during execution.\n- A `.yaml` workflow or write permission attempts to bypass CI policy.\n- Local `node_modules` symlinks exist after locked dependency installation.\n- Catalog text attempts Markdown link injection.\n- Package-lock metadata drifts from the pinned Skills CLI.\n- Two writers attempt to use the same Goal Contract or shared resource without a valid lease.\n",
)
replace_once(
    "CHANGELOG.md",
    "- Both skills now treat repository/external content as untrusted evidence, resist prompt injection, validate state paths, and stop on stale contract state or an ambiguous execution interpretation.\n",
    "- Both skills now treat repository/external content as untrusted evidence, resist prompt injection, validate state paths, and stop on stale contract state or an ambiguous execution interpretation.\n- Goal Contracts and progress state now carry an approval fingerprint, execution lease, and shared-resource locks for stale-state and concurrent-writer detection.\n- Repository validation covers both workflow extensions, forbids write permissions, validates the locked Skills CLI manifest, and ignores local dependency environments while checking committed sources.\n",
)

print("Applied second-pass adversarial refinements")
