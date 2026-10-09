# glab api command reference

> Complete help captured from the checksum-verified glab v1.122.0 macOS arm64 release binary. Only terminal padding/trailing whitespace is removed; renderer wrapping and example truncation are preserved. Archive SHA-256: `cbdd6e28d35f9eb09aef79ad23d2712d67c9254677a60ed6d701b5362f659fef`. No product-spelling substitutions were needed in these captures.

## api

```text

  Makes an authenticated HTTP request to the GitLab API, and prints the response.
  Specify either a path to a GitLab API v4 endpoint, or `graphql` to access the
  GitLab GraphQL API.

  For more information, see:

  - GitLab REST API documentation
  - GitLab GraphQL documentation

  If the current directory is a Git directory, this command uses the GitLab
  authenticated host in the current directory. Otherwise, `gitlab.com` is used.
  To override the GitLab hostname, use `--hostname`.

  When used in the endpoint argument, these placeholder values are replaced
  with values from the repository of the current directory:

  - `:branch`
  - `:fullpath`
  - `:group`
  - `:id`
  - `:namespace`
  - `:repo`
  - `:user`
  - `:username`

  To define your own placeholder, pass `--placeholder <name>=<value>` and use `:<name>` in the endpoint or in `--field`
  values. In the endpoint, the value is encoded as a single path segment. In `--field` values, it is sent unchanged. To
  put a value in a query string, pass it as a field instead: `-X GET -F <key>=:<name>`. A custom placeholder cannot
  reuse the name of a built-in placeholder.

  The default HTTP request method is `GET` when no parameters are added,
  and `POST` otherwise. To override the method, use `--method`.

  Pass one or more `--raw-field` values in `key=value` format to add
  JSON-encoded string parameters to the `POST` body.

  The `--field` flag behaves like `--raw-field` but converts values
  based on their format:

  - Literal values `true`, `false`, `null`, and integer numbers are converted to
    the matching JSON types.
  - Values starting with `[` or `{` are parsed as JSON arrays or objects
    (e.g. `-F 'topics=["my-topic","GitLab"]'`). Invalid JSON returns an error.
    The value must start with the bracket or brace: a leading space, as in
    `-F 'topics= ["a"]'`, is part of the value, so it is sent as a string.
  - Placeholder values `:namespace`, `:repo`, and `:branch` are populated with values
    from the repository of the current directory, including inside JSON
    arrays and objects (e.g. `-F 'input={"projectPath":":fullpath"}'`).
  - If the value starts with `@`, the rest of the value is interpreted as a
    filename to read the value from. Pass `-` to read from standard input.

  `--raw-field` does not parse JSON arrays or objects; those values are
  sent as strings. To pass a JSON body literally, use `--input`.

  A bracketed `--raw-field` value such as `-f 'scopes=[api,read_api]'` is sent as
  the literal string `"[api,read_api]"`. Earlier versions converted that shape
  into an array on request bodies, which `--raw-field` never documented. Use
  `-F 'scopes=["api","read_api"]'` for an array.

  Field names are never parsed. A bracketed name is only meaningful where the
  fields become URL query parameters. That means `GET` and `DELETE` requests,
  and any request where `--input` supplies the body. There the name is used
  literally and percent-encoded, so `-f 'position[base_sha]=abc'` arrives as
  the nested parameter it describes.

  A name ending in `[]` collects values instead of holding one, which is how
  the API reads an array. Repeating the name sends every value, in the order
  the flags were given: `-X GET -f 'ids[]=1' -f 'ids[]=2'` sends both.
  Because every value is sent, `--field` does not override `--raw-field` of
  the same name, as it does for other names.

  Any other name holds a single value. Among values from the same flag, the
  last one wins. When both flags name it, the `--field` value wins, whichever
  order the two were given in.

  The `-F 'ids=[1,2]'` spelling emits `ids[]` as well. Spelling one query
  parameter both ways is therefore an error. Passing `-f 'ids[]=1'` with
  `-F 'ids=[2,3]'` is rejected, because nothing says which order the three
  values belong in.

  In a JSON request body a field name containing a bracket is an error. Such
  a name would be sent as a single literal key, which the API ignores. The
  request would succeed without doing what the name asked. Pass the value as
  JSON instead, as in `-F 'position={"base_sha":"abc"}'` or `-F 'ids=[1,2]'`.
  Or use `--input`.

  With no `--method`, adding any field makes the request a `POST`. Sending
  bracketed names as query parameters therefore needs an explicit
  `--method GET`. `--form` is unaffected: its part names are always literal.

  For GraphQL requests, all fields other than `query` and `operationName` are
  interpreted as GraphQL variables. The bracket rule applies to them
  unchanged: where the request sends a JSON body, a bracketed variable name
  is an error.

  To send data as `multipart/form-data` instead of JSON, use `--form`. This is
  required for API endpoints that accept file uploads, such as wiki attachments.
  Pass one or more `--form` values in `key=value` format. To upload a file,
  prefix the value with `@` followed by the file path. Pass `-` to read from
  standard input. Do not combine `--form` with `--field`, `--raw-field`, or `--input`.

  To pass a raw request body, use `--input` with a file path. Pass `-` to
  read from standard input. In this mode, parameters specified with `--field`
  flags are serialized into URL query parameters.

  In `--paginate` mode, all pages of results are requested sequentially until
  no more pages of results remain. For GraphQL requests:

  - The original query must accept an `$endCursor: String` variable.
  - The query must fetch the `pageInfo{ hasNextPage, endCursor }` set of fields from a collection.

  The `--output` flag controls the output format:

  - `json` (default): Pretty-printed JSON. Arrays are output as a single JSON array.
  - `ndjson`: Newline-delimited JSON, also known as JSON Lines. Each array element
    or object is output on a separate line. This format is more memory-efficient for
    large datasets and works well with tools like `jq`.

  For ndjson format specifications, see the
  ndjson spec and JSON Lines.


  USAGE

    glab api <endpoint> [--flags]

  EXAMPLES

    # List releases for the current project, expanding the :fullpath placeholder
    glab api projects/:fullpath/releases

    # List issues for a project by URL-encoded path
    glab api projects/gitlab-com%2Fwww-gitlab-com/issues

    # Get a branch whose name contains a slash, using a custom placeholder
    glab api projects/:fullpath/repository/branches/:target --placeholder target=feature/login

    # Upload a file to a project wiki
    glab api --method POST projects/:fullpath/wikis/attachments --form "file=@./image.png" --form "branch=main"

    # Debug the HTTP request and response, including headers and body.
    # Use --input to send a complete JSON request body from stdin.
    echo '{"allowed_to_push":[{"user_id":1}]}' | GLAB_DEBUG_HTTP=1 glab api -X PATCH "projects/:fullpath/protected_…

    # Fetch all pages of issues
    glab api issues --paginate

    # Fetch all pages of issues as newline-delimited JSON
    glab api issues --paginate --output ndjson

    # Pipe paginated output to jq to filter open issues
    glab api issues --paginate --output ndjson | jq 'select(.state == "opened")'

    # Run a simple GraphQL query
    glab api graphql -f query="query { currentUser { username } }"

    # Run a multi-line GraphQL query for project metadata
    glab api graphql -f query='
    query {
    project(fullPath: "gitlab-org/gitlab-docs") {
    name
    forksCount
    statistics {
    wikiSize
    }
    issuesEnabled
    boards {
    nodes {
    id
    name
    }
    }
    }
    }
    '

    # Run a paginated GraphQL query using an endCursor variable
    glab api graphql --paginate -f query='
    query($endCursor: String) {
    project(fullPath: "gitlab-org/graphql-sandbox") {
    name
    issues(first: 2, after: $endCursor) {
    edges {
    node {
    title
    }
    }
    pageInfo {
    endCursor
    hasNextPage
    }
    }
    }
    }'

  FLAGS

    -F --field      Add a parameter of inferred type. Using this flag changes the default HTTP method to POST.
    --form          Add a multipart form field. To upload a file, prefix the value with @ followed by the file path. To read from standard input, use @- (at most once). Using this flag changes the default HTTP method to POST.
    -H --header     Add an additional HTTP request header.
    -h --help       Show help for this command.
    --hostname      The GitLab hostname for the request. Defaults to gitlab.com, or the authenticated host in the current Git directory.
    -i --include    Include HTTP response headers in the output.
    --input         The file to use as the body for the HTTP request.
    -X --method     The HTTP method for the request. (GET)
    --output        Format output as: json, ndjson. (json)
    --paginate      Make additional HTTP requests to fetch all pages of results.
    --placeholder   Define a custom placeholder in <name>=<value> format, expanded from :<name>. Repeat the flag to define more than one.
    -f --raw-field  Add a string parameter.
    --silent        Do not print the response body.

```
