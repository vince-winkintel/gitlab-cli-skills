---
name: glab-dependency-firewall
description: Inspect GitLab Dependency Firewall activity from local package-manager workflows with glab. Use when summarizing blocked or flagged packages from CI logs, reviewing .gitlab/df/ci-log.json, or troubleshooting Dependency Firewall exit codes. Triggers on dependency firewall, glab df, glab dependency-firewall, npm registry policy, ci-summary, blocked package, flagged package.
---

# glab dependency-firewall

Inspect GitLab Dependency Firewall activity for local package-manager workflows. The current command group is marked experimental, and the verified release binary exposes `ci-summary` only; do not rely on older `configure` examples unless live help on the target machine still lists them.

## Quick start

```bash
# Summarize the current working directory's Dependency Firewall CI log
glab dependency-firewall ci-summary
```

## Summarize CI activity

`ci-summary` reads `.gitlab/df/ci-log.json` relative to the current working directory. Run it from the same directory as the package-manager/Dependency Firewall operation that produced the log.

```bash
if glab dependency-firewall ci-summary; then
  echo "No blocked dependency entries"
else
  rc=$?
  case "$rc" in
    1) echo "Dependency Firewall log could not be read" >&2 ;;
    3) echo "Dependency Firewall blocked one or more packages" >&2 ;;
    *) echo "Unexpected Dependency Firewall failure: $rc" >&2 ;;
  esac
  exit "$rc"
fi
```

Exit codes:

- `0`: no blocked entries; allow-only, warnings-only, or no recorded activity.
- `1`: the log could not be read or parsed.
- `3`: one or more entries were blocked.

Treat exit `3` as a policy result, not a transient command failure. Surface the blocked package, version, and reason; do not bypass the policy or rewrite the log. Treat warnings as review input even though they do not fail the command.

## Troubleshooting

**No activity is reported:**
- Confirm `.gitlab/df/ci-log.json` exists under the current working directory used for the command.
- Do not assume a log in a repository root applies when the package manager ran in a nested workspace.

**A `configure` example fails:**
- `glab dependency-firewall configure` is not exposed by the verified current release binary.
- Re-check `glab dependency-firewall --help` on the target machine before using older docs or scripts.

**Unsupported package manager:**
- The current visible command surface does not configure package managers.
- Do not invent configuration for another manager; check live help or official docs for the target glab/GitLab version.

## Command reference

See [references/commands.md](references/commands.md) for captured help and flags.
