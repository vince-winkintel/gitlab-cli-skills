---
name: glab-dependency-firewall
description: Run supported package managers through GitLab Dependency Firewall and inspect local firewall activity with glab. Use when enforcing dependency policy for Bundler, gem, Gradle, Maven, npm, pip, Pipenv, pnpm, Poetry, Twine, or uv; summarizing blocked or flagged packages from CI logs; reviewing .gitlab/df/ci-log.json; or troubleshooting Dependency Firewall exit codes. Triggers on dependency firewall, glab df, glab dependency-firewall, package policy, ci-summary, blocked package, flagged package.
---

# glab dependency-firewall

Run supported package managers through GitLab Dependency Firewall and inspect recorded activity. This command group is experimental; confirm availability before relying on it in durable automation.

## Supported wrappers

Each wrapper resolves the GitLab project from the current repository, obtains that project's Dependency Firewall policy, forwards remaining arguments to the named package-manager binary, enforces policy on package traffic, and summarizes the run. The wrappers use the package manager's existing registry, index, or source configuration rather than rewriting it.

| glab command | Executable | Example |
|---|---|---|
| `bundle` | `bundle` | `glab dependency-firewall bundle install` |
| `gem` | `gem` | `glab dependency-firewall gem install rake` |
| `gradle` | `gradle` | `glab dependency-firewall gradle build` |
| `maven` | `mvn` | `glab dependency-firewall maven verify` |
| `npm` | `npm` | `glab dependency-firewall npm ci --ignore-scripts` |
| `pip` | `pip` | `glab dependency-firewall pip install requests` |
| `pipenv` | `pipenv` | `glab dependency-firewall pipenv install requests` |
| `pnpm` | `pnpm` | `glab dependency-firewall pnpm install left-pad` |
| `poetry` | `poetry` | `glab dependency-firewall poetry add requests` |
| `twine` | `twine` | `glab dependency-firewall twine upload dist/*` |
| `uv` | `uv` | `glab dependency-firewall uv pip install requests` |

Run wrappers inside a Git repository whose GitLab remote identifies the intended project, and verify glab authentication first. Treat a policy block as authoritative; do not retry outside the wrapper merely to bypass the result.

## Wrapper help

Package-manager arguments are forwarded verbatim. A wrapper invocation ending in `--help` can therefore invoke the package manager rather than display glab's wrapper help, and repository resolution may happen first.

```bash
# Parent command and supported wrappers
glab dependency-firewall --help

# glab's wrapper help without invoking the package manager
glab help dependency-firewall npm
glab help dependency-firewall maven
glab help dependency-firewall uv
```

Use `glab help dependency-firewall <wrapper>` for every wrapper when generating documentation or automation. Do not rely on `glab dependency-firewall <wrapper> --help` for wrapper discovery.

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

**Wrapper help is confusing:**
- Use `glab help dependency-firewall <wrapper>`.
- Outside a GitLab-remote repository, direct wrapper invocations may fail project resolution before the package manager starts.

**A package manager is not listed:**
- Do not invent a wrapper from internal support code or a similar package ecosystem.
- Check the current parent help and official docs for the target glab/GitLab version.

**The package manager uses the wrong registry/index/source:**
- The wrapper intentionally uses existing package-manager configuration.
- Inspect that configuration without printing credentials, then correct it through the package manager's documented workflow rather than expecting glab to rewrite it.

## Command reference

See [references/commands.md](references/commands.md) for checksum-verified parent and wrapper help.
