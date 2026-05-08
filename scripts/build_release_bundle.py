#!/usr/bin/env python3
"""Build a downloadable release bundle for direct project copy/paste."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build release zip bundle")
    parser.add_argument(
        "--version",
        default="dev",
        help="Version label used in output file name (default: dev)",
    )
    parser.add_argument(
        "--output-dir",
        default="dist",
        help="Output directory for generated zip (default: dist)",
    )
    return parser.parse_args()


def copy_required_files(repo_root: Path, bundle_root: Path) -> None:
    shutil.copytree(repo_root / "multi-agent-framework", bundle_root / "multi-agent-framework")
    shutil.copy2(repo_root / ".project-config.yaml", bundle_root / ".project-config.yaml")
    shutil.copy2(
        repo_root / "multi-agent-framework" / "references" / "MEMORY_TEMPLATE.md",
        bundle_root / "MEMORIES.md",
    )
    shutil.copy2(
        repo_root / "multi-agent-framework" / "references" / "RELEASE.md",
        bundle_root / "RELEASE.md",
    )


def write_zip(source_dir: Path, target_zip: Path) -> None:
    with ZipFile(target_zip, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in sorted(source_dir.rglob("*")):
            if file_path.is_file():
                archive.write(file_path, arcname=file_path.relative_to(source_dir.parent))


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = repo_root / args.output_dir
    work_dir = output_dir / "release-work"
    bundle_name = "copilot-agent-framework"
    bundle_root = work_dir / bundle_name
    zip_path = output_dir / f"{bundle_name}-{args.version}.zip"

    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    copy_required_files(repo_root, bundle_root)
    if zip_path.exists():
        zip_path.unlink()
    write_zip(bundle_root, zip_path)
    shutil.rmtree(work_dir)

    print(f"Release bundle created: {zip_path}")


if __name__ == "__main__":
    main()
