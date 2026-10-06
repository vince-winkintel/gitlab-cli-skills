# glab check-update help

> Help captured from the checksum-verified glab v1.121.0 macOS arm64 release binary. Terminal padding and trailing whitespace are removed. The release archive SHA-256 is `b097f05b09614938de267f23465c8215d9ddbebc264232604eee2b63120746e4`.

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
