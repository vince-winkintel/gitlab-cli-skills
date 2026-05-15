#!/usr/bin/env python3
from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class RefreshAutomationTests(unittest.TestCase):
    def copy_repo(self) -> pathlib.Path:
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="gitlab-cli-skills-refresh-test-"))
        dest = tmp / "repo"
        ignore = shutil.ignore_patterns(".git", "generated-artifacts", "refresh-summary.md", "claude-skill.zip", "__pycache__")
        shutil.copytree(ROOT, dest, ignore=ignore)
        return dest

    def run_cmd(self, repo: pathlib.Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            args,
            cwd=repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )

    def test_no_op_refresh_is_no_op_after_generation(self) -> None:
        repo = self.copy_repo()
        self.run_cmd(repo, "bash", "scripts/refresh-skill.sh", "--summary", "refresh-summary.md", "--manifest", ".github/refresh-manifest.json")
        before = {
            "README.md": (repo / "README.md").read_text(encoding="utf-8"),
            ".github/refresh-manifest.json": (repo / ".github/refresh-manifest.json").read_text(encoding="utf-8"),
        }

        result = self.run_cmd(repo, "bash", "scripts/refresh-skill.sh", "--summary", "refresh-summary.md", "--manifest", ".github/refresh-manifest.json")
        after = {
            "README.md": (repo / "README.md").read_text(encoding="utf-8"),
            ".github/refresh-manifest.json": (repo / ".github/refresh-manifest.json").read_text(encoding="utf-8"),
        }

        self.assertEqual(before, after)
        self.assertIn("No generated changes detected", result.stdout)
        self.run_cmd(repo, "bash", "scripts/validate-skill.sh")

    def test_generated_change_is_reviewable_in_summary_without_writing_dry_run(self) -> None:
        repo = self.copy_repo()
        extra = repo / "glab-zeta"
        extra.mkdir()
        (extra / "SKILL.md").write_text(
            "---\nname: glab-zeta\ndescription: Fixture skill for refresh automation tests.\n---\n\n# glab zeta\n",
            encoding="utf-8",
        )
        before_readme = (repo / "README.md").read_text(encoding="utf-8")

        result = self.run_cmd(
            repo,
            "bash",
            "scripts/refresh-skill.sh",
            "--dry-run",
            "--summary",
            "refresh-summary.md",
            "--manifest",
            ".github/refresh-manifest.json",
        )
        summary = (repo / "refresh-summary.md").read_text(encoding="utf-8")

        self.assertEqual(before_readme, (repo / "README.md").read_text(encoding="utf-8"))
        self.assertIn("Dry run complete", result.stdout)
        self.assertIn("README.md", summary)
        self.assertIn(".github/refresh-manifest.json", summary)
        self.assertIn("glab-zeta", summary)
        self.assertIn("```diff", summary)
        self.assertNotIn(str(repo), summary)


if __name__ == "__main__":
    unittest.main(verbosity=2)
