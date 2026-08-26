#!/usr/bin/env python3
"""Build deterministic and path-safe ZIP packages for the Agent Skills."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import stat
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
VERSION_FILE = ROOT / "VERSION"
SKILL_NAMES = ("shape-goal", "goal-engine")
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
SEMVER = re.compile(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?")
ARTIFACT = re.compile(
    r"(?:shape-goal|goal-engine|loop-engineering-skills)-"
    r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?\.zip|SHA256SUMS"
)
MAX_SKILL_FILE_BYTES = 2 * 1024 * 1024
MAX_SKILL_TOTAL_BYTES = 16 * 1024 * 1024


def within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def read_version() -> str:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        raise ValueError(f"VERSION is not semantic: {version!r}")
    return version


def validate_archive_name(name: str) -> str:
    if not name or "\\" in name or "\x00" in name:
        raise ValueError(f"unsafe archive path: {name!r}")
    parsed = PurePosixPath(name)
    if parsed.is_absolute() or any(part in {"", ".", ".."} for part in parsed.parts):
        raise ValueError(f"unsafe archive path: {name!r}")
    return name


def collision_key(name: str) -> str:
    return unicodedata.normalize("NFC", name).casefold()


def source_files(source_dir: Path) -> list[tuple[str, Path]]:
    if source_dir.is_symlink() or not source_dir.is_dir():
        raise FileNotFoundError(f"{source_dir} is not a safe skill directory")

    entries: list[tuple[str, Path]] = []
    total = 0
    seen: dict[str, str] = {}
    for current, dirnames, filenames in os.walk(source_dir, followlinks=False):
        current_path = Path(current)
        for dirname in list(dirnames):
            candidate = current_path / dirname
            if candidate.is_symlink():
                raise ValueError(f"skill source contains a symlink directory: {candidate}")
        for filename in filenames:
            source = current_path / filename
            if source.is_symlink():
                raise ValueError(f"skill source contains a symlink file: {source}")
            mode = source.stat().st_mode
            if not stat.S_ISREG(mode):
                raise ValueError(f"skill source is not a regular file: {source}")
            size = source.stat().st_size
            if size > MAX_SKILL_FILE_BYTES:
                raise ValueError(f"skill source is too large: {source} ({size} bytes)")
            total += size
            if total > MAX_SKILL_TOTAL_BYTES:
                raise ValueError(f"skill source exceeds {MAX_SKILL_TOTAL_BYTES} bytes: {source_dir}")
            arcname = validate_archive_name(source.relative_to(source_dir).as_posix())
            key = collision_key(arcname)
            if key in seen:
                raise ValueError(
                    f"archive paths collide across case or Unicode normalization: {seen[key]!r} and {arcname!r}"
                )
            seen[key] = arcname
            entries.append((arcname, source))
    return sorted(entries)


def safe_output_dir(requested: Path) -> Path:
    if requested.exists() and requested.is_symlink():
        raise ValueError(f"output directory may not be a symlink: {requested}")
    output = requested.expanduser().resolve(strict=False)
    root = ROOT.resolve()
    if output == root or within(root, output):
        raise ValueError(f"refusing to use repository root or its ancestor as output: {output}")

    forbidden = (
        ROOT / ".git",
        ROOT / ".github",
        ROOT / "docs",
        ROOT / "examples",
        ROOT / "goals",
        ROOT / "scripts",
        ROOT / "skills",
        ROOT / "templates",
        ROOT / "tests",
    )
    for source_root in forbidden:
        source_root = source_root.resolve(strict=False)
        if output == source_root or within(output, source_root):
            raise ValueError(f"refusing to place generated packages inside source tree: {output}")

    if output.exists():
        if not output.is_dir():
            raise ValueError(f"output path is not a directory: {output}")
        for entry in output.iterdir():
            if entry.is_symlink() or not entry.is_file() or not ARTIFACT.fullmatch(entry.name):
                raise ValueError(
                    f"refusing to delete non-generated content from output directory: {entry}"
                )
    return output


def add_file(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(validate_archive_name(arcname), FIXED_TIMESTAMP)
    info.create_system = 3
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def write_skill_zip(skill_name: str, destination: Path) -> list[str]:
    source_dir = SKILLS_DIR / skill_name
    entries = source_files(source_dir)
    names = [name for name, _ in entries]
    if "SKILL.md" not in names:
        raise FileNotFoundError(f"{source_dir}/SKILL.md is missing")
    with zipfile.ZipFile(destination, "w") as archive:
        for arcname, source in entries:
            add_file(archive, source, arcname)
    return names


def write_bundle_zip(destination: Path) -> list[str]:
    entries: list[tuple[str, Path]] = []
    for skill_name in SKILL_NAMES:
        for relative, source in source_files(SKILLS_DIR / skill_name):
            entries.append((validate_archive_name(f"skills/{skill_name}/{relative}"), source))
    entries.sort()
    names = [name for name, _ in entries]
    with zipfile.ZipFile(destination, "w") as archive:
        for arcname, source in entries:
            add_file(archive, source, arcname)
    return names


def validate_zip(path: Path, expected_names: list[str]) -> None:
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            raise zipfile.BadZipFile(f"{path.name}: CRC failure in {bad}")
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if names != expected_names or names != sorted(names):
            raise ValueError(f"{path.name}: archive entries differ from the expected sorted manifest")
        if len(names) != len(set(names)):
            raise ValueError(f"{path.name}: duplicate entries")
        keys = [collision_key(validate_archive_name(name)) for name in names]
        if len(keys) != len(set(keys)):
            raise ValueError(f"{path.name}: case/Unicode-colliding entries")
        for info in infos:
            if info.is_dir() or info.flag_bits & 0x1:
                raise ValueError(f"{path.name}: directory or encrypted entry: {info.filename}")
            if info.date_time != FIXED_TIMESTAMP:
                raise ValueError(f"{path.name}: nondeterministic timestamp: {info.filename}")
            file_type = (info.external_attr >> 16) & 0o170000
            permissions = (info.external_attr >> 16) & 0o777
            if file_type != stat.S_IFREG or permissions != 0o644:
                raise ValueError(f"{path.name}: unsafe mode for {info.filename}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(output_dir: Path) -> list[Path]:
    version = read_version()
    output = safe_output_dir(output_dir)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix=f".{output.name}.tmp-", dir=output.parent))
    try:
        artifacts: list[Path] = []
        for skill_name in SKILL_NAMES:
            path = temp / f"{skill_name}-{version}.zip"
            names = write_skill_zip(skill_name, path)
            validate_zip(path, names)
            artifacts.append(path)

        bundle = temp / f"loop-engineering-skills-{version}.zip"
        bundle_names = write_bundle_zip(bundle)
        validate_zip(bundle, bundle_names)
        artifacts.append(bundle)

        sums = temp / "SHA256SUMS"
        sums.write_text(
            "".join(f"{sha256(path)}  {path.name}\n" for path in artifacts),
            encoding="utf-8",
        )
        artifacts.append(sums)

        if output.exists():
            shutil.rmtree(output)
        os.replace(temp, output)
        return [output / artifact.name for artifact in artifacts]
    except Exception:
        shutil.rmtree(temp, ignore_errors=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "dist",
        help="Directory for generated packages (default: dist)",
    )
    args = parser.parse_args()
    try:
        artifacts = build(args.output_dir)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1

    print("Packaged Agent Skills:")
    for artifact in artifacts:
        try:
            shown = artifact.relative_to(ROOT)
        except ValueError:
            shown = artifact
        print(f"- {shown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
