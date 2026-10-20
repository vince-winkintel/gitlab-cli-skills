---
name: glab-mcp
description: Deprecated glab MCP server compatibility guidance. For new AI assistant integrations use the GitLab MCP Server (https://docs.gitlab.com/user/model_context_protocol/mcp_server/) instead. Use this skill only when maintaining or migrating existing glab mcp serve integrations. Triggers on deprecated glab MCP, Model Context Protocol, glab mcp serve migration.
---

# glab mcp

## Deprecation

`glab mcp` and `glab mcp serve` are deprecated. Upstream directs users to the [GitLab MCP Server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) and collects feedback in [work item 8618](https://gitlab.com/gitlab-org/cli/-/work_items/8618). Existing stdio behavior is documented below for compatibility; do not treat it as a recommended new integration. Help output may omit the runtime deprecation warning.

## Overview

> Capture key `d43ccacec`: checksum-verified macOS arm64 release binary, source commit `d43ccacecb043b0c060dd13224cf993140db6c2b`, binary archive SHA-256 `04aad4d989d98cb030318e09359f02e0ba2637ede682ec0dee1f5974dedd44c1`. Marked help preserves all renderer output except trailing spaces/tabs; unmarked blocks retain their stated older provenance.

> Capture `d43ccacec` (key above).

```text

  Manage Model Context Protocol server features for GitLab integration.

  The MCP server exposes GitLab features as tools for use by
  AI assistants (like Claude Code) to interact with GitLab projects, issues,
  merge requests, pipelines, and other resources.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab mcp <command> [--flags]

  EXAMPLES

    glab mcp serve

  COMMANDS

    serve      Start a MCP server with stdio transport. (EXPERIMENTAL)

  FLAGS

    -h --help  Show help for this command.

```

## Quick start

```bash
glab mcp --help
```

## Current behavior

### Auto-enabled JSON output
`glab mcp serve` automatically enables JSON output format when running — no manual flag needed. This improves parsing reliability for AI assistants consuming the MCP server's tool responses.

### Unannotated commands excluded
Commands that lack MCP annotations are not registered as MCP tools. This means only explicitly supported commands are exposed to AI assistants, reducing noise and improving reliability. If a GitLab operation you expect isn't available as an MCP tool, it may lack MCP annotations.

### Inherited flags advertised
MCP tool schemas include visible inherited flags accepted from parent commands, such as `--repo` on project-scoped operations. Pass these through the tool's `flags` object using the schema's underscore-normalized names (for example, `repo`); do not assume a flag is unavailable merely because it is registered on a parent command.

## Subcommands

See [references/commands.md](references/commands.md) for full `--help` output.
