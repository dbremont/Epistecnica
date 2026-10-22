---
tags: [debug, tool]
---

# GDB (GNU Project Debugger)


> **GDB (GNU Debugger)** is a powerful, open-source debugging tool used for troubleshooting and analyzing the behavior of programs written in languages like C, C++, and Fortran during execution.
> 

> **Watchpoints** in GDB are a debugging tool used to monitor the value of variables or memory locations in a program and halt execution when these values are read from or written to, helping to track down when and where a variable changes its value during the execution process.
> 

QA:

- How to break in the main entry point?
- …

## Debug Symbol Packages

1. Search for the packages’ symbols, e.x `sudo apt search dbgsym | grep <name>`
2. Install the package containing the symbols,
3. Download the sources,
4. Have fun :)

## GDB Commands

The GNU Debugger (GDB) is a powerful tool for debugging applications written in C, C++, and other languages. Here’s a table summarizing some of the most commonly used GDB commands, which can help you control the execution of programs, examine and modify their state, and perform other debugging tasks:

| Command | Description |
| --- | --- |
| `run` | Starts the execution of the program in the debugger. |
| `break [location]` | Sets a breakpoint at the specified location in the code. |
| `continue` | Continues the execution of the program after a breakpoint. |
| `next` | Executes the following line of code without stepping into functions. |
| `step` | Steps into functions, executing lines one at a time. |
| `list` | Lists the source code in the current context. |
| `print [expr]` | Evaluate and print the expression `expr`. |
| `watch [expr]` | Sets a watchpoint that halts execution when `expr` changes. |
| `backtrace` | Displays the call stack of the current thread. |
| `info breakpoints` | Lists all breakpoints and watchpoints. |
| `delete` | Deletes one or all breakpoints or watchpoints. |
| `disable` | Disables specified breakpoints without deleting them. |
| `enable` | Enables specified breakpoints. |
| `quit` | Exits GDB. |
| `help` | Provides help for using GDB, including command documentation. |
| `tui` | … |

## GDB Info

> Here's a table summarizing the various `info` commands in GDB along with their descriptions:
> 

| Command | Description |
| --- | --- |
| `info address` | Describe where symbol SYM is stored. |
| `info all-registers` | List of all registers and their contents, for the selected stack frame. |
| `info args` | All argument variables of the current stack frame or those matching REGEXPs. |
| `info auto-load` | Print current status of auto-loaded files. |
| `info auxv` | Display the inferior's auxiliary vector. |
| `info bookmarks` | Status of user-settable bookmarks. |
| `info breakpoints` / `info b` | Status of specified breakpoints (all user-settable breakpoints if no argument). |
| `info checkpoints` | IDs of currently known checkpoints. |
| `info classes` | All Objective-C classes, or those matching REGEXP. |
| `info common` | Print out the values contained in a Fortran COMMON block. |
| `info connections` | Target connections in use. |
| `info copying` | Conditions for redistributing copies of GDB. |
| `info dcache` | Print information on the dcache performance. |
| `info display` | Expressions to display when the program stops, with code numbers. |
| `info exceptions` | List all Ada exception names. |
| `info extensions` | All filename extensions associated with a source language. |
| `info files` | Names of targets and files being debugged. |
| `info float` | Print the status of the floating point unit. |
| `info frame` / `info f` | All about the selected stack frame. |
| `info frame-filter` | List all registered Python frame-filters. |
| `info functions` | All function names or those matching REGEXPs. |
| `info guile` / `info gu` | Prefix command for Guile info displays. |
| `info inferiors` | Print a list of inferiors being managed. |
| `info line` | Core addresses of the code for a source line. |
| `info locals` | All local variables of the current stack frame or those matching REGEXPs. |
| `info macro` | Show the definition of MACRO, and its source location. |
| `info macros` | Show the definitions of all macros at LINESPEC, or the current source location. |
| `info mem` | Memory region attributes. |
| `info module` | Print information about modules. |
| `info modules` | All module names, or those matching REGEXP. |
| `info os` | Show OS data ARG. |
| `info pretty-printer` | GDB command to list all registered pretty-printers. |
| `info probes` | Show available static probes. |
| `info proc` | Show additional information about a process. |
| `info program` | Execution status of the program. |
| `info record` / `info rec` | Info record options. |
| `info registers` / `info r` | List of integer registers and their contents, for the selected stack frame. |
| `info scope` | List the variables local to a scope. |
| `info selectors` | All Objective-C selectors, or those matching REGEXP. |
| `info sharedlibrary` / `info dll` | Status of loaded shared object libraries. |
| `info signals` / `info handle` | What debugger does when the program gets various signals. |
| `info skip` | Display the status of skips. |
| `info source` | Information about the current source file. |
| `info sources` | All source files in the program or those matching REGEXP. |
| `info stack` / `info s` | Backtrace of the stack, or innermost COUNT frames. |
| `info static-tracepoint-markers` | List target static tracepoints markers. |
| `info symbol` | Describe what symbol is at location ADDR. |
| `info target` | Names of targets and files being debugged. |
| `info tasks` | Provide information about all known Ada tasks. |
| `info terminal` | Print inferior's saved terminal status. |
| `info threads` | Display currently known threads. |
| `info tracepoints` / `info tp` | Status of specified tracepoints (all tracepoints if no argument). |
| `info tvariables` | Status of trace state variables and their values. |
| `info type-printers` | GDB command to list all registered type-printers. |
| `info types` | All type names, or those matching REGEXP. |
| `info unwinder` | GDB command to list unwinders. |
| `info variables` | All global and static variable names or those matching REGEXPs. |
| `info vector` | Print the status of the vector unit. |
| `info vtbl` | Show the virtual function table for a C++ object. |
| `info warranty` | Various kinds of warranty you do not have. |
| `info watchpoints` | Status of specified watchpoints (all watchpoints if no argument). |
| `info win` | List of all displayed windows. |
| `info xmethod` | GDB command to list registered xmethod matches. |

## GDB Dashboard

[GDB Dashboard](https://stackoverflow.com/a/51301717)

![Untitled](../assets/note/technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger/untitled.png)

## GDB Python API

[GDB Python API](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger/gdb-python-api.md)

## Debugging Multithreading Programs

> In GDB, when you are debugging a multi-threaded application, the debugger lets you control and inspect all threads, but it operates in the context of one thread at a time.
> 

```bash
info threads # Show all the threads
thread       # How the current thread
thread 2     # Switch to thread number 2.
break pthread_create
```

## Syscalls

[How can I set breakpoint in GDB for open(2) syscall returning -1](https://stackoverflow.com/questions/25972841/how-can-i-set-breakpoint-in-gdb-for-open2-syscall-returning-1)

## Signals

…

### Visualizing Thread Relationships

> To visualize or understand thread relationships in GDB, you'll mostly look at which threads create other threads and any logical or functional dependencies they have.
> 

> Here are steps and commands in GDB to help explore thread relationships: …
> 

## References

- [GDB WEB UI](https://www.gdbgui.com/)
- Rust: - [Debugging Rust apps with GDB](https://blog.logrocket.com/debugging-rust-apps-with-gdb/) - [Debugging support in the Rust compiler](https://rustc-dev-guide.rust-lang.org/debugging-support-in-rustc.html)
- GO: - [Debugging Go Code with GDB](https://go.dev/doc/gdb)
- [gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard)
- [GDB WEB UI](https://www.gdbgui.com/)
- [Debug Symbol Packages](https://wiki.ubuntu.com/Debug%20Symbol%20Packages)
- [GDB tricks](https://news.ycombinator.com/item?id=8671284)
- [List of all function calls made in an application](https://keep.google.com/#home)
- [How to see all functions that called with debugger](https://reverseengineering.stackexchange.com/questions/19971/how-to-see-all-functions-that-called-with-debugger)
- Gough, Brian. (2005). *An introduction to GCC : for the GNU compilers gcc and g++*. 137.
- Stopping at the first machine code instruction in GDB https://stackoverflow.com/questions/10483544/stopping-at-the-first-machine-code-instruction-in-gdb
- How do I debug the child process after fork() in gdb? https://stackoverflow.com/questions/6199270/how-do-i-debug-the-child-process-after-fork-in-gdb
- gdbserver - Remote Server for the GNU Debugger https://man7.org/linux/man-pages/man1/gdbserver.1.html
- The Architecture of Open Source Applications (Volume 2) GDB https://aosabook.org/en/v2/gdb.html
- https://wwwcdf.pd.infn.it/localdoc/gdbint.pdf
- http://www.staff.city.ac.uk/~kloukin/teaching/cpp/ref-cards/gdb-guide.pdf
- Writing a Linux Debugger https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/
- minidbg https://github.com/wzao1515/minidbg
- GDB8 Linux debugging tools https://www.youtube.com/watch?v=b1EDVH6BuBM
- https://github.com/geohot/qira
- [https://en.wikipedia.org/wiki/Gdbserver](https://en.wikipedia.org/wiki/Gdbserver)
    - [What does the GDB backtrace message "0x0000000000000000 in ?? ()" mean?](https://stackoverflow.com/questions/121326/what-does-the-gdb-backtrace-message-0x0000000000000000-in-mean)
- [https://web.stanford.edu/class/cs107/guide/x86-64.html](https://web.stanford.edu/class/cs107/guide/x86-64.html)
- [https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf](https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf)
- [https://darkdust.net/files/GDB Cheat Sheet.pdf](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf)
- How to look at the stack with gdb
[https://jvns.ca/blog/2021/05/17/how-to-look-at-the-stack-in-gdb/](https://jvns.ca/blog/2021/05/17/how-to-look-at-the-stack-in-gdb/)
- Can I set a breakpoint on 'memory access' in GDB?
[https://stackoverflow.com/questions/58851/can-i-set-a-breakpoint-on-memory-access-in-gdb](https://stackoverflow.com/questions/58851/can-i-set-a-breakpoint-on-memory-access-in-gdb)
- [Neovim](note.html?n=technica/computation/miscelanea/neovim.md)