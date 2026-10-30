# glab cluster help

> Capture key `4dd0d32d1`: checksum-verified official macOS arm64 binary, source commit `4dd0d32d18361db6c1c668eb4ac691c0d6edf255`, archive SHA-256 `11980310aaad2bd9c4e75b5635a60e984da5d0e6245187f2cd6e8db0ec4c5a92`. Only adjacent marked help fences use this provenance; complete renderer output is preserved except trailing spaces/tabs. Other fences retain their stated prior provenance.

<!-- help-capture: 4dd0d32d1:ed5b0c665871 -->

```text

  Agents connect your cluster to GitLab, enabling pull-based deployments
  and secure access to the Kubernetes API.


  USAGE

    glab cluster <command> [command] [--flags]

  COMMANDS

    agent <command> [command] [--flags]  Manage GitLab Agents for Kubernetes.
    graph [--flags]                      Query the Kubernetes object graph using the GitLab Agent for Kubernetes. (EXPERIMENTAL)

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## cluster agent

<!-- help-capture: 4dd0d32d1:d3feac96ec34 -->

```text

  Register new agents, configure existing ones, manage their tokens and kubeconfig
  entries, and check configuration files for deprecated settings.


  USAGE

    glab cluster agent <command> [command] [--flags]

  COMMANDS

    bootstrap <agent-name> [--flags]           Bootstrap a GitLab Agent for Kubernetes in a project.
    check-manifest-usage [--flags]             Find agents using deprecated GitOps manifest settings. (EXPERIMENTAL)
    get-token [--flags]                        Create a personal access token for a GitLab Agent for Kubernetes.
    list [--flags]                             List GitLab Agents for Kubernetes in a project.
    token <command> [command] [--flags]        Manage GitLab Agents for Kubernetes tokens.
    token-cache <command> [command] [--flags]  Manage cached GitLab Agent tokens.
    update-kubeconfig [--flags]                Update your kubeconfig for use with a GitLab Agent for Kubernetes.

  FLAGS

    -h --help                                  Show help for this command.
    -R --repo                                  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## cluster agent list

Alias: `ls`.

<!-- help-capture: 4dd0d32d1:715a04182d47 -->

```text

  Defaults to the current project. Use `--output json` for JSON output.


  USAGE

    glab cluster agent list [--flags]

  EXAMPLES

    # List agents in the current project
    glab cluster agent list

    # List agents in JSON format
    glab cluster agent list --output json

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## cluster agent update-kubeconfig

<!-- help-capture: 4dd0d32d1:54cfd895e27c -->

```text

  Configures `kubectl` to authenticate through the GitLab Agent for Kubernetes
  using an exec credential plugin.

  - Use `--agent` to specify the agent by its numeric ID.
  - Use `--use-context` to set the agent as the default `kubectl` context.
  - Use `--token-expiry-duration` to control how long the generated token is valid.
  - Use `--cache-mode` to control how generated tokens are cached.


  USAGE

    glab cluster agent update-kubeconfig [--flags]

  EXAMPLES

    # Update kubeconfig for agent 123
    glab cluster agent update-kubeconfig --agent 123

    # Update kubeconfig and set as the default context
    glab cluster agent update-kubeconfig --agent 123 --use-context

  FLAGS

    -a --agent               The numeric agent ID to create the kubeconfig entry for.
    -c --cache-mode          Mode to use for caching the token. Allowed values: keyring-filesystem-fallback, force-keyring, force-filesystem, no. (force-keyring)
    --check-revoked          Check if a cached token is revoked. Requires an API call to GitLab, which adds latency every time a cached token is accessed.
    -h --help                Show help for this command.
    --kubeconfig             Use a particular kubeconfig file.
    -R --repo                Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --token-expiry-duration  Duration for generated token's validity. Minimum is 1 day. Expires at end of day, and ignores time. (24h0m0s)
    -u --use-context         Use as default context.

```

## cluster graph

<!-- help-capture: 4dd0d32d1:1479ed309805 -->

```text

  This command starts a web server that shows a live view of the Kubernetes object graph in a browser.
  It uses the GitLab Agent for Kubernetes running in the cluster.
  It requires:

  - Version 18.1 or later of GitLab and the GitLab Agent.
  - At least the Developer role in the agent project.
  - This command requires a personal access token or project access token
    for authentication. The token must have the `read_api` and `k8s_proxy` scopes.

  Leave feedback in issue 7900.

  ### Resource filtering

  To filter resources, namespaces, and select root objects, use
  Common Expression Language (CEL).

  `object_selector_expression`: Filters objects. The expression must return a boolean. These variables are available:

  - `obj`: The Kubernetes object being evaluated.
  - `group`: The group of the object.
  - `version`: The version of the object.
  - `resource`: The resource name of the object, like `pods` for the `Pod` kind.
  - `namespace`: The namespace of the object.
  - `name`: The name of the object.
  - `labels`: The labels of the object.
  - `annotations`: The annotations of the object.

  `resource_selector_expression`: Filters Kubernetes discovery information to include or exclude resources
  from the watch request. The expression must return a boolean. These variables are available:

  - `group`: The group of the object.
  - `version`: The version of the object.
  - `resource`: The resource name of the object, like `pods` for the `Pod` kind.
  - `namespaced`: The scope of group, version, and resource. Can be `bool`, `true`, or `false`.

  To select root objects, use the `--root-expression` flag. When set, only objects that are directly
  or transitively reachable from root objects are shown. This flag uses the same variables
  as `object_selector_expression`, and must return a boolean. Multiple values are joined with `OR`
  statements. If any match, the object is used as root.

  For more information about using label selectors
  and field selectors to select namespaces, see the Kubernetes documentation.

  ### Advanced usage

  Apart from high-level ways to construct the query, this command enables
  you to construct and send the query using all underlying API features.
  To understand what is possible, and how to do it, see the
  technical design doc

  The user should have permission to access the agent project.
  For more information, see Grant users Kubernetes access.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab cluster graph [--flags]

  EXAMPLES

    # Run the default query for agent 123
    glab cluster graph -R user/project -a 123

    # Show common resources from the core and RBAC groups
    glab cluster graph -R user/project -a 123 --core --rbac

    # Show certain resources
    glab cluster graph -R user/project -a 123 --resource=pods --resource=configmaps

    # Same as above, but more compact
    glab cluster graph -R user/project -a 123 -r={pods,configmaps}

    # Select a certain namespace
    glab cluster graph -R user/project -a 123 -n={my-ns,my-stuff}

    # Select namespaces with a certain label
    glab cluster graph -R user/project -a 123 --ns-label-selector environment=production

    # Pass a custom watch request from a file
    glab cluster graph -R user/project -a 123 --stdin < query.json

    # Show objects reachable from pod roots
    glab cluster graph -R user/project -a 123 --root-expression "resource == \"pods\""

  FLAGS

    -a --agent              The numeric agent ID to connect to.
    --apps                  Watch deployments, replicasets, daemonsets, and statefulsets in the apps/v1 group.
    --batch                 Watch jobs and cronjobs in the batch/v1 group.
    --cluster-rbac          Watch clusterroles and clusterrolebindings in the rbac.authorization.k8s.io/v1 group.
    --core                  Watch pods, secrets, configmaps, and serviceaccounts in the core/v1 group.
    --crd                   Watch customresourcedefinitions in the apiextensions.k8s.io/v1 group.
    -h --help               Show help for this command.
    --ignore-arc-direction  Ignore arc direction when evaluating root connectivity. Requires GitLab and agent version 18.3 or later.
    --listen-addr           Address to listen on. (localhost:0)
    --listen-net            Network on which to listen for connections. (tcp)
    --log-watch-request     Log watch request to stdout. Helpful for debugging.
    -n --namespace          Namespaces to watch. If not specified, all namespaces are watched with label and field selectors filtering.
    --ns-expression         Cel expression to select namespaces. Evaluated before a namespace is watched and on any updates for the namespace object.
    --ns-field-selector     Field selector to select namespaces.
    --ns-label-selector     Label selector to select namespaces.
    --rbac                  Watch roles and rolebindings in the rbac.authorization.k8s.io/v1 group.
    -R --repo               Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -r --resource           Resources to watch. You can see the list of resources your cluster supports by running 'kubectl api-resources'.
    --root-expression       Cel expression to select root objects. Requires GitLab and agent version 18.3 or later.
    --stdin                 Read watch request from standard input.

```
