---
tags: [process]
---

# Linux Process Management Stack

- [Linux Network Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-network-stack.md)

> Focus on the process management aspect of operating systems, including process scheduling, synchronization, and communication.
> 

> Understand how processes are created, managed, and terminated, and how the operating system handles interrupts and exceptions.
> 

> **Process**: An instance of a program running on a computer, which includes its own memory space and execution context.
> 

QA:

- Process Memory Structure → How is it determined? Can it be modified? How can you write a raw process without using the ELF format, a linker, or even an assembler? How does executable memory work?
- Which are the process related sys-calls on Linux?
- What it is memory allocation?
- What is a process stack? How the process stack implemented? Is the software stack map to CPU registers?
- How to know how many sockets does a process has open?

## File Format

> In which file formats are Linux processes stored or described?
> 

> See more in https://github.com/torvalds/linux/blob/8b690556d8fe074b4f9835075050fba3fb180e93/fs/binfmt_script.c#L34;  https://github.com/torvalds/linux/blob/8b690556d8fe074b4f9835075050fba3fb180e93/fs/binfmt_elf.c; https://github.com/torvalds/linux/blob/8b690556d8fe074b4f9835075050fba3fb180e93/fs/binfmt_elf_fdpic.c; https://github.com/torvalds/linux/blob/8b690556d8fe074b4f9835075050fba3fb180e93/fs/binfmt_flat.c; https://github.com/torvalds/linux/blob/8b690556d8fe074b4f9835075050fba3fb180e93/fs/binfmt_misc.c
> 

| **Format** | **Description** | **Implementation** |
| --- | --- | --- |
| **ELF (Executable and Linkable Format)** | Standard binary format for Linux executables, shared libraries, and object files. | Implemented via the **binfmt_elf** handler in the kernel; loaded using `execve()` path. |
| **Script (`#!`)** | Text files with a shebang (`#!`) indicating an interpreter. | Implemented via **binfmt_script.c**; registers a handler that invokes the interpreter. |
| **a.out** | Legacy binary format preceding ELF. | Supported by **binfmt_aout**; mostly deprecated but still handled in some kernels. |
| **Core Dump** | Files representing a process’s memory image after a crash. | Managed via **fs/binfmt.c** and the `core_pattern` mechanism in `/proc/sys/kernel/core_pattern`. |
| **Custom/Foreign Binaries** | Non-native binaries handled by user-registered interpreters (e.g., Wine). | Registered via `register_binfmt()` in the kernel’s **binfmt_misc** subsystem. |

## Structure

Everything about a process:

- Status
- Register state (when not in ready state)
- PID, User, Executable, Priority
- Execution time
- Memory space, translation
- Environment Variables

## Process Memory Layout

| Region | Description | Writable | Allocated in file? | Notes |
| --- | --- | --- | --- | --- |
| **.text** | Executable code of the program | No | Yes | Contains compiled instructions; usually at the lowest virtual addresses. |
| **.rodata** | Read-only data, e.g., string literals, constants | No | Yes | Placed near `.text`; attempting to modify causes a segfault. |
| **.data** | Initialized global and static variables | Yes | Yes | Variables with initial values; loaded into memory at startup. |
| **.bss** | Uninitialized global and static variables | Yes | No | Occupies zeroed memory at runtime; doesn’t take space in the file. |
| **Heap** | Dynamically allocated memory (via `malloc`, `new`, etc.) | Yes | No | Grows upwards; managed by allocator and OS. |
| **Mmap & Shared Libs** | Memory mapped files, shared libraries, memory-mapped devices | Varies | Varies | Includes `.so` libraries, dynamic modules, large allocations via `mmap`. |
| **Stack** | Function call frames, local variables, return addresses | Yes | No | Grows downwards (toward lower addresses); managed automatically. |
| **Environment / args** | Command-line arguments and environment variables | Yes | No | Often located near the top of user space memory. |
| **Kernel space** | Reserved by OS; not accessible by user-mode processes | No | No | Starts after the user-space memory limit. |

## Scheduling

> 

## User-Lang View

> 
- Specific Variables / Java Properties
- Environment Variables …

## Interprocess Communication Model(s)

| **Mechanism** | **Description** | **Underlying Implementation** | **Evaluation** |
| --- | --- | --- | --- |
| **Pipes (Anonymous)** | Unidirectional byte stream between parent-child processes. | Kernel **pipe buffer** (circular buffer) in page cache; file descriptors; blocking I/O. | Simple; low latency; not scalable; only for related processes. |
| **Named Pipes (FIFOs)** | Pipes represented as FS nodes for unrelated processes. | **VFS special file** + pipe buffer in kernel; opens via FS path. | Simple; works across processes; same limitations as pipes. |
| **Unix Domain Sockets** | Local socket communication; supports stream or datagram. | **sockfs**, kernel socket layer, AF_UNIX protocol, ancillary data for FD passing. | Very fast; flexible; supports FD passing; moderate overhead. |
| **TCP/UDP Sockets** | Network-based messaging for local or remote processes. | Full **network stack** (INET), TCP/IP protocol, skb buffers, routing layer. | Heavy overhead; network-transparent; robust and scalable. |
| **Signals** | Sends async notifications (SIGINT, SIGUSR1, etc.). | Kernel **task_struct signal handlers**, bitmasks, queues for RT signals. | Minimal data; low overhead; fragile; limited expressiveness. |
| **SysV Message Queues** | Kernel-managed structured message queues. | **msg_queue** kernel objects, global namespace, IPC permissions subsystem. | Legacy; moderate throughput; complex API; limited scaling. |
| **POSIX Message Queues** | Modern message queues with priorities and async notifications. | **mqueuefs**, kernel linked lists of messages, per-FD queue. | Better API than SysV; size limits; moderate overhead. |
| **Shared Memory (SysV)** | Processes share physical memory segments. | **shmem segments**, page tables pointing to shared frames; kernel shm registry. | Highest throughput; external sync required; legacy API. |
| **Shared Memory (POSIX `shm_open`)** | Shared memory backed by file descriptors and `mmap()`. | Backed by **tmpfs** files + **mmap** pages; FD-based semantics. | Clean API; requires synchronization; flexible. |
| **Memory-Mapped Files (`mmap`)** | Maps file contents or anonymous memory into process space. | **Page cache**, VMA structures, unified page frame layer. | Good for large data; sync needed; FS semantics influence behavior. |
| **SysV Semaphores** | Kernel counter-based synchronization. | **sem_array** objects, kernel-managed queues, global SysV IPC namespace. | Slowish; legacy; useful but clunky API. |
| **POSIX Semaphores (`sem_t`)** | Lightweight semaphores in shared memory or named semaphores. | Implemented in **libpthread** + **futex** for blocking; kernel involvement only on contention. | Fast; clean API; best for synchronization across processes. |
| **Futexes** | User-space fast locking with kernel help on contention. | **FUTEX_WAIT / FUTEX_WAKE** syscalls, hashed wait queues in kernel. | Extremely low latency; highly scalable; requires shared memory. |
| **eventfd** | Counter used for event notification. | Kernel **eventfd_ctx** object, 64-bit counter, poll/select compatible. | Very low overhead; ideal for simple signaling; not for data. |
| **signalfd** | Receive signals via a file descriptor instead of handlers. | **signalfd_ctx**, integration with kernel signal delivery and poll/select. | Cleaner than async signals; still limited data. |
| **timerfd** | File-descriptor timers compatible with poll/select. | **hrtimers** subsystem + small kernel FD wrapper. | Great for event loops; not IPC but supports coordination. |
| **inotify** | Notifies of FS events. | **inotify_inode_mark** + fsnotify subsystem. | Good for FS watching; not general-purpose IPC. |
| **D-Bus** | High-level IPC for desktop/system services. | User-space daemon (**dbus-daemon**) + Unix sockets + marshalling protocol. | Easy, structured, but very slow; high overhead. |
| **Netlink Sockets** | Kernel ↔ user structured messaging. | AF_NETLINK protocol, skb buffers, routing layer, multicast groups. | Ideal for kernel notifications; structured; not general IPC. |
| **io_uring (Shared Rings)** | Async I/O with shared submission/completion queues. | Shared **ring buffers** in mapped memory + kernel SQ/CQ polling, io-wq threads. | Extremely fast; modern; complex; can be used as high-performance IPC. |

## What is the program that load the Linux ELF Executable programs  into memory? What is the `user lang` program  that  run  a Linux ELF Executable in Linux / Bash?

> In Linux, the program responsible for running an **ELF (Executable and Linkable Format)** executable is the **`exec` family of system calls** (e.g., `execve`, `execl`, `execvp`, etc.). These system calls are used to replace the current process image with a new one (the ELF executable you want to run).
> 

> Ffrom a user's perspective in **Bash** or the command line, the program that directly runs an ELF executable is typically the **Linux kernel itself**, facilitated by the **loader** (e.g., `/lib64/ld-linux-x86-64.so.2` for 64-bit systems)
> 

1. **Bash / Shell**:

- When you type `./my_program` in Bash, the shell uses the `execve` system call to ask the kernel to load and execute the ELF file.
- Example:
    
    ```bash
    ./my_elf_executable
    
    ```
    

2. **Loader (`ld.so`)**:

- The Linux kernel doesn't directly execute the ELF file. Instead, it uses a **dynamic linker/loader** (e.g., `/lib64/ld-linux-x86-64.so.2`) to:
    1. Load the ELF file into memory.
    2. Resolve and link shared libraries (if the program is dynamically linked).
    3. Transfer control to the program's entry point.
- You can explicitly invoke the loader like this:
    
    ```bash
    /lib64/ld-linux-x86-64.so.2 ./my_elf_executable
    
    ```
    

3. **`exec` System Calls**:

- Programs like Bash use the `execve` system call to run ELF executables. For example:
    
    ```c
    execve("/path/to/my_elf_executable", argv, envp);
    
    ```
    
- This replaces the current process image with the ELF executable.

4. **Direct Execution by the Kernel**:

- When you run an ELF executable, the kernel checks the file's header to ensure it's a valid ELF file.
- If the file is valid, the kernel sets up the process's memory space, loads the program, and starts execution.

## How to mark a piece of memory as executable?

| Method | How to Use | Applies To | Notes |
| --- | --- | --- | --- |
| **`mmap()` at allocation** | `mmap(NULL, size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE |
| **`mprotect()` after allocation** | `mprotect(addr, size, PROT_READ | PROT_EXEC)` | Any allocated memory (heap, mmap, etc.) |
| **ELF section flags** | Mark section with `AX` (Allocated + Executable) in linker script or compiler | Static sections in ELF (`.text`, `.plt`, `.init`) | Loader sets pages as executable automatically; typical for normal program code. |

## References

- [x86](note.html?n=technica/computation/operating-system/x86.md)
- https://en.wikipedia.org/wiki/Chroot
- [ELF (Executable and Linkable Format)](note.html?n=technica/computation/language-system/conceptual-model-language-system/elf-executable-and-linkable-format.md)
- https://stackoverflow.com/questions/13112038/difference-between-system-getenv-system-getproperty
- https://anadoxin.org/blog/the-linux-binfmt-subsystem.html/