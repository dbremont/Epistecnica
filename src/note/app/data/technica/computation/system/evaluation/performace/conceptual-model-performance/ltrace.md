---
tags: [data-collection, tool]
---

# ltrace


**`ltrace`** is a Linux command-line tool that **traces the library calls made by a running program**.

- It intercepts and logs calls to **shared library functions** such as `printf()`, `malloc()`, `open()`, etc.
- Useful for debugging and analyzing how a program interacts with libraries.
- Shows the arguments passed to library functions and their return values.
- Complements `strace` (which traces system calls) by focusing on **user-level library calls**.

## References

- https://en.wikipedia.org/wiki/Ltrace