# glab auth subcommands

Source: <https://docs.gitlab.com/cli/auth/>

## login

Authenticate with GitLab.

```bash
glab auth login
```

Common flags vary by version; consult `glab auth login --help` for options.

## status

Show auth status for current host.

```bash
glab auth status
```

## logout

Remove auth credentials.

```bash
glab auth logout
```

## configure-docker

Configure Docker to use GitLab registry auth.

```bash
glab auth configure-docker
```

## docker-helper

Manage the Docker credential helper for GitLab registry.

```bash
glab auth docker-helper
```

## dpop-gen

Generate a DPoP token for GitLab CLI auth.

```bash
glab auth dpop-gen
```
