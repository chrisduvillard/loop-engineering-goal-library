#!/usr/bin/env python3
"""Validate the locked toolchain, dependency automation, and CI control plane."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NUMERIC = r"(?:0|[1-9]\d*)"
PRERELEASE = r"(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
BUILD = r"[0-9A-Za-z-]+"
SEMVER = re.compile(
    rf"{NUMERIC}\.{NUMERIC}\.{NUMERIC}"
    rf"(?:-{PRERELEASE}(?:\.{PRERELEASE})*)?"
    rf"(?:\+{BUILD}(?:\.{BUILD})*)?"
)
ACTION_PIN = re.compile(r"uses:\s+[^@\s]+@[0-9a-f]{40}(?:\s+#.*)?$")
REQUIRED_VALIDATORS = (
    "python scripts/validate_question_state.py --self-test",
    "python scripts/validate_goal_archives.py --self-test",
    "python scripts/validate_tooling_contract.py --self-test",
)


def load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def validate() -> list[str]:
    errors: list[str] = []
    package_path = ROOT / "package.json"
    lock_path = ROOT / "package-lock.json"
    dependabot_path = ROOT / ".github" / "dependabot.yml"
    workflow_path = ROOT / ".github" / "workflows" / "validate.yml"

    try:
        package = load_json(package_path)
        lock = load_json(lock_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [str(error)]

    dependencies = package.get("devDependencies")
    if not isinstance(dependencies, dict) or set(dependencies) != {"skills"}:
        errors.append("package.json must contain exactly one reviewed devDependency: skills")
        expected = ""
    else:
        expected = dependencies.get("skills", "")
        if not isinstance(expected, str) or not SEMVER.fullmatch(expected):
            errors.append("package.json must pin skills to one exact valid semantic version")

    if package.get("private") is not True:
        errors.append("package.json must remain private")
    if package.get("scripts") != {"test": "python -m unittest discover -s tests -v"}:
        errors.append("package.json scripts changed outside the reviewed test command")

    packages = lock.get("packages")
    if lock.get("lockfileVersion") != 3 or not isinstance(packages, dict):
        errors.append("package-lock.json must use lockfileVersion 3 and a packages object")
    else:
        root_entry = packages.get("", {})
        skills_entry = packages.get("node_modules/skills", {})
        if root_entry.get("devDependencies", {}).get("skills") != expected:
            errors.append("package-lock root dependency differs from package.json")
        if skills_entry.get("version") != expected:
            errors.append("locked Skills CLI version differs from package.json")
        for path, entry in packages.items():
            if path == "":
                continue
            if not isinstance(entry, dict):
                errors.append(f"package-lock entry {path!r} is not an object")
                continue
            if entry.get("dev") is not True:
                errors.append(f"package-lock entry {path!r} is not development-only")
            resolved = entry.get("resolved")
            integrity = entry.get("integrity")
            if not isinstance(resolved, str) or not resolved.startswith("https://registry.npmjs.org/"):
                errors.append(f"package-lock entry {path!r} has unapproved provenance")
            if not isinstance(integrity, str) or not integrity.startswith("sha512-"):
                errors.append(f"package-lock entry {path!r} lacks SHA-512 integrity")
            if entry.get("hasInstallScript") is True:
                errors.append(f"package-lock entry {path!r} declares an install script")

    try:
        dependabot = dependabot_path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(str(error))
    else:
        for ecosystem in ("github-actions", "npm"):
            if f"package-ecosystem: {ecosystem}" not in dependabot:
                errors.append(f"Dependabot is not configured for {ecosystem}")

    try:
        workflow = workflow_path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(str(error))
    else:
        if "concurrency:" not in workflow or "cancel-in-progress: true" not in workflow:
            errors.append("validation workflow lacks superseded-run cancellation")
        if "contents: read" not in workflow:
            errors.append("validation workflow is not read-only")
        if re.search(r"^\s*[A-Za-z-]+:\s*write(?:-all)?\s*$", workflow, re.MULTILINE):
            errors.append("validation workflow contains write permission")
        for line in workflow.splitlines():
            if "uses:" in line and not ACTION_PIN.search(line.strip()):
                errors.append(f"GitHub Action is not pinned to a full SHA: {line.strip()}")
        for command in REQUIRED_VALIDATORS:
            if command not in workflow:
                errors.append(f"validation workflow does not run: {command}")
    return errors


def self_test() -> None:
    valid = (
        "0.0.0",
        "1.2.3",
        "1.2.3-alpha.1",
        "1.2.3-0",
        "1.2.3-01a",
        "1.2.3+001",
    )
    invalid = (
        "01.2.3",
        "1.02.3",
        "1.2.03",
        "1.2",
        "1.2.3-01",
        "1.2.3-alpha..1",
        "^1.2.3",
        "latest",
    )
    assert all(SEMVER.fullmatch(item) for item in valid)
    assert not any(SEMVER.fullmatch(item) for item in invalid)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
            print("Tooling-contract self-test passed.")
        errors = validate()
    except (AssertionError, OSError, ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    if errors:
        print("Tooling-contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Locked tooling, dependency automation, and CI controls are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
