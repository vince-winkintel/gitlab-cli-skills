# Change Request: glab v1.91.0 skill updates

## Context
GitLab CLI `glab` v1.91.0 was released on 2026-04-01.
Release notes: https://gitlab.com/gitlab-org/cli/-/releases/v1.91.0

This repository documents user-facing `glab` command surfaces and recommended workflows. The skill set should be updated when a release adds, removes, or materially changes commands/flags that affect documented usage.

## Release-note audit
Relevant v1.91.0 release notes:

### Features
- `glab api`: add multipart/form-data support via `--form`

### Bug fixes / behavioral changes worth documenting
- auth: improve diagnostics when env-based token fails auth
- duo: lock Duo CLI auto-updates to compatible major version
- duo: improve Duo CLI confirm prompt UX

### Not skill-impacting for this repo
- release asset direct path URL-encoding fix
- nil pointer fix for issue display when `CreatedAt` is null
- internal script shebang fix
- docs standardization and dependency/maintenance changes

## Required documentation changes

### 1) `glab-api/SKILL.md`
Add v1.91.0 guidance for multipart/form-data requests:
- document `--form` in Overview/flags examples
- include at least one practical example, e.g. file upload or multipart field submission
- clearly distinguish `--form` from `--field` / `--raw-field`

### 2) top-level `SKILL.md`
Add a `v1.91.0 Updates` section summarizing user-facing changes that matter to this skill set:
- `glab-api`: multipart/form-data via `--form`
- `glab-auth`: improved diagnostics when env token auth fails (troubleshooting note, not a new workflow surface)
- `glab-duo`: Duo CLI auto-updates are locked to compatible major version; update docs to reflect current `glab duo` surface

### 3) `glab-auth/SKILL.md`
Add a troubleshooting note for env-token auth failures:
- if `GITLAB_TOKEN` / `GITLAB_ACCESS_TOKEN` / `OAUTH_TOKEN` is exported, it overrides stored credentials
- failed env-token auth should be diagnosed before assuming saved login is broken
- reinforce `glab auth status` and `glab api user` as the pre-flight checks before writes

### 4) `glab-duo/SKILL.md`
Update for current v1.91.0 surface:
- `glab duo` now exposes `ask` and `cli`
- prior `glab duo update` guidance is stale and should be removed or rewritten
- add a v1.91.0 note that `glab duo cli` is the relevant experimental surface
- avoid documenting subcommands not present in the live CLI help

## Constraints
- Prefer surgical doc updates only; no speculative features.
- Verify examples against live `glab --help` output where practical.
- Do not invent flags or commands not shown in current CLI or supported by release notes.
- Keep guidance consistent with existing multi-agent identity / review workflow rules.

## Acceptance criteria
- The repo includes a documented `v1.91.0 Updates` summary.
- `glab-api` docs accurately mention multipart/form-data support and show a concrete example.
- `glab-auth` docs mention improved env-token troubleshooting behavior.
- `glab-duo` docs match current `glab duo --help` output and remove stale `duo update` guidance.
- Changes are committed on a branch with an issue-linked PR.
- Sentinel and Probe both review the PR and all of their comments are resolved before final handoff.
