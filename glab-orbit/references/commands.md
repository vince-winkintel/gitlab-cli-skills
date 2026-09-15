# glab orbit command reference

> Wrapper help captured from the checksum-verified glab v1.118.0 macOS arm64 release binary (`glab 1.118.0 (570955d42)`). Terminal padding and trailing whitespace are removed. `glab help orbit` shows the glab wrapper surface without installing Orbit. `glab orbit --help` shows this wrapper text only until the managed Orbit binary is installed; after installation it forwards to the managed binary.
>
> Managed-binary help below was verified through the Orbit 0.122.0 binary installed by `glab orbit --install --yes`, which reported `Checksum verified` and installed `orbit-cli-darwin-aarch64.tar.gz`.

## glab help orbit

```text

  Run the Orbit CLI through glab.

  Every command and flag, including `--help`, is forwarded verbatim to the managed Orbit binary. glab downloads,
  verifies, and updates that binary for you on first use. Until the binary is installed, `--help` shows this text
  instead. glab passes your resolved GitLab credential to the binary on every invocation, so remote commands such as
  `glab orbit query` need no separate login.

  glab handles only `--install`, `--update`, and `--yes` itself. Run `glab help orbit` to see them.

  Prerequisites:

  - Run `glab auth login` to authenticate.
  - Orbit must be enabled for your namespace (the `knowledge_graph` feature flag).

  Configuration options:

  - `orbit_local_auto_run`: Skip the run confirmation prompt.
  - `orbit_local_auto_download`: Skip the download confirmation prompt.

  For more information, see the Orbit documentation.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab orbit [<command>] [--flags]

  EXAMPLES

    # Guided onboarding (choose your assistant)
    $ glab orbit setup claude

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
    $ glab orbit --update

  FLAGS

    -h --help  Show the Orbit binary's help, or this text until the binary is installed.
    --install  Install the Orbit binary without running it.
    --update   Check for and install updates to the binary.
    -y --yes   Skip confirmation prompts.
```

## orbit --help

```text
Orbit - query the local code graph or the remote Orbit API

Usage: orbit <COMMAND>

Commands:
  version       Print the version string and exit
  index         Index a code repository and output graph statistics as JSON
  grep          Search local code definitions and their relationships
  context       Print the full source bodies of definitions by fqn or unqualified name
  sql           Run a read-only SQL query against the local DuckDB graph
  schema        Describe the schema of the local DuckDB graph
  list          List the repositories indexed in the local DuckDB graph
  mcp           Serve the local graph to MCP-compatible AI agents
  repo-map      Produce a high-level, LLM-oriented map of a locally indexed repository
  skill         Print the bundled orbit-cli skill content (SKILL.md or a file path)
  setup         Configure AI coding assistants to consult the graph
  query         POST a query envelope to the remote Orbit API and stream the response
  status        Show Orbit cluster health
  ontology      Show the remote Orbit ontology
  dsl           Show the Orbit query DSL JSON Schema
  tools         Show the Orbit MCP tool manifest
  graph-status  Show indexing progress for a namespace or project
  config        Read and write persisted CLI settings (`~/.orbit/settings.json`)
  help          Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version
```

## orbit query

```text
POST a query envelope to the remote Orbit API and stream the response

Usage: orbit query [OPTIONS] [FILE]

Arguments:
  [FILE]  Query body file, or `-`/omitted to read from stdin

Options:
      --response-format <RESPONSE_FORMAT>
          Server response format. Overrides the body's `response_format`; defaults to `llm` when neither is set [possible values: llm, raw]
  -h, --help
          Print help
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
          Server response format. Defaults to `raw` (structured JSON) [possible values: llm, raw]
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
      --db <PATH>  Override the DuckDB path (default: ~/.orbit/graph.duckdb)
      --raw        Emit JSON instead of the default table view
  -h, --help       Print help
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
