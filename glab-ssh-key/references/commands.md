# glab ssh-key help

> Capture key `2e352a17e`: checksum-verified official macOS arm64 binary, source commit `2e352a17e7e00bef420b0f38e0ce9ab4e1a38e5d`, archive SHA-256 `017b14c9bb8d54ba1ea2007607f86dbde0352ad8dea566e2647e9c1bae86bcac`. Only adjacent fences marked `2e352a17e` use this provenance. Complete output is preserved with trailing spaces/tabs removed only; indentation, blank lines, Fang uppercase headings, examples, wrapping, truncation, and product spelling are unchanged. Unmarked or differently marked fences retain their scoped prior provenance.

> Earlier provenance, applicable only where no newer per-fence marker is present: Complete help captured from the checksum-verified glab v1.123.0 macOS arm64 release binary; see the v1.13.32 entry in `VERSION` for archive checksums. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

<!-- help-capture: 2e352a17e:3d5ce8c7c646 -->

```text

  Add, list, get, and delete the SSH keys associated with your account.

  GitLab uses SSH keys to authenticate Git operations over SSH, and,
  depending on each key's usage type, to verify signed commits.


  USAGE

    glab ssh-key <command> [command] [--flags]

  COMMANDS

    add [key-file] [--flags]     Add an SSH key to your GitLab account.
    delete [<key-id>] [--flags]  Deletes a single SSH key specified by the ID.
    get [<key-id>] [--flags]     Returns a single SSH key specified by the ID.
    list [--flags]               Get a list of SSH keys for the currently authenticated user.

  FLAGS

    -h --help                    Show help for this command.
    -R --repo                    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## ssh-key add

> Earlier provenance, applicable only where no newer per-fence marker is present: Complete help captured from the checksum-verified glab v1.123.0 macOS arm64 release binary; see the v1.13.32 entry in `VERSION` for archive checksums. Only trailing whitespace is removed; indentation, blank lines, wrapping, truncation, and product spelling are preserved.

<!-- help-capture: 2e352a17e:a043fce79fe1 -->

```text

  Creates a new SSH key owned by the currently authenticated user.

  Requires the '--title' flag.

  GitLab rejects a key whose fingerprint is already registered on your account, even when that key has expired. Use '--
  replace' to delete the existing key with the same SHA256 fingerprint and add it again with the new title, usage type,
  and expiration date.


  USAGE

    glab ssh-key add [key-file] [--flags]

  EXAMPLES

    # Read ssh key from stdin and upload.
    glab ssh-key add -t "my title"

    # Read ssh key from specified key file, upload and set the ssh key type to "authentication".
    glab ssh-key add ~/.ssh/id_ed25519.pub -t "my title" --usage-type "auth"

    # Re-register an expired key with a new expiration date.
    glab ssh-key add ~/.ssh/id_ed25519.pub -t "my title" --expires-at 2027-01-01 --replace

  FLAGS

    -e --expires-at  The expiration date of the SSH key. Uses ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
    -h --help        Show help for this command.
    --replace        Delete an existing key with the same fingerprint, such as an expired key, before adding this one.
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --title       New SSH key's title.
    -u --usage-type  Usage scope for the key. Possible values: 'auth', 'signing' or 'auth_and_signing'. Default value: 'auth_and_signing'. (auth_and_signing)

```

## ssh-key delete

<!-- help-capture: 2e352a17e:33da10bc57b1 -->

```text

  Pass the key ID as an argument, or run the command without arguments
  to select a key interactively. Find key IDs by running `glab ssh-key list --show-id`.

  This action is permanent and cannot be undone.


  USAGE

    glab ssh-key delete [<key-id>] [--flags]

  EXAMPLES

    # Delete SSH key with ID as argument
    glab ssh-key delete 7750633

    # Interactive
    glab ssh-key delete

    # Interactive, with pagination
    glab ssh-key delete -P 50 -p 2

  FLAGS

    -h --help      Show help for this command.
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## ssh-key get

<!-- help-capture: 2e352a17e:c974c2e01481 -->

```text

  Pass the key ID as an argument, or run the command without arguments
  to select a key interactively. Find key IDs by running `glab ssh-key list --show-id`.

  By default, the command prints the public key. Use `--output json` to return
  the full key object.


  USAGE

    glab ssh-key get [<key-id>] [--flags]

  EXAMPLES

    # Get ssh key with ID as argument
    glab ssh-key get 7750633

    # Interactive
    glab ssh-key get

    # Interactive, with pagination
    glab ssh-key get -P 50 -p 2

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (20)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## ssh-key list

<!-- help-capture: 2e352a17e:4153b9afb11a -->

```text

  Each row shows the key's title, key, usage type, and creation date.
  Pass `--show-id` to also display the key ID, which the `get` and `delete`
  commands accept as an argument.


  USAGE

    glab ssh-key list [--flags]

  EXAMPLES

    # List your SSH keys
    glab ssh-key list

    # Include the key ID in the output
    glab ssh-key list --show-id

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --show-id      Shows IDs of SSH keys.

```

