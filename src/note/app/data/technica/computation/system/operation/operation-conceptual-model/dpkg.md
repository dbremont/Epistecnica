---
tags: [package-manager]
---

# dpkg


> `dpkg` stands for **Debian Package Manager**. It is the **low-level package management tool** for Debian-based systems (such as Ubuntu) and is responsible for installing, removing, and managing `.deb` packages. It works directly with package files but does not handle dependencies automatically—that's the job of higher-level tools like `apt` or `aptitude`.
> 

QA:

- How dpkg keep  tracks of install software?
- What is `dpkg-divert`, and when would you use it?
- How can you manually recover a broken `dpkg` database?
- How do you extract control information from a `.deb` package without installing it?

## List of Flags

> 

| Flag | Description |
| --- | --- |
| `-i, --install` | Installs a `.deb` package. |
| `-r, --remove` | Removes a package but keeps configuration files. |
| `-P, --purge` | Completely removes a package, including configuration files. |
| `-l, --list` | Lists installed packages matching a pattern. |
| `-s, --status` | Displays the status of an installed package. |
| `-L, --listfiles` | Lists all files installed by a package. |
| `-S, --search` | Finds which installed package a file belongs to. |
| `-c, --control` | Extracts and displays the control file from a `.deb` package. |
| `--configure` | Reconfigures an unpacked package. |
| `-V, --verify` | Verifies installed package integrity. |
| `--force-<option>` | Forces a specific action, even if it might cause issues. |
| `-R, --recursive` | Installs packages recursively from a directory. |
| `--get-selections` | Shows a list of installed and available packages. |
| `--set-selections` | Marks packages for installation or removal. |

## How `dpkg` keep  tracks of install software?

> `dpkg` keeps track of installed software using the **dpkg database**, which is located in `/var/lib/dpkg/`.
> 

This database contains several important files:

1. **`/var/lib/dpkg/status`** – Stores information about all installed packages, including their version, dependencies, and state.
2. **`/var/lib/dpkg/available`** – Lists all available packages that can be installed.
3. **`/var/lib/dpkg/info/`** – A directory containing:
    - **`<package>.list`** – Lists files installed by a package.
    - **`<package>.md5sums`** – Stores checksums for verifying file integrity.
    - **`<package>.postinst`, `<package>.prerm`, etc.** – Scripts executed during installation or removal.

## References

- https://www.digitalocean.com/community/tutorials/dpkg-command-in-linux
- https://en.wikipedia.org/wiki/Dpkg
- https://man7.org/linux/man-pages/man1/dpkg.1.html