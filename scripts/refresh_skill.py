#!/usr/bin/env python3
"""Refresh generated repository metadata for gitlab-cli-skills.

This prototype intentionally keeps generation deterministic: no timestamps,
absolute paths, or environment-specific values are written to tracked files.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Iterable

REPO_SLUG = "vince-winkintel/gitlab-cli-skills"
REFRESH_VERSION = 1
README_START = "### Available Skills"
README_END = "## Installation"


@dataclass(frozen=True)
class PlannedWrite:
    path: pathlib.Path
    old: str | None
    new: str

    @property
    def changed(self) -> bool:
        return self.old != self.new


def repo_root_from_here() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def read_text(path: pathlib.Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def skill_dirs(root: pathlib.Path) -> list[str]:
    names: list[str] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        if child.name.startswith(".") or child.name in {"scripts", "tests", "generated-artifacts"}:
            continue
        if (child / "SKILL.md").is_file():
            names.append(child.name)
    return sorted(names)


def file_sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def generate_readme(existing: str, skills: list[str]) -> str:
    start = existing.find(README_START)
    if start == -1:
        raise ValueError(f"README.md missing marker: {README_START!r}")
    end = existing.find(README_END, start)
    if end == -1:
        raise ValueError(f"README.md missing marker after skill list: {README_END!r}")

    before = existing[: start + len(README_START)]
    after = existing[end:]
    generated = "\n\n" + "\n".join(f"- [`{name}`](./{name})" for name in skills) + "\n\n"
    return before + generated + after


def manifest_payload(root: pathlib.Path, skills: list[str]) -> dict:
    version_file = root / "VERSION"
    version = "unknown"
    if version_file.exists():
        version = version_file.read_text(encoding="utf-8").splitlines()[0].strip() or "unknown"
    tracked_outputs = ["README.md"]
    checksums = {
        rel: file_sha256(root / rel)
        for rel in tracked_outputs
        if (root / rel).exists()
    }
    return {
        "repo": REPO_SLUG,
        "refresh_version": REFRESH_VERSION,
        "source": {
            "type": "repository-filesystem",
            "version_file": "VERSION",
            "glab_version": version,
        },
        "generated_by": "scripts/refresh-skill.sh",
        "tracked_outputs": tracked_outputs,
        "skill_count": len(skills),
        "skills": skills,
        "checksums": checksums,
    }


def generate_manifest(root: pathlib.Path, skills: list[str], readme_text: str) -> str:
    # Checksums must describe the generated README, not necessarily the on-disk README
    # when this is called before writes are applied.
    tmp_root = root
    payload = manifest_payload(tmp_root, skills)
    payload["checksums"]["README.md"] = hashlib.sha256(readme_text.encode("utf-8")).hexdigest()
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def plan(root: pathlib.Path, manifest_path: pathlib.Path) -> list[PlannedWrite]:
    skills = skill_dirs(root)
    readme_path = root / "README.md"
    old_readme = read_text(readme_path)
    if old_readme is None:
        raise FileNotFoundError(readme_path)
    new_readme = generate_readme(old_readme, skills)

    old_manifest = read_text(manifest_path)
    new_manifest = generate_manifest(root, skills, new_readme)
    return [
        PlannedWrite(readme_path, old_readme, new_readme),
        PlannedWrite(manifest_path, old_manifest, new_manifest),
    ]


def diff_for_write(write: PlannedWrite, root: pathlib.Path) -> str:
    old = "" if write.old is None else write.old
    rel = write.path.relative_to(root).as_posix()
    return "".join(
        difflib.unified_diff(
            old.splitlines(keepends=True),
            write.new.splitlines(keepends=True),
            fromfile=f"a/{rel}",
            tofile=f"b/{rel}",
        )
    )


def write_summary(path: pathlib.Path, root: pathlib.Path, planned: list[PlannedWrite], dry_run: bool, source_url_override: str) -> None:
    changed = [w for w in planned if w.changed]
    lines = [
        "# Refresh summary",
        "",
        f"- Repository: {REPO_SLUG}",
        f"- Dry run: {str(dry_run).lower()}",
        f"- Source URL override: {source_url_override or 'none'}",
        f"- Tracked files with generated changes: {len(changed)}",
        "",
        "## Generated changes",
    ]
    if changed:
        for write in changed:
            lines.append(f"- `{write.path.relative_to(root).as_posix()}`")
    else:
        lines.append("No generated changes detected.")
    lines.extend(["", "## Review diff"])
    if changed:
        lines.append("```diff")
        for write in changed:
            lines.append(diff_for_write(write, root).rstrip())
        lines.append("```")
    else:
        lines.append("No diff; generated output already matches the repository state.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def assert_reviewable(planned: Iterable[PlannedWrite], root: pathlib.Path) -> None:
    for write in planned:
        if not write.changed:
            continue
        rel = write.path.relative_to(root).as_posix()
        if write.path.is_absolute() and str(root) in write.new:
            raise ValueError(f"generated output for {rel} contains local repo path")
        if re.search(r"/Users/[A-Za-z0-9._-]+/", write.new):
            raise ValueError(f"generated output for {rel} contains a macOS user path")
        if re.search(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[A-Za-z0-9_./+=-]{12,}", write.new):
            raise ValueError(f"generated output for {rel} appears to contain a secret")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Refresh generated gitlab-cli-skills metadata.")
    parser.add_argument("--root", default=str(repo_root_from_here()), help="Repository root; defaults to this script's parent.")
    parser.add_argument("--summary", default="refresh-summary.md", help="Path for a human-readable refresh summary.")
    parser.add_argument("--manifest", default=".github/refresh-manifest.json", help="Path for the tracked refresh manifest.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write tracked generated files.")
    parser.add_argument("--force", action="store_true", help="Accepted for workflow compatibility; generation is deterministic and always planned.")
    parser.add_argument("--source-url-override", default="", help="Recorded in the untracked summary for reviewer context.")
    args = parser.parse_args(argv)

    root = pathlib.Path(args.root).resolve()
    manifest_path = pathlib.Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = root / manifest_path
    summary_path = pathlib.Path(args.summary)
    if not summary_path.is_absolute():
        summary_path = root / summary_path

    planned = plan(root, manifest_path)
    assert_reviewable(planned, root)
    write_summary(summary_path, root, planned, args.dry_run, args.source_url_override)

    changed = [w for w in planned if w.changed]
    if args.dry_run:
        print(f"Dry run complete: {len(changed)} tracked file(s) would change.")
        return 0

    for write in planned:
        if not write.changed:
            continue
        write.path.parent.mkdir(parents=True, exist_ok=True)
        write.path.write_text(write.new, encoding="utf-8")
        print(f"Updated {write.path.relative_to(root).as_posix()}")
    if not changed:
        print("No generated changes detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
