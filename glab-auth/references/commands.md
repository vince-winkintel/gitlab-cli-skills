# glab auth subcommands

Source: <https://docs.gitlab.com/cli/auth/>

> Help output captured from `glab auth <subcommand> --help`.

## login

```
Authenticates with a GitLab instance.

  Stores your credentials in the global configuration file
  (default `~/.config/glab-cli/config.yml`).
  To store your token in your operating system's keyring instead, use `--use-keyring`.
  After authentication, all `glab` commands use the stored credentials.

  If `GITLAB_TOKEN`, `GITLAB_ACCESS_TOKEN`, or `OAUTH_TOKEN` are set,
  they take precedence over the stored credentials.
  When CI auto-login is enabled, these variables also override `CI_JOB_TOKEN`.

  To pass a token on standard input, use `--stdin`.

  In interactive mode, `glab` detects GitLab instances from your Git remotes
  and lists them as options, so you do not have to type the hostname manually.


  USAGE

    glab auth login [--flags]

  EXAMPLES

    # Start interactive setup
    # (If in a Git repository, glab will detect and suggest GitLab instances from remotes)
    glab auth login

    # Authenticate against `gitlab.com` by reading the token from a file
    glab auth login --stdin < myaccesstoken.txt

    # Authenticate with GitLab Self-Managed or GitLab Dedicated
    glab auth login --hostname salsa.debian.org

    # Non-interactive setup
    glab auth login --hostname gitlab.example.org --token glpat-xxx --api-host gitlab.example.org:3443 --api-protoc…

    # Non-interactive setup reading token from a file
    glab auth login --hostname gitlab.example.org --api-host gitlab.example.org:3443 --api-protocol https --git-pro…

    # Semi-interactive OAuth login, skipping all prompts except browser auth
    glab auth login --hostname gitlab.com --web --git-protocol ssh --container-registry-domains "gitlab.com,gitlab.…

    # Non-interactive CI/CD setup
    glab auth login --hostname $CI_SERVER_HOST --job-token $CI_JOB_TOKEN

  FLAGS

    -a --api-host                 Api host url.
    -p --api-protocol             Api protocol: https, http
    --container-registry-domains  Container registry and image dependency proxy domains (comma-separated).
    -g --git-protocol             Git protocol: ssh, https, http
    -h --help                     Show help for this command.
    --hostname                    The hostname of the GitLab instance to authenticate with.
    -j --job-token                Ci job token.
    --ssh-hostname                Ssh hostname for instances with a different SSH endpoint.
    --stdin                       Read token from standard input.
    -t --token                    Your GitLab access token.
    --use-keyring                 Store token in your operating system's keyring.
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
  or configuration). Use `--all` to check all configured instances, or `--hostname` to
  check a specific instance.


  USAGE

    glab auth status [--flags]

  FLAGS

    -a --all         Check all configured instances.
    -h --help        Show help for this command.
    --hostname       Check a specific instance's authentication status.
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
