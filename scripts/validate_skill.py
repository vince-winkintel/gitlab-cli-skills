#!/usr/bin/env python3
"""Validate generated gitlab-cli-skills refresh metadata."""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
import zipfile

REPO_SLUG = "vince-winkintel/gitlab-cli-skills"


def repo_root_from_here() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def skill_dirs(root: pathlib.Path) -> list[str]:
    return sorted(
        child.name
        for child in root.iterdir()
        if child.is_dir()
        and not child.name.startswith(".")
        and child.name not in {"scripts", "tests", "generated-artifacts"}
        and (child / "SKILL.md").is_file()
    )


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def validate_readme(root: pathlib.Path, skills: list[str]) -> None:
    readme = (root / "README.md").read_text(encoding="utf-8")
    missing = [name for name in skills if f"- [`{name}`](./{name})" not in readme]
    if missing:
        fail(f"README.md missing generated skill links: {', '.join(missing)}")
    listed = re.findall(r"^- \[`([^`]+)`\]\(\.\/[^)]+\)$", readme, flags=re.MULTILINE)
    listed_glab = sorted(name for name in listed if name.startswith("glab-"))
    if listed_glab != skills:
        fail("README.md skill list is not synchronized with SKILL.md directories")


def validate_manifest(root: pathlib.Path, skills: list[str]) -> None:
    manifest_path = root / ".github" / "refresh-manifest.json"
    if not manifest_path.is_file():
        fail(".github/refresh-manifest.json does not exist; run scripts/refresh-skill.sh")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("repo") != REPO_SLUG:
        fail(f"manifest repo mismatch: {manifest.get('repo')!r}")
    if manifest.get("generated_by") != "scripts/refresh-skill.sh":
        fail("manifest generated_by must be scripts/refresh-skill.sh")
    if manifest.get("skills") != skills:
        fail("manifest skill list is not synchronized with SKILL.md directories")
    if manifest.get("skill_count") != len(skills):
        fail("manifest skill_count is not synchronized")
    version = (root / "VERSION").read_text(encoding="utf-8").splitlines()[0].strip()
    if manifest.get("source", {}).get("glab_version") != version:
        fail("manifest glab_version is not synchronized with VERSION")
    readme = (root / "README.md").read_text(encoding="utf-8")
    if manifest.get("checksums", {}).get("README.md") != sha256_text(readme):
        fail("manifest README.md checksum is stale")


def validate_no_local_leaks(root: pathlib.Path) -> None:
    deny = [
        re.compile(r"/Users/[A-Za-z0-9._-]+/"),
        re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[A-Za-z0-9_./+=-]{12,}"),
    ]
    include = [root / "README.md", root / ".github" / "refresh-manifest.json"]
    offenders: list[str] = []
    for path in include:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(text) for pattern in deny):
            offenders.append(path.relative_to(root).as_posix())
    if offenders:
        fail("potential secret or local path leak in " + ", ".join(offenders))


def validate_claude_zip(path: pathlib.Path | None) -> None:
    if path is None or not path.exists():
        return
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    skill_files = [name for name in names if name.endswith("/SKILL.md")]
    if len(skill_files) != 1:
        fail(f"expected exactly one packaged SKILL.md in {path}, found {skill_files}")
    top_levels = {name.split("/")[0] for name in names if "/" in name}
    if len(top_levels) != 1:
        fail(f"expected one top-level directory in {path}, found {sorted(top_levels)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate gitlab-cli-skills generated refresh metadata.")
    parser.add_argument("--root", default=str(repo_root_from_here()))
    parser.add_argument("--claude-zip", default="", help="Optional claude-skill.zip path to validate.")
    args = parser.parse_args(argv)

    root = pathlib.Path(args.root).resolve()
    skills = skill_dirs(root)
    if not skills:
        fail("no sub-skill directories found")
    validate_readme(root, skills)
    validate_manifest(root, skills)
    validate_no_local_leaks(root)
    zip_path = pathlib.Path(args.claude_zip).resolve() if args.claude_zip else None
    validate_claude_zip(zip_path)
    print(f"Validation passed: {len(skills)} skills, manifest synchronized, no generated leaks detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
