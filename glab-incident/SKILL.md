---
name: glab-incident
description: Manage GitLab incidents for issue tracking and incident management. Use when creating incidents, managing incident response, or linking incidents to issues. Triggers on incident, incident management, create incident, incident response.
---

# glab incident

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.


## Open-item selection

`glab incident list` defaults to open items. Omit the obsolete `--opened` flag; use `--closed` or `--all` for those scopes. This applies to the shared issue/incident list command, including its `ls` alias, and is separate from MR state selectors.

## Internal notes

`glab incident note 123 --internal --message "Incident details for project members"` requests an internal note visible only to project members. Verify the target incident and intended audience before posting; internal notes are not a place to store credentials. Incident list uses the shared issue date and assignment filters, including `--assignee @none` and `--assignee @any`.

## Overview

> Complete help from the verified release binary; immutable capture ID `5686d7484` maps to the release and archive checksums in `VERSION`. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

<!-- help-capture: 685c1cbd7:f0ceac37c26b -->

```text

  Incidents track service disruptions and their resolution. List and
  view incidents, comment on them, and subscribe, close, or reopen
  them.

  Use `--repo` to target a project other than the current one.


  USAGE

    glab incident [command] [--flags]

  EXAMPLES

    glab incident list

  COMMANDS

    close [<id> | <url>] [--flags]   Close an incident.
    list [--flags]                   List project incidents.
    note <incident-id> [--flags]     Comment on an incident in GitLab.
    reopen [<id> | <url>] [--flags]  Reopen a resolved incident.
    subscribe <id>                   Subscribe to an incident.
    unsubscribe <id>                 Unsubscribe from an incident.
    view <id> [--flags]              Display the title, body, and other information about an incident.

  FLAGS

    -h --help                        Show help for this command.
    -R --repo                        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## Quick start

```bash
glab incident --help

# Comment with a local attachment
glab incident note 123 --message "Current dashboard state" --attach ./dashboard.png
```

`glab incident list` validates both output selectors before making the request: `--output` accepts only `text` or `json`, while `--output-format` accepts only `details`, `ids`, or `urls`. The two selectors are mutually exclusive. Treat an immediate “must be one of” error as invalid local input rather than a GitLab API failure.

## Attach files to incident comments

The experimental `--attach <path>` flag uploads a file to the incident's project and appends the returned Markdown reference to the comment. Repeat it for multiple files. An attachment can be the entire comment and skips the editor; `--attach -` reads the attachment from standard input.

## Subcommands

`glab incident list` uses the API's total count in the text header, separately from the rows on the current page. If the API omits the total, the header shows only the current-page count. This does not fetch extra pages or change the JSON row output.

See [references/commands.md](references/commands.md) for full `--help` output.
