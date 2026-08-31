#!/usr/bin/env python3
"""Build deterministic, path-safe, reference-closed ZIP packages."""

from __future__ import annotations

import argparse
import hashlib
import os
import posixpath
import re
import shutil
import stat
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path, PurePosixPath
from typing import Iterable, List, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
VERSION_FILE = ROOT / "VERSION"
SKILL_NAMES = ("shape-goal", "goal-engine")
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
SEMVER_TEXT = (
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
SEMVER = re.compile(SEMVER_TEXT)
GENERATED_ARTIFACT = re.compile(
    rf"(?:(?:shape-goal|goal-engine|loop-engineering-skills)-(?:{SEMVER_TEXT})\.zip|SHA256SUMS)"
)
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_PACKAGE_BYTES = 16 * 1024 * 1024
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")
CODE_PATH = re.compile(
    r"`((?:\./|\.\./|references/|templates/|agents/|scripts/|schemas/|profiles/)[^`\s]+\.md(?:#[^`\s]+)?)`"
)
LOCAL_PREFIXES = ("./", "../", "references/", "templates/", "agents/", "scripts/", "schemas/", "profiles/")


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def read_version() -> str:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        raise ValueError(f"VERSION is not semantic; expected a safe semantic version: {version!r}")
    return version


def safe_archive_name(name: str) -> str:
    if not name or "\x00" in name or "\\" in name:
        raise ValueError(f"unsafe archive path: {name!r}")
    candidate = PurePosixPath(name)
    if candidate.is_absolute() or any(part in {"", ".", ".."} for part in candidate.parts):
        raise ValueError(f"unsafe archive path: {name!r}")
    normalized = unicodedata.normalize("NFC", candidate.as_posix())
    if normalized != name:
        raise ValueError(f"archive path is not NFC-normalized: {name!r}")
    return normalized


def validate_unique_names(names: Sequence[str]) -> None:
    seen = {}
    for name in names:
        safe_archive_name(name)
        key = unicodedata.normalize("NFC", name).casefold()
        previous = seen.get(key)
        if previous is not None:
            raise ValueError(
                f"archive paths collide after case-folding or Unicode normalization: {previous!r} and {name!r}"
            )
        seen[key] = name


def collect_source_entries(skill_name: str, *, bundle: bool) -> List[Tuple[str, Path]]:
    source_dir = SKILLS_DIR / skill_name
    skill_file = source_dir / "SKILL.md"
    if source_dir.is_symlink() or not skill_file.is_file() or skill_file.is_symlink():
        raise FileNotFoundError(f"{skill_file} is missing or unsafe")
    entries: List[Tuple[str, Path]] = []
    total_size = 0
    for directory, dirnames, filenames in os.walk(str(source_dir), followlinks=False):
        directory_path = Path(directory)
        for dirname in list(dirnames):
            candidate = directory_path / dirname
            if candidate.is_symlink():
                raise ValueError(f"skill source contains a symlinked directory: {candidate}")
        for filename in filenames:
            source = directory_path / filename
            if source.is_symlink():
                raise ValueError(f"skill source contains a symlinked file: {source}")
            mode = source.stat().st_mode
            if not stat.S_ISREG(mode):
                raise ValueError(f"skill source is not a regular file: {source}")
            size = source.stat().st_size
            if size > MAX_FILE_BYTES:
                raise ValueError(f"skill source is unexpectedly large ({size} bytes): {source}")
            total_size += size
            if total_size > MAX_PACKAGE_BYTES:
                raise ValueError(f"skill package exceeds {MAX_PACKAGE_BYTES} uncompressed bytes")
            relative = source.relative_to(source_dir).as_posix()
            arcname = f"skills/{skill_name}/{relative}" if bundle else relative
            entries.append((safe_archive_name(arcname), source))
    entries.sort(key=lambda item: item[0])
    validate_unique_names([name for name, _ in entries])
    expected_skill = f"skills/{skill_name}/SKILL.md" if bundle else "SKILL.md"
    if expected_skill not in {name for name, _ in entries}:
        raise ValueError(f"{skill_name}: SKILL.md is not at the expected archive location")
    return entries


def add_file(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(safe_archive_name(arcname), FIXED_TIMESTAMP)
    info.create_system = 3
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def write_zip(entries: Sequence[Tuple[str, Path]], destination: Path) -> None:
    with zipfile.ZipFile(str(destination), "w", allowZip64=True) as archive:
        for arcname, source in entries:
            add_file(archive, source, arcname)


def local_markdown_targets(text: str) -> Iterable[str]:
    candidates = [match.group(1).strip() for match in MARKDOWN_LINK.finditer(text)]
    candidates.extend(match.group(1).strip() for match in CODE_PATH.finditer(text))
    for candidate in candidates:
        if candidate.startswith(("http://", "https://", "mailto:", "#", "/")):
            continue
        path = candidate.split("#", 1)[0].split("?", 1)[0]
        if not path.endswith(".md"):
            continue
        if path in {"SKILL.md", "goal-contract-template.md"} or path.startswith(LOCAL_PREFIXES):
            yield path


def validate_markdown_references(archive: zipfile.ZipFile, names: Sequence[str]) -> None:
    available = set(names)
    for name in names:
        if not name.endswith(".md"):
            continue
        try:
            text = archive.read(name).decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError(f"{archive.filename}: Markdown member is not UTF-8: {name}") from error
        parent = posixpath.dirname(name)
        for target in local_markdown_targets(text):
            resolved = posixpath.normpath(posixpath.join(parent, target))
            if resolved == ".." or resolved.startswith("../") or resolved.startswith("/"):
                raise ValueError(f"{archive.filename}: local reference escapes the package: {name} -> {target}")
            if resolved not in available:
                raise ValueError(f"{archive.filename}: unresolved local reference: {name} -> {target} ({resolved})")


def validate_zip(path: Path, expected: Sequence[Tuple[str, Path]], *, individual: bool) -> None:
    expected_names = [name for name, _ in expected]
    validate_unique_names(expected_names)
    with zipfile.ZipFile(str(path)) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise ValueError(f"{path.name}: corrupt member {bad}")
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if names != expected_names or names != sorted(names):
            raise ValueError(f"{path.name}: archive members differ from the expected sorted manifest")
        validate_unique_names(names)
        for info, (name, source) in zip(infos, expected):
            if info.filename != name:
                raise ValueError(f"{path.name}: member order mismatch")
            if info.is_dir() or info.flag_bits & 0x1:
                raise ValueError(f"{path.name}: directories and encrypted members are not allowed")
            if info.date_time != FIXED_TIMESTAMP:
                raise ValueError(f"{path.name}: non-deterministic timestamp for {name}")
            if info.compress_type != zipfile.ZIP_DEFLATED:
                raise ValueError(f"{path.name}: unexpected compression type for {name}")
            mode = (info.external_attr >> 16) & 0xFFFF
            if stat.S_IFMT(mode) != stat.S_IFREG or stat.S_IMODE(mode) != 0o644:
                raise ValueError(f"{path.name}: unsafe or non-deterministic mode for {name}")
            if archive.read(name) != source.read_bytes():
                raise ValueError(f"{path.name}: packaged content differs from its source for {name}")
        if individual and "SKILL.md" not in names:
            raise ValueError(f"{path.name}: SKILL.md is not at the archive root")
        if not individual:
            for skill_name in SKILL_NAMES:
                expected_skill = f"skills/{skill_name}/SKILL.md"
                if expected_skill not in names:
                    raise ValueError(f"{path.name}: missing {expected_skill}")
        validate_markdown_references(archive, names)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_safe_output_dir(output_dir: Path) -> Path:
    if output_dir.exists() and output_dir.is_symlink():
        raise ValueError(f"output directory must not be a symlink: {output_dir}")
    resolved = output_dir.expanduser().resolve(strict=False)
    root = ROOT.resolve()
    skills = SKILLS_DIR.resolve()
    if resolved == root or is_relative_to(root, resolved):
        raise ValueError(f"refusing to delete the repository or one of its ancestors: {resolved}")
    protected_roots = (
        skills,
        (root / ".git").resolve(strict=False),
        (root / ".github").resolve(strict=False),
        (root / "scripts").resolve(strict=False),
        (root / "tests").resolve(strict=False),
        (root / "goals").resolve(strict=False),
        (root / "docs").resolve(strict=False),
        (root / "examples").resolve(strict=False),
        (root / "templates").resolve(strict=False),
    )
    for protected in protected_roots:
        if resolved == protected or is_relative_to(resolved, protected):
            raise ValueError(f"output directory overlaps protected source content: {resolved}")
    if resolved.exists():
        if not resolved.is_dir():
            raise ValueError(f"output path is not a directory: {resolved}")
        for entry in resolved.iterdir():
            if entry.is_symlink() or entry.is_dir() or not GENERATED_ARTIFACT.fullmatch(entry.name):
                raise ValueError(f"refusing to remove a non-generated entry from the output directory: {entry}")
    return resolved


def build(output_dir: Path) -> List[Path]:
    version = read_version()
    output_dir = ensure_safe_output_dir(output_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{output_dir.name}.tmp-", dir=str(output_dir.parent)))
    artifact_names: List[str] = []
    try:
        for skill_name in SKILL_NAMES:
            entries = collect_source_entries(skill_name, bundle=False)
            name = f"{skill_name}-{version}.zip"
            path = temporary / name
            write_zip(entries, path)
            validate_zip(path, entries, individual=True)
            artifact_names.append(name)
        bundle_entries: List[Tuple[str, Path]] = []
        for skill_name in SKILL_NAMES:
            bundle_entries.extend(collect_source_entries(skill_name, bundle=True))
        bundle_entries.sort(key=lambda item: item[0])
        validate_unique_names([name for name, _ in bundle_entries])
        bundle_name = f"loop-engineering-skills-{version}.zip"
        bundle = temporary / bundle_name
        write_zip(bundle_entries, bundle)
        validate_zip(bundle, bundle_entries, individual=False)
        artifact_names.append(bundle_name)
        sums = temporary / "SHA256SUMS"
        with sums.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write("".join(f"{sha256(temporary / name)}  {name}\n" for name in artifact_names))
        artifact_names.append("SHA256SUMS")
        if output_dir.exists():
            shutil.rmtree(str(output_dir))
        os.replace(str(temporary), str(output_dir))
    except Exception:
        shutil.rmtree(str(temporary), ignore_errors=True)
        raise
    return [output_dir / name for name in artifact_names]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    try:
        artifacts = build(args.output_dir)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1
    print("Packaged Agent Skills:")
    for artifact in artifacts:
        try:
            display = artifact.relative_to(ROOT)
        except ValueError:
            display = artifact
        print(f"- {display}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
