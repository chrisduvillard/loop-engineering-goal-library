#!/usr/bin/env python3
"""Build deterministic ZIP packages for the repository's Agent Skills."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
VERSION_FILE = ROOT / "VERSION"
SKILL_NAMES = ("shape-goal", "goal-engine")
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def read_version() -> str:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not version:
        raise ValueError("VERSION is empty")
    return version


def add_file(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(arcname, FIXED_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, source.read_bytes())


def write_skill_zip(skill_name: str, destination: Path) -> None:
    source_dir = SKILLS_DIR / skill_name
    if not (source_dir / "SKILL.md").is_file():
        raise FileNotFoundError(f"{source_dir}/SKILL.md is missing")

    with zipfile.ZipFile(destination, "w") as archive:
        for source in sorted(path for path in source_dir.rglob("*") if path.is_file()):
            add_file(archive, source, source.relative_to(source_dir).as_posix())


def write_bundle_zip(destination: Path) -> None:
    entries: list[tuple[str, Path]] = []
    for skill_name in SKILL_NAMES:
        source_dir = SKILLS_DIR / skill_name
        if not (source_dir / "SKILL.md").is_file():
            raise FileNotFoundError(f"{source_dir}/SKILL.md is missing")
        for source in (path for path in source_dir.rglob("*") if path.is_file()):
            arcname = Path("skills", skill_name, source.relative_to(source_dir)).as_posix()
            entries.append((arcname, source))

    with zipfile.ZipFile(destination, "w") as archive:
        for arcname, source in sorted(entries):
            add_file(archive, source, arcname)


def validate_zip(path: Path, *, individual: bool) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if names != sorted(names):
            raise ValueError(f"{path.name}: entries are not sorted")
        if len(names) != len(set(names)):
            raise ValueError(f"{path.name}: duplicate entries")
        if individual and "SKILL.md" not in names:
            raise ValueError(f"{path.name}: SKILL.md is not at the archive root")
        if not individual:
            for skill_name in SKILL_NAMES:
                expected = f"skills/{skill_name}/SKILL.md"
                if expected not in names:
                    raise ValueError(f"{path.name}: missing {expected}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(output_dir: Path) -> list[Path]:
    version = read_version()
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    artifacts: list[Path] = []
    for skill_name in SKILL_NAMES:
        path = output_dir / f"{skill_name}-{version}.zip"
        write_skill_zip(skill_name, path)
        validate_zip(path, individual=True)
        artifacts.append(path)

    bundle = output_dir / f"loop-engineering-skills-{version}.zip"
    write_bundle_zip(bundle)
    validate_zip(bundle, individual=False)
    artifacts.append(bundle)

    sums = output_dir / "SHA256SUMS"
    sums.write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in artifacts),
        encoding="utf-8",
    )
    artifacts.append(sums)
    return artifacts


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
        artifacts = build(args.output_dir.resolve())
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1

    print("Packaged Agent Skills:")
    for artifact in artifacts:
        print(f"- {artifact.relative_to(ROOT) if artifact.is_relative_to(ROOT) else artifact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
