from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOALCTL = ROOT / "skills" / "goal-engine" / "scripts" / "goalctl.py"
EVALUATOR = ROOT / "scripts" / "evaluate_behavior.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RuntimeHardeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.goalctl = load_module("goalctl_runtime", GOALCTL)
        cls.evaluator = load_module("behavioral_evaluator", EVALUATOR)

    def test_goalctl_self_test(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(GOALCTL), "self-test"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("passed", completed.stdout)

    def test_fingerprint_is_stable_and_detects_contract_drift(self) -> None:
        contract = {
            "schema_version": 1,
            "goal_id": "fingerprint-test",
            "revision": 1,
            "title": "Test",
            "mutation_mode": "read_only",
            "assurance_level": "standard",
            "scope": {"included": [], "excluded": []},
            "acceptance": [{"id": "A1", "description": "Works", "status": "not_run", "evidence": []}],
            "source": {"branch": "main", "commit": "abc"},
            "protected_paths": [],
            "authority_boundaries": [],
        }
        first = self.goalctl.fingerprint(contract)
        contract["acceptance"][0]["status"] = "pass"
        contract["acceptance"][0]["evidence"] = ["runtime proof"]
        self.assertEqual(first, self.goalctl.fingerprint(contract))
        contract["acceptance"][0]["description"] = "Different authority"
        self.assertNotEqual(first, self.goalctl.fingerprint(contract))

    def test_behavioral_evaluator_rejects_false_completion(self) -> None:
        failures = self.evaluator.evaluate(
            {
                "mutation_mode": "read_only",
                "tracked_changes": ["src/changed.py"],
                "acceptance": {"A1": "fail"},
                "verifier_exit": 1,
                "claimed_achieved": True,
                "mutation_check_passed": False,
            }
        )
        self.assertGreaterEqual(len(failures), 4)

    def test_schemas_are_valid_json(self) -> None:
        for path in sorted((ROOT / "skills" / "goal-engine" / "schemas").glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_shape_goal_is_explicit_only(self) -> None:
        skill = (ROOT / "skills" / "shape-goal" / "SKILL.md").read_text(encoding="utf-8")
        metadata = (ROOT / "skills" / "shape-goal" / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("disable-model-invocation: true", skill.split("---", 2)[1])
        self.assertIn("allow_implicit_invocation: false", metadata)


if __name__ == "__main__":
    unittest.main()
