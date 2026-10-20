---
tags: [ipc]
---

# Signal

- [SIGPROF](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/sigprof.md)

> A **signal** is a software **interrupt** delivered to a process or thread to notify it of an event or condition.
> 

> **Signals** are a form of inter-process communication (IPC) that allow processes and threads to communicate with each other asynchronously.
> 

## List of Signals

Here's a table of commonly used **Linux OS signals** along with their purposes and default actions:

| **Signal** | **Signal Number** | **Description** | **Default Action** |
| --- | --- | --- | --- |
| **`SIGHUP`** | 1 | Hangup detected on controlling terminal or death of parent | Terminate the process |
| **`SIGINT`** | 2 | Interrupt from the keyboard (Ctrl+C) | Terminate the process |
| **`SIGQUIT`** | 3 | Quit from keyboard (Ctrl+) | Terminate the process and create a core dump |
| **`SIGILL`** | 4 | Illegal instruction | Terminate the process and create a core dump |
| **`SIGABRT`** | 6 | Abort signal from `abort()` | Terminate the process and create a core dump |
| **`SIGFPE`** | 8 | Floating-point exception (e.g., division by zero) | Terminate the process and create a core dump |
| **`SIGKILL`** | 9 | Kill signal (forcefully terminate) | Immediately terminate the process (cannot be caught or ignored) |
| **`SIGSEGV`** | 11 | Segmentation fault (invalid memory reference) | Terminate the process and create a core dump |
| **`SIGPIPE`** | 13 | Broken pipe (write to a pipe with no readers) | Terminate the process |
| **`SIGALRM`** | 14 | Timer signal from `alarm()` or `setitimer()` | Terminate the process |
| **`SIGTERM`** | 15 | Termination signal (default signal sent by `kill`) | Terminate the process |
| **`SIGUSR1`** | 10 | User-defined signal 1 | User-defined (can be handled) |
| **`SIGUSR2`** | 12 | User-defined signal 2 | User-defined (can be handled) |
| **`SIGCHLD`** | 17 | Child process stopped or terminated | Ignore by default, or handle (e.g., to reap child processes) |
| **`SIGCONT`** | 19 | Continue process if stopped | Resume the process if stopped (from `SIGSTOP`) |
| **`SIGSTOP`** | 17 | Stop the process (cannot be caught or ignored) | Stop the process (used by `kill` or job control) |
| **`SIGTSTP`** | 20 | Stop process from terminal (Ctrl+Z) | Stop the process (can be caught or ignored) |
| **`SIGTTIN`** | 21 | Background process attempting to read from terminal | Stop the process |
| **`SIGTTOU`** | 22 | Background process attempting to write to terminal | Stop the process |
| **`SIGPROF`** | 27 | Profiling timer (used for performance profiling) | User-defined (typically handled by profiling tools like `gprof`) |
| **`SIGSYS`** | 31 | Bad argument to system call (e.g., invalid syscall) | Terminate the process and create a core dump |
| **`SIGPWR`** | 30 | Power failure or system power state change | Terminate the process |
| **`SIGWINCH`** | 28 | Window size change (terminal) | Ignore by default, or handle (e.g., update terminal layout) |
| **`SIGXCPU`** | 24 | CPU time limit exceeded (set by `ulimit`) | Terminate the process |
| **`SIGXFSZ`** | 25 | File size limit exceeded (set by `ulimit`) | Terminate the process |

## References

- https://en.wikipedia.org/wiki/Signal_(IPC)