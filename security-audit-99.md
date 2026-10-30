# ClawHub audit disposition — issue #99

Review date: 2026-10-30. Remediation candidate: **1.13.36**, based on
`85d16e2e328429c5f5dd60bfa80bce74e35d250a` (source and tag `v1.13.35`),
delivered for review in [PR #100](https://github.com/vince-winkintel/gitlab-cli-skills/pull/100).
This records source remediation, not hosted scan clearance or publication.

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
| **PE3: full Docker config disclosure** — ClawScan, published line 1094 | **Confirmed and fixed.** The pre-remediation `glab-auth/SKILL.md`, “Docker authentication fails,” printed the entire file. Commit `09862709d9f05df99a67bc64828a5d940c56dc70` introduced it as troubleshooting, not a requirement to expose credentials. Docker documents that config files can hold base64 credentials ([upstream](https://docs.docker.com/reference/cli/docker/login/)). Replaced with a status-only diagnostic; no raw values, exception details, or helper execution. |
| **PE3: actor identity and env-token guidance** — records at published 38, 49, 977, 1071, 1072 | **Retain legitimate authentication guidance.** `gitlab-cli-skills/SKILL.md` “Multi-agent identity note” and `glab-auth/SKILL.md` “Agentic and multi-account setups” deliberately select an actor, restrict local env-file permissions, clear stale variables, and require host/account preflight before writes. Loading an operator-controlled env file is credential use, not evidence of theft. Such files must remain trusted shell input. No env files were sourced in this review. |
| **PE3: OAuth persistence, keyring, token sources** — 931, 876, 916, 927, 933, 954 | **Retain documented auth behavior and risks.** `glab-auth/SKILL.md` “Credential storage” explains atomic config replacement, refresh persistence, separate actor configs, and plaintext fallback. `--insecure-storage` is expressly conditional on accepted risk. These are glab behaviors, not new helper-side credential extraction. No keyring/auth operations were run. |
| **PE3: token and config help / routing** — 103, 1719, 6220–6223 | **False positive as evidence of malicious access.** These are links, config-key names, and upstream command listings in the overview, `glab-config/SKILL.md`, and `glab-token/SKILL.md`. Merely mentioning access tokens does not read them. Preserve the exact help fences. |
| **PE3: Artifact Registry credentials** — 666, 721, 751 | **Retain supported functionality.** `glab-artifact-registry/SKILL.md` explains short-lived token exchange and per-tool config writes, marks output tokens secret, requires review of destination/host, and warns against printing credentials. Its Docker helper is `glab`, distinct from `auth configure-docker`'s `glab-cli`. Its destination example prints a path, not file contents. Conflict guidance now routes to the status-only diagnostic and includes a standalone safe-stop fallback; configuration inspection is not inherently a request to print secrets. Current source also contains newer approved Maven/sbt config-path guidance; do not revert to 1.13.33. |
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
registry's helper status: `glab-cli`, `glab`, `not configured`, or
`different helper configured`. Arbitrary helper strings are never echoed,
even if they contain only letters, digits, underscores, dots, or hyphens:
a misplaced credential could have that shape. Missing, empty, or extra registry
arguments fail with a fixed usage message before reading configuration.

Empty or JSON-whitespace-only files, null helper maps, and null/empty selected
helpers report `not configured`. This matches the relevant behavior in
[Docker CLI v27.5.1 LoadFromReader and CredentialHelpers](https://github.com/docker/cli/blob/v27.5.1/cli/config/configfile/file.go#L64-L80):
it ignores EOF and decodes a string-valued map. [Go JSON null semantics](https://pkg.go.dev/encoding/json#Unmarshal)
leave the selected string at its empty value. Docker's single decode can also
accept trailing data. This diagnostic deliberately requires one complete JSON
object (or an empty file), rejecting trailing data and non-object roots. It is
not a complete Docker configuration validator. A fixed error is a reason to
stop and seek private operator review, not an instruction to repair the file.
These are source/documentation comparisons, not execution of Docker's loader.

Missing/unreadable/malformed inputs produce fixed errors and exit 1; a successful
inspection exits 0, including absent or different helpers. This does not establish
authentication and does not report global credential-store fallback or legacy
`auths` values. The diagnostic reads the selected file in memory but makes no
writes and never invokes glab, Docker, credential helpers, or network transports.

Both auth and Artifact Registry conflict guidance prohibit exposing configuration
or raw helper values in agent output, logs, or chat. They retain operator approval
for migration and keep backups private. The earlier “back up and review” and
“inspect” wording did not itself require dumping secrets; the clarification
removes ambiguity and fixes the unset-DOCKER_CONFIG path. The literal full-file
printout was the confirmed executable disclosure.

The optional diagnostic requires Python 3 and a Bash-compatible shell. Each
affected standalone skill contains its own safe-stop fallback when the runtime
or diagnostic is unavailable: ask for private operator inspection and only one
of the four fixed statuses. The suggested raw-value jq filter is not an equivalent
safe alternative: it can emit arbitrary credential-shaped values and accepts
invalid selected-value types. No jq/PowerShell implementation is claimed here.
No new shared helper, installation step, runtime-version floor change, root-layout
change, or builder change is needed.

The canonical offline builder propagates the inline diagnostic and safety prose
into the merged output. It embeds skill bodies only; the root audit was never
part of that ZIP. `.gitattributes` now excludes this development audit alongside
`SECURITY.md` from Git archives. That exclusion changes source exports, not the
canonical merged ZIP, and makes no prediction about future scanner results.
The repository's documented Claude build uses `scripts/build-claude-skill.sh`;
it does not call `git archive`. No separate registry publishing workflow is
established by that builder.

All command-reference files and exact help fences remain preserved. Existing
per-block help provenance and release capture details remain in `VERSION`
(current refresh: glab commit `4dd0d32d18361db6c1c668eb4ac691c0d6edf255`).

## Verification and limits

Portable regression commands (from a checkout with Bash and Python 3):

```bash
python3 -m unittest discover -s tests -p test_docker_config_diagnostic.py -v
python3 -m unittest discover -s tests -v
git diff --check
```

Set `TMPDIR` to an approved scratch directory and `PYTHONDONTWRITEBYTECODE=1`.
The tests build and inspect the canonical ZIP in temporary storage and execute
the actual example in synthetic HOME directories, including an isolated selective
install. They assert stdout, stderr, and exit status for credential canaries,
known/unknown helpers, missing files, invalid JSON/encoding/shapes, trailing data,
empty/null inputs, custom paths and registry keys, and invalid argument counts.
Deep nesting and permission-denied reads have dedicated tests; the permission
test skips on root/non-POSIX hosts. Neither case skipped on the review host.
Removing each corresponding handler in an isolated export makes its test fail.

Historical preparation validation at the original correction ran six diagnostic
tests plus 19 existing tests (25 total); the six diagnostic tests failed against
an isolated export of `85d16e2e328429c5f5dd60bfa80bce74e35d250a`. Review remediation
added focused RED→GREEN checks and passed 32 tests. The updated disclosure test
again fails against that original export with synthetic credential canaries.
`SKILL_TEST_ROOT` selects an isolated source export; testing the original printout
also requires explicit `SKILL_TEST_LEGACY_DOCKER=1` and accepts only the known
legacy command. Normal extraction requires exactly one diagnostic section and
one Bash example, with clear assertions on missing or ambiguous content.

No real credential files, authenticated APIs, internal services, databases,
cloud resources, mail, uploads, or active skill installations were used in these
local tests. Recording transports are not live GitLab/OAuth/keyring validation.
The preparation worker could not refresh public GitHub data because of sandbox
DNS restrictions. That was a preparation-stage limit: the delivered PR records
Victor's subsequent live checks of issue/comments, duplicate PRs, and default-
branch state, plus his independent 25-test and build rerun. The retained PR
snapshot at `ce77cd423174b3a24059de96dd1600ece2533bcf` records an open, mergeable
PR with no check runs reported (`statusCheckRollup: []`); it is not a
claim about later live state or hosted CI execution. `RTK.md` was absent from
the checkout and inspected parents during preparation and this review.

Candidate 1.13.36 preserves the newer 1.13.35 source rather than reverting to the
scanned 1.13.33 package. This audit covers source preparation, testing, and PR
review; it does not perform tagging, release, registry publication, or remote
rescanning. Version availability and hosted clearance remain separate checks
for any future approved publication and its resulting scan.
