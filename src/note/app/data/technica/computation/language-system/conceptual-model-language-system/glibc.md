---
tags: [c, language-system]
---

# glibc

- [GCC : GNU Compiler Collection](note.html?n=technica/computation/language-system/conceptual-model-language-system/gcc-gnu-compiler-collection.md)

> 

QA:

- How `gmon` stores profile data?
- What is the spec of the `gmon.out` file? The  gmon.out format is defined in  `/usr/include/sys/gmon_out.h`

## gmon

> In the GNU C Library (glibc), the profiling mechanism is based on the `gmon` system, which is designed to collect performance data for analysis using tools like `gprof`.
> 

> Note: Tools like gprof can be used to read the gmon.out file.
> 

> `/usr/include/sys/gmon.h` .
> 

**Compiling with Profiling**:

To enable profiling, you need to compile your program with the `-pg` flag. This tells the compiler (such as `gcc`) to insert special code to collect profiling data during execution. Specifically, it adds function call instrumentation into the compiled binary, allowing the program to track how often each function is called and how much time is spent in each function.

```bash
gcc -pg -o my_program my_program.c
```

**The `mcount` Function**:

The key part of this profiling process is the `mcount()` function, which is inserted into the program wherever function calls occur. When the program runs, `mcount()` is called at the entry and exit points of functions, recording statistics about function calls, such as:

- How many times a function is called
- The time spent in each function (if profiling for time is enabled)

`mcount()` is provided by the glibc, and its primary job is to update counters and collect statistics into a special data structure.

**Generating the `gmon.out` File**:

At runtime, when the program executes, the profiling data is accumulated. Once the program finishes executing, the profiling data is written to a file called `gmon.out`. This file contains a summary of function calls, the time spent in them, and call graph information.

## References

- https://github.com/bminor/glibc
- https://github.com/lattera/glibc/blob/master/gmon/mcount.c
- https://www.gnu.org/software/libc/manual/html_node/index.html#SEC_Contents
- https://www.gnu.org/savannah-checkouts/gnu/libc/index.html