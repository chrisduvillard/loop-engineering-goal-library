#!/usr/bin/env python3
"""Apply one-time validator updates for the interactive-first dogfood release."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "scripts" / "validate_repository.py"
text = path.read_text(encoding="utf-8")

text = text.replace('            "**Pursuing goal**",\n', '            "Pursuing goal",\n')

anchor = '        "docs/goals/INDEX.md",\n'
addition = (
    '        "docs/goals/INDEX.md",\n'
    '        "docs/goals/2026-08-26-interactive-shaping-first/SHAPING.md",\n'
    '        "docs/goals/2026-08-26-interactive-shaping-first/CONTRACT.md",\n'
    '        "docs/goals/2026-08-26-interactive-shaping-first/PROGRESS.md",\n'
    '        "docs/goals/2026-08-26-interactive-shaping-first/UAT.md",\n'
)
if 'docs/goals/2026-08-26-interactive-shaping-first/UAT.md' not in text:
    if anchor not in text:
        raise SystemExit("required-path anchor not found")
    text = text.replace(anchor, addition, 1)

docs_anchor = '''    require_fragments(
        require("SOURCES.md"),
        (
            "ordinary interactive conversation",
            "another turn begins automatically",
            "stop as **Approval required**",
        ),
    )
'''
dogfood = docs_anchor + '''    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/SHAPING.md"),
        (
            "Main entry point",
            "Question behavior",
            "No additional owner question was necessary",
            "Approval round:** R1",
        ),
    )
    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/CONTRACT.md"),
        (
            "The library uses `shape-goal` as the clear interactive entry point",
            "All 24 profile files expose interactive `shape-goal` commands first",
            "only `main` remains",
        ),
    )
    require_fragments(
        require("docs/goals/2026-08-26-interactive-shaping-first/UAT.md"),
        (
            "Scenario A — Normal interactive shaping",
            "Steer is not required",
            "Scenario C — Owner decision discovered during autonomous execution",
            "Honest boundary",
        ),
    )

    readme = require("README.md")
    if readme.exists() and len(readme.read_text(encoding="utf-8").splitlines()) > 230:
        fail("README.md is too long; keep the generated landing page at 230 lines or fewer")
'''
if 'README.md is too long' not in text:
    if docs_anchor not in text:
        raise SystemExit("dogfood validation anchor not found")
    text = text.replace(docs_anchor, dogfood, 1)

path.write_text(text, encoding="utf-8")
