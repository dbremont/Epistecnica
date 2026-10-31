---
tags: [toolbox]
---

# Linux Toolbox


> 

| **Category** | **Utilities** |
| --- | --- |
| **File and Directory Management** | `cp`, `mv`, `rm`, `touch`, `ln`, `mkdir`, `rmdir`, `cd`, `pwd`, `ls`, `file`, `stat`, `du`, `df` |
| **Text Processing** | `cat`, `more`, `less`, `head`, `tail`, `nano`, `vim`, `emacs`, `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `tr`, `wc`, `paste`, `comm`, `split`, `join` |
| **System Monitoring and Management** | `ps`, `top`, `htop`, `kill`, `pkill`, `nice`, `renice`, `uname`, `uptime`, `dmesg`, `vmstat`, `iostat`, `free`, `netstat`, `ss`, `ifconfig`, `ip`, `ping`, `traceroute`, `nslookup` |
| **File Compression and Archiving** | `gzip`, `bzip2`, `xz`, `zip`, `unzip`, `tar`, `ar`, `cpio` |
| **User and Permissions Management** | `useradd`, `usermod`, `userdel`, `passwd`, `id`, `groups`, `chmod`, `chown`, `chgrp`, `umask` |
| **Networking** | `scp`, `rsync`, `wget`, `curl`, `ifconfig`, `ip`, `route`, `netstat`, `ping`, `ssh`, `telnet`, `ftp` |
| **System Configuration and Startup** | `systemctl`, `service`, `chkconfig`, `vi`, `nano`, `emacs`, `shutdown`, `reboot`, `halt`, `init`, `systemctl` |
| **Package Management** | `apt`, `dpkg`, `yum`, `dnf`, `rpm` |
| **Development and Compilation** | `gcc`, `g++`, `clang`, `make`, `cmake`, `git`, `svn` |
| **System Backup and Restore** | `tar`, `rsync`, `dd` |
| **Miscellaneous Utilities** | `du`, `df`, `env`, `export`, `set`, `date`, `cal`, `timedatectl` |

> Search
> 

| **Tool** | **Description** |
| --- | --- |
| **find** | Searches for files and directories in a directory hierarchy based on various criteria such as name, type, size, modification time, and more. |
| **locate** | Quickly finds files by searching a pre-built database of filenames. It is faster than `find` but may not reflect recent changes unless the database is updated. |
| **grep** | Searches for patterns within files. It can search through plain text files and outputs lines that match the specified pattern. |
| **which** | Finds and shows the path of a command or executable in the directories listed in the `PATH` environment variable. |
| **whereis** | Locates the binary, source, and manual page files for a command. Useful for finding where a command is installed and its associated files. |
| **locate** | Similar to `find`, but it uses a database to perform searches faster. The database is updated periodically using the `updatedb` command. |
| **fgrep** | A variant of `grep` that searches for fixed strings (literal text) rather than regular expressions, making it faster for simple searches. |
| **ack** | A text search tool designed for developers, `ack` is faster than `grep` for searching through source code because it automatically skips non-text and binary files. |
| **ag (The Silver Searcher)** | A code searching tool similar to `ack` but faster, optimized for searching large codebases. Supports regex and ignores file patterns specified in `.gitignore`. |
| **findmnt** | Finds and displays information about mounted filesystems. Useful for determining the mount point of a particular device or file. |
| **fd** | A simple, fast, and user-friendly alternative to `find`. It offers intuitive syntax and sensible defaults, making it easier to use for common file search operations. |
| **rgrep** | Recursive `grep` that searches through directories and subdirectories, combining the functionality of `grep` with the recursive search of `find`. |
| **xargs** | Combines with `find` or other commands to execute a command on each file found. Useful for performing batch operations on search results. |