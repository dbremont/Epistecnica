---
tags: [ipc]
---

# Linux IPC Stack


> In Linux, communication between processes can be achieved through a variety of abstractions, including file system, pipes, signals, message queues, semaphores, shared memory, and sockets, providing a flexible and powerful way for processes to exchange information and work together towards a common goal.
> 

> **IPC** stands for **Inter-Process Communication,** a mechanism that allows processes to communicate with each other in a Linux operating system.
> 

![](https://i.ytimg.com/vi/MYOkrOemcEE/hqdefault.jpg)

## Linux IPC Abstractions

> In Linux, Inter-Process Communication (IPC) mechanisms are vital for enabling processes to exchange data and synchronize their actions.
> 

Here’s a table summarizing the fundamental IPC abstractions available in Linux:

| IPC Mechanism | Description | Use Cases |
| --- | --- | --- |
| **Pipes** | Provides a unidirectional data channel between processes. | Simple parent-child communication. |
| **Named Pipes (FIFOs)** | It acts like a pipe but can be accessed by unrelated processes using a name in the filesystem. | Communication between any processes that know the pipe name. |
| **Signals** | Allows processes to send notifications to other processes. | Interrupting processes, handling exceptions. |
| **Message Queues** | Offers a method to send and receive messages between processes. | Complex data transfer with priority and type settings. |
| **Semaphores** | Used to control access to shared resources by multiple processes. | Synchronization, avoiding race conditions. |
| **Shared Memory** | Maps a region of memory that multiple processes can access. | The fastest method for sharing large amounts of data. |
| **Sockets** | Provides a method for bidirectional data exchange between processes, potentially across different machines. | Network communication, local inter-process communication. |
| **Memory-mapped Files** | Map files or devices are mapped into memory and are accessible by multiple processes. | Fast file access, shared between processes. |
| **UNIX Domain Sockets** | Sockets that provide communication within the same host machine. | Efficient local communication, supporting both stream and datagram protocols. |

This table covers various IPC methods, each suited for different scenarios, from simple notifications (signals) to complex data sharing and synchronization mechanisms (semaphores, shared memory). 

## Process

> Abstraction of a running program is characterized by a memory containing the code, data, and a stack. The code implements the computation; the data is the state in which the computation acts. The stack organized the program’s procedures calls.
> 

> A process runs in user space when needs a service trom the kernel uses a system call.
> 

![](https://1480285644-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M13JlZNu0b_edmxHTQk%2F-M4bi4LFDWarrQTldkn5%2F-M4bienH9ewqFuJ1nrOo%2Fimage.png?alt=media&token=3e730071-271e-4783-a57d-c5eb5011f97b)

## References

- [IPC](https://www.wikiwand.com/en/Interprocess_communication)
- [The Linux Scheduler: a Decade of Wasted Cores](https://blog.acolyer.org/2016/04/26/the-linux-scheduler-a-decade-of-wasted-cores/)
- [How Does the Linux Kernel Start a Process](https://iq.thc.org/how-does-linux-start-a-process)
- [How the heck do we get to main()?](http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html)
- Maxgio. (n.d.). A journey into the Linux scheduler. Retrieved July 12, 2022, from https://blog.maxgio.me/posts/linux-scheduler-journey/
- [A complete guide to Linux process scheduling](https://trepo.tuni.fi/bitstream/handle/10024/96864/GRADU-1428493916.pdf)
- [Teleforking a process onto a different computer!](https://thume.ca/2020/04/18/telefork-forking-a-process-onto-a-different-computer/)
- [Sharing Memory Robustly in Message-Passing Systems](https://groups.csail.mit.edu/tds/papers/Attiya/TM-423.pdf)
- [How fast are Linux pipes anyway? (2022) (mazzo.li)](https://news.ycombinator.com/item?id=37782493)