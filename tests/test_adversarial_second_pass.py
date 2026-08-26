from __future__ import annotations

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
