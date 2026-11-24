---
name: glab-ssh-key
description: Manage SSH keys for GitLab account including add, list, and delete operations. Use when setting up SSH authentication, managing SSH keys, or configuring Git over SSH. Triggers on SSH key, add SSH key, SSH authentication, Git SSH.
---

# glab ssh-key

## DSA key compatibility

In glab v1.132.0+, the bundled SSH parser no longer supports DSA (`ssh-dss`). `ssh-key add` parses the supplied public key before upload, so DSA input can fail locally. This does not change the system SSH client's configuration or authorize replacing keys. Use an approved supported key and keep the existing upload/identity checks.

Source: [SSH-key add parser call](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/internal/commands/ssh-key/add/add.go), and the official v1.132.0 source release's `vendor/golang.org/x/crypto/ssh/keys.go` (`parsePubKey`, DSA removal); dependency version is pinned in [go.mod](https://gitlab.com/gitlab-org/cli/-/blob/00f5b8fe102e1a07471aadd5a2e44f6ff1befeeb/go.mod). This is source-backed compatibility guidance, not a binary execution claim.

> **Help provenance.** Each adjacent marker selects its matching source commit and archive SHA-256 below (checksum-verified official macOS arm64 binary). Preserve complete help bytes except trailing spaces/tabs, including casing, spelling, blank lines, indentation, examples, wrapping, and truncation. Historical keys do not override current markers.
> - `2e352a17e`: `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`; `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`.

## Overview

<!-- help-capture: 2e352a17e:2a3d30b813c3 -->

```text

  Add, list, get, and delete the SSH keys associated with your account.

  GitLab uses SSH keys to authenticate Git operations over SSH, and,
  depending on each key's usage type, to verify signed commits.


  USAGE

    glab ssh-key <command> [command] [--flags]

  COMMANDS

    add [key-file] [--flags]     Add an SSH key to your GitLab account.
    delete [<key-id>] [--flags]  Deletes a single SSH key specified by the ID.
    get [<key-id>] [--flags]     Returns a single SSH key specified by the ID.
    list [--flags]               Get a list of SSH keys for the currently authenticated user.

  FLAGS

    -h --help                    Show help for this command.
    -R --repo                    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## ⚠️ Security Warning: Public Keys Only

**Always verify you are uploading a PUBLIC key, not a private key.**

- ✅ Public keys: `~/.ssh/id_rsa.pub`, `~/.ssh/id_ed25519.pub` (`.pub` extension)
- ❌ Private keys: `~/.ssh/id_rsa`, `~/.ssh/id_ed25519` (no extension — NEVER upload these)

Uploading a private key to GitLab would expose your credentials. Double-check the filename before running `glab ssh-key add`.

```bash
# ✅ Safe — public key
glab ssh-key add ~/.ssh/id_ed25519.pub --title "My Laptop"

# ❌ NEVER do this — private key
# glab ssh-key add ~/.ssh/id_ed25519 --title "My Laptop"
```

**Before uploading, verify your key is public:**
```bash
# Should start with 'ssh-rsa', 'ssh-ed25519', 'ecdsa-sha2-*', etc.
head -c 20 ~/.ssh/id_ed25519.pub
```

## Quick start

```bash
glab ssh-key --help
```

## Replace an existing key

GitLab rejects duplicate public-key fingerprints even when the registered key has expired. After confirming the authenticated account and the key to replace, use:

```bash
glab ssh-key add ~/.ssh/id_ed25519.pub --title "My Laptop" --expires-at 2027-01-01 --replace
```

`--expires-at` accepts both a date-only value such as `2027-01-01` (midnight UTC) and a full RFC 3339 timestamp such as `2027-01-01T00:00:00Z`. The flag help shows the full timestamp form; the date-only example above is also accepted by the CLI parser.

`--replace` parses the public key, searches the current user's keys across pages for the same SHA256 fingerprint, deletes the match, and adds the supplied key with the requested title, usage type, and expiration. With no match it adds the key normally. There is no replacement confirmation prompt or rollback: if adding fails after deletion, the old key is already gone. Review the matching key before using this flag and keep another authorized access method available. This re-registers the same public key; it does not generate or rotate key material.

## Shell completion

`ssh-key get` and `delete` complete the first argument with current-account key IDs and titles through an authenticated API lookup. Completion is therefore not offline discovery or authorization to delete a key. `add` completes file paths without restricting them to `.pub`; verify that the selected file is a public key before uploading. `--usage-type` completes `auth`, `signing`, and `auth_and_signing`. Help inspection does not exercise those completions.

## Structured output

`glab ssh-key list` and `glab ssh-key get` support `--output json` / `-F json` for structured output, which is useful for agent automation.

```bash
# List SSH keys with JSON output
glab ssh-key list --output json
glab ssh-key list -F json

# Get a specific SSH key with JSON output
glab ssh-key get <key-id> --output json
glab ssh-key get <key-id> -F json
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
