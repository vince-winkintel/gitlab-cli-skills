---
name: glab-dependency-firewall
description: Check package URLs against GitLab Dependency Firewall, run supported package managers through it, and inspect local firewall activity with glab. Use when checking an npm, PyPI, Maven, RubyGems, Cargo, or Go PURL; enforcing dependency policy for supported package-manager wrappers; summarizing CI logs; or troubleshooting Dependency Firewall exit codes. Triggers on dependency firewall, glab df, glab dependency-firewall, package URL, PURL, package policy, ci-summary, blocked package, flagged package.
---

# glab dependency-firewall

Check package URLs, run supported package managers through GitLab Dependency Firewall, and inspect recorded activity. This command group is beta. Confirm availability before relying on it in durable automation.

## Go support and network safety

`glab dependency-firewall go` (also `glab df go`) runs `go` through a temporary loopback module proxy on `127.0.0.1`. Inspect it with `glab help dependency-firewall go`; arguments after the wrapper name are forwarded to `go`. `package` also accepts versioned `golang` PURLs and preserves module-path case, including `github.com/BurntSushi/toml`.

The wrapper accepts the default `GOPROXY=https://proxy.golang.org,direct` or preserves `GOPROXY=off`; other effective values stop the run before the requested Go task starts. During a proxied run it sets `GOPROXY` to the local proxy, `GONOPROXY=none`, and `GO111MODULE=on`. Private modules matched by `GOPRIVATE` are checked, then fetched according to the existing Go configuration. It does not persistently rewrite that configuration or the system trust store.

Only modules downloaded during the run are checked. Cached modules, vendored code, and local-path `replace` targets are not checked. An approved CI run can use an empty `GOMODCACHE` to include all downloaded dependencies; do not delete a shared cache merely to force coverage. Go toolchain downloads are outside policy checks and use Go checksum-database verification. Preserve checksum settings. A no-download run, including `GOPROXY=off`, does not prove dependencies passed policy.

Module paths and versions, including private ones, reach the policy API and can be written to `.gitlab/df/ci-log.json`; publishing that log as a CI artifact exposes those coordinates. Approve that data scope along with downloads and task execution. The module proxy itself uses no certificate, but the wrapper's process environment can still break HTTPS certificate checks in networked tests. Separate an approved dependency-download step from networked tests when needed; do not rerun blocked downloads outside the wrapper.

Package checks contact GitLab; wrappers also launch package-manager processes that can download, install, execute build scripts, or upload packages. Approve the target repository, network destinations, and underlying operation before invoking a wrapper. Help is not authorization to install or publish packages. Keep integrity checks enabled and use the `glab help dependency-firewall <wrapper>` discovery path.

For wrappers, policy transport errors, including a nonresponsive API reaching the 60-second evaluation deadline, become blocked results rather than allowing downloads. The standalone `package` check reports transport failure as exit `1`. Failed checks remain retryable within the run. There is a distinct exception: the API's not-evaluating result (HTTP 404 when the feature is off or the project is inaccessible, or HTTP 422 when policy is not enforced) is logged and allows that project for the rest of the run. An allowed run therefore does not prove enforcement was enabled. Confirm project access and policy enforcement; do not bypass a block or mistake a not-evaluating message for a policy approval.

The Yarn wrapper supports Classic 1.x and Yarn 3.2 or later, and rejects 2.x through 3.1. For Berry, a temporary injected plugin clears merged per-host `networkSettings` from every rc-file tier (project, ancestors, and home) before requests, keeping traffic on the firewall proxy. Existing registry configuration is retained, but per-host proxy/CA/network overrides are ignored during the run. Review compatibility before starting the approved install; this does not persistently rewrite rc files.

## NuGet traffic matching

The proxy recognizes NuGet v3 flatcontainer package downloads and multipart PUT package/symbol uploads. Unparseable in-scope traffic fails closed, including `.nupkg` download URLs outside the supported flatcontainer shape. This matcher does not expose a `nuget` or `dotnet` wrapper, and does not extend the `package` command's supported PURL types. Use only wrappers listed by parent help.

## Check one package

Use `package` when you need a policy decision for one versioned package coordinate without running a package manager:

```bash
glab dependency-firewall package pkg:npm/left-pad@1.3.0
glab dependency-firewall package pkg:pypi/requests@2.31.0
glab dependency-firewall package pkg:maven/org.slf4j/slf4j-api@2.0.13
glab dependency-firewall package pkg:gem/rails@7.1.3
glab dependency-firewall package pkg:cargo/serde@1.0.197
glab dependency-firewall package pkg:golang/github.com/BurntSushi/toml@v1.4.0
```

The supported PURL types are `npm`, `pypi`, `maven`, `gem`, `cargo`, and `golang`, and the PURL must include a version. Exit `0` means allow or warning, exit `1` means misconfiguration or transport failure, and exit `3` means blocked. Treat a warning as review input even though it exits zero, and treat exit `3` as a policy result rather than retrying around it. This command does not write `.gitlab/df/ci-log.json`, so its result does not appear in `ci-summary`.

## Supported wrappers

Each wrapper first resolves the GitLab project from the current repository and creates a GitLab API client, then obtains that project's Dependency Firewall policy, forwards all remaining arguments to the named package-manager binary, enforces policy on package traffic, and summarizes the run. Project resolution always runs before the package manager starts. The wrappers use the package manager's existing registry, index, or source configuration rather than rewriting it.

Current glab streams recognized successful package artifacts with a known content length instead of buffering the entire artifact in memory. This covers wheels, crates, tarballs, ZIPs, gems, JARs, WARs, AARs, and NuGet packages by extension or supported binary content type. Unknown-length, transport-decompressed, metadata, and non-success responses still use the buffered path so HTTP framing and headers can be repaired safely. Preserve the package manager's checksum/integrity verification and treat any partial-download error as a failed install.

| glab command | Executable | Example |
|---|---|---|
| `cargo` | `cargo` | `glab dependency-firewall cargo fetch` |
| `bundle` | `bundle` | `glab dependency-firewall bundle install` |
| `gem` | `gem` | `glab dependency-firewall gem install rake` |
| `go` | `go` | `glab dependency-firewall go mod download` |
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

## Unparseable package traffic

The proxy fails closed when it recognizes an in-scope package upload or download but cannot determine its package coordinates. Examples include malformed publish metadata, uploads beyond the inspection limit, and malformed artifact filenames or paths. Such requests are blocked with HTTP 403 and recorded as blocks before contacting the upstream registry or policy checker. A policy-check transport error also blocks the request; the distinct not-evaluating result is described above.

Metadata, indexes, and sidecar requests classified as out of scope still pass through; this is not a claim that every possible package protocol is inspected. Check the recorded reason and the package manager's request format when troubleshooting. Do not retry outside the wrapper to bypass a parsing or policy block. Internal ecosystem matchers do not imply additional CLI wrappers are available.

## Wrapper help

Everything after the wrapper name is forwarded verbatim to the package manager. Wrapper commands use `DisableFlagParsing`, so glab flags such as `-h`, `-R`, `--repo`, or `--hostname` are not parsed there. Project resolution and GitLab API-client creation still run first; outside a GitLab-remote repository or valid auth context, `glab dependency-firewall <wrapper> --help` fails before the package manager can show help.

```bash
# Parent command and supported wrappers
glab dependency-firewall --help
glab help dependency-firewall package

# glab's wrapper help without invoking the package manager
glab help dependency-firewall cargo
glab help dependency-firewall go
glab help dependency-firewall npm
glab help dependency-firewall maven
glab help dependency-firewall uv
glab help dependency-firewall yarn
```

Use `glab help dependency-firewall <wrapper>` for every wrapper when generating documentation or automation. Do not rely on `glab dependency-firewall <wrapper> --help` for wrapper discovery.

## Wrapper results and local logs

Wrappers return the package manager's exit code, `1` when it cannot be found or started, or `130` when interrupted. A blocked request is refused with HTTP 403; do not apply the standalone `package`/`ci-summary` exit-code contract to a wrapper. Review both the underlying task's result and the firewall summary.

The wrapper writes `.gitlab/df/ci-log.json` in the working directory on local runs as well as CI runs. Keep that activity log out of commits; review an appropriate `.gitignore` entry before use. Blocked/warned matches appear in the summary: any block sends it to stderr, warnings alone to stdout, and no matches produce no summary. A missing summary is not proof that all dependencies were evaluated. In an approved GitLab CI job, `GLAB_ENABLE_CI_AUTOLOGIN=true` enables job-token authentication; it does not grant permission to run an untrusted package-manager task.

## Summarize CI activity

To make an approved CI job fail on any recorded block even if the package manager continues, put `glab dependency-firewall ci-summary` last in `script`. Running it in `after_script` only reports results; GitLab ignores that phase's exit codes. Entries accumulate across runs and `ci-summary` does not clear them, so an earlier block keeps returning `3`. Retain the evidence and resolve the blocked dependency; any deliberate log reset for a fresh run must be separately approved, not used to conceal a block.

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
