#!/usr/bin/env python3
"""Generate goal collections and README catalogs from safe canonical sources."""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "goals" / "catalog.json"
README_START = "<!-- goal-catalog:start -->"
README_END = "<!-- goal-catalog:end -->"
CATEGORY_ICONS = {"core": "🟣", "specialist": "🔵", "quality": "🟢"}
EXPECTED_COLLECTIONS = {
    "core": "GOAL_LIBRARY.md",
    "specialist": "SPECIALIST_LOOPS.md",
    "quality": "QUALITY_GOALS.md",
}
GOAL_FILE = re.compile(r"\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md")
PROFILE_BADGE = re.compile(
    r"!\[Profiles\]\(https://img\.shields\.io/badge/profiles-\d+-16A34A\?style=flat-square\)"
)
COMMAND = re.compile(r"```text\n(/goal .*?)\n```", flags=re.DOTALL)


def plain(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    value = value.strip()
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise ValueError(f"{label} contains a control character")
    if any(char in value for char in ("|", "<", ">", "`")):
        raise ValueError(f"{label} contains unsafe Markdown/HTML punctuation")
    return value


def safe_goal_filename(value: object) -> str:
    filename = plain(value, "goal file")
    if Path(filename).name != filename or not GOAL_FILE.fullmatch(filename):
        raise ValueError(f"unsafe goal filename: {filename!r}")
    return filename


def atomic_write(path: Path, content: str) -> None:
    if path.exists() and path.is_symlink():
        raise ValueError(f"refusing to replace symlink: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(temp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temp, path)
    except Exception:
        temp.unlink(missing_ok=True)
        raise


def load_catalog() -> dict:
    if CATALOG_PATH.is_symlink():
        raise ValueError("goals/catalog.json may not be a symlink")
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("goals/catalog.json must be a schema_version 1 object")
    categories = data.get("categories")
    goals = data.get("goals")
    if not isinstance(categories, list) or not isinstance(goals, list):
        raise ValueError("goals/catalog.json categories and goals must be arrays")
    return data


def parse_goal(filename: str) -> dict[str, str]:
    filename = safe_goal_filename(filename)
    path = ROOT / "goals" / filename
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"goals/{filename} must be a regular file")
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# ") or not lines[0][2:].strip():
        raise ValueError(f"goals/{filename} must begin with one non-empty H1 title")
    if len(re.findall(r"^# ", text, flags=re.MULTILINE)) != 1:
        raise ValueError(f"goals/{filename} must contain exactly one H1")

    def match(pattern: str, label: str) -> str:
        found = re.search(pattern, text, flags=re.MULTILINE)
        if not found:
            raise ValueError(f"goals/{filename} is missing {label}")
        return plain(found.group(1), f"goals/{filename} {label}")

    commands = COMMAND.findall(text)
    if len(commands) != 2:
        raise ValueError(f"goals/{filename} must contain exactly two advanced /goal preflights")

    return {
        "title": plain(lines[0][2:], f"goals/{filename} title"),
        "use_when": match(r"^\*\*Use when:\*\* (.+)$", "Use when"),
        "simple": match(r"^\*\*In simple terms:\*\* (.+)$", "In simple terms"),
        "command": commands[0].strip(),
        "fallback": commands[1].strip(),
        "why": match(r"^\*\*Why it works:\*\* (.+)$", "Why it works"),
    }


def validate_catalog(catalog: dict) -> list[tuple[dict, dict[str, str]]]:
    categories = catalog["categories"]
    goals = catalog["goals"]
    expected_keys = list(EXPECTED_COLLECTIONS)
    keys: list[str] = []
    collections: set[str] = set()
    for index, category in enumerate(categories):
        if not isinstance(category, dict):
            raise ValueError(f"category {index} must be an object")
        key = plain(category.get("key"), f"category {index} key")
        title = plain(category.get("title"), f"category {key} title")
        intro = plain(category.get("intro"), f"category {key} intro")
        collection = plain(category.get("collection"), f"category {key} collection")
        if collection != EXPECTED_COLLECTIONS.get(key):
            raise ValueError(f"category {key} has unsafe or unexpected collection path: {collection!r}")
        if collection in collections:
            raise ValueError(f"duplicate collection path: {collection}")
        collections.add(collection)
        keys.append(key)
        category.update(title=title, intro=intro, collection=collection)
    if keys != expected_keys:
        raise ValueError(f"unexpected category order: {keys}")

    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    parsed: list[tuple[dict, dict[str, str]]] = []
    for index, item in enumerate(goals, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"goal {index} must be an object")
        goal_id = plain(item.get("id"), f"goal {index} id")
        filename = safe_goal_filename(item.get("file"))
        category = plain(item.get("category"), f"goal {goal_id} category")
        if goal_id != f"{index:02d}":
            raise ValueError(f"goal {filename}: expected id {index:02d}, found {goal_id}")
        if goal_id in seen_ids or filename in seen_files:
            raise ValueError(f"duplicate goal id or file: {goal_id} / {filename}")
        if category not in EXPECTED_COLLECTIONS:
            raise ValueError(f"unknown category for {filename}: {category}")
        seen_ids.add(goal_id)
        seen_files.add(filename)
        actual = parse_goal(filename)
        for field in ("title", "use_when", "simple"):
            expected = plain(item.get(field), f"catalog {filename} {field}")
            if actual[field] != expected:
                raise ValueError(f"goals/{filename} {field} differs from goals/catalog.json")
        item.update(id=goal_id, file=filename, category=category)
        parsed.append((item, actual))

    disk_files = {
        path.name
        for path in (ROOT / "goals").glob("*.md")
        if path.name != "README.md"
    }
    if disk_files != seen_files:
        raise ValueError(
            f"Catalog/file mismatch. Missing={sorted(seen_files - disk_files)}; "
            f"extra={sorted(disk_files - seen_files)}"
        )
    return parsed


def interactive_commands(title: str) -> tuple[str, str]:
    return f"/shape-goal Use the {title} profile", f"$shape-goal Use the {title} profile"


def render_collection(category: dict, parsed: list[tuple[dict, dict[str, str]]]) -> str:
    entries = [(item, actual) for item, actual in parsed if item["category"] == category["key"]]
    blocks = [
        f"# {category['title'].replace('goals', 'Goal Profiles')}",
        "",
        "> [!NOTE]",
        "> Generated from canonical files under [`goals/`](goals/) and [`goals/catalog.json`](goals/catalog.json). "
        "Edit those sources, then run `python3 scripts/sync_goal_docs.py --write`.",
        "",
        "Start with `shape-goal` outside an active `/goal`. It asks one question at a time and returns the exact execution `/goal` after approval.",
        "",
        category["intro"],
    ]
    for item, actual in entries:
        claude, codex = interactive_commands(actual["title"])
        blocks.extend([
            "",
            "---",
            "",
            f"## [{actual['title']}](goals/{item['file']})",
            "",
            f"**In simple terms:** {actual['simple']}",
            "",
            f"**Use when:** {actual['use_when']}",
            "",
            "| Claude Code | Codex CLI / IDE |",
            "|---|---|",
            f"| `{claude}` | `{codex}` |",
            "",
            f"**Why it works:** {actual['why']}",
            "",
            f"**Advanced autonomous preflight and self-contained fallback:** [Open `goals/{item['file']}`](goals/{item['file']}).",
        ])
    return "\n".join(blocks).rstrip() + "\n"


def render_readme_catalog(catalog: dict, parsed: list[tuple[dict, dict[str, str]]]) -> str:
    by_category: dict[str, list[tuple[dict, dict[str, str]]]] = {}
    for item, actual in parsed:
        by_category.setdefault(item["category"], []).append((item, actual))
    lines = [
        README_START,
        "",
        "## Goal profiles",
        "",
        "You usually do not need to choose one: `shape-goal` can select the best profile from repository evidence. Choose directly only when the type of work is already clear.",
    ]
    for index, category in enumerate(catalog["categories"]):
        lines.extend([
            "",
            "<details open>" if index == 0 else "<details>",
            f"<summary><strong>{CATEGORY_ICONS[category['key']]} {category['title']} ({len(by_category.get(category['key'], []))})</strong></summary>",
            "",
            "| Profile | Best for |",
            "|---|---|",
        ])
        for item, actual in by_category.get(category["key"], []):
            lines.append(f"| [**{actual['title']}**](goals/{item['file']}) | {actual['simple']} |")
        lines.extend(["", "</details>"])
    lines.extend([
        "",
        "When no preset fits, use the [**Custom Contract-Driven fallback**](skills/shape-goal/templates/custom-contract-driven-goal.md).",
        "",
        README_END,
    ])
    return "\n".join(lines)


def replace_readme_catalog(readme: str, section: str) -> str:
    if readme.count(README_START) != 1 or readme.count(README_END) != 1:
        raise ValueError("README.md must contain exactly one ordered pair of goal catalog markers")
    start = readme.index(README_START)
    end = readme.index(README_END)
    if start >= end:
        raise ValueError("README.md goal catalog markers are out of order")
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), flags=re.DOTALL)
    return pattern.sub(lambda _: section, readme, count=1)


def render_documents() -> dict[Path, str]:
    catalog = load_catalog()
    parsed = validate_catalog(catalog)
    documents: dict[Path, str] = {}
    for category in catalog["categories"]:
        documents[ROOT / category["collection"]] = render_collection(category, parsed)

    readme_path = ROOT / "README.md"
    if readme_path.is_symlink():
        raise ValueError("README.md may not be a symlink")
    readme = readme_path.read_text(encoding="utf-8")
    readme, count = PROFILE_BADGE.subn(
        f"![Profiles](https://img.shields.io/badge/profiles-{len(parsed)}-16A34A?style=flat-square)",
        readme,
    )
    if count != 1:
        raise ValueError(f"README.md must contain exactly one generated Profiles badge, found {count}")
    documents[readme_path] = replace_readme_catalog(readme, render_readme_catalog(catalog, parsed))

    category_title = {item["key"]: item["title"] for item in catalog["categories"]}
    lines = [
        "# Goal Catalog",
        "",
        "Interactive-first profiles. Start with `shape-goal`; each linked file also contains advanced autonomous preflight commands.",
        "",
        "| ID | Goal | Category | In simple terms |",
        "|---:|---|---|---|",
    ]
    for item, actual in parsed:
        lines.append(
            f"| {item['id']} | [{actual['title']}]({item['file']}) | {category_title[item['category']]} | {actual['simple']} |"
        )
    lines.extend(["", "The machine-readable source is [`catalog.json`](catalog.json)."])
    documents[ROOT / "goals" / "README.md"] = "\n".join(lines) + "\n"
    return documents


def check_documents(documents: dict[Path, str]) -> int:
    failed = False
    for path, expected in documents.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else ""
        if actual == expected:
            print(f"OK: {path.relative_to(ROOT)}")
            continue
        failed = True
        print(f"OUT OF DATE: {path.relative_to(ROOT)}", file=sys.stderr)
        print("\n".join(difflib.unified_diff(
            actual.splitlines(), expected.splitlines(),
            fromfile=str(path.relative_to(ROOT)),
            tofile=f"{path.relative_to(ROOT)} (generated)", lineterm="",
        )), file=sys.stderr)
    return 1 if failed else 0


def write_documents(documents: dict[Path, str]) -> int:
    for path, content in documents.items():
        atomic_write(path, content)
        print(f"Wrote {path.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        documents = render_documents()
        return check_documents(documents) if args.check else write_documents(documents)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
        print(f"Goal-doc sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
