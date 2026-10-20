# GIT: Snapshot History Operation


> 

## Git Merge Models

> Git provides two primary mechanisms for combining changes from one branch into another: `git merge` and `git rebase`.
> 

Each has its use cases and implications:

- **`git merge`**:   Merges the changes from one branch into another, creating a new merge commit to record the merge operation.
    - **Commit History**: Maintains a more structured and clear commit history, showing the branch’s divergence and merge points.
    - **Collaboration**: When collaborating with others, especially on shared branches like `main` or `develop`, `git merge` is typically preferred to preserve the history and avoid rebasing shared work.
    - **Feature Branches**: Useful for incorporating changes from feature branches into the main development branch.
- **`git rebase`**:   Moves or combines a sequence of commits from one branch to another, creating a new linear history without merging commits.
    - **Commit History**: Produces a linear and cleaner commit history, as if the changes on the rebased branch had been made directly on top of the target branch.
    - **Personal Branches**: Often used to keep a clean and linear history on personal branches or feature branches before merging into the main branch.
    - **Commits Cleanup**: For a more coherent history, you can squash, edit, or reorder commits during interactive rebases.
    - **Note**: Rebasing can be disruptive if used on shared branches or commits already pushed to a remote repository, as it rewrites commit history.
    - **`git pull`** (which includes merging or rebasing):  Combines changes from a remote repository into the current branch.
        - **Commit History**: Depends on the configuration and the state of the remote branch.
        - **Use Cases**:
            - Pulling remote changes into your local branch.
            - Synchronizing your local branch with the remote repository.
    
    ## Algorithms
    
    > **Merge Algorithms**: Git uses several merge algorithms to determine how to merge changes from different branches or repositories. These algorithms include recursive merging, which recursively merges changes until a final merge is produced, and octopus merging, which merges multiple branches simultaneously.
    >