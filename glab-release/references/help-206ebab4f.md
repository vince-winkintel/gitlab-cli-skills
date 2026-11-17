# Captured glab-release help

> **Immutable help provenance — capture key `206ebab4f`:** official macOS arm64 glab v1.131.0, source commit `206ebab4fc3fa590b720d2885ac890c195c46650`; source archive SHA-256 `c3d500e7edb7953565e005405e5b4b2e95c684b0489caad79ed3d9f4475ab60d`; binary archive SHA-256 `905271694af2dd68cc254d9a2f3dae80036e5c752a82ea16dec5220f4bff1de7`; executable SHA-256 `61f5ace19367c1127fb103b45bc5ec0e6cfdd73060e5e3c91d3f1173cc694366`. Captured by the parent in isolated credential-free state with network denied. Marked fences preserve complete stdout after trailing spaces/tabs only are removed; uppercase Fang headings, blank lines, indentation, wrapping, truncation and product spelling are unchanged. No deliberate product-spelling normalization is called byte-exact.

The upstream command examples below are reference output, not authorization to perform mutations, issue tokens, install software, change trust, or upload data.

## glab release

<!-- help-capture: 206ebab4f:d45097eac042 -->

```text

  A release bundles a Git tag with release notes and downloadable
  assets, such as binaries or source archives.

  Create and update releases, list and view them, upload assets, and
  download or delete releases. Use `--repo` to target a project other
  than the current one.


  USAGE

    glab release <command> [command] [--flags]

  COMMANDS

    create <tag> [<files>...] [--flags]  Create a new GitLab release, or update an existing one.
    delete <tag> [--flags]               Delete a GitLab release.
    download [<tag>] [--flags]           Download asset files from a GitLab release.
    list [--flags]                       List releases in a repository.
    upload <tag> [<files>...] [--flags]  Upload release asset files or links to a GitLab release.
    view [<tag>] [--flags]               View information about a GitLab release.

  FLAGS

    -h --help                            Show help for this command.
    -R --repo                            Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab release create

<!-- help-capture: 206ebab4f:46a7b884acb0 -->

```text

  Create a new GitLab release for a repository, or
  update an existing one. Requires at least the Developer role.

  An existing release is updated with the new information you provide.

  To create a release from an annotated Git tag:

  1. Create the tag locally with Git, and push the tag to GitLab.
  2. Run this command.
  3. If the Git tag you specify doesn't exist, the command creates a
     release from the latest state of the default branch, and tags it
     with the tag name you specify.

     To override this behavior, use `--ref`. The `ref`
     can be a commit SHA, another tag name, or a branch name.
  4. Optional. To fetch the new tag locally after the release, run
     `git fetch --tags origin`.

  Authentication in CI/CD:

  - Recommended: Use `CI_JOB_TOKEN` and turn on CI auto-login by
    setting `GLAB_ENABLE_CI_AUTOLOGIN=true`. glab sends
    `CI_JOB_TOKEN` in the `JOB-TOKEN` header, which the Releases
    API accepts.
    - The Milestones API does not accept `CI_JOB_TOKEN`, so the token cannot
      close milestones.
    - If you use `--milestone`, the release is still created and the command
      exits successfully. The milestone stays open and glab logs an error.
      To avoid the error, use `--no-close-milestone`.
  - Alternative: Use `GITLAB_TOKEN` set to a project or group access token with the
    `api` scope. With this token, `--milestone` can close milestones.
  - Do not set `GITLAB_TOKEN=$CI_JOB_TOKEN` because the Releases API will
    return a `404 Not Found`. `GITLAB_TOKEN` is sent as a personal access token in
    the `PRIVATE-TOKEN` header, which the Releases API does not accept.

  The `--publish-to-catalog` flag is an experiment: it might be
  unstable or removed at any time, and is not ready for production use.
  For more information, see
  https://docs.gitlab.com/policy/development_stages_support/.


  USAGE

    glab release create <tag> [<files>...] [--flags]

  EXAMPLES

    # Create a release interactively
    glab release create v1.0.1

    # Create a release non-interactively by specifying a note
    glab release create v1.0.1 --notes "bugfix release"

    # Use release notes from a file
    glab release create v1.0.1 -F changelog.md

    # Update an existing release (e.g., change the release date) without modifying notes
    glab release create v1.0.1 --released-at "2024-01-15T10:00:00Z"

    # Upload a release asset with a display name (type will default to 'other')
    glab release create v1.0.1 '/path/to/asset.zip#My display label'

    # Upload a release asset with a display name and type
    glab release create v1.0.1 '/path/to/asset.png#My display label#image'

    # Upload all assets in a specified folder (types default to 'other')
    glab release create v1.0.1 ./dist/*

    # Upload all tarballs in a specified folder (types default to 'other')
    glab release create v1.0.1 ./dist/*.tar.gz

    # Create a release from a CI/CD job using the job token
    GLAB_ENABLE_CI_AUTOLOGIN=true glab release create v1.0.1 --notes "See CHANGELOG.md" --ref "$CI_COMMIT_SHA"

    # Create a release from a CI/CD job using a project or group access token with the 'api' scope
    GITLAB_TOKEN="$ACCESS_TOKEN" glab release create v1.0.1 --notes "See CHANGELOG.md" --ref "$CI_COMMIT_SHA"

    # Create a release with assets, such as packages, specified as a JSON object
    glab release create v1.0.1 --assets-links='
    [
    {
    "name": "Asset1",
    "url":"https://<domain>/some/location/1",
    "link_type": "other",
    "direct_asset_path": "path/to/file"
    }
    ]'

    # (EXPERIMENTAL) Create a release and publish it to the GitLab CI/CD catalog
    # Requires the feature flag `ci_release_cli_catalog_publish_option` to be enabled
    # for this project in your GitLab instance. Do NOT run this manually. Use it as part
    # of a CI/CD pipeline with the "release" keyword:
    #
    # - It retrieves components from the current repository by searching for
    #   `yml` files within the "templates" directory and its subdirectories.
    # - It fails if the feature flag `ci_release_cli_catalog_publish_option`
    #   is not enabled for this project in your GitLab instance.

    # Components can be defined:

    # - In single files ending in `.yml` for each component, like `templates/secret-detection.yml`.
    # - In subdirectories containing `template.yml` files as entry points,
    #   for components that bundle together multiple related files. For example,
    #   `templates/secret-detection/template.yml`.

    glab release create v1.0.1 --publish-to-catalog

  FLAGS

    -a --assets-links       Json string representation of assets links. See Examples for usage.
    -h --help               Show help for this command.
    -m --milestone          The title of each milestone the release is associated with. Multiple milestones can be comma-separated or specified by repeating the flag.
    -n --name               The release name or title.
    --no-close-milestone    Prevent closing milestones after creating the release.
    --no-update             Prevent updating the existing release.
    -N --notes              The release notes or description. Accepts Markdown.
    -F --notes-file         Read release notes 'file'. To read from stdin, use '-'. If both --notes and --notes-file are set, --notes takes precedence.
    --package-name          The package name, when uploading assets to the generic package release with --use-package-registry. (release-assets)
    --publish-to-catalog    (Experimental) Publish the release to the GitLab CI/CD catalog.
    -r --ref                If the specified tag doesn't exist, create a release from the ref and tag it with the specified tag name. Accepts a commit SHA, tag name, or branch name.
    -D --released-at        Iso 8601 datetime when the release was ready. Defaults to the current datetime.
    -R --repo               Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -T --tag-message        Message to use if creating a new annotated tag.
    --use-package-registry  Upload release assets to the generic package registry of the project. Overrides the GITLAB_RELEASE_ASSETS_USE_PACKAGE_REGISTRY environment variable.

```

## glab release delete

<!-- help-capture: 206ebab4f:c47b79f9adfb -->

```text

  Delete release assets to GitLab release. Requires the Maintainer role or higher.

  Deleting a release does not delete the associated tag, unless you specify `--with-tag`.


  USAGE

    glab release delete <tag> [--flags]

  EXAMPLES

    # Delete a release (with a confirmation prompt)
    glab release delete v1.1.0

    # Skip the confirmation prompt and force delete
    glab release delete v1.0.1 -y

    # Delete release and associated tag
    glab release delete v1.0.1 --with-tag

  FLAGS

    -h --help      Show help for this command.
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -t --with-tag  Delete the associated tag.
    -y --yes       Skip the confirmation prompt.

```

## glab release download

<!-- help-capture: 206ebab4f:d72c1518ee6b -->

```text

  Download asset files from a GitLab release.

  If no tag is specified, downloads assets from the latest release.
  To specify a file name to download from the release assets, use `--asset-name`.
  `--asset-name` flag accepts glob patterns.

  If a file already exists in the download directory, the command stops with an error. Use `--clobber` to overwrite it,
  or `--skip-existing` to keep it and continue with the other assets.


  USAGE

    glab release download [<tag>] [--flags]

  EXAMPLES

    # Download all assets from the latest release
    glab release download

    # Download all assets from the specified release tag
    glab release download v1.1.0

    # Download assets with names matching the glob pattern
    glab release download v1.10.1 --asset-name="*.tar.gz"

    # Replace files that were downloaded before
    glab release download v1.1.0 --clobber

    # Download only the assets that are missing
    glab release download v1.1.0 --skip-existing

  FLAGS

    -n --asset-name  Download only assets that match the name or a glob pattern.
    --clobber        Overwrite files that already exist in the download directory.
    -D --dir         Directory to download the release assets to. (.)
    -h --help        Show help for this command.
    -R --repo        Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --skip-existing  Keep files that already exist in the download directory, and download only the missing assets.

```

## glab release list

<!-- help-capture: 206ebab4f:54ad6ab74bee -->

```text

  By default, lists the releases for the current project, most recent
  first. Use `--repo` to target a different project, or `-F json` for
  machine-readable output.


  USAGE

    glab release list [--flags]

  EXAMPLES

    glab release list
    glab release list --per-page 50
    glab release list -R owner/repository
    glab release list -F json

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab release ls

<!-- help-capture: 206ebab4f:bafc94b9d2a8 -->

```text

  By default, lists the releases for the current project, most recent
  first. Use `--repo` to target a different project, or `-F json` for
  machine-readable output.


  USAGE

    glab release list [--flags]

  EXAMPLES

    glab release list
    glab release list --per-page 50
    glab release list -R owner/repository
    glab release list -F json

  FLAGS

    -h --help      Show help for this command.
    --jq           Filter JSON output with a jq expression.
    -F --output    Format output as: text, json. (text)
    -p --page      Page number. (1)
    -P --per-page  Number of items to list per page. (30)
    -R --repo      Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.

```

## glab release upload

<!-- help-capture: 206ebab4f:767273ad685a -->

```text

  Upload release assets to a GitLab release.

  Define the display name by appending '#' after the filename.
  The link type comes after the display name, like this: 'myfile.tar.gz#My display name#package'


  USAGE

    glab release upload <tag> [<files>...] [--flags]

  EXAMPLES

    # Upload a release asset with a display name. 'Type' defaults to 'other'.
    glab release upload v1.0.1 '/path/to/asset.zip#My display label'

    # Upload a release asset with a display name and type.
    glab release upload v1.0.1 '/path/to/asset.png#My display label#image'

    # Upload all assets in a specified folder. 'Type' defaults to 'other'.
    glab release upload v1.0.1 ./dist/*

    # Upload all tarballs in a specified folder. 'Type' defaults to 'other'.
    glab release upload v1.0.1 ./dist/*.tar.gz

    # Upload release assets links specified as JSON string
    glab release upload v1.0.1 --assets-links='
    [
    {
    "name": "Asset1",
    "url":"https://<domain>/some/location/1",
    "link_type": "other",
    "direct_asset_path": "path/to/file"
    }
    ]'

  FLAGS

    -a --assets-links       `Json` string representation of assets links, like: `--assets-links='[{"name": "Asset1", "url":"https://<domain>/some/location/1", "link_type": "other", "direct_asset_path": "path/to/file"}]'`.
    -h --help               Show help for this command.
    --package-name          The package name to use when uploading the assets to the generic package release with --use-package-registry. (release-assets)
    -R --repo               Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    --use-package-registry  Upload release assets to the generic package registry of the project. Alternatively to this flag you may also set the GITLAB_RELEASE_ASSETS_USE_PACKAGE_REGISTRY environment variable to either the value true or 1. The flag takes precedence over this environment variable.

```

## glab release view

<!-- help-capture: 206ebab4f:0a306d66ea8b -->

```text

  View information about a GitLab release.

  Without an explicit tag name argument, shows the latest release in the project.


  USAGE

    glab release view [<tag>] [--flags]

  EXAMPLES

    # View the latest release of a GitLab repository
    glab release view

    # View a release with specified tag name
    glab release view v1.0.1

  FLAGS

    -h --help    Show help for this command.
    --jq         Filter JSON output with a jq expression.
    -F --output  Format output as: text, json. (text)
    -R --repo    Select another repository. You can use either OWNER/REPO or GROUP/NAMESPACE/REPO. The full URL or Git URL is also accepted.
    -w --web     Open the release in the browser.

```

