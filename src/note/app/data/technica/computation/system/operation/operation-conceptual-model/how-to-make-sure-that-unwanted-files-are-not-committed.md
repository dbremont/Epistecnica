---
tags: [how-s-to]
---

# How to make sure that unwanted files are not committed?


> 

How to make sure that unwanted files are not committed?

- **Goal**:  Push only wanted files.
- **Evaluation**:
    - Given a human review of the committed file set, every file included must be explicitly intended for commit.
- **Strategies**:
    - **Explicit Staging Discipline:** Stage files individually to ensure only explicitly selected files enter the commit.
    - **Pre-Commit Inspection:** Always review the staged set using status and diff before committing.
    - **Negative Marking:** Attach to the files content a (mark) - nocheckin, … - and create a hook that rejects those files.
    - **Positive Marking:**  Attach to the files a mark (checkin) - and create a hook that only allows the addition of files with the mark.
    - **Commit Scope Isolation:** Restrict each commit to a single logical concern to avoid accidental inclusion.
    - **Index Reset Strategy:** Clear the staging area and rebuild it explicitly when it becomes polluted.
    - **Pathspec Constraints:** Limit staging operations to specific directories or file sets to reduce scope.
    - **Dry-Run Simulation:** Preview staging operations before execution to detect unintended inclusions.
    - **File-Level Ownership Heuristic:** Only commit files that you have directly modified or explicitly verified.
    - **Metadata - Attribute Controls:** Use file attributes combined with tooling to enforce handling constraints.
    - **Continuous Review Mindset:** Treat every commit as a production-ready artifact requiring strict intentionality.
- Comparison:
    - Do we need to edit the final file - to remove some marks?
    - …
- **Implementation  Mechanism(s)**:
    - **Pre-Commit Hooks:** Enforce automated rules that block commits containing disallowed files or patterns.
    - Meta data annotations.
    - In File Annotations.   (We should used the metadata approach - and to some kind of reporting) - some modified ls.
- Implementation:
    - [https://github.com/dbremont/configs/tree/main/global/git](https://github.com/dbremont/configs/tree/main/global/git)
    - **TODO:  Called mark from commit - the files that have `@checkin` on them.**
    - This pre-commit hook implements a **positive file authorization** mechanism for Git commits. Rather than attempting to detect unwanted files, it only permits files that have been explicitly approved for inclusion in the commit. Every staged file with an **Added**, **Copied**, or **Modified** status is checked for the extended file attribute `user.checkin`, which must have the value `1`. Files that lack this attribute (or have an incorrect value) cause the commit to be rejected, ensuring that every committed file has been intentionally authorized.
    - When the hook detects unauthorized files, it aborts the commit and presents a concise error message listing the affected files along with a ready-to-run command (`./mark-for-commit.sh ...`) to apply the required authorization marks. If all staged files are correctly marked, the hook prints a success message and allows the commit to proceed. This positive authorization model helps reduce accidental commits, reinforces deliberate staging practices, and can serve as part of a broader commit authorization or workflow enforcement system.
    - setfattr -n user.checkin  -v "1" `paths …`
    - getfattr -n user.checkin  --only-values `paths ….`

```jsx
                edit file
                     │
                     ▼
              Modified (Unauthorized)
                     │
                     │
          mark file with @checkin
                     │
                     ▼
      Authorization Script (one-shot)
                     │
                     ├── reads @checkin
                     ├── sets filesystem metadata
                     └── optionally removes @checkin
                     │
                     ▼
          Modified (Authorized)
                     │
                     ▼
               git add
                     │
                     ▼
             pre-commit hook
                     │
         verifies metadata only
                     │
                     ▼
                 commit
                     │
                     ▼
            post-commit hook
                     │
             clears metadata
                     ▼
                 Clean State
```

## References

- [https://www.reddit.com/r/Jai/comments/jp0vjy/comment/gbfhzd1/](https://www.reddit.com/r/Jai/comments/jp0vjy/comment/gbfhzd1/)
- https://pre-commit.com/
- https://exiftool.org/