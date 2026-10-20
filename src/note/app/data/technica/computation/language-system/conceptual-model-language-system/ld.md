---
tags: [linker, tool]
---

# ld

- [Linker](note.html?n=technica/computation/language-system/conceptual-model-language-system/linker.md)

> The **GNU Linker**.
> 

> **ldconfig** - configure dynamic linker run-time bindings.
> 

QA:

- …

## Linker Model

| Linker Model | Description | Example |
| --- | --- | --- |
| Static Linking | Links the object code of libraries and dependencies into the final executable during compile time, resulting in a standalone executable with all required code included. | Linking C libraries using `gcc -static` |
| Dynamic Linking (Load Time) | The final executable is linked to shared libraries (.dll, .so) during runtime, allowing multiple programs to share the same library code and reducing overall memory usage. | Using shared libraries in Linux (`libc.so`) or Windows (`kernel32.dll`) |
| Incremental Linking | Only re-links the parts of a program that have changed since the last compilation, speeding up the build process by avoiding unnecessary re-linking of unchanged code. | Microsoft Visual C++'s incremental linker (`/INCREMENTAL`) |
| Lazy Binding | Delays the resolution of symbols until they are first referenced during program execution, reducing startup time and memory usage by loading libraries on demand. | Lazy loading of shared libraries in Linux (`LD_BIND_NOW`) |
| Dynamic Linking (dlopen) |  |  |

## References

- http://wiki.osdev.org/LD
- https://man7.org/linux/man-pages/man8/ldconfig.8.html
- https://linux.die.net/man/1/ld
- https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_node/ld_toc.html
- https://jsandler18.github.io/explanations/linker_ld.html
- [https://www.eecs.umich.edu/courses/eecs373/readings/Linker.pdf](https://www.eecs.umich.edu/courses/eecs373/readings/Linker.pdf)
- https://ostechnix.com/introduction-to-gnu-binutils/
- https://github.com/alisw/gcc-toolchain/tree/master/binutils-2.25.1/ld