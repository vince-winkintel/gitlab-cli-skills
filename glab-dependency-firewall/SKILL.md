---
name: glab-dependency-firewall
description: Check package URLs against GitLab Dependency Firewall, run supported package managers through it, and inspect local firewall activity with glab. Use when checking an npm, PyPI, Maven, or RubyGems PURL; enforcing dependency policy for supported package-manager wrappers; summarizing CI logs; or troubleshooting Dependency Firewall exit codes. Triggers on dependency firewall, glab df, glab dependency-firewall, package URL, PURL, package policy, ci-summary, blocked package, flagged package.
---

# glab dependency-firewall

Check package URLs, run supported package managers through GitLab Dependency Firewall, and inspect recorded activity. This command group is experimental; confirm availability before relying on it in durable automation.

## Check one package

Use `package` when you need a policy decision for one versioned package coordinate without running a package manager:

```bash
glab dependency-firewall package pkg:npm/left-pad@1.3.0
glab dependency-firewall package pkg:pypi/requests@2.31.0
glab dependency-firewall package pkg:maven/org.slf4j/slf4j-api@2.0.13
glab dependency-firewall package pkg:gem/rails@7.1.3
```

The supported PURL types are `npm`, `pypi`, `maven`, and `gem`, and the PURL must include a version. Exit `0` means allow or warning, exit `1` means misconfiguration or transport failure, and exit `3` means blocked. Treat a warning as review input even though it exits zero, and treat exit `3` as a policy result rather than retrying around it. This command does not write `.gitlab/df/ci-log.json`, so its result does not appear in `ci-summary`.

## Supported wrappers

Each wrapper first resolves the GitLab project from the current repository and creates a GitLab API client, then obtains that project's Dependency Firewall policy, forwards all remaining arguments to the named package-manager binary, enforces policy on package traffic, and summarizes the run. Project resolution always runs before the package manager starts. The wrappers use the package manager's existing registry, index, or source configuration rather than rewriting it.

Current glab streams recognized successful package artifacts with a known content length instead of buffering the entire artifact in memory. This covers wheels, crates, tarballs, ZIPs, gems, JARs, WARs, AARs, and NuGet packages by extension or supported binary content type. Unknown-length, transport-decompressed, metadata, and non-success responses still use the buffered path so HTTP framing and headers can be repaired safely. Preserve the package manager's checksum/integrity verification and treat any partial-download error as a failed install.

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
| `yarn` | `yarn` | `glab dependency-firewall yarn add left-pad` |

Run wrappers inside a Git repository whose GitLab remote identifies the intended project, and verify glab authentication first. Treat a policy block as authoritative; do not retry outside the wrapper merely to bypass the result.

## Wrapper help

Everything after the wrapper name is forwarded verbatim to the package manager. Wrapper commands use `DisableFlagParsing`, so glab flags such as `-h`, `-R`, `--repo`, or `--hostname` are not parsed there. Project resolution and GitLab API-client creation still run first; outside a GitLab-remote repository or valid auth context, `glab dependency-firewall <wrapper> --help` fails before the package manager can show help.

```bash
# Parent command and supported wrappers
glab dependency-firewall --help
glab help dependency-firewall package

# glab's wrapper help without invoking the package manager
glab help dependency-firewall npm
glab help dependency-firewall maven
glab help dependency-firewall uv
glab help dependency-firewall yarn
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

Current human-readable summaries use a colored Unicode box when the terminal supports it. Do not parse that presentation format; use exit codes and the underlying log for automation.

## Troubleshooting

**No activity is reported:**
- Confirm `.gitlab/df/ci-log.json` exists under the current working directory used for the command.
- Do not assume a log in a repository root applies when the package manager ran in a nested workspace.

**Wrapper help is confusing:**
- Use `glab help dependency-firewall <wrapper>`.
- Direct wrapper invocations always resolve the GitLab project and client before starting the package manager, and glab flags after the wrapper name are passed to the package manager.

**A package manager is not listed:**
- Do not invent a wrapper from internal support code or a similar package ecosystem.
- Check the current parent help and official docs for the target glab/GitLab version.

**The package manager uses the wrong registry/index/source:**
- The wrapper intentionally uses existing package-manager configuration.
- Inspect that configuration without printing credentials, then correct it through the package manager's documented workflow rather than expecting glab to rewrite it.

## Command reference

See [references/commands.md](references/commands.md) for checksum-verified parent, package-check, wrapper, and summary help.
