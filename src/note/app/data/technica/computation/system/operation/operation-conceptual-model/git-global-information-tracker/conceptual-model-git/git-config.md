# GIT: Config


> In Git, the configuration file (`.gitconfig`) stores settings and configuration options for a particular user or repository. The file can be global (user-specific) or local (repository-specific) and contains a set of key-value pairs that define various aspects of Git’s behavior.
> 

Use

- `git config --global --list`
- `git config --local --list`
- `git config --list`

## Grammar

> Which are the git configs parameters?
> 

| **Parameter** | **Description** | **Case(s)** |
| --- | --- | --- |
| `user.name` | Sets the name used in commits. | Personal or project identity for commits. Example: `git config --global user.name "Daniel Bremont"` |
| `user.email` | Sets the email used in commits. | Personal or project identity for commits. Example: `git config --global user.email "daniel@example.com"` |
| `core.editor` | Defines the text editor Git will use. | Editing commit messages. Example: `git config --global core.editor "vim"` |
| `core.autocrlf` | Controls line ending conversions between Windows and Unix systems. | Prevents line-ending issues in cross-platform projects. Example: `git config --global core.autocrlf true` |
| `core.fileMode` | Determines whether executable permissions are tracked. | Useful when working across file systems with different permission handling. |
| `core.ignoreCase` | Treats file names as case-insensitive on case-insensitive file systems. | Avoids file tracking issues on Windows/macOS. |
| `merge.tool` | Specifies the merge tool to use. | Resolving merge conflicts. Example: `git config --global merge.tool meld` |
| `diff.tool` | Specifies the diff tool to use. | Viewing differences between commits. Example: `git config --global diff.tool kdiff3` |
| `push.default` | Defines the default behavior for `git push`. | `simple`, `current`, `matching`. Example: `git config --global push.default simple` |
| `alias.<name>` | Creates shortcuts for Git commands. | Saves time on repetitive commands. Example: `git config --global alias.st status` |
| `color.ui` | Enables or disables colored output. | Improves readability of Git output. Example: `git config --global color.ui auto` |
| `credential.helper` | Manages storing credentials. | Caches passwords or integrates with system credential stores. Example: `git config --global credential.helper store` |
| `http.proxy` | Sets a proxy for Git HTTP operations. | Required when behind a corporate proxy. Example: `git config --global http.proxy http://proxy.example.com:8080` |
| `core.excludesfile` | Points to a global `.gitignore` file. | Centralizes ignored files across repositories. Example: `git config --global core.excludesfile ~/.gitignore_global` |
| gpg.ssh.program | Defines the GPG or SSH program Git will use for signing. | Useful when using an external GPG/SSH agent. Example: `git config --global gpg.ssh.program "gpg"` |
| gpg.format | Sets the signature format (`openpgp` or `ssh`). | Determines how Git creates signed commits or tags. Example: `git config --global gpg.format openpgp` |
| commit.gpgsign | Automatically signs commits using GPG. | Ensures all commits are signed for verification. Example: `git config --global commit.gpgsign true` |
| user.signingkey | Specifies the GPG key ID used to sign commits. | Selects which key to use for commit/tag signatures. Example: `git config --global user.signingkey ABCDEF1234567890` |

## References

- https://git-scm.com/docs/git-config