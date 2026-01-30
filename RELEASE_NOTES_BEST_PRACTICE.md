# Release Notes Best Practice

To avoid newline/escaping issues in GitHub release notes, always write notes to a file and pass that file to the CLI.

## Recommended workflow

```bash
cat <<'EOF' >/tmp/release-notes.md
Title line

- Bullet 1
- Bullet 2
EOF

# Create release with proper newlines

gh release create vX.Y.Z --title "vX.Y.Z" --notes-file /tmp/release-notes.md --repo vince-winkintel/gitlab-cli-skills
```

## Why this works

Shell-escaped newlines ("\\n") can be interpreted literally when passed inline. Using a file preserves exact formatting.
