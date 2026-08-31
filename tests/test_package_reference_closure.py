from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "package_skills.py"


def load_packager():
    spec = importlib.util.spec_from_file_location("package_skills_reference_test", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PackageReferenceClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.packager = load_packager()

    def test_all_advertised_packages_are_reference_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="package-closure-") as temporary:
            artifacts = self.packager.build(Path(temporary) / "dist")
            archives = [path for path in artifacts if path.suffix == ".zip"]
            self.assertEqual(len(archives), 3)
            for archive_path in archives:
                with zipfile.ZipFile(archive_path) as archive:
                    self.packager.validate_markdown_references(archive, archive.namelist())

    def test_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="package-escape-") as temporary:
            archive_path = Path(temporary) / "bad.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("SKILL.md", "See [`bad`](../outside.md).")
            with zipfile.ZipFile(archive_path) as archive:
                with self.assertRaisesRegex(ValueError, "escapes the package"):
                    self.packager.validate_markdown_references(archive, archive.namelist())


if __name__ == "__main__":
    unittest.main()
