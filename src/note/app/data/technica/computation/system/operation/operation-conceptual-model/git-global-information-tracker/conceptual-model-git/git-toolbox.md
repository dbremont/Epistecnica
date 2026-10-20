# GIT: Toolbox


> Git commands: Git provides a set of commands that can be used to manipulate and interact with the Git repository, such as “git commit,” “git push,” and “git pull.”
> 

> `git help -a`
> 

## Command

| **Category** | **Command** | **Description** |
| --- | --- | --- |
| 📁 Repository Management | init | Create empty git repository or re-initialize an existing one |
|  | clone | Clone repository into new directory |
|  | config | Get and set repository or global options |
|  | remote | Manage set of tracked repositories |
|  | worktree | Manage multiple working dirs attached to the same repository |
|  | archive | Create archive of files from named tree |
|  | archimport | Import an Arch repository into git |
|  | bundle | Move objects and refs by archive |
|  | pack-objects | Create packed archive of objects |
|  | pack-redundant | Find redundant pack files |
|  | pack-refs | Pack heads and tags for efficient repository access |
|  | multi-pack-index | Write and verify multi-pack-indexes |
|  | update-index | Register file contents in the working directory to the index |
|  | update-ref | Update object name stored in a reference safely |
|  | update-server-info | Update auxiliary information file to help dumb servers |
|  | receive-pack | Receive what is pushed into repository |
|  | upload-pack | Send objects packed back to git fetch-pack |
|  | upload-archive | Send archive back to git-archive |
|  | unpack-objects | Unpack objects from packed archive |
|  | unpack-file | Create temporary file with blob's contents |
|  | write-tree | Create tree from the current index |
|  | cvsexportcommit | Export a single commit to a CVS checkout |
|  | cvsimport | Import a CVS "repository" into a git repository |
|  | cvsserver | Run a CVS server emulator for git |
|  | instaweb | Instantly browse your working repository in gitweb |
|  | read-tree | Read tree information into directory index |
|  | subtree | Split repository into subtrees and merge them |
|  | svn | Bidirectional operation between a Subversion repository and git |
|  | shell | Restricted login shell for GIT-only SSH access |
|  | get-tar-commit-id | Extract commit ID from an archive created using git archive |
| 🧰 Change Management | add | Add file contents to index |
|  | commit | Record changes to repository |
|  | restore | Restore working tree files |
|  | rm | Remove files from the working tree and from the index |
|  | mv | Move or rename file, directory, or symlink |
|  | checkout-index | Copy files from index to working directory |
|  | am | Apply patches from a mailbox |
|  | apply | Apply patch to files and/or to index |
| 🌿 Branching and Merging | branch | List, create, or delete branches |
|  | checkout | Checkout branch or paths to working tree |
|  | merge | Join two or more development histories together |
|  | rebase | Forward-port local commits to the updated upstream head |
|  | switch | Switch branches |
|  | merge-base | Find as good a common ancestor as possible for a merge |
|  | merge-file | Run a three-way file merge |
|  | merge-index | Run merge for files needing merging |
|  | merge-one-file | Standard helper-program to use with git merge-index |
|  | mergetool | Run merge conflict resolution tools to resolve merge conflicts |
|  | merge-tree | Show three-way merge without touching index |
|  | rerere | Reuse recorded resolution of conflicted merges |
|  | cherry | Find commits not merged upstream |
|  | cherry-pick | Apply changes introduced by some existing commits |
|  | show-branch | Show branches and their commits |
| 🌐 Remote Interaction | fetch | Download objects and refs from another repository |
|  | fetch-pack | Receive missing objects from another repository |
|  | pull | Fetch from and merge with another repository or local branch |
|  | push | Update remote refs along with associated objects |
|  | ls-remote | Show references in a remote repository |
|  | send-pack | Push objects over git protocol to another repository |
|  | http-fetch | Download from remote git repository via HTTP |
|  | http-push | Push objects over HTTP/DAV to another repository |
|  | parse-remote | Routines to help parsing remote repository access parameters |
| 🧹 Maintenance & Optimization | gc | Cleanup unnecessary files and optimize local repository |
|  | clean | Remove untracked files from working tree |
|  | filter-branch | Rewrite branches |
|  | commit-graph | Write and verify Git commit-graph files |
|  | count-objects | Count unpacked objects and display their disk consumption |
|  | prune-packed | Remove extra objects that are already in pack files |
|  | prune | Prune all unreachable objects from the object database |
|  | repack | Pack unpacked objects in a repository |
|  | index-pack | Build pack index file for an existing packed archive |
| 🔍 Inspection and Logging | log | Show commit logs |
|  | show | Show various types of objects |
|  | diff | Show changes between commits, commit and working tree, etc. |
|  | diff-files | Compare files in working tree and index |
|  | diff-index | Compare content and mode of blobs between index and repository |
|  | diff-tree | Compare content and mode of blobs found via two tree objects |
|  | difftool | Show changes using common diff tools |
|  | status | Show working-tree status |
|  | whatchanged | Show commit-logs and differences they introduce |
|  | shortlog | Summarize git log output |
|  | describe | Show most recent tag that is reachable from a commit |
|  | grep | Print lines matching a pattern |
|  | cat-file | Provide content or type information for repository objects |
|  | ls-tree | List contents of a tree object |
|  | ls-files | Information about files in index/working directory |
|  | show-index | Show packed archive index |
|  | for-each-ref | Output information on each ref |
|  | name-rev | Find symbolic names for given revisions |
|  | rev-list | List commit object in reverse chronological order |
|  | rev-parse | Pick out and massage parameters for other git commands |
|  | show-ref | List references in a local repository |
| 🧩 Metadata and Notes | notes | Add or inspect object notes |
|  | tag | Create, list, delete or verify tag object signed with GPG |
|  | mktag | Create tag object |
|  | mktree | Build tree-object from git ls-tree formatted text |
|  | var | Show git logical variable |
|  | mailinfo | Extract patch and authorship from a single email message |
|  | mailsplit | Split mbox file into a list of files |
|  | format-patch | Prepare patches for e-mail submission |
|  | send-email | Send collection of patches as emails |
|  | imap-send | Send a collection of patches to an IMAP folder |
|  | quiltimport | Apply a quilt patchset |
|  | interpret-trailers | Add or parse structured information in commit messages |
|  | patch-id | Compute unique ID for a patch |
|  | request-pull | Generate summary of pending changes |
|  | replace | Create, list, delete refs to replace objects |
|  | check-mailmap | Show canonical names and email addresses of contacts |
|  | symbolic-ref | Read and modify symbolic references |
| ⚙️ Tools and Hooks | gui | Run portable graphical interface to git |
|  | help | Display help information about git |
|  | daemon | Run a really simple server for git repositories |
|  | http-backend | Run a server side implementation of Git over HTTP |
|  | column | Display data in columns |
|  | stripspace | Filter out empty lines |
|  | submodule | Initialize, update, or inspect submodules |
| 🛠️ Stashing | stash | Stash away changes to dirty working directory |
| 🐞 Debugging & Bisecting | bisect | Find, by binary search, change that introduced a bug |
|  | blame | Show what revision and author last modified each line of a file |
|  | fsck | Verify connectivity and validity of objects in database |
|  | range-diff | Compare two commit ranges |
|  | citool | Graphical alternative to git commit |
|  | reset | Reset current HEAD to specified state |
|  | reflog | Manage reflog information |
|  | revert | Revert existing commits |
|  | verify-commit | Check GPG signature of commits |
|  | verify-pack | Validate packed git archive files |
|  | verify-tag | Check GPG signature of tags |
|  | version | Show git version |
|  | check-attr | Display gitattributes information |
|  | check-ref-format | Ensure that a reference name is well formed |

## References

- https://git-scm.com/docs/git#_git_commands