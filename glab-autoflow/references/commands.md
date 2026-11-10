# glab autoflow command reference

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

## autoflow

<!-- help-capture: 9b430a11f:8f332cb30f49 -->

```text

  Run workflows on the AutoFlow service of GitLab Relay.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab autoflow <command> [command] [--flags]

  COMMANDS

    workflow <command> [command]  Manage AutoFlow workflows. (EXPERIMENTAL)

  FLAGS

    -h --help                     Show help for this command.

```

## autoflow workflow

<!-- help-capture: 9b430a11f:a99291911e85 -->

```text

  Start, read, cancel and send values to workflows on the AutoFlow service of GitLab Relay.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab autoflow workflow <command> [command] [--flags]

  COMMANDS

    cancel <workflow-key> [--flags]  Cancel an AutoFlow workflow. (EXPERIMENTAL)
    get <workflow-key> [--flags]     Get the state and result of an AutoFlow workflow. (EXPERIMENTAL)
    send [--flags]                   Send a value to a channel of an AutoFlow workflow. (EXPERIMENTAL)
    start [--flags]                  Start an AutoFlow workflow. (EXPERIMENTAL)

  FLAGS

    -h --help                        Show help for this command.

```

## autoflow workflow cancel

<!-- help-capture: 9b430a11f:acbd865970e4 -->

```text

  Request the cancellation of a workflow on the AutoFlow service of GitLab Relay. The cancellation is asynchronous: the
  command returns once AutoFlow accepted the request.

  The command needs the workflow token that `glab autoflow workflow start` printed. Pass it in a file with `--workflow-
  token-file` or in its environment variable.

  With `--wait`, the command polls until the workflow has finished and exits with an error unless it ended canceled. A
  workflow that finished before the cancellation reached it keeps its state.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab autoflow workflow cancel <workflow-key> [--flags]

  EXAMPLES

    # Cancel a workflow on Runway staging and wait until it is canceled
    glab autoflow workflow cancel "$WORKFLOW_KEY" --hostname staging.gitlab.com \
      --address staging.autoflow-gke.svc.gitlab.net:443 \
      --workflow-token-file workflow-token.txt --wait

  FLAGS

    --address              Address of the AutoFlow service, as <host>:<port>.
    --ca-cert              Path to a PEM-encoded CA certificate to trust for the AutoFlow service, in addition to the system roots.
    -h --help              Show help for this command.
    --hostname             Gitlab hostname to exchange the token with. Defaults to the configured GitLab instance.
    --insecure             Connect to the AutoFlow service without TLS, for a local service only. The AutoFlow token and the workflow's credentials travel in cleartext.
    --namespace-id         Uuid of the AutoFlow namespace. Defaults to the organization of your token.
    --poll-interval        How often to poll the workflow with --wait. (2s)
    --wait                 Poll until the workflow has finished.
    --workflow-token-file  Path to a file with the workflow token that 'glab autoflow workflow start' printed. Use - to read from standard input. Defaults to the GLAB_AUTOFLOW_WORKFLOW_TOKEN environment variable.

  ENVIRONMENT VARIABLES

    GLAB_AUTOFLOW_WORKFLOW_TOKEN: the workflow token that 'glab autoflow workflow start' printed, used when --workflow-token-file is not set.

```

## autoflow workflow get

<!-- help-capture: 9b430a11f:01fbeeffa02a -->

```text

  Get the state of a workflow on the AutoFlow service of GitLab Relay and, once it has finished, its result.

  The command needs the workflow token that `glab autoflow workflow start` printed. Pass it in a file with `--workflow-
  token-file` or in its environment variable.

  With `--wait`, the command polls until the workflow has finished and exits with an error unless it completed.

  The result value is printed as JSON: `None` becomes `null`, an integer or a float a number, a list an array and a dict
  with string keys an object. A value without a JSON equivalent, such as a tuple, bytes or a channel, is printed in the
  protobuf JSON form of `gitlab.autoflow.v1.Value`. `--value-format protojson` prints the whole value in that form.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab autoflow workflow get <workflow-key> [--flags]

  EXAMPLES

    # Wait until a workflow on Runway staging has finished
    glab autoflow workflow get "$WORKFLOW_KEY" --hostname staging.gitlab.com \
      --address staging.autoflow-gke.svc.gitlab.net:443 \
      --workflow-token-file workflow-token.txt --wait

  FLAGS

    --address              Address of the AutoFlow service, as <host>:<port>.
    --ca-cert              Path to a PEM-encoded CA certificate to trust for the AutoFlow service, in addition to the system roots.
    -h --help              Show help for this command.
    --hostname             Gitlab hostname to exchange the token with. Defaults to the configured GitLab instance.
    --insecure             Connect to the AutoFlow service without TLS, for a local service only. The AutoFlow token and the workflow's credentials travel in cleartext.
    --jq                   Filter JSON output with a jq expression.
    --namespace-id         Uuid of the AutoFlow namespace. Defaults to the organization of your token.
    -F --output            Format output as: text, json. (text)
    --poll-interval        How often to poll the workflow with --wait. (2s)
    --value-format         Format of the result value: json, protojson. (json)
    --wait                 Poll until the workflow has finished.
    --workflow-token-file  Path to a file with the workflow token that 'glab autoflow workflow start' printed. Use - to read from standard input. Defaults to the GLAB_AUTOFLOW_WORKFLOW_TOKEN environment variable.

  ENVIRONMENT VARIABLES

    GLAB_AUTOFLOW_WORKFLOW_TOKEN: the workflow token that 'glab autoflow workflow start' printed, used when --workflow-token-file is not set.

```

## autoflow workflow send

<!-- help-capture: 9b430a11f:fcadb5d66c23 -->

```text

  Send a value to a channel of a workflow on the AutoFlow service of GitLab Relay.

  The channel token addresses the channel: `glab autoflow workflow start --channel` prints one for each channel it
  creates, and modules hand out more while the workflow runs. The workflow token of the same workflow authorizes the
  send. Pass each token in a file with `--channel-token-file` and `--workflow-token-file`, or in their environment
  variables.

  `--value` is JSON, converted like the keyword arguments of `glab autoflow workflow start`. Sensitive values are not
  supported yet.

  AutoFlow delivers a value at most once per idempotency key. To retry a send without delivering the value twice, pass
  the same `--idempotency-key`.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab autoflow workflow send [--flags]

  EXAMPLES

    # Send a string to a channel of a workflow on Runway staging
    glab autoflow workflow send --hostname staging.gitlab.com \
      --address staging.autoflow-gke.svc.gitlab.net:443 \
      --workflow-token-file workflow-token.txt --channel-token-file inbox-token.txt \
      --value '"hello"'

  FLAGS

    --address              Address of the AutoFlow service, as <host>:<port>.
    --ca-cert              Path to a PEM-encoded CA certificate to trust for the AutoFlow service, in addition to the system roots.
    --channel-token-file   Path to a file with the channel token from 'glab autoflow workflow start --channel' or from a module. Use - to read from standard input. Defaults to the GLAB_AUTOFLOW_CHANNEL_TOKEN environment variable.
    -h --help              Show help for this command.
    --hostname             Gitlab hostname to exchange the token with. Defaults to the configured GitLab instance.
    --idempotency-key      Key that deduplicates deliveries to the workflow. Defaults to a random key.
    --insecure             Connect to the AutoFlow service without TLS, for a local service only. The AutoFlow token and the workflow's credentials travel in cleartext.
    --namespace-id         Uuid of the AutoFlow namespace. Defaults to the organization of your token.
    --value                Value to send, as JSON.
    --workflow-token-file  Path to a file with the workflow token that 'glab autoflow workflow start' printed. Use - to read from standard input. Defaults to the GLAB_AUTOFLOW_WORKFLOW_TOKEN environment variable.

  ENVIRONMENT VARIABLES

    GLAB_AUTOFLOW_WORKFLOW_TOKEN: the workflow token that 'glab autoflow workflow start' printed, used when --workflow-token-file is not set.
    GLAB_AUTOFLOW_CHANNEL_TOKEN: the channel token from 'glab autoflow workflow start --channel' or from a module, used when --channel-token-file is not set.

```

## autoflow workflow start

<!-- help-capture: 9b430a11f:8b43d43459cd -->

```text

  Submit a Starlark workflow definition to the AutoFlow service of GitLab Relay and start a workflow for it. The command
  returns once the workflow is persisted and does not wait for it to run.

  The command exchanges your GitLab credential for a short-lived token for AutoFlow, so your user needs the
  `token_exchange_autoflow_audience` feature flag on the GitLab instance. By default, the workflow belongs to the
  namespace of your organization.

  `--kwarg` passes a keyword argument to the workflow's `main` function as JSON: `null` becomes `None`, a number without
  a fraction or exponent an integer, an array a list and an object a dict. Sensitive values are not supported yet. `--
  channel` creates a channel and passes it as the keyword argument of the same name, so `glab autoflow workflow send`
  can send to it.

  The output contains the workflow token, the token binding and a token for each channel. All of them are credentials:

  - The workflow key and workflow token read or cancel the workflow later with `glab autoflow workflow get` and `glab
  autoflow workflow cancel`.
  - The idempotency key and token binding re-submit the same workflow to get fresh tokens. Pass them with `--
  idempotency-key` and `--token-binding-file`, or the token binding in its environment variable. A re-submission returns
  the existing workflow and ignores the definition and the keyword arguments. A key without its binding gets
  `PermissionDenied`. It returns channel tokens for the channels it passes again.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab autoflow workflow start [--flags]

  EXAMPLES

    # Start the workflow in main.star on Runway staging
    glab autoflow workflow start --hostname staging.gitlab.com \
      --address staging.autoflow-gke.svc.gitlab.net:443 \
      --script-file main.star

    # Start a workflow with a keyword argument and a channel
    glab autoflow workflow start --address relay.example.com:443 \
      --script 'def main(w, count, inbox): return [gather(inbox) for _ in range(count)]' \
      --kwarg count=2 --channel inbox

    # Re-submit a workflow to get fresh tokens for it
    glab autoflow workflow start --address relay.example.com:443 \
      --idempotency-key glab-T3KQZ7WMXH4RJ2NVB6YLC5DPEA \
      --token-binding-file token-binding.txt --script-file main.star

    # Start an inline workflow and print the result as JSON
    glab autoflow workflow start --address relay.example.com:443 \
      --script 'def main(w): return "hello"' --output json

  FLAGS

    --address             Address of the AutoFlow service, as <host>:<port>.
    --ca-cert             Path to a PEM-encoded CA certificate to trust for the AutoFlow service, in addition to the system roots.
    --channel             Name of a channel to create and pass to the workflow's main function as the keyword argument of the same name. Repeat for more channels.
    -h --help             Show help for this command.
    --hostname            Gitlab hostname to exchange the token with. Defaults to the configured GitLab instance.
    --idempotency-key     Key that deduplicates submissions within the namespace. Defaults to a random key. Without a token binding, the key starts a new workflow, and Relay refuses a key that an earlier workflow uses.
    --insecure            Connect to the AutoFlow service without TLS, for a local service only. The AutoFlow token and the workflow's credentials travel in cleartext.
    --jq                  Filter JSON output with a jq expression.
    --kwarg               Keyword argument of the workflow's main function, as <name>=<JSON value>. Sensitive values are not supported. Repeat for more arguments.
    --namespace-id        Uuid of the AutoFlow namespace. Defaults to the organization of your token.
    -F --output           Format output as: text, json. (text)
    --script              Workflow definition as Starlark source.
    --script-file         Path to a file with the workflow definition. Use - to read from standard input.
    --token-binding-file  Path to a file with the token binding of an earlier submission, base64-encoded as 'glab autoflow workflow start' printed it. Use - to read from standard input. Defaults to the GLAB_AUTOFLOW_TOKEN_BINDING environment variable.

  ENVIRONMENT VARIABLES

    GLAB_AUTOFLOW_TOKEN_BINDING: the token binding of an earlier submission, base64-encoded as 'glab autoflow workflow start' printed it, used when --token-binding-file is not set.

```
