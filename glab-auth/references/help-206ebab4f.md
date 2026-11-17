# Captured glab-auth help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab auth

<!-- help-capture: 206ebab4f:ccd5d353d4ab -->

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

## glab auth configure-docker

<!-- help-capture: 206ebab4f:f7b6b5a5c867 -->

```text

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

## glab auth credential-helper

<!-- help-capture: 206ebab4f:edfc79a4cab6 -->

```text

  Outputs a JSON object on stdout with `type` set to `success` or `error`.

  An `error` response always has a `code` field. Use it instead of matching on the `message` text, which can change. The
  codes are:

  - `not_authenticated`: glab has no credentials for the host.
  - `unsupported_auth_source`: the authentication method in use does not provide a token.
  - `refresh_failed`: the OAuth2 token could not be refreshed.
  - `keyring_unavailable`: the operating system keyring could not be read or written.
  - `invalid_repo_override`: the `--repo` flag or the `GITLAB_REPO` environment variable is not valid.
  - `unknown`: any other error.

  An `error` response also has `host` whenever glab resolved a host, and `oauth_error` when the OAuth2 server returned
  an error code such as `invalid_grant`.

  Callers must parse the JSON response on stdout to detect `type: "error"` responses rather than relying on the process
  exit code, because credential resolution errors exit with status 0 while flag validation errors exit with a non-zero
  status.


  USAGE

    glab auth credential-helper [--flags]

  FLAGS

    -h --help  Show help for this command.
    -R --repo  Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab auth docker-helper

<!-- help-capture: 206ebab4f:58f68f7e92f1 -->

```text

  Responds to Docker credential helper requests for GitLab container
  registries and Artifact Registries. Docker invokes this command
  automatically.


  USAGE

    glab auth docker-helper [--flags]

  EXAMPLES

    # Docker invokes the helper automatically; supported actions are 'store', 'get', and 'erase'.
    # Retrieve the stored credentials for a registry:
    echo registry.gitlab.com | glab auth docker-helper get

  FLAGS

    -h --help  Show help for this command.

```

## glab auth dpop-gen

<!-- help-capture: 206ebab4f:a0aa63da20ee -->

```text

  Generates a demonstrating-proof-of-possession (DPoP) proof JSON Web Token (JWT).
  DPoP cryptographically binds personal access tokens to their owners.

  Use the JWT with a personal access token (PAT) to authenticate to the GitLab API.
  glab signs the JWT with your SSH private key. The JWT remains valid for five
  minutes. After it expires, generate another one.

  Prerequisites:

  - An SSH key pair in RSA, ed25519, or ECDSA format.
  - Enabled DPoP for your account.

  This feature is an experiment and is not ready for production use.
  It might be unstable or removed at any time.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab auth dpop-gen [--flags]

  EXAMPLES

    # Generate a DPoP JWT using an SSH private key and a personal access token
    glab auth dpop-gen --private-key "~/.ssh/id_rsa" --pat "glpat-xxxxxxxxxxxxxxxxxxxx"

    # Generate a DPoP JWT without a PAT (uses the token from 'glab auth login')
    glab auth dpop-gen --private-key "~/.ssh/id_rsa"

    # Generate a DPoP JWT for a different GitLab instance
    glab auth dpop-gen --private-key "~/.ssh/id_rsa" --hostname "https://gitlab.com"

  FLAGS

    -h --help         Show help for this command.
    --hostname        The hostname of the GitLab instance to authenticate with. (gitlab.com)
    --pat             Personal access token (PAT) to generate a DPoP proof for. Defaults to the token set with 'glab auth login'.
    -p --private-key  Location of the private SSH key on the local system.

```

## glab auth git-credential

<!-- help-capture: 206ebab4f:c782a6b30194 -->

```text

  Implements Git credential helper manager.

  USAGE

    glab auth git-credential [--flags]

  FLAGS

    -h --help  Show help for this command.

```

## glab auth login

<!-- help-capture: 206ebab4f:09be01acf2d3 -->

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
  enabled, these variables also override `CI_JOB_TOKEN`. They apply only
  to the host named by `GITLAB_HOST` or `GITLAB_REPO`, and to hosts in the
  configuration file.

  To pass a token on standard input, use `--stdin`.

  On instances where personal access tokens are disabled, sign in with OAuth and use glab as the Git credential helper
  instead of Git Credential Manager. glab automatically refreshes the OAuth token for Git and doesn't need an OAuth
  client secret.

  To configure glab as the Git credential helper non-interactively (for example, in a CI/CD job), use `--setup-git-
  credential-helper`.

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

    # Sign in with OAuth and configure glab as the Git credential helper (recommended when personal access tokens a…
    glab config set client_id <CLIENT_ID> --host gitlab.example.com
    glab auth login --hostname gitlab.example.com --web --setup-git-credential-helper

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

## glab auth logout

<!-- help-capture: 206ebab4f:f59af26e9e4d -->

```text

  Logs out from a GitLab instance. The credentials for the specified instance
  are removed from the global configuration file (default
  `~/.config/glab-cli/config.yml`) and from the operating system's keyring,
  if a token was stored there.


  USAGE

    glab auth logout [--flags]

  EXAMPLES

    # Log out of a specific instance
    glab auth logout --hostname gitlab.example.com

  FLAGS

    -h --help   Show help for this command.
    --hostname  The hostname of the GitLab instance.

```

## glab auth status

<!-- help-capture: 206ebab4f:b2fde3776952 -->

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

