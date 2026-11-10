---
name: glab-dependency-firewall
description: Check package URLs against GitLab Dependency Firewall, run supported package managers through it, and inspect local firewall activity with glab. Use when checking an npm, PyPI, Maven, RubyGems, Cargo, or Go PURL; enforcing dependency policy for supported package-manager wrappers; summarizing CI logs; or troubleshooting Dependency Firewall exit codes. Triggers on dependency firewall, glab df, glab dependency-firewall, package URL, PURL, package policy, ci-summary, blocked package, flagged package.
---

# glab dependency-firewall

Check package URLs, run supported package managers through GitLab Dependency Firewall, and inspect recorded activity. This command group is beta. Confirm availability before relying on it in durable automation.

## Package-manager proxies and Maven mirrors

The inspection proxy checks and forwards plain-HTTP registry requests as well as HTTPS; this does not encrypt plain HTTP. The general registry transport uses `HTTPS_PROXY` for HTTPS and `HTTP_PROXY` for plain HTTP, falling back to `HTTPS_PROXY` when `HTTP_PROXY` is unset (outside CGI environments). npm/pnpm prefer `HTTPS_PROXY` for HTTP too. Package-manager proxy environment variables take precedence where supported: `npm_config_https_proxy` / `npm_config_proxy`, `YARN_HTTPS_PROXY`, `PIP_PROXY`, and `CARGO_HTTP_PROXY`. These are environment settings, not newly supported parsing of every manager configuration file. npm's `npm_config_noproxy` combines with `NO_PROXY`; a set `PIP_PROXY` and Yarn's own proxy settings do not apply `NO_PROXY`, while Cargo does. Review the actual destination and keep proxy credentials out of argv/output.

Maven downloads through a mirror are matched against known catch-all mirror bases where available, including `external:*` behavior; otherwise the matcher enumerates plausible repository prefixes. Review user/global settings and mirror destinations. Preserving mirrors does not bypass policy checks or authorize uploads; unsupported/unparseable in-scope requests remain subject to the firewall's failure rules.

## Go support and network safety

`glab dependency-firewall go` (also `glab df go`) runs `go` through a temporary loopback module proxy on `127.0.0.1`. Inspect it with `glab help dependency-firewall go`; arguments after the wrapper name are forwarded to `go`. `package` also accepts versioned `golang` PURLs and preserves module-path case, including `github.com/BurntSushi/toml`.

Go uses a separate module fetcher, not the general registry transport above. Its help lists `HTTPS_PROXY` and `NO_PROXY`; do not assume the general transport's HTTP-to-HTTPS proxy fallback applies to Go. The wrapper reads the effective `GOPROXY` from the environment or Go environment file and fetches checked modules through that configuration, including custom proxy lists and Go's native comma/pipe fallback rules. `GOPROXY=off` remains off. During a proxied run the package-manager process receives the loopback `GOPROXY`, `GONOPROXY=none`, and `GO111MODULE=on`; the upstream fetch uses the original effective Go proxy configuration. Private modules matched by `GOPRIVATE` are checked, then fetched according to the existing Go configuration. Review all configured proxy and direct-fetch destinations before approving downloads. It does not persistently rewrite that configuration or the system trust store.

Go proxy authentication uses the existing `.netrc`, `GOAUTH`, or proxy URL credentials. A `GOSUMDB` with its own URL also passes through the loopback proxy, but `.netrc` and `GOAUTH` do not authenticate that checksum-database URL. Its supported credential source is the URL itself; do not expose it in command arguments or logs, and stop if no approved protected configuration path exists. Go module downloads use the Go fetcher's existing trust configuration (system roots, or `SSL_CERT_FILE` where the platform supports it), not the general registry transport's additional `ca_cert` and package-manager CA bundles. On macOS, Go/git use the system trust store. Preserve checksum verification and approve credential destinations separately.

Only modules downloaded during the run are checked. Cached modules, vendored code, and local-path `replace` targets are not checked. An approved CI run can use an empty `GOMODCACHE` to include all downloaded dependencies; do not delete a shared cache merely to force coverage. Go toolchain downloads are outside policy checks and use Go checksum-database verification. Preserve checksum settings. A no-download run, including `GOPROXY=off`, does not prove dependencies passed policy.

Module paths and versions, including private ones, reach the policy API and can be written to `.gitlab/df/ci-log.json`; publishing that log as a CI artifact exposes those coordinates. Approve that data scope along with downloads and task execution. The module proxy itself uses no certificate, but the wrapper's process environment can still break HTTPS certificate checks in networked tests. Separate an approved dependency-download step from networked tests when needed; do not rerun blocked downloads outside the wrapper.

Package checks contact GitLab; wrappers also launch package-manager processes that can download, install, execute build scripts, or upload packages. Approve the target repository, network destinations, and underlying operation before invoking a wrapper. Help is not authorization to install or publish packages. Keep integrity checks enabled and use the `glab help dependency-firewall <wrapper>` discovery path.

For wrappers, policy transport errors, including a nonresponsive API reaching the 60-second evaluation deadline, become blocked results rather than allowing downloads. The standalone `package` check reports transport failure as exit `1`. Failed checks remain retryable within the run. There is a distinct exception: the API's not-evaluating result (HTTP 404 when the feature is off or the project is inaccessible, or HTTP 422 when policy is not enforced) is logged and allows that project for the rest of the run. An allowed run therefore does not prove enforcement was enabled. Confirm project access and policy enforcement; do not bypass a block or mistake a not-evaluating message for a policy approval.

The Yarn wrapper supports Classic 1.x and Yarn 3.2 or later, and rejects 2.x through 3.1. For Berry, a temporary injected plugin clears merged per-host `networkSettings` from every rc-file tier (project, ancestors, and home) before requests, keeping traffic on the firewall proxy. Existing registry configuration is retained, but per-host proxy/CA/network overrides are ignored during the run. Review compatibility before starting the approved install; this does not persistently rewrite rc files.

## Registries behind an upstream proxy

The general registry transport follows the proxy precedence above and honors `NO_PROXY` except for the package-manager overrides described there; package-manager traffic still enters the local inspection proxy. Proxy URL credentials are sent to that proxy; keep them out of command arguments, logs, and reports. Registry and HTTPS-proxy certificates remain verified. The general registry transport trusts system roots, the configured GitLab host's `ca_cert`, and CA bundles named by `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `PIP_CERT`, `TWINE_CERT`, `NODE_EXTRA_CA_CERTS`, `BUNDLE_SSL_CA_CERT`, and `CARGO_HTTP_CAINFO`. GitLab API calls trust only system roots plus `ca_cert`, not those package-manager bundles. For a private-CA outbound proxy, configure the approved CA through `ca_cert` to cover both paths; a registry-only bundle does not fix API trust. See the complete [parent help capture](references/commands.md#dependency-firewall). An upstream proxy refusal is an error, not permission to bypass the proxy or disable TLS verification. This registry transport is separate from the per-host GitLab API `proxy` setting and the Go module wrapper's own `GOPROXY` handling.

A registry transport request failure emits a warning at most once per registry authority during a run. Failed reads of an incoming upload body are excluded. This is not a warning for every HTTP error response or later response-body failure, and it is not a policy verdict. Inspect the package manager's exit status and policy summary; absence of repeated warnings does not prove registry health or policy approval.

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

The supported PURL types are `npm`, `pypi`, `maven`, `gem`, `cargo`, and `golang`, and the PURL must include a version. Exit `0` means allowed, warned, or the Dependency Firewall is not evaluating the project. Check for the output line ending `the Dependency Firewall is not evaluating this project; allowing.`; zero alone does not prove GitLab checked the package or approved it under policy. Exit `1` means an invalid or versionless PURL, unresolved project or credentials, or a failed request to GitLab. Exit `3` means blocked. Treat a warning as review input even though it exits zero, and treat exit `3` as a policy result rather than retrying around it. This command does not write `.gitlab/df/ci-log.json`, so its result does not appear in `ci-summary`.

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
| `pnpm` | `pnpm` | `glab dependency-firewall pnpm add left-pad` |
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
