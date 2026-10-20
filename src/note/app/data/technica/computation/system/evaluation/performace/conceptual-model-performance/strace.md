---
tags: [data-collection]
---

# strace


**`strace`** is a powerful Linux command-line tool used to **trace system calls and signals** made by a running process.

- It intercepts and records all system calls a program makes (like `open()`, `read()`, `write()`, `mmap()`, `execve()`, etc.).
- It helps developers and system administrators **debug and diagnose** issues by showing how a program interacts with the kernel.
- Common uses:
    - Debugging failed file accesses or permission errors.
    - Tracking down crashes or unexpected behavior.
    - Understanding program behavior at the system call level.
    - Monitoring interactions with files, network, and processes.

## References

- https://en.wikipedia.org/wiki/Strace