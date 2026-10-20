# GIT: Protocols


QA:

- How `git config --global http.postBuffer 1048576000` works?

## Protocols

Git supports several communication protocols for sharing repositories and collaborating with others:

- **Local Protocol**: The local protocol allows Git repositories to be accessed and shared on the same machine without a network connection. This is useful for development workflows where multiple developers are working on the same codebase on the same machine.
- **SSH Protocol**: The SSH protocol allows repositories to be accessed securely over a network connection. This is useful for remote collaboration workflows where developers work on different machines or the same machine but over a network connection.
- **HTTP(S) Protocol**: The HTTP(S) protocol allows repositories to be accessed over the internet using standard web protocols. This is useful for sharing repositories with collaborators who may not have SSH access.
- **Git Protocol**: The Git protocol is a lightweight protocol designed specifically for Git. It is faster and more efficient than the HTTP(S) protocol, and is typically used for large-scale public repositories.