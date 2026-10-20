# xv6

> A simple, Unix-like teaching operating system.
> 

> The interface (shell) uses the kernel interface to access the services, implemented using a set of simple mechanisms.
> 

> The shell is an ordinary program that reads commands from the user and executed them.
> 

QA:

- How to debug xv8 using VS Code?

## Build

> 

## Debug

> 

```bash
gdb kernel

target remote localhost:26000

symbol-file ls.o

symbol-file kernel
```

## Services

- Processes
- I/O and File Descriptors
- Pipes
- File System
- Memory

### Processes

> A xv6 process consists of user-space memory (instruction, data, and tack) and per process state provide to the kernel.
> 

> xv6 **time-shares** a process: it transparently switches the available CPUs among the est of process waiting to execute.
> 

> ¿Why fork and exec syscall’s?
> 

### I/O and File Descriptors

> A **file descriptor** is a small integer representing a **kernel-managed object** that a process may read or write to it.
> 

> A process may open a **file descriptor** by opening a file, directory, or device, creating a pipe, or duplicating an existing descriptor.
> 

> The xv6 kernel uses the file descriptor as an **index** into a **per-process table**, so every process has a private space of file descriptors starting a zero.
> 

> By **convention,** the file descriptor 0 is the stdin, 1 is the stdout and 2 is the stderr. The shell ensures that it always has three file descriptors open, which by default file descriptors for the **console**.
> 

> A newly allocated file descriptor is always the **lowest numbered unused** descriptor of the current process.
> 

### Pipes

> A pipe is a small kernel buffer exposed to processes as a pair of file descriptors, one for reading and one for writing.
> 

> Pipes provide a way for processes to communicate.
> 

### File System

> The xv6 file system provides data files, which contain uninterpreted byte arrays, and directories, which contain named references to data files and other directories.
> 

> A path is the direction of a file / directory.
> 

> A file is an abstraction for an is an array of bytes in disk.
> 

> An inode holds metadata about a file, including its type (file, directory, or device), it’s length, it’s location on disk, and the number of links to it.
> 

## Interface

> The interface is the set of system calls.
> 

## Mechanisms

- Time sharing
- Process Isolation
- System Calls Implementations
- User Modes
- CPU Modes → Instruction Types
- Virtual Memory
- Page Tables
- Trap: ecall, exception, interrupt.
- Driver’s System
- Coordination: Locking, …
- Scheduling
- File System: Modular Design

## Shell

- ¿How is I/O redirection implemented? / 14.
- …

## QA

- How **QEMU** support **GDB Debug Protocol**? What is **the used**?

## References

- https://github.com/dbremont/xv6
- [xv6-public source](https://github.com/mit-pdos/xv6-public)
- [Debugging user-code on xv6 with gdb](https://stackoverflow.com/questions/10534798/debugging-user-code-on-xv6-with-gdb)
- [QEMU (Quick Emulator)](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/qemu-quick-emulator.md)
- https://www.reddit.com/r/osdev/comments/fgxe6x/tcpip_network_stack_on_xv6/
- https://github.com/vibhorvatsa/xv6-networking-stack