# Linux Documentation


Here's a table summarizing various types of Linux documentation available, including `man` pages, `info` pages, and others:

| **Documentation Type** | **Description** | **Command** |
| --- | --- | --- |
| **Man Pages** | Manual pages that provide documentation on commands, system calls, libraries, file formats, and more. | `man <command>` |
| **Info Pages** | Hypertextual, often more detailed, documentation. Allows for navigation between sections. | `info <command>` |
| **Help Command** | Quick reference for basic usage of commands. | `<command> --help` or `<command> -h` |
| **README Files** | Plain text files typically found in source code directories or `/usr/share/doc/`, providing setup or usage. | `cat README` or `less README` |
| **HOWTOs** | Detailed guides and tutorials on various topics, often found in `/usr/share/doc/` or `/usr/doc/`. | `cat /usr/share/doc/HOWTO` |
| **/usr/share/doc/** | Directory containing documentation, including README files, changelogs, and other guides. | `ls /usr/share/doc/` |
| **apropos** | Search the man page descriptions for keywords. | `apropos <keyword>` |
| **whatis** | Display one-line descriptions of commands. | `whatis <command>` |
| **/usr/share/man/** | Directory where man pages are stored, categorized by section. | `ls /usr/share/man/man[section]` |
| **GNU Texinfo** | GNU's documentation system, using info files. | `info <topic>` |
| **/proc/** | Virtual filesystem providing real-time system information, often considered self-documenting. | `cat /proc/<file>` |
| **dmesg** | Kernel ring buffer messages, useful for troubleshooting. | `dmesg |
| **/usr/src/linux/Documentation/** | Kernel documentation directory containing a wealth of information about kernel features and APIs. | `ls /usr/src/linux/Documentation/` |
| **man -k** | Search for a string in the man pages database. | `man -k <keyword>` |
| **bash help** | Built-in help for bash built-in commands and syntax. | `help <bash-command>` |