# glab orbit command reference

> Wrapper help captured from the checksum-verified glab v1.121.0 macOS arm64 release binary (`glab 1.121.0 (4d447cc6c)`). Terminal padding and trailing whitespace are removed. The release archive SHA-256 is `b097f05b09614938de267f23465c8215d9ddbebc264232604eee2b63120746e4`. `glab help orbit` shows the glab wrapper surface without installing Orbit. `glab orbit --help` shows this wrapper text only until the managed Orbit binary is installed; after installation it forwards to the managed binary.
>
> Managed-binary help below was verified through the Orbit 0.137.0 binary installed by the checksum-verified glab v1.121.0 binary with `glab orbit --install --yes`. The installer reported `Checksum verified` for `orbit-cli-darwin-aarch64.tar.gz` before installing it.

## glab help orbit

```text

  Run the GitLab Orbit CLI through glab.

  Every command and flag, including `--help`, is forwarded verbatim to the managed Orbit binary. glab downloads,
  verifies, and updates that binary for you on first use. Until the binary is installed, `--help` shows this text
  instead. glab passes your resolved GitLab credential to the binary on every invocation, so remote commands such as
  `glab orbit query` need no separate login.

  glab handles only the `update` command and the `--install`, `--update`, and `--yes` flags itself. Run `glab help
  orbit` to see them.

  Prerequisites:

  - Run `glab auth login` to authenticate.
  - Orbit must be enabled for your namespace (the `knowledge_graph` feature flag).

  Configuration options:

  - `orbit_cli_auto_run`: Skip the run confirmation prompt.
  - `orbit_cli_auto_download`: Skip the download confirmation prompt.

  For more information, see the Orbit documentation.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab orbit [command] [<command>] [--flags]

  EXAMPLES

    # Connect Orbit to the coding agents on this machine, or undo it
    $ glab orbit setup
    $ glab orbit uninstall

    # Query the remote Orbit graph (authenticates automatically)
    $ glab orbit status
    $ glab orbit query ./query.json
    $ glab orbit graph-status --full-path gitlab-org/gitlab

    # Index and search a local copy of the code graph
    $ glab orbit index .
    $ glab orbit grep "parse config"

    # Show the Orbit binary's own help and version
    $ glab orbit --help
    $ glab orbit version

    # Install or update the managed binary without running it
    $ glab orbit --install
    $ glab orbit update

  COMMANDS

    update [--flags]  Update the GitLab Orbit CLI binary to the latest version. (EXPERIMENTAL)

  FLAGS

    -h --help         Show the Orbit binary's help, or this text until the binary is installed.
    --install         Install the Orbit binary without running it.
    --update          Check for and install updates to the binary. Same as the update command.
    -y --yes          Skip confirmation prompts.

```

## orbit update

```text

  Checks for a newer GitLab Orbit CLI version and installs it. If the binary is not installed yet, `glab` downloads the
  latest version.

  Updates do not apply when you use a custom binary set with `GLAB_ORBIT_CLI_BINARY_PATH` or the `orbit_cli_binary_path`
  configuration key.

  `glab orbit --update` does the same thing.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab orbit update [--flags]

  EXAMPLES

    # Update the GitLab Orbit CLI, or download it if not installed
    glab orbit update

    # Skip the download prompt
    glab orbit update --yes

  FLAGS

    -h --help  Show help for this command.
    -y --yes   Skip the download prompt when the binary is not installed.
```

## orbit --help

```text
Orbit - query the local code graph or the remote Orbit API

Usage: orbit <COMMAND>

Commands:
  version       Print the version string and exit
  index         Index a code repository into the local graph
  grep          Search local definition names, paths, and bodies
  context       Expand local code context
  sql           Run a read-only SQL query against the local DuckDB graph
  schema        Describe the schema of the local DuckDB graph
  list          List the repositories indexed in the local DuckDB graph
  mcp           Serve the local graph to MCP-compatible AI agents
  repo-map      Print a compact map of an indexed repository for LLM use
  skills        Discover and read instance-matched agent skill files with `glab orbit skills get`
  setup         Configure AI coding agents to consult the graph
  uninstall     Remove what `orbit setup` wrote into AI coding agents
  query         POST a query to the remote Orbit API and stream the response
  status        Show Orbit cluster health
  ontology      Show the remote Orbit ontology
  dsl           Show the Orbit query DSL JSON Schema
  tools         Show the Orbit MCP tool manifest
  graph-status  Show indexing progress for a namespace or project
  config        Read and write persisted CLI settings (`~/.gitlab/orbit/settings.json`)
  help          Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version

Coding agents: load the instance-matched usage guidance first with `glab orbit skills get orbit`, then follow the returned skill.
```

## orbit query

```text
POST a query to the remote Orbit API and stream the response

Usage: orbit query [OPTIONS] <QUERY|--file <FILE>>

Arguments:
  [QUERY]
          Query text

Options:
      --file <FILE>
          Read a request envelope from FILE, or from stdin when FILE is '-'

      --response-format <RESPONSE_FORMAT>
          Server response format. Overrides the body's `response_format`; defaults to `llm` when neither is set

          Possible values:
          - llm
          - raw
          - gql: Graph pattern table (requires GitLab support)

  -h, --help
          Print help (see a summary with '-h')
```

## orbit graph-status

```text
Show indexing progress for a namespace or project

Usage: orbit graph-status [OPTIONS] <--full-path <FULL_PATH>|--namespace-id <NAMESPACE_ID>|--project-id <PROJECT_ID>>

Options:
      --full-path <FULL_PATH>
          Full path of a project or group, such as `gitlab-org/gitlab`
      --namespace-id <NAMESPACE_ID>
          Namespace (group) ID to inspect
      --project-id <PROJECT_ID>
          Project ID to inspect
      --response-format <RESPONSE_FORMAT>
          Server response format. Defaults to raw (structured JSON). [possible values: llm, raw]
  -h, --help
          Print help
```

## orbit schema

```text
Describe the schema of the local DuckDB graph

Usage: orbit schema [OPTIONS] [TABLE]...

Arguments:
  [TABLE]...  Optional table names to scope the output. When provided, only columns for those tables are shown. e.g. `orbit schema gl_definition gl_edge`

Options:
      --db <PATH>  Override the DuckDB path (default: ~/.gitlab/orbit/graph.duckdb)
      --raw        Emit JSON instead of the default table view
  -h, --help       Print help
```

## orbit setup

```text
Configure AI coding agents to consult the graph

Detects the agents installed on this machine and gives each one the Orbit instruction section, hooks, and skill. A picker lists the detected agents; `--yes` skips it. `--mcp` also registers the MCP server. Inside a Git repository it then indexes the repository; `--no-index` skips that. Writes user-global configuration unless `--project` or `--dir` is given. Existing files get a one-time `.orbit-backup` sibling. Re-running updates in place. `orbit uninstall` reverts it.

Usage: orbit setup [OPTIONS] [AGENT]...

Arguments:
  [AGENT]...
          Agents to pre-select in the picker. Default: every agent detected on this machine

          [possible values: claude, codex, duo, opencode, pi]

Options:
      --all
          Configure every supported agent, detected or not

      --mcp
          Also register the `orbit` MCP server. Off by default

      --skip <COMPONENT>
          Leave a component out (repeatable)

          [possible values: instructions, hooks, skill, mcp]

      --no-index
          Do not index the current repository after configuring

      --graph-first
          Make agents start search with Orbit. Claude Code sometimes skips Orbit, so this blocks its first search or file read each session and points it to the graph. Later calls get the usual nudge. Override at runtime with ORBIT_GRAPH_FIRST=1 or 0

  -y, --yes
          Skip the agent picker and apply to the pre-selected agents

      --dry-run
          Print what would change and exit without writing

  -v, --verbose
          List every file touched instead of a per-component summary

      --project
          Write into the current project instead of the user-global config files

      --dir <PATH>
          Project directory (implies --project; default: current directory)

  -h, --help
          Print help (see a summary with '-h')
```

## orbit uninstall

```text
Remove what `orbit setup` wrote into AI coding agents

Removes the instruction section, hooks, MCP server entry, and skill files that `orbit setup` wrote. A picker lists the detected agents that have Orbit installed; `--yes` skips it. Files you edited after setup are kept, with their `.orbit-backup` copies. Targets user-global configuration unless `--project` or `--dir` is given.

Usage: orbit uninstall [OPTIONS] [AGENT]...

Arguments:
  [AGENT]...
          Agents to clean up. Default: all of them

          [possible values: claude, codex, duo, opencode, pi]

Options:
  -y, --yes
          Skip the agent picker and apply to the pre-selected agents

      --dry-run
          Print what would change and exit without writing

  -v, --verbose
          List every file touched instead of a per-component summary

      --project
          Write into the current project instead of the user-global config files

      --dir <PATH>
          Project directory (implies --project; default: current directory)

  -h, --help
          Print help (see a summary with '-h')
```

## orbit discovery

```text
Show the Orbit query DSL JSON Schema

Usage: orbit dsl

Options:
  -h, --help  Print help
```

```text
Show the Orbit MCP tool manifest

Usage: orbit tools

Options:
  -h, --help  Print help
```

```text
Show the remote Orbit ontology

Usage: orbit ontology [NODE]...

Arguments:
  [NODE]...  Node names to expand with full properties and edge lists

Options:
  -h, --help  Print help
```
