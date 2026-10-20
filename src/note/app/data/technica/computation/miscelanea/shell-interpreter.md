---
tags: [shell-interpreter]
---

# Shell Interpreter

- [Terminal Emulator](note.html?n=technica/computation/miscelanea/terminal-emulator.md)

> **Shell Interpreter:** A program that interprets shell commands, expands them, executes programs, manages processes, and provides an interactive command-line environment.
> 

> **Terminal Emulator:** A program that provides a graphical interface to a terminal session by emulating a hardware terminal and providing input/output to a shell or other terminal application.
> 

> Shell Interpreter (Zsh) vs Terminal Emulator (Kitty):
> 

## Shell System Space

| **Shell Interpreter** | **Description** | **Default on** |
| --- | --- | --- |
| **Bash (Bourne Again Shell)** | The most widely used shell interpreter on Linux systems, known for its scripting capabilities, command-line editing, and job control. It is an enhanced version of the Bourne Shell (sh). | Most Linux distributions |
| **sh (Bourne Shell)** | The original Unix shell, designed for simple command execution and scripting. It is the predecessor to many modern shells, including Bash. It is lightweight and commonly used for scripting. | Legacy systems, POSIX systems |
| **Zsh (Z Shell)** | An advanced shell with many features from other shells, including Bash, ksh, and tcsh. It is known for its powerful scripting, customization options, and interactive use. | macOS (starting from Catalina), customizable on Linux |
| **csh (C Shell)** | A shell with a C-like syntax, primarily used for scripting and job control. It was popular in early Unix systems but has largely been replaced by more modern shells like Bash and Zsh. | Legacy Unix systems |
| **tcsh (TENEX C Shell)** | An enhanced version of csh, providing additional features like command-line editing and improved scripting capabilities. It is often used as an interactive shell. | Some Unix systems |
| **ksh (Korn Shell)** | A powerful shell that combines features of the Bourne Shell with enhancements like command history, job control, and built-in arithmetic. It is often used in enterprise environments. | AIX, Solaris |
| **dash (Debian Almquist Shell)** | A lightweight POSIX-compliant shell that is faster than Bash, often used as the default `/bin/sh` in Debian-based systems for script execution. | Debian, Ubuntu |
| **fish (Friendly Interactive Shell)** | A user-friendly shell focused on interactive use. It offers features like syntax highlighting, autosuggestions, and an easy-to-use scripting language. | Customizable on Linux |
| **ash (Almquist Shell)** | A lightweight and fast shell derived from the Bourne Shell, designed for small systems and embedded environments. It is often used in busybox environments. | Embedded systems |
| **mksh (MirBSD Korn Shell)** | A successor to the original Korn Shell (ksh), designed to be portable and lightweight. It includes many enhancements while maintaining compatibility with POSIX standards. | Android, OpenBSD, MirBSD |
| **es (Extensible Shell)** | A shell inspired by the Plan 9 shell `rc`, offering advanced functional programming features and extensibility. It is more of a niche shell used by advanced users. | Niche systems |

## References

- https://en.wikipedia.org/wiki/Command-line_interface
- https://en.wikipedia.org/wiki/List_of_command-line_interpreters