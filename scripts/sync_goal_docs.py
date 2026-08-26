#!/usr/bin/env python3
"""Generate goal collections and compact README catalogs from canonical goal files."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "goals" / "catalog.json"
README_START = "<!-- goal-catalog:start -->"
README_END = "<!-- goal-catalog:end -->"


def load_catalog() -> dict:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported goals/catalog.json schema_version")
    return data


def parse_goal(filename: str) -> dict[str, str]:
    path = ROOT / "goals" / filename
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"goals/{filename} must begin with one H1 title")

    def match(pattern: str, label: str) -> str:
        found = re.search(pattern, text, flags=re.MULTILINE)
        if not found:
            raise ValueError(f"goals/{filename} is missing {label}")
        return found.group(1).strip()

    commands = re.findall(r"```text\n(/goal .*?)\n```", text, flags=re.DOTALL)
    if len(commands) < 2:
        raise ValueError(f"goals/{filename} must contain two advanced /goal preflights")

    return {
        "title": lines[0][2:].strip(),
        "use_when": match(r"^\*\*Use when:\*\* (.+)$", "Use when"),
        "simple": match(r"^\*\*In simple terms:\*\* (.+)$", "In simple terms"),
        "command": commands[0].strip(),
        "fallback": commands[1].strip(),
        "why": match(r"^\*\*Why it works:\*\* (.+)$", "Why it works"),
    }


def validate_catalog(catalog: dict) -> list[tuple[dict, dict[str, str]]]:
    category_keys = {item["key"] for item in catalog["categories"]}
    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    parsed: list[tuple[dict, dict[str, str]]] = []

    for item in catalog["goals"]:
        goal_id = item["id"]
        filename = item["file"]
        if goal_id in seen_ids:
            raise ValueError(f"Duplicate goal id: {goal_id}")
        if filename in seen_files:
            raise ValueError(f"Duplicate goal file: {filename}")
        if item["category"] not in category_keys:
            raise ValueError(f"Unknown category for {filename}: {item['category']}")
        seen_ids.add(goal_id)
        seen_files.add(filename)

        actual = parse_goal(filename)
        for field in ("title", "use_when", "simple"):
            if actual[field] != item[field]:
                raise ValueError(f"goals/{filename} {field} differs from goals/catalog.json")
        parsed.append((item, actual))

    disk_files = {
        path.name
        for path in (ROOT / "goals").glob("*.md")
        if path.name != "README.md"
    }
    if disk_files != seen_files:
        missing = sorted(seen_files - disk_files)
        extra = sorted(disk_files - seen_files)
        raise ValueError(f"Catalog/file mismatch. Missing={missing}; extra={extra}")
    return parsed


def interactive_commands(title: str) -> tuple[str, str]:
    return (
        f"/shape-goal Use the {title} profile",
        f"$shape-goal Use the {title} profile",
    )


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
        "You usually do not need to choose one: `shape-goal` can select the best profile from repository evidence. "
        "Choose directly only when the type of work is already clear.",
    ]
    for index, category in enumerate(catalog["categories"]):
        open_attr = " open" if index == 0 else ""
        lines.extend([
            "",
            f"<details{open_attr}>",
            f"<summary><strong>{category['title']} ({len(by_category.get(category['key'], []))})</strong></summary>",
            "",
            "| Profile | Best for |",
            "|---|---|",
        ])
        for item, actual in by_category.get(category["key"], []):
            lines.append(
                f"| [**{actual['title']}**](goals/{item['file']}) | {actual['simple']} |"
            )
        lines.extend(["", "</details>"])

    lines.extend([
        "",
        "When no preset fits, use the [**Custom Contract-Driven fallback**](skills/shape-goal/templates/custom-contract-driven-goal.md).",
        "",
        README_END,
    ])
    return "\n".join(lines)


def replace_readme_catalog(readme: str, section: str) -> str:
    if README_START not in readme or README_END not in readme:
        raise ValueError("README.md is missing goal catalog markers")
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), flags=re.DOTALL)
    return pattern.sub(section, readme)


def render_documents() -> dict[Path, str]:
    catalog = load_catalog()
    parsed = validate_catalog(catalog)
    documents: dict[Path, str] = {}
    for category in catalog["categories"]:
        documents[ROOT / category["collection"]] = render_collection(category, parsed)

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    documents[readme_path] = replace_readme_catalog(readme, render_readme_catalog(catalog, parsed))

    goal_index_lines = [
        "# Goal Catalog",
        "",
        "Interactive-first profiles. Start with `shape-goal`; each linked file also contains advanced autonomous preflight commands.",
        "",
        "| ID | Goal | Category | In simple terms |",
        "|---:|---|---|---|",
    ]
    category_title = {item["key"]: item["title"] for item in catalog["categories"]}
    for item, actual in parsed:
        goal_index_lines.append(
            f"| {item['id']} | [{actual['title']}]({item['file']}) | "
            f"{category_title[item['category']]} | {actual['simple']} |"
        )
    goal_index_lines.extend(["", "The machine-readable source is [`catalog.json`](catalog.json)."])
    documents[ROOT / "goals" / "README.md"] = "\n".join(goal_index_lines) + "\n"
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
        diff = difflib.unified_diff(
            actual.splitlines(),
            expected.splitlines(),
            fromfile=str(path.relative_to(ROOT)),
            tofile=f"{path.relative_to(ROOT)} (generated)",
            lineterm="",
        )
        print("\n".join(diff), file=sys.stderr)
    return 1 if failed else 0


def write_documents(documents: dict[Path, str]) -> int:
    for path, content in documents.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
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
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Goal-doc sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
