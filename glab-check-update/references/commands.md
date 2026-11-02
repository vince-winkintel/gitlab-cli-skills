# glab check-update help

> **Help provenance.** An adjacent `help-capture` marker selects only its matching key below; an explicit per-block capture label applies only when no marker is present. Historical unmarked notes never override either selector. Keyed captures use checksum-verified official macOS arm64 glab binaries. Complete renderer output is preserved except trailing spaces/tabs: indentation, blank lines, heading/flag casing, product spelling (including `Gitlab`), examples, wrapping, and truncation are unchanged. Unmarked legacy captures retain the scoped normalization and older-version guidance stated below.
>
> - `2e352a17e`: source commit `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`; archive SHA-256 `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`.
>
> Historical capture, superseded by the current marker: checksum-verified macOS arm64 v1.121.0 archive SHA-256 `b097f05b09614938de267f23465c8215d9ddbebc264232604eee2b63120746e4`. That older capture removed terminal padding/trailing whitespace.

<!-- help-capture: 2e352a17e:75de342182b4 -->

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
