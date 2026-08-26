from __future__ import annotations

import importlib.util
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
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
sync_goal_docs = load_script("sync_goal_docs")
sync_goal_launchers = load_script("sync_goal_launchers")
shaping = load_script("validate_shaping_history_diff")


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


class PackagingAttackTests(unittest.TestCase):
    def test_refuses_repository_root_without_deleting_it(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            result = run(repo, "scripts/package_skills.py", "--output-dir", str(repo))
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue((repo / "README.md").exists())

    def test_refuses_existing_foreign_content(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            output = repo / "custom-output"
            output.mkdir()
            marker = output / "keep.txt"
            marker.write_text("do not delete", encoding="utf-8")
            result = run(repo, "scripts/package_skills.py", "--output-dir", str(output))
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "do not delete")

    def test_rejects_invalid_version_before_writing(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            (repo / "VERSION").write_text("../../escape\n", encoding="utf-8")
            result = run(repo, "scripts/package_skills.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("not semantic", result.stderr)

    def test_rejects_symlinked_skill_content(self):
        if not hasattr(os, "symlink"):
            self.skipTest("symlinks unavailable")
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            repo = copy_repo(root)
            secret = root / "secret.txt"
            secret.write_text("secret", encoding="utf-8")
            link = repo / "skills" / "shape-goal" / "references" / "leak.txt"
            try:
                os.symlink(secret, link)
            except OSError as error:
                self.skipTest(f"symlink unavailable: {error}")
            result = run(repo, "scripts/package_skills.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("symlink", result.stderr.lower())

    def test_rejects_casefold_collision(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            directory = repo / "skills" / "shape-goal" / "references"
            first, second = directory / "Collision.md", directory / "collision.md"
            first.write_text("one", encoding="utf-8")
            try:
                second.write_text("two", encoding="utf-8")
            except OSError:
                self.skipTest("case-insensitive filesystem")
            if first.samefile(second):
                self.skipTest("case-insensitive filesystem")
            result = run(repo, "scripts/package_skills.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("collide", result.stderr.lower())

    def test_build_is_deterministic_and_archive_paths_are_safe(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            out1, out2 = Path(raw) / "out1", Path(raw) / "out2"
            self.assertEqual(run(repo, "scripts/package_skills.py", "--output-dir", str(out1)).returncode, 0)
            self.assertEqual(run(repo, "scripts/package_skills.py", "--output-dir", str(out2)).returncode, 0)
            for first in sorted(out1.glob("*.zip")):
                second = out2 / first.name
                self.assertEqual(first.read_bytes(), second.read_bytes())
                with zipfile.ZipFile(first) as archive:
                    self.assertIsNone(archive.testzip())
                    for info in archive.infolist():
                        self.assertNotIn("..", Path(info.filename).parts)
                        self.assertFalse(info.filename.startswith("/"))
                        self.assertEqual(info.date_time, package_skills.FIXED_TIMESTAMP)


class GeneratedDocsAttackTests(unittest.TestCase):
    def test_baseline_sync_is_stable(self):
        self.assertEqual(run(ROOT, "scripts/sync_goal_docs.py", "--check").returncode, 0)
        self.assertEqual(run(ROOT, "scripts/sync_goal_launchers.py", "--check").returncode, 0)

    def test_collection_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            repo = copy_repo(root)
            catalog_path = repo / "goals" / "catalog.json"
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog["categories"][0]["collection"] = "../ESCAPE.md"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--write")
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((root / "ESCAPE.md").exists())

    def test_duplicate_or_reversed_markers_are_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            readme = repo / "README.md"
            source = readme.read_text(encoding="utf-8")
            readme.write_text(source + "\n<!-- goal-catalog:start -->\n<!-- goal-catalog:end -->\n", encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--check")
            self.assertNotEqual(result.returncode, 0)

    def test_extra_goal_command_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            goal = repo / "goals" / "01-brownfield-continue-finish.md"
            goal.write_text(goal.read_text(encoding="utf-8") + "\n```text\n/goal unexpected third command\n```\n", encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--check")
            self.assertNotEqual(result.returncode, 0)

    def test_catalog_markdown_injection_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            catalog_path = repo / "goals" / "catalog.json"
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog["goals"][0]["simple"] += " | injected |"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--write")
            self.assertNotEqual(result.returncode, 0)

    def test_replacement_treats_backslashes_literally(self):
        readme = f"before\n{sync_goal_docs.README_START}\nold\n{sync_goal_docs.README_END}\nafter\n"
        result = sync_goal_docs.replace_readme_catalog(readme, r"\1 literal")
        self.assertIn(r"\1 literal", result)

    def test_catalog_link_injection_is_rejected(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            catalog_path = repo / "goals" / "catalog.json"
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog["goals"][0]["simple"] = "safe](https://attacker.example)"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--write")
            self.assertNotEqual(result.returncode, 0)

    def test_malformed_catalog_fails_without_traceback(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            (repo / "goals" / "catalog.json").write_text('{"schema_version":1,"categories":["bad"],"goals":[]}', encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--check")
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Traceback", result.stderr)

    def test_launcher_empty_file_fails_without_traceback(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            (repo / "goals" / "99-empty.md").write_text("", encoding="utf-8")
            result = run(repo, "scripts/sync_goal_launchers.py", "--check")
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Traceback", result.stderr)

    def test_launcher_rejects_unsafe_title(self):
        original = (ROOT / "goals" / "01-brownfield-continue-finish.md").read_text(encoding="utf-8")
        with self.assertRaises(ValueError):
            sync_goal_launchers.transform(original.replace("# Brownfield Continue / Finish", "# Bad | Table"))

    def test_all_canonical_launcher_transforms_are_idempotent(self):
        for path in sync_goal_launchers.canonical_goal_paths():
            source = path.read_text(encoding="utf-8")
            self.assertEqual(sync_goal_launchers.transform(source), source, path.name)


class ShapingHistoryAttackTests(unittest.TestCase):
    def sample(self) -> str:
        return """# History

## Round R1

#### R1-Q1 — Scope

- **Status:** Answered
- **Exact question:** Keep exports?
- **User answer:** Yes.
- **Normalized decision:** Preserve exports.
- **Supersedes:** none

#### R1-Q2 — Browser

- **Status:** Answered
- **Exact question:** Which browsers?
- **User answer:** Current majors.
- **Normalized decision:** Current majors.
- **Supersedes:** none

## Approval record

| Round | Question | Answer | Rev | Date |
|---|---|---|---:|---|
| R1 | Approve? | Yes | 1 | today |
"""

    def test_reordering_is_rejected(self):
        before = self.sample()
        first = before.index("#### R1-Q1")
        second = before.index("#### R1-Q2")
        approval = before.index("## Approval record")
        reordered = before[:first] + before[second:approval] + before[first:second] + before[approval:]
        self.assertTrue(shaping.validate_document(before, reordered, "history"))

    def test_inserting_before_committed_questions_is_rejected(self):
        before = self.sample()
        inserted = before.replace("#### R1-Q1", "#### R1-Q0 — Hidden\n\n- **Status:** Proposed\n\n#### R1-Q1")
        self.assertTrue(shaping.validate_document(before, inserted, "history"))

    def test_fenced_fake_questions_are_ignored(self):
        text = """# History

```md
#### R1-Q1 — Fake
```

## Round R1

#### R1-Q1 — Real

- **Status:** Answered
"""
        self.assertEqual(list(shaping.question_blocks(text)), ["R1-Q1"])

    def test_status_change_is_allowed_but_answer_change_is_not(self):
        before = self.sample()
        self.assertFalse(shaping.validate_document(before, before.replace("- **Status:** Answered", "- **Status:** Superseded", 1), "history"))
        self.assertTrue(shaping.validate_document(before, before.replace("- **User answer:** Yes.", "- **User answer:** No."), "history"))

    def test_new_invalid_history_is_checked_even_without_base_ref(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            bad = repo / "docs" / "goals" / "new" / "SHAPING.md"
            bad.parent.mkdir(parents=True)
            bad.write_text("#### R1-Q1 — One\n\n#### R1-Q1 — Duplicate\n", encoding="utf-8")
            result = run(repo, "scripts/validate_shaping_history_diff.py", "--base-ref", "0000000000000000000000000000000000000000")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate", result.stderr.lower())

    def test_random_append_and_mutation_properties(self):
        random.seed(20260826)
        for _ in range(100):
            count = random.randint(1, 8)
            blocks = []
            for index in range(1, count + 1):
                blocks.append(
                    f"#### R1-Q{index} — D{index}\n\n- **Status:** Answered\n- **Exact question:** Q{index}?\n- **User answer:** A{index}.\n- **Normalized decision:** D{index}.\n"
                )
            before = "# History\n\n## Round R1\n\n" + "\n".join(blocks)
            appended = before + f"\n## Round R2\n\n#### R2-Q1 — Next\n\n- **Status:** Proposed\n"
            self.assertFalse(shaping.validate_document(before, appended, "fuzz"))
            victim = random.randint(1, count)
            mutated = before.replace(f"- **User answer:** A{victim}.", f"- **User answer:** CHANGED{victim}.")
            self.assertTrue(shaping.validate_document(before, mutated, "fuzz"))


class RepositoryRedTeamTests(unittest.TestCase):
    def test_repository_validator_rejects_extra_write_workflow(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            evil = repo / ".github" / "workflows" / "evil.yml"
            evil.write_text("name: evil\non: push\npermissions:\n  contents: write\njobs: {}\n", encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("workflow", result.stdout.lower())

    def test_repository_validator_rejects_yaml_workflow(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            evil = repo / ".github" / "workflows" / "evil.yaml"
            evil.write_text("name: evil\non: push\njobs: {}\n", encoding="utf-8")
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
        if not hasattr(os, "symlink"):
            self.skipTest("symlinks unavailable")
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            repo = copy_repo(root)
            outside = root / "outside.md"
            outside.write_text("outside", encoding="utf-8")
            link = repo / "skills" / "shape-goal" / "references" / "outside.md"
            try:
                os.symlink(outside, link)
            except OSError as error:
                self.skipTest(f"symlink unavailable: {error}")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("symlink", result.stdout.lower())

    def test_repository_validator_rejects_nul_text(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            (repo / "skills" / "shape-goal" / "references" / "nul.md").write_bytes(b"hello\x00world")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("nul", result.stdout.lower())

    def test_repository_validator_handles_malformed_catalog_without_traceback(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            (repo / "goals" / "catalog.json").write_text("[]", encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Traceback", result.stderr + result.stdout)

    def test_dangerous_output_cli_never_destroys_copied_repository(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            marker = repo / "README.md"
            run(repo, "scripts/package_skills.py", "--output-dir", str(repo))
            self.assertTrue(marker.exists())


if __name__ == "__main__":
    unittest.main()
