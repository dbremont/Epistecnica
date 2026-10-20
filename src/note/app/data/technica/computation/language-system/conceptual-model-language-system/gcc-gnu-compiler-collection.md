---
tags: [c-c, language-system, tool]
---

# GCC : GNU Compiler Collection

- [glibc](note.html?n=technica/computation/language-system/conceptual-model-language-system/glibc.md)

> **GCC (GNU Compiler Collection)** is a modular, retargetable, and optimizing compiler system that translates high-level source code (C, C++, Fortran, Ada, and others) into machine code through a multi-stage pipeline involving lexical analysis, parsing, intermediate representation (GIMPLE, SSA), optimization (loop transformations, inlining, vectorization), and target-specific code generation using **RTL (Register Transfer Language)** before final assembly and linking, supporting multiple architectures and extensions via backend code generators.
> 

QA:

- Which are the limitations of gprof?  See more  [Profiling S**hortcomings**](https://app.notion.com/p/Profiling-Shortcomings-1c1c0f5171ec80c3adabc27e6393e65c?pvs=21).
- Does gprof log every function call during profiling, or does it sample a subset of calls? If it samples, how frequently does this occur, and what are the implications on accuracy? [Does `gcc -pg` log every function call during profiling, or does it sample a subset of calls? If it samples, how frequently does this occur, and what are the implications on accuracy?](note.html?n=technica/computation/language-system/conceptual-model-language-system/gcc-gnu-compiler-collection.md)

## List of Features

> The main idea of the GCC (GNU Compiler Collection) compiler is to provide a versatile and high-performance compiler suite for various programming languages, including C, C++, Objective-C, Fortran, Ada, and more.
> 

> It aims to produce efficient machine code while adhering to language standards and supporting multiple target architectures.
> 

> Key features and goals of GCC include:
> 

| **Features** | **Description** |
| --- | --- |
| **Portability** | Designed to be highly portable, GCC can run on various platforms, making it accessible to a wide range of developers and environments. |
| **Language Support** | Supports multiple programming languages and provides comprehensive language features while following specified language standards. |
| **Optimizations** | Offers a range of optimization levels to produce optimized machine code, enhancing program performance by analyzing and transforming source code. |
| **Extensibility** | Designed to be extensible, allowing developers to add their own language front-ends, optimizations, and target back-ends. |
| **Open Source** | Released under the GNU General Public License (GPL), allowing developers to study, modify, and distribute the compiler freely. |
| **Wide Target Architectures** | Capable of generating machine code for various target architectures, enabling cross-compilation and support for embedded systems and specialized hardware. |
| **Continuous Development** | Continuously developed and maintained by a large community of contributors, ensuring ongoing improvements and updates. |

## List of GCC Flags

> Here’s a table summarizing some commonly used GCC flags and their descriptions:
> 

| **Flag** | **Description** |
| --- | --- |
| `-o <output_file>` | Specifies the name of the output file. By default, GCC outputs an executable named `a.out`. |
| `-c` | Compiles the source files without linking, producing object files (`.o` files). |
| `-g` | Generates debugging information to be used by a debugger like GDB. |
| `-O0, -O1, -O2, -O3, -Os` | Sets the optimization level. `-O0` means no optimization, `-O3` provides the highest level of optimization, and `-Os` optimizes for size. |
| `-Wall` | Enables all commonly used warning messages, helping to identify potential issues in the code. |
| `-Werror` | Treats all warnings as errors, stopping the compilation if any warnings are generated. |
| `-I <directory>` | Adds the specified directory to the list of directories to be searched for header files. |
| `-L <directory>` | Adds the specified directory to the list of directories to be searched for libraries during linking. |
| `-l<library>` | Links with the specified library. For example, `-lm` links with the math library `libm`. |
| `-D<macro>[=<value>]` | Defines a macro to be used by the preprocessor, optionally assigning it a value. |
| `-std=<standard>` | Specifies the language standard to be used (e.g., `-std=c99` for C99, `-std=c++11` for C++11). |
| `-pedantic` | Enforces strict adherence to the language standard, generating warnings for any code that does not conform. |
| `-shared` | Generates a shared library instead of an executable. |
| `-static` | Links the executable statically, including all necessary libraries within the binary, rather than relying on shared libraries. |
| `-fPIC` | Generates position-independent code, which is often required when creating shared libraries. |
| `-pthread` | Enables multithreading with the pthreads library. It also sets flags for threading-safe code generation. |
| `-march=<architecture>` | Generates code optimized for a specific CPU architecture (e.g., `-march=x86-64` for 64-bit x86 architecture). |
| `-Wextra` | Enables additional warning messages that are not covered by `-Wall`. |
| `-v` | Shows detailed information about the compilation process, including the commands executed by GCC. |
| `-E` | Preprocesses the source files only, outputting the result to standard output or a specified file without compiling. |
| `-S` | Compiles the source files to assembly code, producing `.s` files instead of object files or executables. |
| `-M` | Generates a list of makefile dependencies, which can be used for managing the build process in a makefile. |
| `-fstack-protector` | Enables stack protection to help prevent stack overflow attacks, adding guards to stack variables. |
| `-ftime-report` | Provides a detailed report on the time taken by different stages of the compilation process, useful for performance analysis. |
| `-Wconversion` | Warns about implicit conversions that may alter a value, such as changing a `float` to an `int`. |
| `-fno-exceptions` | Disables C++ exception handling, which can reduce code size and improve performance if exceptions are not used. |
| `-pg` | **GCC** modifies the compiled code to insert function call counters and time measurements.  The **output** can be read with `gprof`. |

## GNU Toolchain

> Here’s a table summarizing the tools mentioned:
> 

| **Tool** | **Description** |
| --- | --- |
| **GNU Compiler Collection (GCC)** | A compiler suite that supports many languages, such as C/C++ and Objective-C/C++. |
| **GNU Make** | An automation tool for compiling and building applications. |
| **GNU Binutils** | A suite of binary utility tools, including linker and assembler. |
| **GNU Debugger (GDB)** | A tool for debugging programs, allowing developers to examine and control the execution of programs. |
| **GNU Autotools** | A build system including Autoconf, Autoheader, Automake, and Libtool. |
| **GNU Bison** | A parser generator, similar to lex and yacc, used to convert grammar descriptions into a C program. |

## GCC Pipeline

> The GCC (GNU Compiler Collection) pipeline generally consists of several stages that transform your C or C++ source code into an executable binary. Here’s a high-level overview of the typical GCC pipeline:
> 

> Here’s a table summarizing the typical GCC pipeline stages:
> 

| **Stage** | **Description** |
| --- | --- |
| **Preprocessing (cpp)** | The preprocessor processes the source code and handles directives like `#include`, `#define`, and `#ifdef`. It generates a preprocessed version of the source code. |
| **Compilation (cc1)** | The preprocessed code is passed to the C or C++ compiler (cc1), which translates it into assembly code specific to the target architecture, checking for errors and performing optimizations. |
| **Assembly (as)** | The assembly code is assembled into machine code (binary code) using the assembler (as), producing object files (usually with a `.o` extension). |
| **Linking (ld)** | The linker (ld) combines object files and libraries into a single executable binary, resolving symbols and addresses across different files. |

## The GNU C Library

> The GNU C Library (glibc) includes several tools and utilities, primarily focused on supporting and managing the library's functionality.
> 

| **Tool/Component** | **Description** |
| --- | --- |
| [**libc.so**](http://libc.so/) | The shared library that provides standard C library functions such as `printf`, `malloc`, `memcpy`, and more. It is linked dynamically at runtime. |
| **libc.a** | The static version of the C library, allowing programs to be linked statically, including all necessary functions within the executable. |
| [**ld-linux.so**](http://ld-linux.so/) | The dynamic linker/loader for Linux. It loads and links the shared libraries needed by a program when it is executed. |
| **ldd** | A command-line utility that prints the shared libraries required by each program or shared library. |
| **ldconfig** | A command-line tool used to update the system's dynamic library cache, ensuring that shared libraries can be found and loaded by the linker. |
| **iconv** | A tool and function library for converting text from one character encoding to another. |
| **nscd** | The Name Service Cache Daemon, which provides a cache for common name service requests like hostname or user ID lookups to speed up these operations. |
| **locale** | A command-line tool and function for setting and querying the locale (language and region settings) of the system or an application. |
| **getconf** | A command-line tool for querying system configuration variables and limits. |
| **mtrace** | A memory tracing tool that can be used to detect memory leaks in programs that use the GNU C Library’s `malloc` and `free` functions. |
| **gencat** | A tool used to generate message catalogs, which are used by programs for internationalization (i18n) support. |
| **localedef** | A tool to compile locale definition files into binary format for use by applications and the system. |

## GCC Instrumentation

> **GCC Instrumentation** refers to the **compiler-assisted** modification of a program's binary and execution flow to enable profiling, debugging, performance analysis, or runtime monitoring. It involves inserting additional instructions into the compiled code at compile-time, which collect metadata about function calls, execution paths, branch coverage, and system interactions.
> 

> Note: After the program is instrumented with **`-pg`**, a **`gmon.out`** file will be generated, which can then be analyzed using [gprof](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gprof.md).
> 

| **Option** | **Use Case** | **Instrumentation Method** |
| --- | --- | --- |
| `-pg` | Profiling with `gprof` | Inserts `mcount()` calls |
| `-fprofile-arcs -ftest-coverage` | Code coverage with `gcov` | Adds execution counters in each branch |
| `-finstrument-functions` | Custom function tracing | Calls `__cyg_profile_func_enter/exit()` |
| `-fsanitize=` | Injects runtime checks to detect memory errors (`AddressSanitizer`), undefined behavior (`UBSan`), and thread race conditions (`ThreadSanitizer`). |  |

References:

- [gmon](note.html?n=technica/computation/language-system/conceptual-model-language-system/glibc.md)
- [SIGPROF](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/sigprof.md) (Signal)
- https://github.com/lattera/glibc/blob/master/gmon/mcount.c
- https://github.com/lattera/glibc/tree/master/gmon
- https://gcc.gnu.org/onlinedocs/gcc-9.1.0/gcc/Instrumentation-Options.html

## Does `gcc -pg` log every function call during profiling, or does it sample a subset of calls? If it samples, how frequently does this occur, and what are the implications on accuracy?

> `gprof` (enabled with `-pg`) does **not** log every function call individually. Instead, it uses **sampling** and **instrumentation**:
> 
1. **Instrumentation (mcount / _mcount)**
    - Every function call is instrumented at **entry** (via `mcount()` or `_mcount()` in glibc).
    - This provides a **call graph** but does not record precise timing for each call.
2. **Sampling-Based Timing (gmon.out)**
    - The program is **periodically interrupted** by a timer (usually 100 Hz).
    - The program counter (PC) is **sampled at these intervals**, which means:
        - **Frequently executed functions appear more often.**
        - **Short-lived functions may be missed.**

## References

- https://gist.github.com/dbremont/1c34bfb3a47e063d459c26c1f8fd4e6a
- [GNU Compiler Collection](https://gcc.gnu.org/)
- [Diving into GCC internals](https://news.ycombinator.com/item?id=31731145)
- [Architecture for a Next-Generation GCC](https://llvm.org/pubs/2003-05-01-GCCSummit2003.pdf)
- GCC Profiler Internals ([trofi.github.io](http://trofi.github.io/))
[https://news.ycombinator.com/item?id=31448836](https://news.ycombinator.com/item?id=31448836)
- Extracting the abstract syntax tree from GCC (2015) ([lwn.net](http://lwn.net/))
[https://news.ycombinator.com/item?id=26590524](https://news.ycombinator.com/item?id=26590524)
- Understanding GCC Builtins to Develop Better Tools [pdf] ([manuelrigger.at](http://manuelrigger.at/))
[https://news.ycombinator.com/item?id=20845828](https://news.ycombinator.com/item?id=20845828)
- Spec Files Specifying Subprocesses and the Switches to Pass to Them [https://unix.stackexchange.com/questions/77779/relationship-between-cc1-and-gcc](https://unix.stackexchange.com/questions/77779/relationship-between-cc1-and-gcc)
- [An introduction to creating GCC plugins](https://lwn.net/Articles/457543/)
- [gcc -print-file-name=plugin](https://github.com/rofirrim/gcc-plugins)
- [GCC plugin speller.c](https://lwn.net/Articles/458806/)
- [Extracting the abstract syntax tree from GCC (2015)](https://news.ycombinator.com/item?id=26590524)
- [GCC Profiler Internals (trofi.github.io)](https://news.ycombinator.com/item?id=31448836)
- [Understanding GCC Builtins to Develop Better Tools [pdf] (manuelrigger.- at)](https://news.ycombinator.com/item?id=20845828)
- [GNU Compiler Collection (GCC) Internals](https://gcc.gnu.org/onlinedocs/gccint/)
- [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
- [Diving into GCC Internals](https://news.ycombinator.com/item?id=31731145)
- [Mini Workshop on GCC Internals](https://www.cse.iitb.ac.in/~uday/gcc-mini-workshop/)
- [CPP Search Path](https://gcc.gnu.org/onlinedocs/cpp/Search-Path.html)
- [C Preprocessor](https://en.wikipedia.org/wiki/C_preprocessor)
- What is a GCC toolchain?
[https://stackoverflow.com/questions/50307733/what-is-a-gcc-toolchain](https://stackoverflow.com/questions/50307733/what-is-a-gcc-toolchain)
- [Profiler](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/profiler.md)
- https://stackoverflow.com/questions/27082959/gcc-static-and-pie-are-incompatible-for-x86
- [LLVM (Low Level Virtual Machine)](note.html?n=technica/computation/language-system/conceptual-model-language-system/llvm-low-level-virtual-machine.md)