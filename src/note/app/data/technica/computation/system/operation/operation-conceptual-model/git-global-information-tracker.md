---
tags: [tool]
---

# GIT (Global Information Tracker)

- [Source Code](note.html?n=technica/computation/system/operation/operation-conceptual-model/source-code.md)

> In this note, we explore **Git** from first principles, moving from the interface down to the implementation layer, and back.
> 

> **Git** is an interface for distributed source control, implemented as a **Merkle-DAG content-addressable datastore** whose core objects (blob, tree, commit, tag) encode repository state and history.
> 

> **Git Design Philosophy**: Set of principles/ideas that can be confined in powerful, if you know the tools they use will be evident.
> 

- [How to make sure that unwanted files are not committed?](note.html?n=technica/computation/system/operation/operation-conceptual-model/how-to-make-sure-that-unwanted-files-are-not-committed.md)

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | … |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | … |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | Git is a **distributed version control system** that captures the **state of a repository as a directed acyclic graph of commits**, allowing precise tracking of changes over time. Its essence is **snapshot-based, content-addressable storage for collaborative software development**. |
| **Evidentia (Evidence) 📊** | Verification comes from: `git log`, `git diff`, `git status`, and inspecting objects via `git cat-file`. Its correctness is **provable via hashing (SHA-1/256), DAG structure, and reproducibility of history**. Peer-reviewed adoption and success in large-scale projects like Linux demonstrate its reliability. |
| **Telos (Intent) 🎯** | Git exists to **track changes, coordinate collaboration, manage code history**, and support branching/merging. It **intends to make code development reliable, traceable, and collaborative**, with outcomes like conflict resolution, reproducibility, and auditability. |
| **Gnosis (Understanding) 🧠** | Mental model: **repository = DAG of commits → trees → blobs**, with operations modifying snapshots. Build understanding gradually: basic commit workflow → branching & merging → low-level objects & refs → distributed collaboration. Hierarchical mental model: file content → trees → commits → branches → remotes. **Requires prior knowledge of filesystems, hashing, and graph structures**. |
| **Epignosis (Application) 🛠️** | Skills: branching/merging strategies, rebasing, cherry-picking, history rewriting. Advanced use: monorepos, submodules, CI/CD pipelines. Real-world problems: managing collaborative development, reverting mistakes, auditing code history, scaling distributed teams. |
| **Relatio (Connections) 🔗** | Related to: **version control theory, distributed systems, cryptographic hashing, DAGs, software engineering practices, DevOps, continuous integration**. Interdisciplinary connections: graph theory, systems thinking, collaboration psychology. |
| **Idoneitas (Suitability) 📐** | Git is extremely effective at **version tracking, collaboration, and maintaining integrity**. Metrics: adoption rate, speed, robustness in large-scale projects (Linux kernel has >1M commits), low conflict rates in well-structured workflows. |
| **Limites (Limits) ⛔** | Limitations: **steep learning curve, complexity of rebasing/cherry-picking, large binary files inefficient, non-linear history can confuse beginners**. Constraints: storage tied to snapshot-based model, operation atomicity depends on local/remote coordination. |
| **Contextus (Context) 🌍** | Developed by **Linus Torvalds (2005)** for Linux kernel development. Context: need for **distributed, fast, reliable VCS** after BitKeeper issues. Cultural: open-source collaboration and large-scale distributed dev practices. |
| **Dynamis (Evolution) 🌱** | Evolving toward: **better large file support (Git LFS), improved GUIs, better conflict resolution, AI-assisted merges, deeper integration into DevOps pipelines**. Git's principles inspire **new distributed tools**. |
| **Critica (Critique) 🔍** | Criticisms: **complexity, confusing CLI, potential for destructive commands, merge conflicts, usability for non-developers**. Addressed via GUIs (GitKraken, GitHub Desktop), training, and workflow conventions. |
| **Verbum Usus (Language Use) 🗣️** | Commonly used as verb/noun: *“I’ll git this branch”*, *“push to GitHub”*. Semantic patterns: branching, merging, pushing, cloning. Stylistically technical; evolves with CI/CD practices and community conventions (GitHub, GitLab, etc.). |

### 🧠 Mental Representation

> How should we think about **GIT**?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

### 📘 Study Guide

**Why should we look into git internals?**

- Git was designed for Linux kernel development by Linux kernel development.
- Internals > Usage.
- They envision the project as a set of simple abstractions that can be composed.
- Knowing the fundamentals of abstraction gives you insight on how to use the tool sufficiently.
- That means the git interface does not make sense if you don’t understand the fundamental abstractions.

## **Version Control Model**

> The **Version Control Model** tracks changes to files over time by creating snapshots of the entire project at specific points, allowing users to revert to previous states, compare changes, and collaborate efficiently.
> 

> **Snapshot History Graph:** A Git repository is a directed acyclic graph $G=(V,E)$ where each node $c \in V$ is a commit storing a full snapshot tree $T_c$, and each edge $(c,p) \in E$ records that commit $c$ was derived from parent $p$; thus history is represented as a graph of snapshots rather than a log of diffs.
> 

> snapshot history operations (merge, apply, cherry-pick, rebase, etc.)
> 

### Repository

![](https://i.redd.it/nm1w0gnf2zh11.png)

A **repository** (or *repo*) is the fundamental data structure of a version control system. It contains:

- **Project files**: the current working version of the project.
- **History**: all past commits, representing snapshots of the project over time.
- **Metadata**: branches, tags, configuration, and references.

In Git specifically, a repository is composed of:

- **.git directory**: the hidden folder storing the entire history, objects (blobs, trees, commits, tags), and configuration.
- **Working directory**: the actual project files you see and edit.
- **Staging area (index)**: a preparation space for commits.

### File State

| **File State** | **Description** |
| --- | --- |
| **Untracked** | Files not tracked by Git; they are not part of the commit history and Git has not recorded changes. |
| **Staged** | Files modified and added to the **staging area**, preparing them for the next commit. |
| **Committed** | Files stored in the repository as a **snapshot**, forming part of the commit history. |
| **Modified** | Files altered but **not yet staged**; changes are not yet part of the commit history. |
| **Unmodified** | Files that **have not changed** since the last commit. |
| **Ignored** | Files explicitly ignored by Git; they are not tracked or included in commit history. |
| **Conflicted** | Files with **merge conflicts**, where changes from two branches conflict. |

### **Distributed Repository Model**

> In a **Distributed Repository Model**, every developer has a **complete copy** of the project’s repository, including all files, commit history, branches, and tags.
> 

Key properties:

- **Full clones**: Each clone is a self-contained repository, not just a client.
- **Local operations**: Commits, branching, and merging happen locally without needing network access.
- **Collaboration by synchronization**: Developers exchange changes by pushing and pulling between repositories (e.g., GitHub, GitLab, or peer-to-peer).
- **Resilience**: Because every clone contains the full history, there is no single point of failure.
- **Flexible workflows**: Supports centralized (hub-and-spoke), feature-branch, and fork-and-pull models.

### GIT Distributed Protocol

> 

### Snapshot History Operation

| **Operation** | **Description** | **Possible Failures** | **Procedure** |
| --- | --- | --- | --- |
| **Commit** | Creates a snapshot of the current repository state. | Fail if no staged changes or hooks reject commit. | Create blobs for staged files, build a tree linking them, and make a commit pointing to the tree. |
| **Checkout** | Restores repository to a specific commit. | Fails if local changes would be overwritten. | Replace working directory and index with the tree of the target commit and move HEAD. |
| **Branch** | Creates a new pointer to a commit. | Fails if branch name exists. | Create a ref pointing to the current commit hash. |
| **Merge** | Combines two branches into a single commit. | Conflicts if same files modified differently. | Compute diffs from the merge base, combine trees, resolve conflicts, and create a commit with two parents. |
| **Revert** | Generates a commit that undoes a previous commit. | Conflicts if overlapping changes exist. | Apply the inverse of the target commit’s changes to the current tree and commit the result. |
| **Cherry-pick** | Applies changes from a specific commit onto current branch. | Conflicts if overlapping changes exist. | Apply the commit’s diff to the current tree and create a new commit, resolving conflicts if needed. |
| **Reset** | Moves branch pointer to a previous commit. | Can discard uncommitted changes. | Update the branch ref to the target commit and optionally reset the index and working directory. |
| **Rebase** | Reapplies a sequence of commits onto another base commit. | Conflicts possible; rewrites history. | Sequentially apply diffs of commits onto the new base tree and create new commits, resolving conflicts if any. |
| **Tag** | Labels a commit with a human-readable name. | Fails if tag already exists. | Create a tag object pointing to a commit and update the refs/tags entry. |
| **Diff** | Shows differences between snapshots. | Safe, but may show unexpected differences. | Compare tree objects recursively and report blob-level differences. |
| **Pull** | Fetches changes from a remote repository and integrates them into the current branch. | Conflicts if local changes overlap with remote changes; network errors; authentication failures. | Perform a `fetch` to update remote-tracking branches, then merge (or rebase) the fetched commits into the current branch, resolving conflicts if necessary. |

## Storage Model

> What is the Git object model, and how are its abstractions represented on disk?
> 

> The **Git** Storage **Model** is a **content-addressable storage system** that uses immutable objects—blobs (file content), trees (directory structure), commits (snapshots with metadata), and tags (references to commits)—identified by unique SHA-1 hashes to efficiently store and manage version history.
> 

### **Object**

| **Object Type** | **Description** | **Unique Identifier** | **Content** |
| --- | --- | --- | --- |
| **Blob** | Represents the content of a file. It stores the file's data but no filename or metadata (like permissions). | SHA-1 (or SHA-256) hash of content | Raw file content (e.g., source code, text, or binary data). |
| **Tree** | Represents a directory. It contains references to blobs (files) and other trees (subdirectories). | SHA-1 (or SHA-256) hash of tree | File and directory structure, including filenames, file types, permissions, and object references. |
| **Commit** | Represents a snapshot of the repository. It ties together a tree, parent commits, and metadata. | SHA-1 (or SHA-256) hash of commit | Metadata (author, timestamp, message), reference to a tree object, and parent commit(s). |
| **Tag** | Represents a human-readable reference to a specific commit or object (lightweight or annotated). | SHA-1 (or SHA-256) hash of tag | For annotated tags: metadata (tagger, timestamp, message) and reference to another object (usually a commit). |

### .git

> The **.git directory** is the hidden metadata folder at the root of a Git repository that stores all version control information, including objects (blobs, trees, commits, tags), references (branches, tags), configuration, hooks, and logs, enabling Git to track and manage the project's history.
> 

| **Directory/File** | **Purpose** | **Contents** |
| --- | --- | --- |
| **`HEAD`** | Points to the current branch or commit. | Contains a reference (e.g., `ref: refs/heads/main`) or a commit hash. |
| **`config`** | Repository-specific configuration settings. | Git configuration options (e.g., remote URLs, branch settings). |
| **`description`** | Repository description (used by GitWeb). | A plain text file describing the repository. |
| **`hooks/`** | Directory for Git hooks (custom scripts triggered by Git events). | Sample hook scripts (e.g., `pre-commit`, `post-receive`). |
| **`info/`** | Additional repository information. | Contains `exclude` file for local ignore rules (like `.gitignore`). |
| **`objects/`** | Stores all Git objects (blobs, trees, commits, tags). | Subdirectories with SHA-1 hashes as filenames, storing compressed objects. |
| **`refs/`** | Stores references (pointers to commits). | Contains: |
|  | - `heads/`: Branch references. | Files named after branches (e.g., `main`, `feature-branch`). |
|  | - `tags/`: Tag references. | Files named after tags (e.g., `v1.0`, `v2.0`). |
|  | - `remotes/`: Remote-tracking references. | Files tracking remote branches (e.g., `origin/main`). |
| **`index`** | The staging area (also called the index). | Tracks changes to be included in the next commit. |
| **`logs/`** | Logs of changes to references (e.g., branches, HEAD). | Contains `refs/heads/` and `HEAD` logs for tracking commit history. |
| **`packed-refs`** | Compressed file storing all references (branches, tags) for efficiency. | Lists references in a single file to optimize performance. |
| **`COMMIT_EDITMSG`** | Temporary file storing the commit message during a commit. | Contains the most recent commit message. |
| **`FETCH_HEAD`** | Temporary file storing fetched references from remote repositories. | Lists branches fetched during the last `git fetch`. |
| **`ORIG_HEAD`** | Backup of the previous state of HEAD before dangerous operations. | Stores the commit hash of HEAD before operations like merge or rebase. |
| **`MERGE_HEAD`** | Tracks the commit being merged during a merge operation. | Contains the commit hash of the branch being merged. |
| **`CHERRY_PICK_HEAD`** | Tracks the commit being cherry-picked during a cherry-pick operation. | Contains the commit hash of the cherry-picked commit. |

### **Merkle-DAG Content-Addressable Datastore**

> In simplified form, git object storage is "just" a DAG of objects, with a handful of different types of objects. They are all stored compressed and identified by an SHA-1 hash (that, incidentally, isn't the SHA-1 of the contents of the file they represent, but of **their representation in git**).
> 

## Hooking Model

> The **Git Hooking Model** allows users to trigger custom scripts at specific points in Git's workflow (e.g., before a commit or after a merge), enabling automation, policy enforcement, and integration with external tools.
> 

> See more here for the general concept - [Adaptation](note.html?n=technica/computation/system/programming/conceptual-model-programming/adaptation.md).
> 

| **Hook Name** | **Trigger Point** | **Purpose** | **Common Use Cases** |
| --- | --- | --- | --- |
| **Client-Side Hooks** |  |  |  |
| `pre-commit` | Before a commit is created. | Inspect the snapshot being committed. | Run linters, check for syntax errors, or enforce coding standards. |
| `prepare-commit-msg` | Before the commit message editor is launched. | Modify the default commit message. | Add a template or include issue tracking information. |
| `commit-msg` | After the commit message is entered but before the commit is finalized. | Validate or modify the commit message. | Enforce a specific commit message format. |
| `post-commit` | After the commit is completed. | Perform actions after a commit. | Send notifications or update logs. |
| `pre-rebase` | Before a rebase operation starts. | Prevent rebasing certain commits or branches. | Block rebasing of specific branches (e.g., `main`). |
| `post-checkout` | After a successful `git checkout` or `git clone`. | Set up the working directory. | Install dependencies or update configuration files. |
| `post-merge` | After a successful `git merge`. | Perform cleanup tasks or rebuild files. | Rebuild project files or update dependencies. |
| `pre-push` | Before a `git push` operation. | Validate changes before they are pushed to the remote repository. | Run tests or check for sensitive data. |
| **Server-Side Hooks** |  |  |  |
| `pre-receive` | Before any references are updated on the remote repository. | Enforce policies on incoming changes. | Reject pushes that don’t meet certain criteria (e.g., unauthorized users). |
| `update` | For each reference being updated (e.g., branch or tag). | Enforce fine-grained access control or validation. | Validate changes to specific branches or tags. |
| `post-receive` | After all references have been updated. | Perform actions after changes are accepted. | Trigger CI/CD pipelines or send notifications. |

## Reference Model

> The **Git Reference Model** uses lightweight, mutable pointers (like branches, tags, and HEAD) to track and navigate commits, providing human-readable names for specific points in the commit history while the underlying objects (blobs, trees, commits) remain immutable and content-addressable.
> 

| **Type of Reference** | **Description** | **Storage Location** | **Example** |
| --- | --- | --- | --- |
| **Branch** | A pointer to the latest commit in a line of development. | `.git/refs/heads/` | `main`, `feature-branch`. |
| **Tag** | A pointer to a specific commit, often used to mark releases or important points. | `.git/refs/tags/` | `v1.0`, `v2.0`. |
| **HEAD** | A special pointer to the current branch or commit. | `.git/HEAD` | `ref: refs/heads/main` (points to the `main` branch). |
| **Remote Reference** | Tracks the state of branches in remote repositories. | `.git/refs/remotes/<remote-name>/` | `origin/main`, `upstream/develop`. |
| **Notes** | Additional metadata attached to commits (rarely used). | `.git/refs/notes/` | Used for adding notes to commits. |

## **Limits**

| Question | Answer | Notes |
| --- | --- | --- |
|  **Maximum size of a single blob Git can store efficiently?** | Practically, up to **100 MB** per file is recommended. Git can technically store larger files, but performance degrades. | GitHub blocks files >100 MB by default. |
| **Handling very large repositories (millions of commits/files)?** | Git can handle large repos, but **operations like clone, fetch, or diff** slow down. Shallow clones or sparse-checkouts help. | Linux kernel (~1.5M commits) is manageable due to careful workflow. |
| **Practical performance limits for operations (`clone`, `fetch`, `checkout`, `merge`) in large repos?** | Depends on system memory, disk speed, and repo structure. `clone` can take hours for very large repos. `merge` conflicts become harder with complex histories. | Sparse checkout, partial clone, and incremental fetch mitigate problems. |
| **Handling large binary files** | Git does **not efficiently store large binaries** due to snapshot-based storage. **Git LFS** (Large File Storage) is recommended. | Git LFS stores pointer files in repo; actual binaries on external storage. |
| **Hosting service limits** | GitHub: 100 MB per file, 5 GB repo recommended limit; GitLab: 10 GB repo recommended; Bitbucket: 2 GB repo limit. | Limits vary by service; exceeding them may require LFS or splitting repos. |
| **Scaling of Git objects** | Each commit/tree/blob is stored as a SHA-1/256 object. Millions of objects increase `.git` folder size and slow down operations like `git gc`. | Running `git gc` (garbage collection) periodically improves performance. |
| **Network limits for push/pull** | Large pushes/pulls may hit **HTTP timeout, bandwidth, or hosting service restrictions**. Shallow clones or pushing in smaller batches helps. | Use Git LFS or mirroring for huge assets. |
| **Branching and merging complexity in large histories** | Merge conflicts increase with number of branches and commits; history rewriting (`rebase`) becomes slower. | Keeping a clean branching strategy (feature branches, trunk-based) mitigates issues. |
| **Theoretical limits of Git’s hash-based storage** | SHA-1/256 hashes make collisions extremely unlikely. Practical limit is more about **disk/memory** than hash collisions. | SHA-1 collision risk negligible for normal repos; SHA-256 used in newer Git versions. |
| **Strategies to mitigate limits in large-scale projects** | - Use **Git LFS** for large files |  |

## Conceptual Model

> The **Git object model** consists of four core objects—**blobs** (file content), **trees** (directory structure), **commits** (snapshots with metadata), and **tags** (references to specific commits)—all identified by unique SHA-1 hashes and stored in a content-addressable system for efficient version control.
> 

Conceptual Model: GIT

## ❓ QA

- What happens when you run git gc?
- How does Git handle large repositories or binary files?
- What are Git packfiles, and how do they optimize storage?
- How can you interactively edit the history of a branch in Git?
- What is a detached HEAD state in Git, and how can it occur?
- What does git reflog do, and how can it help recover lost commits?
- What is the difference between git reset --soft, --mixed, and --hard?
- What happens internally when you run git add, git commit, and git push?
- How does Git handle submodules, and what are the challenges of working with them?
- What is the difference between git merge and git rebase, and when would you use each?

### How can I list all objects that represent a Git repository?

- `git rev-list --objects --all`
- `git rev-list --all`
- `git rev-list --objects --all | git cat-file --batch-check='%(objectname) %(objecttype) %(rest)'`

### How can I Explore the Object Content?

> Git stores data as **objects** (blobs, trees, commits, and tags) in a **content-addressable datastore**. You can explore these objects to inspect the repository history and contents.
> 

| **Command** | **Description** |
| --- | --- |
| `git cat-file -t <hash>` | Shows the **type** of the object (`blob`, `tree`, `commit`, or `tag`). |
| `git cat-file -p <hash>` | Shows the **contents** of the object in a human-readable form. For example: file content for blobs, directory listing for trees, commit metadata for commits. |
| `git ls-tree <tree-hash>` | Lists the contents of a **tree object**, showing files and subtrees with their types and hashes. |
| `git show <commit-hash>` | Displays the **commit details** along with the diff introduced by that commit. |
| `git rev-list --objects --all` | Lists all object hashes and their paths in the repository. Can be combined with `git cat-file --batch-check` to show types. |
| `git log --raw` | Shows the commit history and **affected files** in each commit. |

**Tips:**

- To explore an object efficiently in bulk, use **`git cat-file --batch`** or **`git cat-file --batch-check`**.
- Every Git object can be inspected since Git uses a **Merkle-DAG**: commits point to trees, trees point to blobs. Following these links allows complete exploration.
- Objects are stored in `.git/objects/` or packed in `.git/objects/pack/`.

### In Git, how does a tree object represent the repository’s current state? When a commit changes only some files, does the tree still reference the existing blobs for files that remain unchanged?

- **Tree objects** in Git represent the **state of a directory** at a point in time.
    - Each tree contains **entries for files and subdirectories** in that directory.
    - Each entry references either a **blob** (file content) or another **tree** (subdirectory) by its SHA-1/256 hash.
- **Commit objects** point to a single **root tree**, which represents the entire repository snapshot at that commit.
- **Unchanged files are reused**:
    - Git does **not duplicate unchanged file content**.
    - If a commit modifies only some files, the new tree references the **same blobs** for files that were not changed.
    - Similarly, unchanged subtrees are reused, so Git stores only **new blobs and new tree objects for changed directories**.
- **Implications**:
    - Efficient storage: Git only creates objects for **new or modified content**.
    - Integrity: Every tree references blobs by hash, so any modification changes the tree’s hash.
    - Snapshot-based model: Each commit represents a **complete snapshot**, but actual storage is mostly incremental due to object reuse.

### Given a blob node in the Git Merkle-DAG, how can we find all parent tree nodes that reference it (degree)?

- List the tree object: `git rev-list --objects --all | git cat-file --batch-check='%(objectname) %(objecttype)' | grep tree`
- List tree object name - file path:

```bash
git rev-list --objects --all \
| cut -d' ' -f1 \
| git cat-file --batch-check \
| awk '$2=="tree"{print $1}' \
| xargs -I {} sh -c 'git ls-tree -r "{}" | awk -v t="{}" "{print t \" - \" \$3}"'
```

### How many blobs are in a git Repo?

```bash
git rev-list --objects --all \
| cut -d' ' -f1 \
| git cat-file --batch-check \
| awk '$2=="blob"{count++} END{print count}'
```

### How many times does a file has been references by a Blob?

> 

### How does Git's content-addressable storage work?

> echo "Hello World" | git hash-object --stdin
> 

> git cat-file -p e090cd1a83414176193ed133458d4861b97044be | git hash-object --stdin
> 

**Objects in Git**

> Git stores everything as objects in its **object database** (`.git/objects`). There are four main types of objects:
> 
1. **Blob** – stores the content of a file (no filename, no path).
2. **Tree** – stores the structure of a directory: names, modes, and hashes of blobs or other trees.
3. **Commit** – points to a tree and stores metadata (author, message, parent commits).
4. **Tag** – annotated tags pointing to another object.

**Content-Addressable Storage Concept**

- Each object is **identified by a hash of its content**.
- Git uses **SHA-1** (or SHA-256 in newer versions) to compute this hash.
- The hash is called the **object ID**.

### What happens if two object share the same hash?

> A collision occurs if **two different objects have exactly the same hash**. In Git terms: Different content (different blob, tree, or commit) → same SHA hash.
> 

> Git identifies every object (blob, tree, commit, tag) by the **hash of its content**.
> 

Hash:

- SHA-1 produces a **160-bit hash**, giving ~1.46×10⁴⁸ possible values.
- SHA-256 (used in newer Git versions) produces **256-bit hashes**, giving ~1.16×10⁷⁷ possible values.
- This makes collisions **extremely unlikely** in practice.

### How does git cherry-pick work?

> How does Git compute the resulting tree during a cherry-pick, given the `commit’s parent tree`, the `commit tree`, and the current `HEAD tree`?
> 

> Let’s say we have a branch with three commits: `a → b → c` (with `c` at the tip), and I want to cherry-pick commit `b` onto another branch. Will the new branch also get the changes introduced by commit `a`, or not? How is this handled?
> 

> Note: All snapshot history operations (merge, apply, cherry-pick, rebase, etc.) work directly on tree objects, manipulating repository state at the commit-snapshot level.
> 

> Note: In the process there can be `conflicts`. See more here [What do conflicts mean in snapshot-based history manipulation?](note.html?n=technica/computation/system/operation/operation-conceptual-model/git-global-information-tracker.md).
> 

Procedure:

1. [**Commit’s changes**]  Git first identifies the modifications introduced by the commit being cherry-picked (`b`): new files, edited files, or deletions. These changes are determined relative to the commit’s parent (`a`), ignoring earlier commits. This produces a tree representing only the new or modified content.
2. Compare the tree-a with the target tree, to generate a new commit pointing to the merge tree.

**Commit’s Changes Formalism:**

Let:

- $F_a$ = set of file states in the **parent commit** $a$
- $F_b$ = set of file states in the **commit being cherry-picked** $b$
- $F_\Delta$ = set of **changes introduced by $b$ relative to $a$**

Then the cherry-pick diff at the tree level is:

> $F_\Delta = \{ f \in F_b \mid f \notin F_a \text{ or } \text{content}(f_b) \neq \text{content}(f_a) \}$
> 

> The resulting tree representing the cherry-picked changes is:  $T_\Delta = \text{Tree}(F_\Delta)$ where `Tree()` constructs a Git tree object from the set of file states.
> 

This includes:

- **New files**: $f \in F_b \setminus F_a$
- **Modified files**: $f \in F_b \cap F_a$ but $\text{content}(f_b) \neq \text{content}(f_a)$
- **Deleted files**: $f \in F_a \setminus F_b$

### How merge works?

> See `git log --graph` to see the commit history.
> 

> How to find $T_0$?
> 

> Given two commits $a, b$ with trees $T_a, T_b$ and merge base $T_0$, the merge tree is $T_c(p) = m\!\big(T_0(p), T_a(p), T_b(p)\big) \quad \forall p \in \mathcal{P}$,  where $m$ is the **per-path 3-way merge operator** (agree $\to$ keep, one-sided change $\to$ take, two-sided change $\to$ conflict).
> 

> **What happens with the merge $T_b$ history path?** The commit $c$ does not erase or override the path from the root to $b$. Instead, the path through $b$ is now part of the **ancestry of** $c$.
> 

### How to generate a beautiful Git commit history graph?

See

- https://www.nicoespeon.com/gitgraph.js/#0,
- `git log --oneline --graph --decorate --all`,
- `git log --graph`
- …

### What do conflicts mean in snapshot-based history manipulation?

> In **snapshot-based history manipulation**—like Git’s model, where each commit represents a full snapshot of the repository—**conflicts occur when two changes cannot be automatically merged because they affect the same part of the snapshot in incompatible ways**.
> 

> A conflict in snapshot-based history means **two snapshots made incompatible changes to overlapping parts of the repository**, preventing automatic merging.
> 

Let $T_a$ and $T_b$ be snapshots (trees) based on a common ancestor $T_0$. Define the **modification set** of each snapshot relative to the ancestor:  $M_a = T_a \setminus T_0, \quad M_b = T_b \setminus T_0$

A **conflict exists** if: $M_a \cap M_b \neq \emptyset \quad \text{and the changes in }$ $M_a$$\text{ and } M_b \text{ are incompatible.}$

**Resolution**:

- The developer must manually reconcile the conflicting modifications.
- Once resolved, a new snapshot (commit) is created representing the merged state.

### How to create a remote git repo with Docker - SSH?

> 

### How does git parse "git push -u origin HEAD”?

> Pushes the currently checked-out local branch to the remote named `origin` and sets the corresponding remote branch as the upstream tracking branch for future push/pull operations.
> 
- git:  The Git command-line client.
- push:  The Git subcommand that **transfers local commits to a remote repository**.
- -u:  Short for `--set-upstream`. After a successful push, Git records the pushed remote branch as the **upstream (tracking) branch** of the current local branch, updating `.git/config` accordingly.
- origin:   The name of the remote repository. Git resolves it via the local configuration and uses its associated URLs and refspec rules to determine where objects and references are sent.
- HEAD:   A symbolic reference to the currently checked-out local branch (e.g., `refs/heads/feature-x`). When used as a push refspec, Git expands it to mean *“push the current branch to a branch of the same name on the remote.”*

Changes in .gitconfig:

```bash
branch.proto.remote = origin
branch.proto.merge  = refs/heads/proto
```

This configuration enables:

- `git pull` → pulls from `origin/proto`
- `git push` → pushes to `origin/proto`
- `git status` → reports ahead/behind relative to `origin/proto`

### How configure  git to enable the presentation of the signatures?

`git config --global gpg.ssh.allowedSignersFile /home/dvictoriano/configs/local/allowed_signers`

Format:

user <public key>

Verify:

git log —show-signature

### **How to make sure that unwanted files are not committed?**

> See [How to make sure that unwanted files are not committed?](note.html?n=technica/computation/system/operation/operation-conceptual-model/how-to-make-sure-that-unwanted-files-are-not-committed.md).
> 

### How to check if a file is ignore?

```html
git check-ignore -v path/to/nvim/lazy-lock.json -- check ignore's file status
```

### Where is our code annotation model?

> In [Source Code](note.html?n=technica/computation/system/operation/operation-conceptual-model/source-code.md).
> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- 
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- https://github.com/git/git
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Git from the inside out. (n.d.). Retrieved July 21, 2022, from [https://codewords.recurse.com/issues/two/git-from-the-inside-out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
- Chacon, S. (2009). Pro Git (1st ed.). APress.
- How to explain git in simple words? (n.d.). Retrieved July 21, 2022, from [https://xosh.org/explain-git-in-simple-words/](https://xosh.org/explain-git-in-simple-words/)
- Git from the Bottom Up. (n.d.). Retrieved July 21, 2022, from [https://jwiegley.github.io/git-from-the-bottom-up/](https://jwiegley.github.io/git-from-the-bottom-up/)
- Git for Computer Scientists. (n.d.). Retrieved July 21, 2022, from [https://eagain.net/articles/git-for-computer-scientists/](https://eagain.net/articles/git-for-computer-scientists/)
- Oh Shit, Git!?! (n.d.). Retrieved July 21, 2022, from [https://ohshitgit.com/](https://ohshitgit.com/)
- Alibaba Cloud Community. (n.d.). A Detailed Explanation of the Underlying Data Structures and Principles of Git. Retrieved July 21, 2022, from [https://www.alibabacloud.com/blog/a-detailed-explanation-of-the-underlying-data-structures-and-principles-of-git_597391](https://www.alibabacloud.com/blog/a-detailed-explanation-of-the-underlying-data-structures-and-principles-of-git_597391)
- The missing semester of your cs education. (n.d.). Version Control (Git). Retrieved July 21, 2022, from [https://missing.csail.mit.edu/2020/version-control/](https://missing.csail.mit.edu/2020/version-control/)
- Ell Docu, W., Perez, S., Rosso, D., Jackson, D. (n.d.). Purposes, Concepts, Misfits, and a Redesign of Git. [https://doi.org/10.1145/2983990.2984018](https://doi.org/10.1145/2983990.2984018)
- [‣](https://app.notion.com/p/178598edb79080668cf3d129fa8a0792?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081f8951bd4feaac03d57?pvs=21)
- [‣](https://app.notion.com/p/178598edb79080259268ffbb29086951?pvs=21)
- [Git’s database internals I: packed object store](https://github.blog/2022-08-29-gits-database-internals-i-packed-object-store/)
- [Git’s database internals II: commit history queries](https://github.blog/2022-08-30-gits-database-internals-ii-commit-history-queries/)
- [Git’s Database Internals III: File History Queries](https://github.blog/2022-08-31-gits-database-internals-iii-file-history-queries/)
- Osullivan, B. (2009). Making Sense of Revision-control Systems. Queue, 7(7), 30–40. [https://doi.org/10.1145/1594204.1595636](https://doi.org/10.1145/1594204.1595636)
- [‣](https://app.notion.com/p/10e598edb790813fa0b8e05089d42ba9?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081299878c44c6c46e477?pvs=21)
- [‣](https://app.notion.com/p/178598edb79080618f4fc6c6c246396e?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790819dabcbd8d93471d2f6?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081cebb79d6b4525231a8?pvs=21)
- Top Answers to Git Interview Questions [https://intellipaat.com/blog/interview-question/git-interview-questions-answers/](https://intellipaat.com/blog/interview-question/git-interview-questions-answers/)
- https://learngitbranching.js.org/
- https://initialcommit.com/blog/git-sim
- https://think-like-a-git.net/
- [Better Git configuration](https://news.ycombinator.com/item?id=14045787)
- [How to undo almost anything with Git (2015)](https://news.ycombinator.com/item?id=21867133)
- [The Architecture of Git](https://news.ycombinator.com/item?id=18309596)
- [Git Query Language](https://github.com/filhodanuvem/gitql/tree/v2.3.1)
- [Git’s list of banned C functions (github.com/git)](https://news.ycombinator.com/item?id=26347867)
- [Git Tips (alexkras.com)](https://news.ycombinator.com/item?id=11532281)
- Git History / [https://githistory.xyz/](https://githistory.xyz/)
- https://tom.preston-werner.com/2009/05/19/the-git-parable.html
- https://downgit.github.io/#/home
- https://github.com/anuraghazra/github-readme-stats
- https://www.youtube.com/watch?v=MYP56QJpDr4
- https://www.youtube.com/watch?v=pfOAxFWNUkQ
- Driessen, V. (n.d.). A successful Git branching model. Retrieved July 21, 2022, from
- https://alchemists.io/articles/git_trailers
- https://en.wikipedia.org/wiki/Merkle_tree
- [Set](https://app.notion.com/p/Set-176c0f5171ec800f8b41f66b6d8cc5b3?pvs=21)
- https://mattrickard.com/git-merge-strategies-and-algorithms
- `watch .`
- https://piechowski.io/post/git-commands-before-reading-code/