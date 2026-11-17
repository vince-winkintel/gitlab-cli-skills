# Captured glab-check-update help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab check-update

<!-- help-capture: 206ebab4f:bab0e5ce7534 -->

```text

  Checks for the latest version of glab available on GitLab.com.

  When you run this command explicitly, glab always checks for updates,
  even if the previous check was less than 24 hours ago.

  When glab runs this check automatically after other commands, it
  checks for updates at most once every 24 hours.

  When you run this command, glab also reports updates for the GitLab Duo CLI and GitLab Orbit CLI binaries, if they are
  installed.

  To turn off the automatic update check, run
  `glab config set check_update false`. To turn it back on,
  run `glab config set check_update true`.


  USAGE

    glab check-update [--flags]

  EXAMPLES

    # Check for the latest glab version
    glab check-update

    # Check for the latest glab version using the alias
    glab update

  FLAGS

    -h --help  Show help for this command.

```

## glab update

<!-- help-capture: 206ebab4f:5229c22b0e81 -->

```text

  Checks for the latest version of glab available on GitLab.com.

  When you run this command explicitly, glab always checks for updates,
  even if the previous check was less than 24 hours ago.

  When glab runs this check automatically after other commands, it
  checks for updates at most once every 24 hours.

  When you run this command, glab also reports updates for the GitLab Duo CLI and GitLab Orbit CLI binaries, if they are
  installed.

  To turn off the automatic update check, run
  `glab config set check_update false`. To turn it back on,
  run `glab config set check_update true`.


  USAGE

    glab check-update [--flags]

  EXAMPLES

    # Check for the latest glab version
    glab check-update

    # Check for the latest glab version using the alias
    glab update

  FLAGS

    -h --help  Show help for this command.

```

