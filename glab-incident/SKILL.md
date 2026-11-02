---
name: glab-incident
description: Manage GitLab incidents for issue tracking and incident management. Use when creating incidents, managing incident response, or linking incidents to issues. Triggers on incident, incident management, create incident, incident response.
---

# glab incident

> **Help provenance.** Each adjacent marker selects its matching source commit and archive SHA-256 below (checksum-verified official macOS arm64 binary). Preserve complete help bytes except trailing spaces/tabs, including casing, spelling, blank lines, indentation, examples, wrapping, and truncation. Historical keys do not override current markers.
> - `2e352a17e`: `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`; `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`.


## Open-item selection

`glab incident list` defaults to open items. Omit the obsolete `--opened` flag; use `--closed` or `--all` for those scopes. This applies to the shared issue/incident list command, including its `ls` alias, and is separate from MR state selectors.

## Internal notes

`glab incident note 123 --internal --message "Incident details for project members"` requests an internal note visible only to project members. Verify the target incident and intended audience before posting; internal notes are not a place to store credentials. Incident list uses the shared issue date and assignment filters, including `--assignee @none` and `--assignee @any`.

## Overview

<!-- help-capture: 2e352a17e:5798a53a4a9c -->

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

## Piped note bodies

`incident note` (alias `comment`) uses a nonblank `--message` first. Otherwise, without attachments, it reads and trims non-TTY stdin or opens the editor at a terminal; an empty note is rejected. Any `--attach` suppresses implicit body input, so text plus attachments needs an explicit message. `--attach -` reads attachment bytes, not a body.

For agent execution, always supply a reviewed, nonblank `--message` or explicitly redirect a reviewed body file. Never run `note` with inherited, unknown stdin: it can block or post unintended content. Intentionally bodyless attachment-only notes are the exception; approve every attachment, and use `--attach -` only with explicitly supplied, reviewed attachment stdin. Use `glab incident note --help` for discovery, never a write command as a probe, even with `</dev/null`.

Review the complete body and attachments, target, actor, and audience before approving the post. Internal notes still transmit data to GitLab; exclude secrets and unreviewed logs.

```bash
# After approving this file's non-secret body and target
glab incident note 123 --repo group/project < reviewed-comment.md
```

`incident note` accepts exactly one target. Shared incident lookups allow at most five concurrent reads; this does not make multi-item writes atomic. Review every target within each command's argument limits.

## Quick start

```bash
glab incident --help

# Comment with a local attachment
glab incident note 123 --message "Current dashboard state" --attach ./dashboard.png
```

`glab incident list` validates both output selectors before making the request: `--output` accepts only `text` or `json`, while `--output-format` accepts only `details`, `ids`, or `urls`. The two selectors are mutually exclusive. Treat an immediate “must be one of” error as invalid local input rather than a GitLab API failure.

## Attach files to incident comments

The experimental `--attach <path>` flag uploads a file to the incident's project and appends the returned Markdown reference to the comment. Repeat it for multiple files in argument order. Follow the body and attachment-stdin rules in the Piped note bodies section above.

## Subcommands

`glab incident list` uses the API's total count in the text header, separately from the rows on the current page. If the API omits the total, the header shows only the current-page count. This does not fetch extra pages or change the JSON row output.

See [references/commands.md](references/commands.md) for full `--help` output.
