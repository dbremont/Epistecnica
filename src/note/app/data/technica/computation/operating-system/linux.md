# Linux

> An operating system (OS) is a fundamental software that manages computer hardware and provides a platform for running applications, enabling user interaction, and facilitating communication between software and hardware components.
> 

> The job of an OS is to share a computer among multiple programs and to provide a more useful set of service than the hardware alone supports.
> 

> Multiplexing: multiplexing (sometimes contracted to muxing) is a method by which multiple analog or digital signals are combined into one signal over a shared medium. In computing, I/O multiplexing can also be used to refer to the concept of processing multiple input/output events from a single event loop, with system calls like poll and select (Unix). https://www.wikiwand.com/en/Multiplexing
> 

> Linux traps are mechanisms by which the kernel handles exceptions and interrupts, providing a controlled method for executing a specific routine or handling an error when a process requests a system resource or when an unexpected event occurs during execution.
> 

![](https://i.pinimg.com/originals/b0/80/06/b080063dbe7f9cf817972c558ef96e78.png)

[https://pbs.twimg.com/media/Giz5jQtWkAA-MI_?format=jpg&name=small](https://pbs.twimg.com/media/Giz5jQtWkAA-MI_?format=jpg&name=small)

QA:

- Linux Everything is a File Philosophy.
- System Limits and Performance Modelling.
- …

## Study Guide

> Study Method: Use Linux to study the basics concepts of OS;   Create technical profiles for others OS’s.
> 

## History

> 

## List of OS

| Category | Name | Description | Year |
| --- | --- | --- | --- |
| **Unix-like** | Linux | Open-source, Unix-based OS, widely used in servers, workstations, and embedded systems. | 1991 |
|  | BSD (FreeBSD, OpenBSD, NetBSD) | Unix-like systems known for their security, performance, and code clarity. | 1993 |
| **Windows-based** | Windows NT | Microsoft’s operating system for both personal computers and servers. | 1993 |
|  | Windows 10 | Latest major release of the Windows OS, focused on productivity and security. | 2015 |
| **Mac-based** | macOS | Unix-based OS by Apple for Mac computers, known for its polished UI and integration with other Apple devices. | 2001 |
| **Real-time Operating System (RTOS)** | FreeRTOS | Open-source real-time operating system for embedded devices. | 2003 |
| **Mobile OS** | Android | Open-source mobile OS based on the Linux kernel, primarily used in smartphones and tablets. | 2008 |
|  | iOS | Mobile OS by Apple, used in iPhones and iPads, known for its security and seamless integration with Apple hardware. | 2007 |
|  | **KaiOS** | A lightweight OS for feature phones, based on Firefox OS. |  |
|  | **HarmonyOS** | Huawei's multi-device OS, designed for smartphones, IoT, and smart devices. |  |
| **Embedded Systems** | Raspbian (now Raspberry Pi OS) | A Debian-based OS optimized for Raspberry Pi boards, widely used for embedded systems. | 2012 |
| **Mainframe** | z/OS | IBM's mainframe operating system designed for high-performance and secure enterprise environments. | 2001 |
| **Specialized OS** | Plan 9 | Distributed operating system developed by Bell Labs, focusing on simplicity and research. | 1992 |
|  | MINIX | A Unix-like OS used primarily for educational purposes and research on microkernel architecture. | 1987 |
| **Open-source** | Ubuntu | Debian-based Linux distribution, popular for desktops and servers due to ease of use. | 2004 |
|  | Debian | A robust and highly flexible Linux distribution, used as the foundation for many other distros. | 1993 |
| **Cloud/Container OS** | **CoreOS** | A lightweight Linux OS designed for running containers in cloud environments. |  |
|  | **RancherOS** | A minimalist Linux OS for running Docker containers. |  |
|  | **Photon OS** | VMware's lightweight Linux OS optimized for cloud and container workloads. |  |
| **Historical OS** | **MS-DOS** | Microsoft's early OS for IBM-compatible PCs, primarily command-line based. |  |
|  | **AmigaOS** | The OS for Commodore Amiga computers, known for its multimedia capabilities. |  |
|  | Unix | … |  |
|  | Multics | …. |  |

## Build and Debug

> [A Guide to Build & Debug the Linux Kernel](https://app.notion.com/p/A-Guide-to-Build-Debug-the-Linux-Kernel-1a8c0f5171ec80d19474e2d019cd11db?pvs=21)
> 

## Linux Mechanism

> Here's the information organized into a table format, detailing the mechanisms within a kernel, their descriptions, and their purposes:
> 

| **Mechanism** | **Description** | **Purpose** |
| --- | --- | --- |
| Process Scheduling | Manages the execution of processes and threads using various scheduling algorithms. | Ensures efficient CPU utilization, fairness among processes, and responsiveness of interactive applications. |
| Interrupt Handling | Manages responses to hardware or software interrupts by temporarily halting current CPU activities. | Enables the system to respond promptly to hardware events and manage system calls from user-space applications. |
| Memory Management | Includes memory allocation, paging, segmentation, and virtual memory management mechanisms. | Manages system memory resources efficiently, ensuring isolation and optimizing memory usage. |
| System Calls | Provides a controlled interface for user-space applications to request services from the kernel. | Allows processes to perform operations under the supervision of the kernel, enhancing security and functionality. |
| File System Management | Manages storage, retrieval, and data organization on storage devices through file systems. | Provides a structured way to store data persistently, managing space allocation and data integrity. |
| Device Drivers | Acts as intermediaries between the operating system and hardware devices. | Enables the kernel to interface transparently with various hardware devices, abstracting hardware complexities. |
| Security Mechanisms | Includes strategies like access controls, auditing, and secure boot processes. | Protects system resources and data from unauthorized access or misuse. |
| Inter-process Communication (IPC) | Mechanisms such as message queues, semaphores, shared memory, and sockets. | Facilitates communication and coordination between processes sharing data or operations. |
| Network Stack | Implements protocols for managing network communications, such as TCP/IP stack and routing. | Handles all aspects of network communications, allowing data transmission over network interfaces. |
| Virtualization Support | Provides support for running multiple virtual machines on a single physical host. | It enables hosting multiple isolated operating system instances for better resource utilization and security. |
| Power Management | The kernel includes power management features to control the system's power consumption. These include CPU frequency scaling, suspend and resume, and ACPI (Advanced Configuration and Power Interface) support. |  |
| Kernel Introspection |  |  |

## Linux Implementation Abstractions

> Here's a concise table listing some of the fundamental abstractions provided by Linux, detailing their descriptions and purposes to showcase how they simplify complex interactions within the system:
> 

| **Abstraction** | **Description** | **Purpose** |
| --- | --- | --- |
| **File System** | Treats all input/output devices as files, providing a uniform interface for interacting with them. | Simplifies file and device operations; files, directories, and devices are accessed through standard APIs. |
| **Process** | Represents a running program, encapsulating its state, memory, and other resources. | Isolates and manages execution contexts, allowing multiple programs to run concurrently. |
| **Virtual Memory** | It separates physical memory into a logical memory space with which applications interact. | Allows programs to use more memory than is physically available and isolates application memory spaces for security and stability. |
| **System Calls** | Interfaces between user-space applications and the kernel allow programs to perform operations like opening files, sending network data, etc. | Provides a controlled mechanism for accessing hardware resources and sensitive operations, maintaining system integrity and security. |
| **Threads** | Lightweight processes that allow parallel execution within the same application context. | Enhances application performance by utilizing multi-core processor capabilities without heavy overhead. |
| **Inter-process Communication (IPC)** | Mechanisms such as message queues, semaphores, shared memory, and sockets allow processes to communicate and synchronize their actions. | Facilitates cooperation between processes needing to share data or coordinate operations. |
| **Sockets** | Endpoints for sending and receiving data between processes over a network. | Simplifies network communication, allowing applications to transmit data across networks transparently. |
| **Device Drivers** | Software interfaces for hardware devices. | Enables the kernel and applications to interact with hardware without needing to know the details of how the hardware works. |
| **User and Group IDs** | Identifiers for users and groups, providing a way to manage permissions and access controls. | Enhances security by controlling which users and applications can access specific system resources. |
| **Signals** | Notifications are sent to a process to inform it of events like interrupts, termination requests, etc. | Provides a mechanism for handling asynchronous events, allowing processes to react to external or system-initiated actions. |
| **Procfs** | The "process file system" is a unique virtual filesystem in Linux that provides a window into the kernel.  |  |
| **Sysfs** | Sysfs is a virtual filesystem provided by the Linux kernel that presents information about various kernel subsystems, hardware devices, and associated device drivers in a structured way, enabling user space applications to obtain hardware and configuration information. |  |
| **System timers** | The kernel manages system timers for various purposes, including scheduling processes, performing timekeeping functions, and triggering periodic events. |  |
| **Interrupt handling** | The kernel manages interrupts generated by hardware devices, ensuring they are handled promptly and efficiently. It also allows interrupt handlers to respond to specific events generated by devices. |  |

## Linux System Calls

> **Linux system** calls are predefined, low-level functions provided by the Linux kernel that allow user-space applications to request various types of operating system services and resources, such as file operations, process control, and network communication.
> 

## Linux Kernel Threads

> 

Here is a table of common **Linux kernel threads**, along with their functions and typical behavior:

| **Kernel Thread** | **Description** | **Function** | **Typical Behavior** |
| --- | --- | --- | --- |
| **`ksoftirqd`** | Handles soft IRQs (interrupts) that are deferred for later processing. | Processes soft IRQs, helping in efficient interrupt handling. | Runs in the background, periodically handling deferred interrupts. |
| **`kswapd`** | Manages the swapping of pages between RAM and swap space. | Performs page swapping to manage memory pressure. | Periodically wakes up to free memory by swapping out pages. |
| **`kworker`** | Handles workqueue tasks in the kernel. | Executes deferred work queued by various kernel subsystems. | Runs tasks queued by kernel subsystems for deferred execution. |
| **`kmod`** | Manages kernel module loading and unloading. | Loads and unloads kernel modules. | Typically invoked during boot or when modules are added/removed. |
| **`khugepaged`** | Manages transparent huge pages (THP) to optimize memory usage. | Handles huge page allocations and defragmentation. | Periodically defragments memory to maintain large pages. |
| **`ksmd`** | Performs kernel-side memory deduplication for anonymous memory. | Merges duplicate memory pages to save memory. | Runs periodically to reduce memory usage by deduplicating pages. |
| **`kclean`** | Cleans up stale memory mappings. | Cleans up unused memory mappings. | Runs periodically to free up resources by cleaning stale mappings. |
| **`kexec`** | Manages the kexec system call, which allows loading and executing a new kernel without rebooting. | Facilitates kernel loading and booting without rebooting. | Invoked when a new kernel is loaded via kexec. |
| **`kthreadd`** | The kernel thread daemon that creates and manages other kernel threads. | Manages the lifecycle of kernel threads. | Runs continuously, creating and managing kernel threads. |
| **`kpfault`** | Handles page faults that occur in the kernel. | Manages page faults and ensures proper page handling. | Triggered when a page fault occurs in kernel space. |
| **`kcmp`** | Manages kernel comparisons of process memory maps. | Compares process memory mappings for various system calls. | Used for process comparison, especially for debugging. |

## Linux ABI

> The Linux ABI (Application Binary Interface) defines a standard interface between binary program files and the operating system, specifying details such as data types, system calls, and conventions for function calls and memory layouts, which ensure that compiled applications can operate correctly across different versions of the OS without needing recompilation.
> 

## Process Management

> Focus on the process management aspect of operating systems, including process scheduling, synchronization, and communication. Understand how processes are created, managed, and terminated, and how the operating system handles interrupts and exceptions.
> 

## Memory Management

> Study the **memory management** aspect of operating systems, including how virtual memory works, how page replacement algorithms function, and how memory protection is implemented. Learn about memory allocation, fragmentation, and garbage collection.
> 

## Linux File Systems Stack

> See more in [Linux  File Systems Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-file-systems-stack.md).
> 

> The **Linux File Systems Stack** is a modular and hierarchical system that facilitates file operations, from user-space requests down to physical disk I/O. It includes the **VFS**, **file system drivers**, **block layer**, **page cache**, and **storage device drivers**, each responsible for specific aspects of file management, storage access, and performance optimization. The stack ensures that different file systems can coexist and interact seamlessly within the Linux environment.
> 

## Linux Security Stack

> Explore the security features of operating systems, including authentication, authorization, and access control. Study how the operating system manages user accounts, passwords, and file permissions, and how it defends against malware, viruses, and other security threats.
> 

## Linux Networking Stack

> **Berkeley Sockets** is an **API Standard** for network communication in Unix-like operating systems that provides a standardized interface for creating and managing sockets to facilitate data exchange between devices over a network.
> 

## Linux IPC Stack

> In Linux, communication between processes can be achieved through a variety of abstractions, including file system, pipes, signals, message queues, semaphores, shared memory, and sockets, providing a flexible and powerful way for processes to exchange information and work together towards a common goal.
> 

## Linux Performance

> Study how operating systems optimize performance, including how they manage system resources such as CPU, memory, and disk I/O. Learn about performance monitoring, tuning, and profiling, and how to identify and resolve performance issues in operating systems.
> 

## Linux Driver Model

> 
> 

> The "Linux Driver Model" is a framework within the Linux kernel that provides standardized interfaces and mechanisms for hardware interaction, device management, and power management, facilitating the development, integration, and runtime control of device drivers.
> 

## Linux Device Model

> See more here https://www.notion.so/Linux-Device-Model-224c0f5171ec8084aa40dedacfb3fbcc?source=copy_link
> 

## Linux Multimedia Stack

> See more in [Linux Multimedia Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-multimedia-stack.md).
> 

## Linux System Introspection

> Provides interfaces for monitoring, tracing, and analyzing kernel behavior at runtime.
> 

> See more in https://www.notion.so/Linux-System-Introspection-287c0f5171ec80faa61fec0038d5b546?source=copy_link
> 

## Linux Distribution

See more in [Linux Distribution](note.html?n=technica/computation/operating-system/linux-distribution.md).

---

## Conceptual Model

Conceptual Model: Linux

## References

- https://cs61.seas.harvard.edu/site/2022/#gsc.tab=0
- [A Guide to Linux Tools](https://app.notion.com/p/A-Guide-to-Linux-Tools-20fc0f5171ec8050a102fe8bb284f9e7?pvs=21)
- [A Guide to Binary Tools](https://app.notion.com/p/A-Guide-to-Binary-Tools-e44641d2394b46cf9e95a57fb6bc176b?pvs=21)
- [A Guide  to Hardware Hacking](https://app.notion.com/p/A-Guide-to-Hardware-Hacking-1aec0f5171ec80b38296d1f8c8a0186c?pvs=21)
- [A Guid to Rooting Phone Systems](https://app.notion.com/p/A-Guid-to-Rooting-Phone-Systems-1aec0f5171ec800db6ccc5de4c029f74?pvs=21)
- https://device.report/maxxter
- https://linux-kernel-labs.github.io/refs/heads/master/index.html
- https://en.wikipedia.org/wiki/Linux
- [Linux ABI](https://kernelnewbies.org/ABI)
- The Linux Kernel Documentation
[https://www.kernel.org/doc/html/latest/index.html](https://www.kernel.org/doc/html/latest/index.html)
- Kernel Debugging
    - A gentle introduction to Linux Kernel fuzzing [https://blog.cloudflare.com/a-gentle-introduction-to-linux-kernel-fuzzin](https://blog.cloudflare.com/a-gentle-introduction-to-linux-kernel-fuzzing/)
    - drgn: How the Linux Kernel Team at Meta Debugs the Kernel at Scale https://developers.facebook.com/blog/post/2021/12/09/drgn-how-linux-kernel-team-meta-debugs-kernel-scale/
- linux-insides [https://0xax.gitbooks.io/linux-insides/content/](https://0xax.gitbooks.io/linux-insides/content/)
- User-space interface for Crypto API https://lwn.net/Articles/410536/
- Myths Programmers Believe about CPU Caches https://software.rajivprab.com/2018/04/29/myths-programmers-believe-about-cpu-caches/
- [Interactive Map of the Linux Kernel](https://makelinux.github.io/kernel/map/)
- [Linux Directory Structure](https://www.geeksforgeeks.org/linux-directory-structure/)
- [Implementation of Epoll](https://fd3kyt.github.io/posts/implementation-of-epoll/)
- [Some possible reasons for 8-bit bytes](https://jvns.ca/blog/2023/03/06/possible-reasons-8-bit-bytes/)
- [OS Dev](https://wiki.osdev.org/Main_Page)
- [The Linux Kernel documentation](https://docs.kernel.org/index.html)
- [The Linux Kernel Module Programming Guide](https://sysprog21.github.io/lkmpg/)
- [Linux Kernel Teaching](https://linux-kernel-labs.github.io/refs/heads/master/index.html)
- “Operating Systems, Concurrent and Distributed Software Design“, Jean Bacon and Tim Harris, Addison-Wesley 2003
- “Modern Operating Systems”, (3rd Ed), Andrew Tannenbaum, Prentice-Hall 2007
- Love, R. (2004). Linux Kernel Development (2nd ed.). Novell Press.
- Bovet, D. P., Cesati, M. (2000). Understanding the Linux Kernel. O’Reilly Media.
- McKusick, M. K., Neville-Neil, G. v. (2004). The design and implementation of the FreeBSD operating system. Addison Wesley.
- Cox, R., Kaashoek, F., Morris, R. (2021). xv6: a simple, Unix-like teaching operating system.
- McKusick, M. K., Neville-Neil, G. v. (2004). The design and implementation of the FreeBSD operating system. Addison Wesley.
- [‣](https://app.notion.com/p/10e598edb79081d5b312c05f68e3069c?pvs=21)
- https://github.com/dbremont/linux-api-labs/
- [A Guide to Build & Debug the Linux Kernel](https://app.notion.com/p/A-Guide-to-Build-Debug-the-Linux-Kernel-1a8c0f5171ec80d19474e2d019cd11db?pvs=21)
- https://arcanenibble.github.io/hardware-hotplug-events-on-linux-the-gory-details.html