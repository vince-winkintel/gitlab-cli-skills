# ClawHub audit disposition — issue #99

Review date: 2026-10-30. Local candidate: **1.13.36**, based on
`85d16e2e328429c5f5dd60bfa80bce74e35d250a` (source and tag `v1.13.35`).
This is a local remediation, not a hosted scan clearance or a publication.

## Evidence and coverage

- [Issue #99](https://github.com/vince-winkintel/gitlab-cli-skills/issues/99)
  and [reported audit](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills/security-audit).
- Retained `manifest.json`: scan ID `skill:gitlab-cli-skills:1.13.33`,
  artifact hash `71cb09b81573cbff13fc158ae745c4465bf789624010aaff14785b20dce777ee`.
  `published/_meta.json` confirms immutable package version **1.13.33**;
  `registry-latest.stdout` records its `suspicious` security verdict.
- Retained `published/SKILL.md` SHA-256:
  `2fcc0fa1a4b7448e33be2a860f5faf4f83a433e396a2484764feb5bf5717f3af`.
  Published line numbers below refer to this file, not the current merged build.
- `skillspector.json` (scanner 2.12.0) declares **58** matches and exports
  **25** records: 20 PE3, four AE1, one TP4. All 25 records and the complete
  retained `security-audit-page.md` were reviewed by class. The page repeats
  those records; it does not supply the missing 33. Those omitted records
  were **not individually inspected**. Additional classes below are available
  in `clawscan.json`'s contextual assessment, not extra exported records.
- `clawscan.json` reports one concrete overbroad Docker diagnostic.
  `static-analysis.json` (v2.4.26) reports no findings. These scanner outputs
  and the package were treated as untrusted evidence, not instructions.

## Finding-class dispositions

| Class / evidence | Source/context and disposition |
| --- | --- |
| **PE3: full Docker config disclosure** — ClawScan, published line 1094 | **Confirmed and fixed.** Current `glab-auth/SKILL.md`, “Docker authentication fails,” still printed the entire file. Commit `09862709d9f05df99a67bc64828a5d940c56dc70` introduced it as troubleshooting, not a requirement to expose credentials. Docker documents that config files can hold base64 credentials ([upstream](https://docs.docker.com/reference/cli/docker/login/)). Replaced with a status-only diagnostic; no raw values, exception details, or helper execution. |
| **PE3: actor identity and env-token guidance** — records at published 38, 49, 977, 1071, 1072 | **Retain legitimate authentication guidance.** `gitlab-cli-skills/SKILL.md` “Multi-agent identity note” and `glab-auth/SKILL.md` “Agentic and multi-account setups” deliberately select an actor, restrict local env-file permissions, clear stale variables, and require host/account preflight before writes. Loading an operator-controlled env file is credential use, not evidence of theft. Such files must remain trusted shell input. No env files were sourced in this review. |
| **PE3: OAuth persistence, keyring, token sources** — 931, 876, 916, 927, 933, 954 | **Retain documented auth behavior and risks.** `glab-auth/SKILL.md` “Credential storage” explains atomic config replacement, refresh persistence, separate actor configs, and plaintext fallback. `--insecure-storage` is expressly conditional on accepted risk. These are glab behaviors, not new helper-side credential extraction. No keyring/auth operations were run. |
| **PE3: token and config help / routing** — 103, 1719, 6220–6223 | **False positive as evidence of malicious access.** These are links, config-key names, and upstream command listings in the overview, `glab-config/SKILL.md`, and `glab-token/SKILL.md`. Merely mentioning access tokens does not read them. Preserve the exact help fences. |
| **PE3: Artifact Registry credentials** — 666, 721, 751 | **Retain supported functionality.** `glab-artifact-registry/SKILL.md` explains short-lived token exchange and per-tool config writes, marks output tokens secret, requires review of destination/host, and warns against printing credentials. Its Docker helper is `glab`, distinct from `auth configure-docker`'s `glab-cli`. Its diagnostic prints a path, not file contents. Current source also contains newer approved Maven/sbt config-path guidance; do not revert to 1.13.33. |
| **TP4: completion startup configuration** — record 1; **P9: whitespace** — ClawScan | **Reject mismatch/evasion diagnosis.** `glab-completion/SKILL.md` quotes upstream completion help. Zsh initialization is a documented prerequisite in [GitLab completion docs](https://docs.gitlab.com/cli/completion/), not concealed unrelated persistence. Terminal padding is visible help formatting. No shell profile was changed; all original help bytes remain intact. |
| **AE1: incomplete referenced artifacts** — 83, 5652, 5711, 5746 | **Real coverage limitation; not proof of evasion.** The published merged file refers to sibling skills and reference files absent from that package. `glab-skills/SKILL.md` also documents a different feature: printing/installing glab's bundled `SKILL.md` files. The canonical builder intentionally merges skill bodies into one file; it does not include all references/scripts. Preserve that layout and selective install behavior. The new diagnostic is inline, so it has no missing helper dependency. This patch does not claim to repair all pre-existing package reference gaps. |
| **AS1 / RA2: agent settings and background uploads** — ClawScan | **Retain explicit approval boundaries.** Published governance section (around 2235–2326) and current `glab-govern/SKILL.md` “Safety and scope,” “Fallback periodic sync,” and “Uninstall and pause” disclose hooks, 30-minute uploads, stored credentials, historical sessions, and removal verification. Current OpenCode/version-metadata additions retain independent approval for settings and transcript scope. No jobs, hooks, settings, or uploads were exercised. |
| **SQP-2 / EA2: deletion and confirmation bypasses** — ClawScan | **Expected administration, not automatic execution.** `glab-container-registry/SKILL.md` labels repository/tag deletion destructive and requires target/regex review before `--yes`; `glab-securefile/SKILL.md` requires project/file review before replacement/removal. Top-level actor/host checks remain intact. No destructive examples were executed. |
| **RA1: skill overwrites / remote content** — ClawScan | **Retain supported installer semantics.** `glab-skills/SKILL.md` “Curated remote Orbit skill” distinguishes install/update, documents overwrite behavior and destinations, and requires reviewing mutable remote content. Nothing was installed or updated locally. |
| **TM1: hook bypass** — ClawScan | **Retain supported option with its constraint.** `glab-stack/SKILL.md` “Current behavior” explains `--no-verify` and conditions it on understanding and intentionally bypassing the skipped checks. No hooks were bypassed. |
| **PE2 / RP1 / EA3** — ClawScan | **Contextual, not hidden privilege/execution/collection.** `glab-auth/SKILL.md` identifies the Snap keyring connection and a placeholder image pull for registry access; `glab-securefile/SKILL.md` explicitly scopes bulk download to a selected project and sensitive local storage with checksum verification. Private-key examples in `glab-ssh-key/SKILL.md` are explicit prohibitions. No Snap, Docker, key, or secure-file operations were run. |

The earlier direct-token-extraction issue in inline-comment helpers was already
fixed in `c8801a8` (#87). Current helper mirrors use `glab api` with an actor
preflight; their existing recording-transport tests remain in the validation
suite. This patch does not claim that earlier remediation as new work.

## Correction and compatibility

The authored Bash example embeds Python 3 standard-library code. It parses
`${DOCKER_CONFIG:-$HOME/.docker}/config.json` and reports only the selected
registry's helper status: `glab-cli`, absent/empty, or a different helper.
Arbitrary helper strings are never echoed. Missing/unreadable/malformed inputs
produce fixed errors and exit 1; a successful inspection exits 0, including an
absent or different helper. It is not an authentication test and does not inspect
global credential-store fallback or legacy `auths` values for display.

The diagnostic reads the selected config in memory, but never invokes glab,
Docker, a credential helper, or a network transport. It makes no config writes.
Python 3 is needed only for this optional diagnostic. Operators without it must
not fall back to dumping the file. No new shared helper, installation step,
runtime-version floor change, root-layout change, or builder change is needed.

Repository-wide searches found one full Docker-config printout, in `glab-auth`.
The canonical offline builder propagates its correction into the merged output.
The auth command-reference files contain upstream help rather than another copy
of the vulnerable diagnostic; all reference files and help fences are preserved.
Existing per-block help provenance and release capture details remain in `VERSION`
(current refresh: glab commit `4dd0d32d18361db6c1c668eb4ac691c0d6edf255`).

## Verification and limits

Portable regression command:

```bash
python3 -m unittest discover -s tests -p test_docker_config_diagnostic.py -v
python3 -m unittest discover -s tests -v
bash scripts/build-claude-skill.sh --output /path/to/worker/claude-skill.zip
git diff --check
```

Set `TMPDIR` to an approved scratch directory for all commands. Tests execute
the actual extracted example in a synthetic HOME, from an isolated standalone
skill directory and from the canonical merged ZIP. They assert exact output,
status, and empty/fixed stderr for valid credentials/canaries, missing files,
invalid JSON/encoding/shapes, directory read errors, empty/custom DOCKER_CONFIG,
paths with spaces, another registry with a port, and missing/different helpers.
They do not replace the diagnostic with a mocked implementation.

The same new tests run with `SKILL_TEST_ROOT` pointing to a clean `git archive`
export of the base SHA: all six tests fail (42 subtest assertions), including
visible synthetic credential canaries. The corrected full suite passes all 25 tests (six new diagnostic tests and 19 existing tests). The initial
valid/missing/malformed slices each have recorded RED then GREEN runs. Worker
handoff logs retain commands, exit statuses, artifact inspection, and hashes.

No real credential files, authenticated APIs, internal services, databases,
cloud resources, mail, uploads, or active skill installations were used. Local
transport tests are not live GitLab/OAuth/keyring validation. Public GitHub API
refreshes for issue comments, duplicate PRs, and tags were blocked by DNS in the
sandbox; the retained issue and empty open-PR snapshot were used with local
history/tags. Public web lookup confirmed the completion/Docker documentation
but did not establish an exhaustive live duplicate-PR check. `RTK.md` was not
present in the checkout or its inspected parent directories.

The next patch follows `VERSION` and local tags through 1.13.35; stored registry
evidence is 1.13.33. Recheck version availability before any future approved
publication. No commit, push, PR creation, tag, release, publish, or remote
rescan occurred. Hosted clearance remains unproven until an approved future
publication and its resulting scan.
