# GIT: Data Model


> The **Git storage model** is structured to efficiently manage and retrieve data. It consists of several core objects and concepts stored in a content-addressable way.
> 

| **Component** | **Description** | **Details** |
| --- | --- | --- |
| **Blob** | Stores the contents of a file. | - Represents raw file data.  - Identified by a SHA-1 hash.  - Does not store filenames. |
| **Tree** | Represents a directory and its contents. | - Points to blobs (files) and other trees (subdirectories).  - Contains metadata like filenames. |
| **Commit** | Represents a snapshot of the repository at a specific point in time. | - Points to a tree object (root of the directory structure).  - Contains metadata (author, message). |
| **Tag** | Points to a specific commit and adds metadata like names or descriptions. | - Lightweight: just a reference.  - Annotated: includes additional metadata (author, message). |
| **Branch** | A movable pointer to the tip of a commit chain. | - Stored in the `refs/heads/` directory.  - Moves forward with each commit. |
| **HEAD** | A special pointer indicating the current branch or commit in use. | - Often points to the tip of the current branch. |
| **Index (Staging Area)** | Temporarily stores changes before committing them to the repository. | - Lives in `.git/index`.  - Prepares changes for the next commit. |
| **Objects Database** | Stores all objects (blobs, trees, commits, tags). | - Located in `.git/objects`.  - Uses content-addressable storage. |
| **References** | Pointers to commits, including branches, tags, and remotes. | - Stored in `.git/refs/`.  - Example: `refs/heads/main`. |
| **Pack Files** | Efficiently stores objects by compressing and packing them together. | - Located in `.git/objects/pack`.  - Optimizes storage for large repositories. |
| **Delta Compression** | Technique to store changes efficiently between similar objects. | - Used in pack files.  - Saves only differences between similar objects. |

## Data Model

**Git Layers**: - Object Layer: Stores objects in a content-addressable store - Tree Layer: Organizes “blobs” into a directory-like hierarchy - Commit Layer: Versions the tree layer - Reference Layer: Provides human-readable names for trees, blobs, commits

**Git index**: The Git index, also known as the staging area, tracks changes to files before they are committed. It provides a way to review and selectively include changes in a commit.

**Git repository**: The Git repository is the core component of Git and contains all of the objects, references, and other data that make up a Git project.

Git has a simple and elegant **data model** that efficiently manages and stores the history of changes in a repository. The model consists of four main objects: blobs, trees, commits, and tags.

- **Blobs**: A blob (binary large object) is a data unit in Git. It represents the contents of a file and is identified by a unique SHA-1 hash. Blobs are immutable and cannot be changed once they are created.
- **Trees**: A tree is a directory listing in Git. It represents a snapshot of a directory and contains references to blobs and other trees. Like blobs, trees are identified by a unique SHA-1 hash.
- **Commits**: A commit is a snapshot of the entire repository at a given time. It contains a reference to a tree object that represents the top-level directory of the repository at the time of the commit. It also contains metadata such as the author, commit message, and a pointer to the parent commit (or commits) that came before it.
- **Tags**: A tag is a reference to a specific commit. It is commonly used to mark a particular point in the repository’s history, such as a release.

Together, these objects form a directed acyclic graph (DAG) of the repository’s history. Each commit points to one or more parent commits, forming a chain of commits representing the history of repository changes over time. The objects are stored in a compressed format, allowing Git to manage large repositories with many changes over time efficiently.

**Git data structures** are the building blocks of the Git data model. These structures represent and manage the various objects of a Git repository.

- **SHA-1 Hash**: Git uses a 40-character SHA-1 hash to identify each object in the repository. This hash is calculated based on the object's contents and is unique for each object.
- **Commit Object**: A commit object contains metadata such as the author, commit message, and a pointer to the tree object that represents the state of the repository at the time of the commit.
- **Tree Object**: A tree object represents a directory in the repository and contains references to the blobs and other trees that comprise the contents.
- **Blob Object**: A blob object represents the contents of a file in the repository. It is identified by its SHA-1 hash and is stored as a binary file.
- **Tag Object**: A tag object marks a specific commit in the repository’s history. It contains metadata such as the tagger, tag message, and a pointer to the commit object it is tagging.
- **Index File**: The index file, also known as the staging area, tracks changes made to the working directory but not yet committed to the repository. It contains references to the blobs and trees that make up the repository's current state.
- **Packfile**: A packfile is a compressed archive of Git objects used to efficiently store and transfer objects between repositories. Git creates packfiles when the repository becomes too large to efficiently store individual objects.

Together, these data structures allow Git to efficiently manage the history and contents of a repository, while also providing mechanisms for tracking changes and collaborating with others.