---
name: glab-user
description: View and manage GitLab user information including profile, events, and SSH keys. Use when viewing user profiles, checking user activity, or managing user settings. Triggers on user, profile, user info, view user, user activity.
---

# glab user

> **Help provenance — capture key `519ea19f7`:** checksum-verified official macOS arm64 binary; source commit `519ea19f7d3e9c701a4063f277ae27254bbafdad`; binary archive SHA-256 `541cdde6a0f706b4b69fed9fb558b421a361f63408d072d78ffdf304aee04248`. Applies only to adjacent `519ea19f7` markers. Complete output is preserved except trailing spaces/tabs.

Complete marked help captures and their provenance are documented in [references/commands.md](references/commands.md).

## Overview

<!-- help-capture: 519ea19f7:f646d51bf9bd -->

```text

  Look up information about GitLab users, such as the events a user has
  generated.


  USAGE

    glab user <command> [command] [--flags]

  COMMANDS

    events [--flags]  View user events.

  FLAGS

    -h --help         Show help for this command.

```

## Event totals and pagination

`glab user events --all` uses the API-reported total in its text header when available. `--all` selects events across projects; it does not fetch every page. The default current-project display has no such total header. JSON contains the requested page, and `--page`/`--per-page` control pagination. Do not equate the number of returned rows with the API total or treat missing total metadata as proof that there are no more events.

## Quick start

```bash
glab user --help
```

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
