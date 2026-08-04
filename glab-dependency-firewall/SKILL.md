---
name: glab-dependency-firewall
description: Configure and inspect GitLab Dependency Firewall for local package-manager workflows with glab. Use when setting npm resolve/deploy registry URLs, reviewing .gitlab/df/config.json, summarizing blocked or flagged packages from CI logs, or troubleshooting Dependency Firewall exit codes. Triggers on dependency firewall, glab df, glab dependency-firewall, npm registry policy, ci-summary, blocked package.
---

# glab dependency-firewall

Configure and monitor GitLab Dependency Firewall for local package managers. The command group is beta; verify live help before relying on it in long-lived automation.

## Quick start

```bash
# Configure both npm registry paths from the package-manager working directory
glab dependency-firewall configure npm \
  --repo-resolve https://gitlab.com/api/v4/projects/42/packages/npm/ \
  --repo-deploy https://gitlab.com/api/v4/projects/42/packages/npm/

# Preserve the existing deploy URL and update only the resolve URL
glab df configure npm \
  --repo-resolve https://gitlab.com/api/v4/projects/42/packages/npm/

# Summarize the current working directory's Dependency Firewall CI log
glab dependency-firewall ci-summary
```

## Configure npm registry URLs

`configure` currently supports `npm`. It writes `.gitlab/df/config.json` relative to the current working directory, so run it from the same directory where npm will run. Only explicitly supplied values are changed; omitted values, other package-manager blocks, and unknown keys are preserved.

Before writing:

1. Confirm the intended project/package registry URLs.
2. Run from the package-manager working directory.
3. Do not embed access tokens or other credentials in registry URLs.
4. Review the resulting config diff before committing it.

```bash
# Resolve/install only
glab dependency-firewall configure npm \
  --repo-resolve https://gitlab.example.com/api/v4/projects/42/packages/npm/

# Publish/deploy only; existing resolve configuration is preserved
glab dependency-firewall configure npm \
  --repo-deploy https://gitlab.example.com/api/v4/projects/42/packages/npm/

git diff -- .gitlab/df/config.json
```

At least one of `--repo-resolve` or `--repo-deploy` is required. The command does not accept `--repo`; its configuration is local to the current working directory.

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

**Config changed the wrong checkout:**
- Revert the unintended `.gitlab/df/config.json` change.
- Change to the package-manager working directory and rerun with the verified URL.

**Unsupported package manager:**
- The current command surface supports `npm` only.
- Do not invent configuration for another manager; check a newer `glab dependency-firewall configure --help` or official docs.

## Command reference

See [references/commands.md](references/commands.md) for captured help and flags.
