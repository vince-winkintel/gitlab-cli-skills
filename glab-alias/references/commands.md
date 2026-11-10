# glab alias help

> **Help provenance — capture key `9b430a11f`:** official macOS arm64 glab v1.130.0; source commit `9b430a11f95ec78d87f19be071d1c381d8803630`; binary archive SHA-256 `5791b652e774e4eca85afba1ebfd9db8498138c3311e0ed0a39d19590311f232`. Adjacent `9b430a11f` markers preserve complete binary stdout except trailing spaces/tabs, including Fang headings and original product spelling. Existing legacy product-spelling normalization remains separately scoped; it is not byte-exact.

> Help output captured from `glab alias --help`.

<!-- help-capture: 9b430a11f:6cdbed27d9b0 -->

```text

  Aliases are shortcuts for longer glab commands. Use aliases to save
  keystrokes for commands you run often, or to compose shell pipelines
  around glab commands.


  USAGE

    glab alias [command] [--flags]

  COMMANDS

    delete <alias name> [--flags]           Delete an alias.
    list [--flags]                          List aliases.
    set <alias name> '<command>' [--flags]  Set an alias for a longer command.

  FLAGS

    -h --help                               Show help for this command.

```

## alias delete

<!-- help-capture: 9b430a11f:a23f1069701d -->

```text

  Delete an alias by name. The deletion is permanent. To restore the
  alias, run `glab alias set` with the original expansion.


  USAGE

    glab alias delete <alias name> [--flags]

  EXAMPLES

    # Delete the alias named "mrv"
    glab alias delete mrv

  FLAGS

    -h --help  Show help for this command.

```

## alias list

<!-- help-capture: 9b430a11f:ed9d04e3c577 -->

```text

  List all configured aliases and their expansions. Results are sorted
  alphabetically by alias name.


  USAGE

    glab alias list [--flags]

  EXAMPLES

    # List all configured aliases
    glab alias list

  FLAGS

    -h --help  Show help for this command.

```

## alias set

<!-- help-capture: 9b430a11f:07d308ccd1e4 -->

```text

  Declare a word as an alias for a longer command.

  Use quotation marks when you define a command, as shown in the examples.

  Your expansion can include arguments and flags. If your expansion
  includes positional placeholders such as `$1` or `$2`, any extra
  arguments that follow the invocation of the alias are inserted into
  those placeholders.

  To run an alias through `sh`, a shell converter, specify the
  `--shell` flag. With shell conversion, you can compose commands
  with `|` or redirect with `>`. Shell aliases have these caveats:

  - Extra arguments that follow the alias are not passed to the expansion.
    To accept arguments, use `$1`, `$2`, and so on.
  - To accept all arguments, use `$@`.

  On Windows, shell aliases run through `sh` as installed by Git for
  Windows. If you installed Git in another way on Windows, shell aliases
  might not work.


  USAGE

    glab alias set <alias name> '<command>' [--flags]

  EXAMPLES

    # Define an alias for "mr view"
    glab alias set mrv 'mr view'
    # Run the alias; it expands to "glab mr view -w 123"
    glab mrv -w 123

    # Define an alias with a positional placeholder
    glab alias set createissue 'issue create --title "$1"'
    # Run the alias with an argument and an extra flag
    glab createissue "My Issue" --description "Something is broken."

    # Define a shell alias that pipes glab output to grep
    glab alias set --shell igrep 'glab issue list --assignee="$1" | grep $2'
    # Run the shell alias with two arguments
    glab igrep user foo

  FLAGS

    -h --help   Show help for this command.
    -s --shell  Declare an alias to be passed through a shell interpreter.

```

