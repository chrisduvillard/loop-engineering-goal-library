#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean(content: str) -> str:
    return "\n".join(line.rstrip() for line in content.strip("\n").splitlines()) + "\n"


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(clean(content), encoding="utf-8", newline="\n")


def replace_function(path: str, name: str, next_name: str, replacement: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    start = source.index(f"def {name}(")
    end = source.index(f"\n\ndef {next_name}(", start)
    source = source[:start] + clean(replacement).rstrip("\n") + source[end:]
    target.write_text(source, encoding="utf-8", newline="\n")


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    if source.count(old) != 1:
        raise RuntimeError(f"{path}: expected one occurrence of {old!r}, found {source.count(old)}")
    target.write_text(source.replace(old, new, 1), encoding="utf-8", newline="\n")


replace_once(
    "scripts/validate_repository.py",
    'ACTION_PIN = re.compile(r"uses:\\s+[^@\\s]+@([0-9a-f]{40})(?:\\s+#.*)?$")\n',
    'ACTION_PIN = re.compile(r"uses:\\s+[^@\\s]+@([0-9a-f]{40})(?:\\s+#.*)?$")\n'
    'SEMVER = re.compile(\n'
    '    r"(?:0|[1-9]\\d*)\\.(?:0|[1-9]\\d*)\\.(?:0|[1-9]\\d*)"\n'
    '    r"(?:-[0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*)?"\n'
    '    r"(?:\\+[0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*)?"\n'
    ')\n',
)
replace_once(
    "scripts/validate_repository.py",
    '    if not re.fullmatch(r"\\d+\\.\\d+\\.\\d+(?:[-+][0-9A-Za-z.-]+)?", version):\n',
    '    if not SEMVER.fullmatch(version):\n',
)

replace_function(
    "scripts/validate_repository.py",
    "parse_frontmatter",
    "require_fragments",
    r'''def parse_frontmatter(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    source = path.read_text(encoding="utf-8")
    if not source.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}, {}
    parts = source.split("---\n", 2)
    if len(parts) < 3:
        fail(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}, {}

    top: dict[str, str] = {}
    metadata: dict[str, str] = {}
    seen_top: set[str] = set()
    seen_metadata: set[str] = set()
    in_metadata = False
    for raw_line in parts[1].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if "\t" in raw_line[: len(raw_line) - len(raw_line.lstrip())]:
            fail(f"{path.relative_to(ROOT)}: tabs are not allowed in skill frontmatter")
        if raw_line.startswith(("  ", "\t")):
            if not in_metadata or ":" not in raw_line:
                fail(f"{path.relative_to(ROOT)}: unsupported nested frontmatter line {raw_line!r}")
                continue
            key, value = raw_line.strip().split(":", 1)
            key = key.strip()
            if key in seen_metadata:
                fail(f"{path.relative_to(ROOT)}: duplicate metadata key {key!r}")
            seen_metadata.add(key)
            metadata[key] = unquote_yaml(value)
            continue
        in_metadata = False
        if ":" not in raw_line:
            fail(f"{path.relative_to(ROOT)}: malformed frontmatter line {raw_line!r}")
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        if key in seen_top:
            fail(f"{path.relative_to(ROOT)}: duplicate frontmatter key {key!r}")
        seen_top.add(key)
        if key == "metadata":
            in_metadata = True
        else:
            top[key] = unquote_yaml(value)
    return top, metadata''',
)

replace_once(
    "scripts/validate_repository.py",
    '        for key in ("user-invocable", "disable-model-invocation"):\n'
    '            if key not in top:\n'
    '                fail(f"{rel}: missing {key}")\n',
    '        for key in ("user-invocable", "disable-model-invocation"):\n'
    '            if key not in top:\n'
    '                fail(f"{rel}: missing {key}")\n'
    '        if top.get("user-invocable") != "true":\n'
    '            fail(f"{rel}: user-invocable must be true")\n'
    '        if top.get("disable-model-invocation") != "false":\n'
    '            fail(f"{rel}: disable-model-invocation must be false")\n',
)

replace_function(
    "scripts/validate_repository.py",
    "validate_package_manifest",
    "validate_scripts_and_ci",
    r'''def validate_package_manifest() -> None:
    try:
        package = json.loads(text("package.json"))
        lock = json.loads(text("package-lock.json"))
    except (json.JSONDecodeError, TypeError) as error:
        fail(f"npm package metadata is invalid: {error}")
        return
    if not isinstance(package, dict) or not isinstance(lock, dict):
        fail("npm package metadata must use JSON objects")
        return

    expected = "1.5.23"
    if package.get("name") != "loop-engineering-goal-library" or package.get("private") is not True:
        fail("package.json must remain the private loop-engineering-goal-library package")
    if package.get("devDependencies", {}).get("skills") != expected:
        fail(f"package.json must pin skills exactly to {expected}")
    if package.get("scripts") != {"test": "python -m unittest discover -s tests -v"}:
        fail("package.json may contain only the reviewed test script")
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

    for package_path, entry in packages.items():
        if package_path == "":
            continue
        if not isinstance(entry, dict):
            fail(f"package-lock.json entry {package_path!r} must be an object")
            continue
        version = entry.get("version")
        resolved = entry.get("resolved")
        integrity = entry.get("integrity")
        if not isinstance(version, str) or not version:
            fail(f"package-lock.json entry {package_path!r} has no version")
        if not isinstance(resolved, str) or not resolved.startswith("https://registry.npmjs.org/"):
            fail(f"package-lock.json entry {package_path!r} must resolve from the npm registry over HTTPS")
        if not isinstance(integrity, str) or not integrity.startswith("sha512-"):
            fail(f"package-lock.json entry {package_path!r} must have a sha512 integrity hash")
        if entry.get("dev") is not True:
            fail(f"package-lock.json entry {package_path!r} must remain development-only")
        if entry.get("hasInstallScript") is True:
            fail(f"package-lock.json entry {package_path!r} may not declare an install script")''',
)

replace_once(
    "scripts/validate_repository.py",
    '    if re.search(r"^\\s*[A-Za-z-]+:\\s*write\\s*$", source, flags=re.MULTILINE):\n'
    '        fail(".github/workflows/validate.yml: write permission is forbidden")\n',
    '    if re.search(r"^\\s*[A-Za-z-]+:\\s*write(?:-all)?\\s*$", source, flags=re.MULTILINE):\n'
    '        fail(".github/workflows/validate.yml: write permission is forbidden")\n'
    '    if re.search(r"^\\s*permissions:\\s*\\{[^}]*\\bwrite(?:-all)?\\b", source, flags=re.MULTILINE):\n'
    '        fail(".github/workflows/validate.yml: inline write permission is forbidden")\n',
)
replace_once(
    "scripts/validate_repository.py",
    '        "tests/test_adversarial_robustness.py",\n',
    '        "tests/test_adversarial_robustness.py",\n'
    '        "tests/test_adversarial_second_pass.py",\n',
)
replace_once(
    "scripts/validate_repository.py",
    '    print("- adversarial mutation tests and repository hygiene are enforced")\n',
    '    print("- adversarial mutation tests and repository hygiene are enforced")\n'
    '    print("- locked transitive dependencies, strict frontmatter, and archive-source parity are enforced")\n',
)

write(
    "tests/test_adversarial_second_pass.py",
    r'''from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


package_skills = load_script("package_skills")


def copy_repo(temp: Path) -> Path:
    destination = temp / "repo"
    shutil.copytree(
        ROOT,
        destination,
        ignore=shutil.ignore_patterns(".git", "dist", "node_modules", "__pycache__", "*.pyc"),
    )
    return destination


def run(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        (sys.executable, *args),
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class PackagingSecondPassTests(unittest.TestCase):
    def test_strict_semver_rejects_leading_zero_and_empty_identifiers(self):
        for version in ("01.2.3", "1.02.3", "1.2.03", "1.2.3-", "1.2.3+", "1.2.3-alpha..1"):
            with self.subTest(version=version), tempfile.TemporaryDirectory() as raw:
                repo = copy_repo(Path(raw))
                (repo / "VERSION").write_text(version + "\n", encoding="utf-8")
                result = run(repo, "scripts/package_skills.py")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("semantic version", result.stderr)

    def test_zip_validation_compares_packaged_bytes_to_source(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            source = root / "source.md"
            source.write_text("original", encoding="utf-8")
            archive = root / "test.zip"
            entries = [("source.md", source)]
            package_skills.write_zip(entries, archive)
            source.write_text("changed after packaging", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "differs from its source"):
                package_skills.validate_zip(archive, entries, individual=True)

    def test_decomposed_unicode_archive_name_is_rejected(self):
        decomposed = "Cafe\u0301.md"
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            candidate = repo / "skills" / "shape-goal" / "references" / decomposed
            candidate.write_text("test", encoding="utf-8")
            if candidate.name != decomposed:
                self.skipTest("filesystem normalized the test filename")
            result = run(repo, "scripts/package_skills.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("NFC", result.stderr)


class ShapingSecondPassTests(unittest.TestCase):
    def test_dependency_directories_are_not_treated_as_project_history(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            fake = repo / "node_modules" / "dependency" / "SHAPING.md"
            fake.parent.mkdir(parents=True)
            fake.write_text("#### R0-Q0 — Invalid dependency fixture\n", encoding="utf-8")
            result = run(
                repo,
                "scripts/validate_shaping_history_diff.py",
                "--base-ref",
                "0000000000000000000000000000000000000000",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_zero_based_question_id_is_rejected_in_new_history(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            history = repo / "docs" / "goals" / "new" / "SHAPING.md"
            history.parent.mkdir(parents=True)
            history.write_text(
                "#### R0-Q1 — Invalid\n\n- **Status:** Proposed\n- **Exact question:** Invalid?\n",
                encoding="utf-8",
            )
            result = run(repo, "scripts/validate_shaping_history_diff.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("R1-Q1", result.stderr)

    def test_duplicate_approval_sections_are_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            history = repo / "docs" / "goals" / "new" / "SHAPING.md"
            history.parent.mkdir(parents=True)
            history.write_text(
                "# History\n\n## Approval record\n\n| R1 | Approve? | Yes | 1 | now |\n\n"
                "## Approval record\n\n| R2 | Approve? | Yes | 2 | later |\n",
                encoding="utf-8",
            )
            result = run(repo, "scripts/validate_shaping_history_diff.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate Approval record", result.stderr)


class RepositorySecondPassTests(unittest.TestCase):
    def test_write_all_permission_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            workflow = repo / ".github" / "workflows" / "validate.yml"
            workflow.write_text(
                workflow.read_text(encoding="utf-8").replace(
                    "permissions:\n  contents: read",
                    "permissions: write-all\n# contents: read",
                ),
                encoding="utf-8",
            )
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("write permission", result.stdout.lower())

    def test_every_locked_transitive_dependency_requires_integrity(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            path = repo / "package-lock.json"
            lock = json.loads(path.read_text(encoding="utf-8"))
            lock["packages"]["node_modules/minipass"].pop("integrity")
            path.write_text(json.dumps(lock), encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("sha512 integrity", result.stdout)

    def test_duplicate_frontmatter_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            path = repo / "skills" / "shape-goal" / "SKILL.md"
            source = path.read_text(encoding="utf-8")
            path.write_text(source.replace("name: shape-goal", "name: shape-goal\nname: shadow-goal", 1), encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate frontmatter key", result.stdout)

    def test_skill_invocation_booleans_are_exact(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            path = repo / "skills" / "shape-goal" / "SKILL.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace("user-invocable: true", "user-invocable: false", 1),
                encoding="utf-8",
            )
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("user-invocable must be true", result.stdout)


if __name__ == "__main__":
    unittest.main()
''',
)

with (ROOT / "docs/ROBUSTNESS_AUDIT.md").open("a", encoding="utf-8") as handle:
    handle.write(clean(r'''
## Third-pass findings

A final inversion pass closed quieter failure modes that often appear only after a project matures: loose semantic-version parsing, ZIP manifests that were self-consistent but not compared with source bytes, decomposed Unicode archive names, generated dependency directories being mistaken for project shaping history, zero-based decision IDs, duplicate approval sections, `write-all` workflow permissions, ambiguous duplicate skill frontmatter, and unverified transitive lockfile entries.
'''))

with (ROOT / "docs/goals/2026-08-26-adversarial-robustness/UAT.md").open("a", encoding="utf-8") as handle:
    handle.write(clean(r'''
## Final inversion cases

- Reject leading-zero or incomplete semantic versions.
- Reject a ZIP whose member bytes no longer match the declared source manifest.
- Reject decomposed Unicode archive names that can normalize differently across filesystems.
- Ignore generated dependency directories when discovering project shaping histories.
- Reject zero-based question IDs and duplicate approval sections.
- Reject workflow `write-all`, duplicate skill frontmatter, noncanonical invocation booleans, and any transitive lock entry without HTTPS resolution and sha512 integrity.
'''))

with (ROOT / "docs/goals/2026-08-26-adversarial-robustness/PROGRESS.md").open("a", encoding="utf-8") as handle:
    handle.write(clean(r'''
## Third-pass review

The final review strengthened semantic versions, archive/source parity, Unicode normalization, shaping-history discovery, approval structure, workflow permission parsing, skill frontmatter, and the full npm lock graph. The adversarial suite now includes the corresponding regression cases.
'''))

print("Applied second-pass adversarial refinement")
