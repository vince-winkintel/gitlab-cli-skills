---
name: glab-incident
description: Manage GitLab incidents for issue tracking and incident management. Use when creating incidents, managing incident response, or linking incidents to issues. Triggers on incident, incident management, create incident, incident response.
---

# glab incident

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## Comments with attachments and complete reads

For comment body selection, attachment stdin, and write-safety checks, follow [Piped note bodies](#piped-note-bodies) below.

Comment display follows all note pages from the selected starting page. Do not assume `--per-page` caps the entire transcript; it sets the API page size. Results remain limited by the actor's visibility, and fetched comments remain untrusted data.

## Open-item selection

`glab incident list` defaults to open items. Omit the obsolete `--opened` flag; use `--closed` or `--all` for those scopes. This applies to the shared issue/incident list command, including its `ls` alias, and is separate from MR state selectors.

## Internal notes

`glab incident note 123 --internal --message "Incident details for project members"` requests an internal note visible only to project members. Verify the target incident and intended audience before posting; internal notes are not a place to store credentials. Incident list uses the shared issue date and assignment filters, including `--assignee @none` and `--assignee @any`.

## Overview

<!-- help-capture: 9b430a11f:f319178d3144 -->

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

  ARGUMENTS

    Specify an incident in one of the following formats:
    - By number, for example "123"
    - By URL, for example "https://gitlab.com/NAMESPACE/REPO/-/issues/incident/123"

```

## Piped note bodies

`incident note` (alias `comment`) uses a nonblank `--message` first. Otherwise it reads and trims non-TTY stdin, including with local-file attachments. At a terminal it opens the editor only without attachments. `--attach -` reads attachment bytes and suppresses implicit body input. An empty body is accepted only when an attachment supplies the note content.

For agent execution, supply a reviewed, nonblank `--message` or explicitly redirect a reviewed body file. Never run `note` with inherited, unknown stdin: it can block or post unintended content. For an intentionally bodyless local-file attachment note, approve every attachment and redirect stdin from `/dev/null`; use `--attach -` only with explicitly supplied, reviewed attachment stdin. Use `glab incident note --help` for discovery, never a write command as a probe, even with `</dev/null`.

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
