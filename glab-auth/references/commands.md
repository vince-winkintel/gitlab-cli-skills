# glab auth subcommands

> Capture key `685c1cbd7`: checksum-verified macOS arm64 binary, source commit `685c1cbd74c882e0c93d7011657adde811582ed7`; archive SHA-256 `e77f5756c3c8d9ffeaef0bf234533f395680ab9f128a75cec4c1bd7a1049788c`. Only fences marked `685c1cbd7` use this capture. Normalization removes trailing spaces/tabs only; indentation, blank lines, wrapping, truncation, and product spelling (including `Gitlab`) are preserved. Other fences retain their individual prior provenance.

> Older capture notes below apply only to fences without the `685c1cbd7` marker.


Source: <https://docs.gitlab.com/cli/auth/>

> The `login` block has per-block provenance below. The unchanged `status` block remains a v1.122.0 capture as documented beside it, `configure-docker` remains exact v1.119.0 output, and other earlier refreshed blocks remain from v1.117.0. The v1.119.0 release archive SHA-256 is `d9cddd1dbe9a8bea8d5709f90a9ac13c3dd3eb0d0e94e3bc4fae6b27abd6a3db`.

Copyable credential-helper opt-in: `glab auth login --setup-git-credential-helper` (the help renderer may split this flag across lines). Review the documented global Git configuration effects before using it.

## login

<!-- help-capture: 685c1cbd7:7b0ed4079b2a -->

```text

  Authenticates with a GitLab instance.

  By default, glab stores your credentials in your operating system's
  keyring (macOS Keychain, Windows Credential Manager, or the Secret
  Service on Linux) when one is available. If no keyring is available,
  or if you pass `--insecure-storage`, glab stores them in the global
  configuration file (default `~/.config/glab-cli/config.yml`) as
  plaintext instead. After authentication, all glab commands use the
  stored credentials.

  If you previously signed in and your credentials are stored as
  plaintext in the configuration file, run `glab auth login` again to
  move them into the keyring.

  In CI (when `GITLAB_CI` or `CI` is set), glab stores credentials in the
  configuration file rather than the keyring. Credentials in CI are
  usually supplied through environment variables, and an OS keyring is
  often unavailable there.

  If `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, or `OAUTH_TOKEN` are set,
  they take precedence over the stored credentials. When CI auto-login is
  enabled, these variables also override `CI_JOB_TOKEN`.

  To pass a token on standard input, use `--stdin`.

  To configure glab as the Git credential helper for the host without a prompt, for example in a CI/CD job, use `--
  setup-git-credential-helper`.

  In interactive mode, glab detects GitLab instances from your Git remotes
  and lists them as options, so you do not have to type the hostname manually.

  After you sign in, glab can make the instance your default `host`, which
  glab uses outside a Git repository. glab does this automatically when the
  default is still `gitlab.com` and you have no `gitlab.com` credentials.
  Otherwise, it asks first, or in a non-interactive run prints the
  `glab config set` command to run. glab leaves `host` unchanged in CI,
  or when `GITLAB_HOST`, `GITLAB_URI`, or `GL_HOST` is set.

  When you omit `--hostname` in a non-interactive run, glab authenticates
  with the first of these that applies:

  - The host of the base repository, if you're in a Git repository with a GitLab remote.
  - The `GITLAB_HOST` environment variable, if it's set.
  - The `host` key in your configuration file, if it's set.
  - `gitlab.com`, if none of the above apply.


  USAGE

    glab auth login [--flags]

  EXAMPLES

    # Start interactive setup
    # If in a Git repository, glab detects and suggests GitLab instances from remotes
    glab auth login

    # Authenticate against `gitlab.com` by reading the token from a file
    glab auth login --stdin < myaccesstoken.txt

    # Authenticate with GitLab Self-Managed or GitLab Dedicated
    glab auth login --hostname salsa.debian.org

    # Non-interactive setup
    glab auth login --hostname gitlab.example.org --token glpat-xxx --api-host gitlab.example.org:3443 --api-protoc…

    # Non-interactive setup reading the token from a file
    glab auth login --hostname gitlab.example.org --api-host gitlab.example.org:3443 --api-protocol https --git-pro…

    # Semi-interactive OAuth login, skipping all prompts except browser auth
    glab auth login --hostname gitlab.com --web --git-protocol ssh --container-registry-domains "gitlab.com,gitlab.…

    # Semi-interactive OAuth login for GitLab Self-Managed, with every
    # prompted value supplied by a flag.
    glab auth login --hostname gitlab.example.com --web --api-host gitlab.example.com --ssh-hostname gitlab.example…

    # OAuth device authorization flow for headless environments without a local browser.
    # glab displays a one-time code and verification URL; you authorize on any
    # other device with a browser. Requires GitLab 17.9 or later.
    glab auth login --hostname gitlab.com --device

    # CI/CD setup: for most cases, prefer auto-login over manual login
    GLAB_ENABLE_CI_AUTOLOGIN=true glab release list -R $CI_PROJECT_PATH

    # CI/CD setup with manual login: use when the command does not support CI job tokens, or you need a personal ac…
    glab auth login --hostname $CI_SERVER_FQDN --job-token $CI_JOB_TOKEN --api-protocol $CI_SERVER_PROTOCOL

    # Non-interactive setup that also lets Git push and pull with the same token
    glab auth login --hostname $CI_SERVER_FQDN --token $GITLAB_TOKEN --setup-git-credential-helper

  FLAGS

    -a --api-host                  Hostname for the API endpoint, if different from --hostname. Accepts a hostname or hostname:port. Also skips the API hostname prompt in interactive mode.
    -p --api-protocol              Api protocol. Options: https, http.
    --container-registry-domains   Container registry and image dependency proxy domains, comma-separated.
    --device                       Use the OAuth 2.0 device authorization flow. Useful for headless environments where a local browser is not available. Requires GitLab 17.9 or later.
    -g --git-protocol              Git protocol. Options: ssh, https, http.
    -h --help                      Show help for this command.
    --hostname                     The hostname of the GitLab instance to authenticate with. When omitted, glab prompts in interactive mode, or uses the host resolved from your Git remotes, GITLAB_HOST, and your configuration.
    --insecure-storage             Store the token as plaintext in the configuration file instead of the operating system's keyring.
    -j --job-token                 Ci job token.
    --setup-git-credential-helper  Configure glab as the Git credential helper for this host without prompting. Use this in non-interactive runs, such as CI/CD jobs.
    --ssh-hostname                 Ssh hostname for instances with a different SSH endpoint. A port is not required; Git uses the port from the remote URL. Also skips the SSH hostname prompt in interactive mode.
    --stdin                        Read the token from standard input.
    -t --token                     Your GitLab access token.
    --web                          Skip the login type prompt and use web/OAuth login.

```

### Complete login examples (source, not rendered help)

The exact help capture above retains renderer ellipses for auditability. Do not copy a command containing `…`. The complete examples below come from the matching release-tag `login.go` source, not byte-for-byte rendered output. `glpat-xxx` is an upstream placeholder, not a credential; prefer the `--stdin` form, keep token files outside Git, and never print their contents.

```bash
# Non-interactive setup
glab auth login --hostname gitlab.example.org --token glpat-xxx --api-host gitlab.example.org:3443 --api-protocol https --git-protocol ssh

# Non-interactive setup reading the token from a file
glab auth login --hostname gitlab.example.org --api-host gitlab.example.org:3443 --api-protocol https --git-protocol ssh --stdin < myaccesstoken.txt

# Semi-interactive OAuth login, skipping all prompts except browser auth
glab auth login --hostname gitlab.com --web --git-protocol ssh --container-registry-domains "gitlab.com,gitlab.com:443,registry.gitlab.com"

# Semi-interactive OAuth login for GitLab Self-Managed, with every
# prompted value supplied by a flag.
glab auth login --hostname gitlab.example.com --web --api-host gitlab.example.com --ssh-hostname gitlab.example.com --api-protocol https --git-protocol ssh --container-registry-domains registry.gitlab.example.com

# OAuth device authorization flow for headless environments without a local browser.
# glab displays a one-time code and verification URL; you authorize on any
# other device with a browser. Requires GitLab 17.9 or later.
glab auth login --hostname gitlab.com --device

# CI/CD setup: for most cases, prefer auto-login over manual login
GLAB_ENABLE_CI_AUTOLOGIN=true glab release list -R $CI_PROJECT_PATH

# CI/CD setup with manual login: use when the command does not support CI job tokens, or you need a personal access token
glab auth login --hostname $CI_SERVER_FQDN --job-token $CI_JOB_TOKEN --api-protocol $CI_SERVER_PROTOCOL
```

## logout

```
Logout from a GitLab instance.
  Configuration and credentials are stored in the global configuration file (default `~/.config/glab-cli/config.yml`)


  USAGE

    glab auth logout [--flags]

  EXAMPLES

    Logout of a specific instance
    - glab auth logout --hostname gitlab.example.com

  FLAGS

    -h --help   Show help for this command.
    --hostname  The hostname of the GitLab instance.
```

## status

> Complete help captured from the checksum-verified glab v1.122.0 macOS arm64 release binary. Only terminal padding/trailing whitespace is removed; renderer wrapping and example truncation are preserved. Archive SHA-256: `cbdd6e28d35f9eb09aef79ad23d2712d67c9254677a60ed6d701b5362f659fef`. No product-spelling substitutions were needed in these captures.

```text

  Verifies and displays information about your authentication state.

  By default, this command checks the authentication state of the GitLab instance
  determined by your current context (`git remote`, `GITLAB_HOST` environment variable,
  or configuration). To check all configured instances, use `--all`.
  To check a specific instance, use `--hostname`.


  USAGE

    glab auth status [--flags]

  EXAMPLES

    # Check authentication status for the instance in your current context
    glab auth status

    # Check authentication status for all configured instances
    glab auth status --all

    # Check authentication status for a specific instance
    glab auth status --hostname gitlab.example.com

    # Display the authentication token alongside the status
    glab auth status --show-token

    # Print the authentication status of all configured instances as JSON
    glab auth status --all --output json

  FLAGS

    -a --all         Check the authentication status of all configured instances.
    -h --help        Show help for this command.
    --hostname       Check the authentication status of a specific instance.
    --jq             Filter JSON output with a jq expression.
    -F --output      Format output as: text, json. (text)
    -t --show-token  Display the authentication token.

```

## configure-docker

```

  Configures Docker to use glab for authentication with GitLab
  container registries. This command runs only on Linux and macOS.

  After you run this command, Docker uses glab to obtain credentials
  when it pulls from or pushes to a GitLab container registry.

  Docker looks for the credential helper script by name on your `PATH`. By default, glab installs the script next to the
  glab binary. If that directory is not writable, glab falls back to `~/.local/bin`, then to any other writable
  directory on your `PATH`. If the script lands in a directory that is not on your `PATH`, glab tells you which
  directory to add.


  USAGE

    glab auth configure-docker [--flags]

  EXAMPLES

    # Configure Docker to use glab for GitLab container registry authentication
    glab auth configure-docker

  FLAGS

    -h --help  Show help for this command.

```

## docker-helper

```
A Docker credential helper for GitLab container registries

  USAGE

    glab auth docker-helper [--flags]

  FLAGS

    -h --help  Show help for this command.
```

## dpop-gen

```
Demonstrating-proof-of-possession (DPoP) is a technique to
  cryptographically bind personal access tokens to their owners. This command provides
  the tools to manage the client aspects of DPoP. It generates a DPoP proof JWT
  (JSON Web Token).

  Prerequisites:

  - You must have a SSH key pair in RSA, ed25519, or ECDSA format.
  - You have enabled DPoP for your account, as described in the [GitLab
  documentation.](https://docs.gitlab.com/user/profile/personal_access_tokens/#require-dpop-headers-with-personal-
  access-tokens)

  Use the JWT in combination with a Personal Access Token (PAT) to authenticate to
  the GitLab API. Your JWT remains valid for 5 minutes. After it expires, you must
  generate another token. Your SSH private key is then used to sign the JWT.

  This feature is experimental. It might be broken or removed without any prior notice.
  Read more about what experimental features mean at
  https://docs.gitlab.com/policy/development_stages_support/

  Use experimental features at your own risk.


  USAGE

    glab auth dpop-gen [--flags]

  EXAMPLES

    # Generate a DPoP JWT for authentication to GitLab
    $ glab auth dpop-gen [flags]
    $ glab auth dpop-gen --private-key "~/.ssh/id_rsa" --pat "glpat-xxxxxxxxxxxxxxxxxxxx"

    # No PAT required if you previously used the 'glab auth login' command with a PAT
    $ glab auth dpop-gen --private-key "~/.ssh/id_rsa"

    # Generate a DPoP JWT for a different GitLab instance
    $ glab auth dpop-gen --private-key "~/.ssh/id_rsa" --hostname "https://gitlab.com"

  FLAGS

    -h --help         Show help for this command.
    --hostname        The hostname of the GitLab instance to authenticate with. Defaults to 'gitlab.com'. (gitlab.com)
    --pat             Personal Access Token (PAT) to generate a DPoP proof for. Defaults to the token set with 'glab auth login'. Returns an error if both are empty.
    -p --private-key  Location of the private SSH key on the local system.
```

## auth

<!-- help-capture: 685c1cbd7:d5f029899100 -->

```text

  Manages authentication for glab against one or more GitLab instances. Use
  these commands to log in, log out, check your authentication status,
  and configure glab as a credential helper for Git and Docker.

  glab can authenticate with a personal access token, an OAuth token from
  a web flow, or a CI job token when running in a GitLab CI/CD job.


  USAGE

    glab auth <command> [command] [--flags]

  COMMANDS

    configure-docker    Register glab as a Docker credential helper.
    docker-helper       A Docker credential helper for GitLab container and artifact registries.
    dpop-gen [--flags]  Generate a DPoP (demonstrating-proof-of-possession) proof JWT. (EXPERIMENTAL)
    login [--flags]     Authenticate with a GitLab instance.
    logout [--flags]    Log out from a GitLab instance.
    status [--flags]    View authentication status.

  FLAGS

    -h --help           Show help for this command.

```
