# GIT: Notes


> **Git Notes** are a Git feature that allows you to **attach arbitrary metadata or annotations to a commit** (or other Git objects like tags, blobs, and trees) **without changing the object itself**.
> 

> **Git Notes** are references stored under `refs/notes/` that link additional information (notes) to Git objects—most commonly commits—allowing for non-invasive annotation of the Git history.
> 

## Breviarium

| **Property** | **Description** |
| --- | --- |
| **Non-destructive** | Notes do *not* alter the original commit (unlike amend or rebase) |
| **Structured Metadata** | Notes can be plain text, structured data (e.g., JSON), or programmatically generated |
| **Git Object** | Notes themselves are stored as Git blob objects |
| **Namespace-based** | Notes can be grouped by custom namespaces (e.g., `refs/notes/review`) |
| **Not Pushed by Default** | Notes are not included in `git push` unless explicitly pushed |

## Uses

| **Purpose** | **Command** | **Description** |
| --- | --- | --- |
| 🆕 Add note to HEAD | `git notes add -m "Your message"` | Attaches a note to the latest commit |
| 🆕 Add note to a commit | `git notes add -m "Note text" <commit>` | Attach note to a specific commit |
| ✏️ Edit a note | `git notes edit <commit>` | Opens editor to modify the note |
| ❌ Remove a note | `git notes remove <commit>` | Deletes the note on the given commit |
| 📄 Show note for a commit | `git notes show <commit>` | Displays note attached to a commit |
| 📜 Show notes in log | `git log --show-notes` | Shows notes along with commit log |
| 📚 List all notes | `git notes list` | Lists all notes and their commit hashes |
| 🔄 Merge notes | `git notes merge <notes-branch>` | Merges notes from another ref |
| 🔀 Rebase notes | `git notes rebase <old-base>` | Re-applies notes from one base to another |
| 🌲 Use custom namespace | `git notes --ref=<namespace> <subcommand>` | Use alternate note ref (e.g., `review`, `ci`, `audit`) |
| 📤 Push notes to remote | `git push origin refs/notes/*` | Push all notes namespaces to remote |
| 📥 Fetch notes | `git fetch origin refs/notes/*:refs/notes/*` | Fetch all remote notes refs |

## References

- https://git-scm.com/docs/git-notes
- https://news.ycombinator.com/item?id=44345334