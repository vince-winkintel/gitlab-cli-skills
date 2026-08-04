# glab auth subcommands

Source: <https://docs.gitlab.com/cli/auth/>

> Help output captured from `glab auth <subcommand> --help`.

## login

```
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

  In interactive mode, glab detects GitLab instances from your Git remotes
  and lists them as options, so you do not have to type the hostname manually.

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
    glab auth login --hostname gitlab.example.org --token glpat-xxx --api-host gitlab.example.org:3443 --api-protocol https --git-protocol ssh

    # Non-interactive setup reading the token from a file
    glab auth login --hostname gitlab.example.org --api-host gitlab.example.org:3443 --api-protocol https --git-protocol ssh --stdin < myaccesstoken.txt

    # Semi-interactive OAuth login, skipping all prompts except browser auth
    glab auth login --hostname gitlab.com --web --git-protocol ssh --container-registry-domains "gitlab.com,gitlab.com:443,registry.gitlab.com"

    # OAuth device authorization flow for headless environments without a local browser.
    # glab displays a one-time code and verification URL; you authorize on any
    # other device with a browser. Requires GitLab 17.9 or later.
    glab auth login --hostname gitlab.com --device

    # CI/CD setup: for most cases, prefer auto-login over manual login
    GLAB_ENABLE_CI_AUTOLOGIN=true glab release list -R $CI_PROJECT_PATH

    # CI/CD setup with manual login: use when the command does not support CI job tokens, or you need a personal access token
    glab auth login --hostname $CI_SERVER_FQDN --job-token $CI_JOB_TOKEN --api-protocol $CI_SERVER_PROTOCOL

  FLAGS

    -a --api-host                 Hostname for the API endpoint, if different from --hostname. Accepts a hostname or hostname:port. Use only when the API is served from a different host than the Git remote.
    -p --api-protocol             Api protocol. Options: https, http.
    --container-registry-domains  Container registry and image dependency proxy domains, comma-separated.
    --device                      Use the OAuth 2.0 device authorization flow. Useful for headless environments where a local browser is not available. Requires GitLab 17.9 or later.
    -g --git-protocol             Git protocol. Options: ssh, https, http.
    -h --help                     Show help for this command.
    --hostname                    The hostname of the GitLab instance to authenticate with.
    --insecure-storage            Store the token as plaintext in the configuration file instead of the operating system's keyring.
    -j --job-token                Ci job token.
    --ssh-hostname                Ssh hostname for instances with a different SSH endpoint. A port is not required; Git uses the port from the remote URL.
    --stdin                       Read the token from standard input.
    -t --token                    Your GitLab access token.
    --web                         Skip the login type prompt and use web/OAuth login.
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

```
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

  FLAGS

    -a --all         Check the authentication status of all configured instances.
    -h --help        Show help for this command.
    --hostname       Check the authentication status of a specific instance.
    -t --show-token  Display the authentication token.
```

## configure-docker

```
Register glab as a Docker credential helper

  USAGE

    glab auth configure-docker [--flags]

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
