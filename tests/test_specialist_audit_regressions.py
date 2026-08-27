from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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


class MetadataSynchronizationTests(unittest.TestCase):
    def test_readme_badge_matches_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(
            f"![Version](https://img.shields.io/badge/version-{version}-7C3AED?style=flat-square)",
            readme,
        )

    def test_goal_doc_sync_updates_version_badge(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            (repo / "VERSION").write_text("9.8.7\n", encoding="utf-8")
            result = run(repo, "scripts/sync_goal_docs.py", "--write")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            readme = (repo / "README.md").read_text(encoding="utf-8")
            self.assertIn("version-9.8.7-7C3AED", readme)
            self.assertEqual(len(re.findall(r"!\[Version\]", readme)), 1)


class DependencyPinTests(unittest.TestCase):
    def test_validator_derives_skills_pin_from_package_json(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = copy_repo(Path(raw))
            package_path = repo / "package.json"
            lock_path = repo / "package-lock.json"
            package = json.loads(package_path.read_text(encoding="utf-8"))
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            package["devDependencies"]["skills"] = "1.5.24"
            lock["packages"][""]["devDependencies"]["skills"] = "1.5.24"
            lock["packages"]["node_modules/skills"]["version"] = "1.5.24"
            lock["packages"]["node_modules/skills"]["resolved"] = (
                "https://registry.npmjs.org/skills/-/skills-1.5.24.tgz"
            )
            package_path.write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
            lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
            result = run(repo, "scripts/validate_repository.py")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_dependabot_covers_npm_and_actions(self):
        source = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
        self.assertIn("package-ecosystem: github-actions", source)
        self.assertIn("package-ecosystem: npm", source)


class SpecialistReviewerProtocolTests(unittest.TestCase):
    def test_all_specialists_and_isolation_rules_are_documented(self):
        protocol = (
            ROOT / "skills" / "goal-engine" / "references" / "specialist-reviewers.md"
        ).read_text(encoding="utf-8")
        for reviewer in (
            "Contract & State-Machine Reviewer",
            "Agent-Control & Interaction Reviewer",
            "Security & Supply-Chain Reviewer",
            "Tooling & Portability Reviewer",
            "Verification & Mutation Reviewer",
            "Documentation & Adoption Reviewer",
        ):
            self.assertIn(reviewer, protocol)
        self.assertIn("Reviews are read-only by default", protocol)
        self.assertIn("hypothesis until reproduced", protocol)
        self.assertIn("independently re-check important fixes", protocol)

    def test_goal_engine_links_the_protocol(self):
        engine = (ROOT / "skills" / "goal-engine" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/specialist-reviewers.md", engine)


class CatalogMaintainabilityTests(unittest.TestCase):
    def test_validator_no_longer_freezes_release_specific_profile_totals(self):
        source = (ROOT / "scripts" / "validate_repository.py").read_text(encoding="utf-8")
        self.assertNotIn("Expected 31 goals", source)
        self.assertNotIn('expected_counts = {"core": 7, "specialist": 9, "quality": 15}', source)


if __name__ == "__main__":
    unittest.main()
