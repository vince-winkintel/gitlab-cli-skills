# Captured glab-whatsnew help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab whatsnew

<!-- help-capture: 206ebab4f:ed540117ac71 -->

```text

  With no arguments, shows release notes for every glab release
  published since the last time you ran 'whatsnew' or saw the
  post-upgrade banner — capped at the most recent 10 releases.

  Pass a version argument to view notes for a specific release,
  or use --since to set an explicit baseline.


  USAGE

    glab whatsnew [version] [--flags]

  EXAMPLES

    # Show release notes for every release since you last looked
    glab whatsnew

    # Show notes for the latest published release
    glab whatsnew --latest

    # Show notes for a specific version
    glab whatsnew v1.85.0

    # Show notes for every release published after a given version
    glab whatsnew --since v1.80.0

  FLAGS

    -h --help  Show help for this command.
    --latest   Show release notes for the latest published release only.
    --since    Show release notes for every release newer than this version.

```

