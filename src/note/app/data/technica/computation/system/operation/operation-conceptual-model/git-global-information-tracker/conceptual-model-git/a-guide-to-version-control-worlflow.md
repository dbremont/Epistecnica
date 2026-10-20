# A Guide to Version Control Worlflow


- is two people working on the same branch a good model?
- git stashe → git stashe pop

## SMM - Branching Model

There are several popular Git branching models, each designed to suit different workflows and development practices. Here are some of the most well-known ones:

- [Gitflow](https://nvie.com/posts/a-successful-git-branching-model/): This model defines a strict branching structure with long-lived branches for features, releases, and hotfixes, promoting a more formalized and organized workflow.
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow): A simpler branching model emphasizing short-lived branches, where all development occurs on feature branches, and changes are merged directly into the main branch (usually “master” or “main”).
- [GitLab Flow](https://about.gitlab.com/topics/version-control/what-is-gitlab-flow/): Similar to GitHub Flow but introduces a step of creating a merge request (pull request) before merging changes into the main branch, allowing for code reviews and feedback.
- [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow): In this model, each new feature or bug fix gets its own branch, and developers merge their changes back into the main branch when the work is completed.
- [Centralized Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows): Suitable for small teams or single developers, this model uses a single main branch (e.g., “master” or “main”) and developers commit directly to it.
- [Forking Workflow](https://gitprotect.io/blog/git-forking-workflow/): Commonly used in open-source projects, contributors create forks of the main repository, make changes in their forks, and propose changes through pull requests.

## Git Commit Messages

> Proposed format of the commit message
> 

```bash
<type>(<optional scope>): <description><optional body><optional footer><fix>: jira-46564
```

Allowed `<type>`

- feat (feature)
- fix (bug fix)
- docs (documentation)
- style (formatting, missing semi colons, …)
- refactor
- test (when adding missing tests)
- chore (maintain)