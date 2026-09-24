---
tags: [git, branching, merging]
---

# Lecture 2 — Commit, Branch, Merge

> The core loop: record a snapshot, diverge safely, recombine deliberately.

## Formulation

### What is a commit?

> An immutable snapshot with identity, parent pointer, author, and message. History is a linked list (usually a DAG) of commits — the "why" lives in the message.

### What are branches and merges?

> A branch is a movable pointer to a commit: cheap divergence. A merge reconciles two lines of history into one, pausing for human judgment on conflicts. The loop — commit, branch, merge — is the same in every tool; only the storage model differs.

## Takeaway

> Branch to explore, commit to record, merge to agree. Everything else is interface.
