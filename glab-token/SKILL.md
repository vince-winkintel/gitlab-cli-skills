---
name: glab-token
description: Manage GitLab personal, project, and group access tokens, including explicitly approved self-rotation. Use when creating tokens, revoking access, or managing API authentication. Triggers on token, access token, PAT, personal access token, API token.
---

# glab token

Historical captured help and immutable provenance: [command reference](references/help-206ebab4f.md). Older [command captures](references/commands.md) retain their original provenance and describe earlier interfaces.

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

## Shell completion boundaries

Requires glab v1.132.0 or later for the behavior in this section. This is a source-backed summary; retained help captures keep their original immutable version and are not v1.132.0 binary verification.

Revoke/rotate positional completion lists active token IDs and names for the selected project, group, or user, including all API pages. These completions can make authenticated network requests and disclose token metadata; they are not an offline help check. `rotate --self` suppresses positional suggestions. User completion suggests `@me`; group completion disables file suggestions without enumerating groups. Creation offers fixed access-level choices; free-text, duration, expiry, scope, repository, and jq inputs disable file completion. Shared structured-output completion suggests `text` and `json`. Revoke text output now ends with a newline. None of this changes approval or protected handoff requirements for issuing, revoking, or rotating tokens.

Source: [completions.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/token/tokenutils/completions.go), [create.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/token/create/create.go), [rotate.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/token/rotate/rotate.go), [revoke.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/token/revoke/revoke.go), [output_format.go](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/cmdutils/output_format.go).

## Rotate the current credential

`glab token rotate --self` (alias `rot`) rotates the access token currently authenticating the selected host. It requires GitLab 17.9 or later and a token allowed to use the self-rotation endpoint. Confirm the host, visible actor, credential source, and every client sharing that token before approving rotation. The old secret stops working immediately; this is an operational credential write, not an authentication test.

Do not pass a token name/ID, `--user`, or `--group` with `--self`. Without `--self`, a token name/ID is required. Repository context can select the host; outside a checkout, the default host applies. Use an explicit trusted host context rather than assuming the current token belongs to the intended instance.

`--duration` defaults to `30d` (maximum `365d`; hours must be multiples of 24), and `--expires-at YYYY-MM-DD` is mutually exclusive with it. Expiry is at midnight UTC on the selected date. Default text output is the new secret; JSON output includes it too. Arrange a secure output destination before the approved command, disable shell tracing, and keep both forms out of logs and chat. After printing the replacement, `--self` updates the host's stored token in glab's config or keyring. An environment-sourced token cannot be changed: glab warns on stderr and the operator must replace it through the approved protected environment mechanism before the next command. A storage failure happens after server rotation and after the secret was printed; it does not roll rotation back. Authorization must cover this local credential-store write as well as the remote rotation. Other clients sharing the old token still need approved updates. If output is lost or the result is uncertain, inspect/recover the credential state rather than blindly retrying rotation.

```bash
# Credential-free discovery only
glab token rotate --help
# After approval, capture the secret directly into the approved secure store:
# glab token rotate --self --duration 30d
```

## Overview

<!-- help-capture: 685c1cbd7:49ae17d452aa -->

```text

  Create, list, revoke, and rotate access tokens for your user
  account, a project, or a group.


  USAGE

    glab token [command] [--flags]

  COMMANDS

    create <name> [--flags]                   Creates user, group, or project access tokens.
    list [--flags]                            List user, group, or project access tokens.
    revoke <token-name|token-id> [--flags]    Revoke user, group, or project access tokens.
    rotate [<token-name|token-id>] [--flags]  Rotate user, group, or project access tokens.

  FLAGS

    -h --help                                 Show help for this command.
    -R --repo                                 Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## Quick start

```bash
glab token --help
```

## Subcommands

See [historical command help](references/help-206ebab4f.md) for captured `--help` output. Earlier captures remain in [the historical reference](references/commands.md).
