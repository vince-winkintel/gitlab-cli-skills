---
name: glab-quick-actions
description: Use GitLab quick actions — text-based slash commands in comments, descriptions, and MR/issue bodies — via glab CLI. Quick actions execute automatically when saved. Multiple commands can be combined in one comment, making them powerful for batching state changes in a single API call. Triggers on quick actions, slash commands, batch update, /assign, /label, /merge, /approve, /close, /estimate.
---

# glab quick-actions

Use GitLab quick actions (slash commands) via the `glab` CLI to batch multiple state changes in a single API call.

## Quick start

```bash
# Post a single quick action on an issue
glab issue note 123 -m "/assign @alice"

# Batch multiple quick actions in one comment
glab issue note 123 -m "/assign @alice
/label ~bug ~priority::high
/milestone %\"Sprint 5\""

# Post quick actions on a merge request
glab mr note 456 -m "/assign_reviewer @bob
/label ~needs-review
/estimate 2h"
```

## Key concept: batching via CLI

While `glab` has native commands for many individual operations (`glab issue update`, `glab mr update`, etc.), posting quick actions via `glab issue note` or `glab mr note` lets you **batch multiple state changes atomically in a single API call**.

```bash
# Native commands — 3 separate API calls
glab issue update 123 --assignee @alice
glab issue update 123 --label bug,priority::high
glab issue update 123 --milestone "Sprint 5"

# Quick actions — 1 API call, same result
glab issue note 123 -m "/assign @alice
/label ~bug ~priority::high
/milestone %\"Sprint 5\""
```

**When batching is the right choice:**
- Applying 3+ changes to a single issue/MR
- Scripting triage workflows across multiple items
- Triggering actions not exposed by `glab update` flags (e.g., `/spend`, `/epic`, `/promote_to`)

## Syntax rules

| Rule | Detail |
|------|--------|
| Prefix | Every quick action starts with `/` |
| Case | Case-insensitive (`/Assign` = `/assign`) |
| Placement | One command per line; can appear anywhere in a comment/description |
| Parameters | Separated by space after the command name |
| Labels | Prefix with `~` (e.g., `~bug`, `~"priority::high"`) |
| Milestones | Prefix with `%` (e.g., `%"Sprint 5"`) |
| Users | Prefix with `@` (e.g., `@alice`, `@me`) |
| MR/Issue refs | Prefix with `#` for same-project, `group/project#IID` for cross-project |
| Epics | Prefix with `&` (e.g., `&42`) |
| Quoting | Use quotes for multi-word values: `~"priority::high"`, `%"Sprint 5"` |
| Ignored text | Non-quick-action lines are posted as normal comment text |

---

## Issue quick actions

### Assignment

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/assign` | `@user [@user2 ...]` | Assign one or more users |
| `/unassign` | `@user [@user2 ...]` or none | Remove specific assignees or clear all |
| `/reassign` | `@user [@user2 ...]` | Replace all assignees with given users |

```bash
glab issue note 123 -m "/assign @alice @bob"
glab issue note 123 -m "/reassign @charlie"
glab issue note 123 -m "/unassign"
```

### Labels

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/label` | `~label1 ~label2 ...` | Add labels |
| `/unlabel` | `~label1 ...` or none | Remove specific labels or clear all |
| `/relabel` | `~label1 ...` | Replace all labels with given ones |

```bash
glab issue note 123 -m "/label ~bug ~\"priority::high\""
glab issue note 123 -m "/relabel ~\"type::feature\""
glab issue note 123 -m "/unlabel ~needs-triage"
```

### Milestone & scheduling

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/milestone` | `%milestone` | Set milestone |
| `/remove_milestone` | — | Remove milestone |
| `/due` | `<date>` | Set due date (YYYY-MM-DD, `tomorrow`, `next week`) |
| `/remove_due_date` | — | Remove due date |

```bash
glab issue note 123 -m "/milestone %\"Sprint 5\""
glab issue note 123 -m "/due 2024-03-31"
glab issue note 123 -m "/due next week"
```

### Time tracking

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/estimate` | `<time>` | Set time estimate (e.g., `1h30m`, `3d`) |
| `/remove_estimate` | — | Remove time estimate |
| `/spend` | `<time> [<date>]` | Log time spent (e.g., `2h`, `-30m` to subtract) |
| `/remove_time_spent` | — | Remove all time spent |

```bash
glab issue note 123 -m "/estimate 4h"
glab issue note 123 -m "/spend 1h30m 2024-03-15"
glab issue note 123 -m "/spend -30m"
```

### State changes

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/close` | — | Close the issue |
| `/reopen` | — | Reopen a closed issue |
| `/confidential` | — | Make issue confidential |
| `/done` | — | Mark as done (for todos) |
| `/todo` | — | Add to your to-do list |

```bash
glab issue note 123 -m "/close"
glab issue note 123 -m "/reopen"
```

### Relations

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/duplicate` | `#issue` | Mark as duplicate of another issue |
| `/relate` | `#issue [#issue2 ...]` | Add related issue links |
| `/blocks` | `#issue [#issue2 ...]` | This issue blocks others |
| `/blocked_by` | `#issue [#issue2 ...]` | This issue is blocked by others |
| `/unrelate` | `#issue` | Remove relation to another issue |

```bash
glab issue note 123 -m "/duplicate #456"
glab issue note 123 -m "/relate #789 #790"
glab issue note 123 -m "/blocks #800"
```

### Planning & hierarchy

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/epic` | `&epic` or `group&epic` | Add to epic |
| `/remove_epic` | — | Remove from epic |
| `/iteration` | `*iteration:"name"` | Set iteration/sprint |
| `/remove_iteration` | — | Remove iteration |
| `/weight` | `<number>` | Set issue weight |
| `/clear_weight` | — | Clear issue weight |
| `/health_status` | `on_track`, `needs_attention`, `at_risk` | Set health status |
| `/clear_health_status` | — | Remove health status |
| `/board_move` | `~list-label` | Move issue to board list |

```bash
glab issue note 123 -m "/epic &42"
glab issue note 123 -m "/iteration *iteration:\"Sprint 7\""
glab issue note 123 -m "/weight 3"
glab issue note 123 -m "/health_status on_track"
```

### Advanced

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/copy_metadata` | `#issue` or `!mr` | Copy labels and milestone from another item |
| `/clone` | `[path/to/project]` | Clone issue to another project |
| `/move` | `path/to/project` | Move issue to another project |
| `/create_merge_request` | `[branch-name]` | Create MR from this issue |
| `/promote_to` | `incident` or `epic` | Promote issue to another type |

```bash
glab issue note 123 -m "/copy_metadata #456"
glab issue note 123 -m "/move group/other-project"
glab issue note 123 -m "/create_merge_request 123-my-feature"
glab issue note 123 -m "/promote_to incident"
```

---

## MR quick actions

### Approval

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/approve` | — | Approve the MR |
| `/unapprove` | — | Remove your approval |

```bash
glab mr note 456 -m "/approve"
```

### Assignment

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/assign` | `@user [@user2 ...]` | Assign MR to one or more users |
| `/unassign` | `@user ...` or none | Remove assignees |
| `/reassign` | `@user ...` | Replace all assignees |
| `/assign_reviewer` | `@user [@user2 ...]` | Add reviewer(s) |
| `/unassign_reviewer` | `@user ...` or none | Remove reviewer(s) |
| `/reassign_reviewer` | `@user ...` | Replace all reviewers |
| `/request_review` | `@user [@user2 ...]` | Request review from user(s) |

```bash
glab mr note 456 -m "/assign_reviewer @alice @bob
/label ~needs-review"
```

### Labels & milestone

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/label` | `~label1 ...` | Add labels |
| `/unlabel` | `~label1 ...` or none | Remove labels |
| `/relabel` | `~label1 ...` | Replace all labels |
| `/milestone` | `%milestone` | Set milestone |
| `/remove_milestone` | — | Remove milestone |

### Time tracking

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/estimate` | `<time>` | Set time estimate |
| `/remove_estimate` | — | Remove time estimate |
| `/spend` | `<time> [<date>]` | Log time spent |
| `/remove_time_spent` | — | Remove all time spent |

### Merge control

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/merge` | — | Merge when pipeline succeeds |
| `/draft` | — | Mark MR as draft |
| `/ready` | — | Mark MR as ready for review |
| `/rebase` | — | Rebase source branch on target |
| `/squash` | — | Enable squash on merge |
| `/target_branch` | `<branch>` | Change target branch |

```bash
glab mr note 456 -m "/approve
/merge"

glab mr note 456 -m "/draft"
glab mr note 456 -m "/ready
/assign_reviewer @lead"
```

### State & other

| Command | Parameters | Description |
|---------|-----------|-------------|
| `/close` | — | Close the MR |
| `/reopen` | — | Reopen a closed MR |
| `/copy_metadata` | `#issue` or `!mr` | Copy labels and milestone from another item |
| `/react` | `:emoji:` | Add emoji reaction |
| `/title` | `<new title>` | Change MR title |
| `/todo` | — | Add to your to-do list |
| `/done` | — | Mark todo as done |
| `/subscribe` | — | Subscribe to MR notifications |
| `/unsubscribe` | — | Unsubscribe from MR notifications |
| `/relate` | `#issue [#issue2 ...]` | Add related issue links |
| `/blocks` | `#issue [#issue2 ...]` | This MR blocks issues |
| `/blocked_by` | `#issue [#issue2 ...]` | This MR is blocked by issues |

---

## When to use quick actions vs native glab commands

| Scenario | Recommended approach |
|----------|---------------------|
| Single field update | `glab issue update` / `glab mr update` (explicit flags) |
| 3+ changes at once | Quick actions batch in one comment |
| Action not in `update` flags | Quick actions (e.g., `/spend`, `/epic`, `/promote_to`, `/rebase`) |
| Scripting triage of many items | Loop with `glab issue note` quick actions |
| Need flag autocomplete | Native `glab update` commands |
| Audit trail via comment | Quick actions (visible in activity feed) |
| Approve + merge atomically | `/approve` then `/merge` in same comment |

### Decision guide

```
Do you need to update a single field?
├─ Yes → Use native glab command (e.g., glab issue update --label)
│
├─ No, multiple fields at once?
│   ├─ 2-3 fields supported by --flags → native glab update
│   └─ 3+ fields OR unsupported fields → quick actions batch
│
└─ Is the action not available in glab update?
    └─ Yes → Quick actions only (e.g., /spend, /epic, /promote_to, /rebase, /merge)
```

---

## Automation examples

### Triage script: label + assign + milestone in one pass

```bash
#!/usr/bin/env bash
# triage-issues.sh — apply triage metadata to a list of issue IDs
# Usage: ./triage-issues.sh 123 456 789

ASSIGNEE="${ASSIGNEE:-@me}"
LABEL="${LABEL:-~needs-triage}"
MILESTONE="${MILESTONE:-%\"Sprint 5\"}"

for IID in "$@"; do
  glab issue note "$IID" -m "/assign $ASSIGNEE
/label $LABEL
/milestone $MILESTONE"
  echo "Triaged #$IID"
done
```

### Bulk close stale issues

```bash
#!/usr/bin/env bash
# close-stale.sh — close all issues with label ~stale
glab issue list --label stale --state opened --output json \
  | jq -r '.[].iid' \
  | while read -r IID; do
      glab issue note "$IID" -m "/close
/unlabel ~stale"
      echo "Closed #$IID"
    done
```

### MR ready for review + assign reviewer

```bash
#!/usr/bin/env bash
# ready-for-review.sh — mark current branch MR ready and request review
MR_IID=$(glab mr list --source-branch "$(git branch --show-current)" --output json | jq -r '.[0].iid')

glab mr note "$MR_IID" -m "/ready
/assign_reviewer @team-lead
/label ~needs-review"
echo "MR !$MR_IID marked ready"
```

### Time tracking: log spent time from CLI

```bash
#!/usr/bin/env bash
# log-time.sh — log time spent on an issue
# Usage: ./log-time.sh 123 2h30m "2024-03-15"
IID="$1"
TIME="$2"
DATE="${3:-}"

if [[ -n "$DATE" ]]; then
  glab issue note "$IID" -m "/spend $TIME $DATE"
else
  glab issue note "$IID" -m "/spend $TIME"
fi
echo "Logged $TIME on #$IID"
```

### Sprint rotation: move issues to next milestone

```bash
#!/usr/bin/env bash
# rotate-sprint.sh — move open issues from one milestone to the next
OLD_MILESTONE="Sprint 5"
NEW_MILESTONE="Sprint 6"

glab issue list --milestone "$OLD_MILESTONE" --state opened --output json \
  | jq -r '.[].iid' \
  | while read -r IID; do
      glab issue note "$IID" -m "/milestone %\"$NEW_MILESTONE\""
      echo "Moved #$IID to $NEW_MILESTONE"
    done
```

### Approve and queue merge

```bash
# Approve an MR and queue it to merge when pipeline passes
glab mr note 456 -m "/approve
/merge"
```

---

## Notes & limitations

- Quick actions that require specific permissions (e.g., `/merge`, `/approve`) will silently fail if you lack the role.
- `/merge` queues the MR to merge when the pipeline succeeds — it does not force-merge immediately.
- Quick actions in issue/MR descriptions are processed on creation and on edit.
- Some quick actions are only available on specific GitLab tiers (e.g., `/epic`, `/iteration`, `/weight`, `/health_status` require GitLab Premium or Ultimate).
- Quick actions posted as comments are not editable after the fact — post a corrective comment if needed.
- The `glab` CLI does not validate quick action syntax before posting — check for typos in user/label names.

## Related sub-skills

- `glab-issue` — native issue create/update/close commands
- `glab-mr` — native MR create/update/approve/merge commands
- `glab-label` — manage labels before using `/label`
- `glab-milestone` — manage milestones before using `/milestone`
- `glab-iteration` — manage iterations before using `/iteration`

## References

- [GitLab Quick Actions documentation](https://docs.gitlab.com/user/project/quick_actions/)
- `glab issue note --help`
- `glab mr note --help`
