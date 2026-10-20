# glab mcp help

> Per-block capture IDs below override older file-level provenance; unmarked blocks retain their existing provenance.

> Help output captured from `glab mcp --help`.

> Complete help from the checksum-verified release binary; immutable capture ID `d43ccacec` maps to release/checksum evidence in `VERSION`. Only trailing spaces/tabs are removed; leading indentation, blank lines, uppercase headings, wrapping, truncation, and product spelling (including renderer `Gitlab`) are preserved.

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

## mcp serve

> Complete help from the checksum-verified release binary; immutable capture ID `d43ccacec` maps to release/checksum evidence in `VERSION`. Only trailing spaces/tabs are removed; leading indentation, blank lines, uppercase headings, wrapping, truncation, and product spelling (including renderer `Gitlab`) are preserved.

````text

  Start a Model Context Protocol server to expose GitLab features
  as tools for AI assistants like Claude Code.

  The server uses stdio (standard input and output) transport for
  communication, and provides tools to:

  - Manage issues (list, create, update, close, add notes)
  - Manage merge requests (list, create, update, merge, add notes)
  - Manage projects (list, get details)
  - Manage CI/CD pipelines and jobs

  To configure this server in Claude Code, add this code to your
  MCP settings:

  ```json
  {
    "mcpServers": {
      "glab": {
        "type": "stdio",
        "command": "glab",
        "args": ["mcp", "serve"]
      }
    }
  }
  ```

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab mcp serve [--flags]

  EXAMPLES

    glab mcp serve

  FLAGS

    -h --help  Show help for this command.

````

