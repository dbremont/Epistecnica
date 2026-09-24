# McKusick, M. K. (2014). The design and implementation of the freebsd operating system. Addison-Wesley Professional.

Related Catalogus Documentorum: Organick, E. I. (1972). The Multics System: An Examination of Its Structure. MIT Press. (Organick,%20E%20I%20(1972)%20The%20Multics%20System%20An%20Examina%203ba598edb790802d9578ed795a3092e1.md)

```python
@BOOK{McKusick2014-ye,
  title     = "The design and implementation of the freebsd operating system",
  author    = "McKusick, Marshall Kirk",
  publisher = "Addison-Wesley Professional",
  month     =  aug,
  year      =  2014
}
```

## Notes

---

QA:

- What is a terminal?
- Does every process have a terminal?
- How many terminals are created by the OS? tty1, …
- What is the anatomy of a process address space? Who determines that anatomy?

## Index

## Overview

### History and Goals

> Multics History.
> 

> Unix History.
> 

> Unix was written in a High Level Language  / C.
> 

> Unix Distribution: …
> 

> FreeBSD Organization Model: …
> 

> **BSD:** Berkeley Software Distribution.
> 

> Computer Systems Research Group (CSRG): **…**
> 

> **Portable Operating System Interface** (**POSIX) - 1988.**
> 

> **BSD:** UNIX + Utilities → Core Contributions (Socket API, TCP/IP Stack, FFS, virtual memory, job control, signals, …) → Increasingly Independent BSD Code → AT&T/USL Legal Dispute → Settlement → 4.4BSD-Lite (AT&T Code Removed) → BSD-derived Operating Systems (FreeBSD, NetBSD, OpenBSD, DragonFly BSD).
> 

> **Berkeley Software Distribution (BSD)** originated at the University of California, Berkeley, as a set of enhancements to the **AT&T UNIX** operating system. The first BSD release appeared in **1977 (1BSD)**, primarily distributing additional software developed at Berkeley, including the `ex` editor and Pascal tools.
> 

> During the late 1970s and early 1980s, BSD evolved from a collection of UNIX additions into a substantial operating-system distribution. **4.1BSD (1981)** and subsequent releases introduced major improvements in performance, virtual memory, networking, and system utilities.
> 

> A major milestone was **4.2BSD (1983)**, which incorporated **TCP/IP networking**, the Berkeley sockets API, and the Fast File System (FFS). These mechanisms became foundational to Internet-connected UNIX systems and were subsequently adopted widely.
> 

> With **4.3BSD (1986)** and later releases, Berkeley continued improving networking, kernel performance, and system facilities. The **BSD UNIX source code** also became increasingly important as a basis for other UNIX systems.
> 

> In the early 1990s, Berkeley separated much of its independently developed code from AT&T's proprietary UNIX code. The **4.4BSD-Lite** releases provided a largely freely redistributable BSD system and became the direct ancestor of modern BSD operating systems such as **FreeBSD, NetBSD, and OpenBSD**.
> 

#### Time Line of BD Contribution Set

> UNIX Extensions → Virtual Memory → BSD Utilities → Fast File System (FFS) → TCP/IP Stack → Berkeley Sockets API → Network Programming Model → Performance & Kernel Improvements → Open BSD Source → BSD as an Independent UNIX System
> 

#### BSD: Core People and Institutions

- **Bill Joy** — co-founder of BSD; central figure in early Berkeley UNIX, **ex/vi**, networking, and the BSD distribution.
- **Chuck Haley** — worked with Joy on the early Berkeley UNIX environment and helped develop **ex**.
- **Ken Thompson** — co-creator of UNIX; important because BSD originated as modifications and extensions to AT&T UNIX.
- **Dennis Ritchie** — co-creator of UNIX and C; C was fundamental to BSD's implementation.
- **Kirk McKusick** — major BSD developer; central to the **Fast File System (FFS)** and later BSD development.
- **Marshall Kirk McKusick** — same person; often cited as **Kirk McKusick**.
- **Sam Leffler** — major contributor to **4.2BSD/4.3BSD**, particularly networking and system development.
- **Mike Karels** — important BSD kernel and networking developer; later involved in the BSD legal and organizational transition.
- **Eric Allman** — developed **sendmail**, one of the major pieces of software distributed with BSD.
- **Keith Bostic** — key figure in removing AT&T-derived code and producing **4.4BSD-Lite**.
- **Chris Torek** — important contributor to the C/compiler and BSD development ecosystem.
- **Theo de Raadt** — founder of **OpenBSD**.
- **Jordan Hubbard** — co-founder and early leader of **FreeBSD**.
- **Lynne Jolitz & William Jolitz** — produced **386BSD**, an important ancestor of FreeBSD, NetBSD, and OpenBSD.
- **Matthew Dillon** — founder of **DragonFly BSD**.
- **Bell Labs / AT&T** — creator and original owner of UNIX.
- **University of California, Berkeley (UCB)** — home of the BSD project.
- **Computer Systems Research Group (CSRG), UC Berkeley** — the primary institutional group behind BSD development.
- **DARPA** — major sponsor of Berkeley networking research, especially the TCP/IP work.
- **USL (Unix System Laboratories)** — AT&T subsidiary that pursued the legal case against BSD.
- **Berkeley Software Design, Inc. (BSDI)** — commercial company founded around BSD technology and involved in the UNIX/BSD legal dispute.

#### The FreeBSD Development Model

- **Core Developer:** A selected group of people elected every two years by the committers. Gatekeepers of the source code.
- Control Model of Code Merging Into the Main Developmetn Line: …
- Screenign Process:
- Code Review & Approval Mechanism: …
- Organization: Similar to CSRG: Code, Documentation,  Bug Report Database, Mailing List, Administrative Data, it’s maintain publicly.
- Software Development Process Automation - Specially of Repetitive Operations.
- https://www.freebsd.org/administration/

### Design Overview of FreeBSD

> The **`FreeBSD Kernel Provides`** process, filesystem, communication,  and a system startup.
> 

> Kernel: $H$ → $H_{vm}$  is the core component of an operating system that abstracts the physical hardware $H$ into a virtualized, abstract hardware model ($H_{vm}$). It provides user processes with a secure and consistent interface to  interact with system resources, translating high-level operations into hardware-specific instructions.
> 
- How to model the Hardware?
    - What is `Hardware`?
    - What is the Structure of a **Modern Computer System**?
    - Which is the **Hardware type space**? Bus, …
    - Which are the **types of mechanisms** by which hardware entities interact with other hardware in the computer? And how, through the **CPU, can one communicate** with them? Which are the `connectivity` `mechanism hierarchy` (up - directly interact with the CPU), lower (does not)?
    - How is **hardware** detected and **configured** by the system?
- How to formulate the $H_{vm}$? How does it abstracts hardware?
- How is  $H_{vm}$ implemented?

> **Kernel Implementation Abstractions** (Implementation): …
> 

> **Kernel Services** (Interface / Specification): …
> 

> The machine-dependent aspects of the kernel are isolated from the mainstream code.
> 

> The Kernel Operate in a different address space that is  inaccessible to user processes.|
> 

**Free BSD Kernel Services:**

- Basic Kernel Facilities: timer and system-clock handling, descriptor management, and process management,
- Memory-management support: paging and swapping,
- Generic system interfaces: the I/O, control, and multiplexing operations performed on descriptors,
- the filesystem: files, directories, pathname translation

**Implementation Abstractions:**

- Basic: timer and system clock-handling, descriptor management, and process management,
- Memory-management support:  paging and swapping,
- Generic system interfaces, I/O, control, and multiplexing operations performed on descriptors,
- The filesystem: files, directories, pathname translation, file locking, and I/O buffer management
- Terminal-handling support: the pseudo-terminal interface and terminal line disciplines
- Interprocess-communication facilities: sockets
- Support for network communication: communication protocols and generic work facilities, such as routing

**Machine dependent software:** 

- Low-level system-startup actions,
- Trap and fault-handling
- Low-level manipulation of the run-time context of a process
- Configuration and inititialization of hardware devices
- Run-time support for I/O devices

**System Call:**

- Service interface of the kernel.
- A **system call usually** is implemented as hardware trap that changes the CPU’s execution mode and the current address-space mapping.

**Process Management:**

- A thread or task of execution if called a process.
- Processes are scheduled for execution according to a process priority parameter.
- **Real-time process** have the highest priority and did not need to share the underlying resources.
- Process are organized in process groups.
- **Process Groups**: are used to control access to terminals an to provide a means  of distributing signals to collection of related process.

**Signals:**

- The system defines a set of `signal` that may be delivered to a process. A signal like many other concepts can be define

Networking

- What is the minimum trasmision unit of  `x` technolgy?

**Memory Management**:

- Each process has it’s own private address space. The address space is initially divided into three logical segments: text, data, and stack. The text segment is read-only and contains the  machine instructions of a program.
- `nmap:`   allow a process to extend it’s address space using a an external file.

**Kernel Memory Management**:

- The kernel stack is limited;
- Most kernel allocation are dynamic (not stack or what?)

**I/0 System:**

- The basic model of the UNIX I/O system is a sequence of bytes that can be accessed either randomly or sequentially.
- I/O Stream: An Stream of Bytes.

Descriptors and I/O:

- UNIX processes use descriptors to reference I/O streams. Descriptors are small unsigned integers obtained from the open and socket system calls.
- Descriptors can denote file, pipe, fifo and  socket .

Descriptor Management:

- Standard descriptors in proccesses? Input, Output; Error.
- Descriptor remmaping: I/O Redirection
- Pipeline: A series of proceses connected by pipes.

Devices:

- Hardware devices have filenames and many be accessed by the user via the same system calls used for regular files.
- Device Special File / Special File.
- Network devices uses syscalls;  and not files; because interaction between two end-points it’s hard to model as a filed.

Socket:

- Socket IPC: a communication endpoint;   it denoted by a file descriptor.

Scatter/Gather I/O:

- Multiple buffer - single read.

### Kernel Services

> Saying that the kernel is a service provider to userlang -  to me  is a wrong formulation. The kernel - fundamental provides a abstract interface to the underlying hardware - that is it exposed the capabilities of the hardware though a interaction interface.
> 

> I need to reason very deeply - about the concept of technical service, and if this concept - match the piece of reality - being abstracted via the concept.
> 

Interaction Interface:

- Syscalls (`ioctl, mmap`),
- `/proc`
- `/sys`
- ptty
- device files
- signals
- shared memory
- IPC interfaces
- sockets
- virtual filesystems

…

- System Process
- Kernel Process
- Execution Abstractions
    - Process
    - Kernel Process
    - Process Group
- Permanent Kernel Proceses
- What can trigger the executing of the kernel code?  Hardware interrupt, Hardware trap, Software-initiated trap (which is also hardware 😎).
- 👁️ What is the difference between a trap and a interrupt? [https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt](https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt)
    - They are both events,  the difference comes from role, triggering mechanism, etc.
- …

```jsx
         CPU Execution
               │
               ▼
             EVENT
          /          \
   synchronous     asynchronous
    (exception)     (interrupt)
        │                │
        ▼                ▼
   handler          handler
```

- Run time organization of the kernel: top half, button half.
- Entry to the kernel:  when we switch from user process - the kernel must save the current state?
    - How does this works?
    - What happens with new inputs? Networking,  and other kinds of devices.
    - How the returning to the process happens?

*While process P is suspended in kernel context, how are concurrent external events handled, and under what semantics are they eventually delivered to P, coalesced, or discarded?*

```jsx
Process P ──► Kernel ───────────────► Resume P
                │
                │  P's context saved
                │
                ├───────┐
                │       │ concurrent event
                │       ▼
                │   [Mouse / I/O / Network]
                │       │
                │       ▼
                │   Kernel handling
                │       │
                │       ▼
                └────►  ?
                        │
              queued / coalesced / dropped
                        │
                        ▼
                    delivered to P?
```

- Is a system **call a trap**?
- What is a **page**?
- Which security capabilities does **FreeBSD** offer, and how are **they implemented**?
- How to control the underlying resources? Assigments, …
- How the accoutnign works? How  the os keeps tracks of the resources being consume?

## Processes

### Process Management

### Memory Management

## I/O System

### I/O System Overview

### Device

### Local Filesystems

### The Network Filesystem

### Terminal Handling

## Interprocess Communication

### Interprocess Communication

### Network Communication

### Network Protocols

## System Operation

### Startup and Shutdown

## QA

### How is the **IO Bus** Implemented? How to list the bus recognize by the **OS (Linux/Ubuntu)**?

> …
> 

### Which technique is behind the design of the memory paging mechanism?

> **Model-mediated abstraction technique**: **Complex system → Simplified model → Human operates on the model → Translation layer → Real system.**
> 

And there are several distinct **products** of the technique:

1. **Representation abstraction** — hide implementation details.
2. **Interface abstraction** — expose a smaller interaction surface.
3. **Execution abstraction** — make one computational system appear as another.
4. **Resource abstraction** — turn physical resources into logical resources.
5. **Isolation abstraction** — make shared resources appear private.
6. **Semantic abstraction** — represent low-level operations using higher-level concepts.
7. **Translation mechanism** — maintain correspondence between model and reality.
8. **Composition mechanism** — allow models to be combined into larger models.

### Which are the origins of the term ‘Unix’?

The term **Unix** came from **UNICS**, a pun on **MULTICS**.

- **MULTICS** = **Multiplexed Information and Computing Service**
- **UNICS** = originally **UNiplexed Information and Computing Service**
- It was later spelled **UNIX**.

### Which are the set of concepts that renders the FreeBSD Interaction Surface Intelligible?

> Commands, utilities, system calls, files, processes, signals, pipes, sockets, devices, filesystems, users, groups, permissions, shells, daemons, configuration mechanisms, APIs, and ABIs.
> 

### What is the quality of the concepts that emerge from the interface? Is there overlap between them?

> The concepts are primarily abstractions of resources, operations, actors, and interaction mechanisms. They exhibit substantial conceptual coherence and composability, but also intentional overlap: the same underlying resource may be exposed through multiple interfaces. The key question is whether these overlaps preserve distinct and predictable semantics or introduce conceptual redundancy and ambiguity.
> 

### Which are the set of concepts that renders the FreeBSD Implementation Intelligible?

> Kernels, subsystems, modules, kernel objects, data structures, system-call implementations, processes and threads, schedulers, virtual memory, VFS, filesystems, device drivers, networking, IPC, synchronization mechanisms, interrupt and trap handling, resource management, protection mechanisms, ABI compatibility layers, and hardware-abstraction mechanisms.
> 

### What is the quality of the concepts that emerge from the implementation? Is there overlap between them?

> The implementation concepts are more concrete and mechanism-oriented. They form a layered and highly interconnected conceptual structure, with significant overlap at subsystem boundaries. This overlap is generally functional rather than redundant: multiple mechanisms may participate in realizing a single abstraction, while a single implementation mechanism may support several abstractions.
> 

## References

- https://en.wikipedia.org/wiki/FreeBSD_Core_Team
- https://en.wikipedia.org/wiki/Input%E2%80%93output_memory_management_unit
- https://www.freebsd.org/administration/
- https://docs.freebsd.org/en/books/developers-handbook/
- https://github.com/aleksander0m/libdrm
- https://wiki.archlinux.org/title/AMDGPU
- https://docs.kernel.org/driver-api/vfio.html
- [Bovet, D. P., & Cesati, M. (2005). Understanding the Linux Kernel: from I/O ports to process management. “ O’Reilly Media, Inc.” ](Bovet,%20D%20P%20,%20&%20Cesati,%20M%20(2005)%20Understanding%20the%20%2010e598edb790818980dffd57d1adf8ef.md)
- https://en.wikipedia.org/wiki/I2C
- https://www.igorslab.de/en/rebelstool-1-0-6-ready-to-download-the-new-more-power-tool-under-linux-just-in-a-different-form/
- [Silberschatz, A., Galvin, P. B., & Gagne, G. (2008). Operating System Concepts (8th ed.). Wiley.](Silberschatz,%20A%20,%20Galvin,%20P%20B%20,%20&%20Gagne,%20G%20(2008)%20%20368598edb7908029b97edb067a92ff42.md)
- https://github.com/freebsd/freebsd-src
- https://en.wikipedia.org/wiki/Computer_Systems_Research_Group
- [6.828 Operating System Engineering](https://app.notion.com/p/6-828-Operating-System-Engineering-368598edb79080918a2ad2e8f419e88e?pvs=21)
- https://en.wikipedia.org/wiki/Computer_Systems_Research_Group
- https://en.wikipedia.org/wiki/Berkeley_Software_Distribution
- https://en.wikipedia.org/wiki/Unix_wars
- **AT&T. (1987).** *The System V Interface Definition (SVID), Issue 2*. American Telephone and Telegraph, Murray Hill, NJ, January 1987.
- **Babaoglu, O., & Joy, W. N. (1981).** “Converting a Swap-Based System to Do Paging in an Architecture Lacking Page-Referenced Bits.” *Proceedings of the Eighth Symposium on Operating Systems Principles*, 78–86.
- **Bach, M. J. (1986).** *The Design of the UNIX Operating System*. Prentice-Hall.
- **Comer, D. (2000).** *Internetworking with TCP/IP, Volume 1* (4th ed.). Prentice-Hall.
- **Comer, D. (1984).** *Operating System Design: The Xinu Approach*. Prentice-Hall.
- **Compton, M. (Ed.). (1985).** “The Evolution of UNIX.” *UNIX Review*, 3(1).
- **Debevoise, D. (1993).** *Unix System Laboratories Inc. vs. Berkeley Software Design Inc.*, Civ. No. 92-1667.
- **DiBona et al., 1999.** C. DiBona, S. Ockman, & M. Stone, *Open Sources: Voices from the Open Source Revolution*, pp. 31–46, Chapter 2—“Twenty Years of Berkeley UNIX: From AT&T-Owned to Freely Redistributable,” O’Reilly & Associates, 1999.
- **Ewens et al., 1985.** P. Ewens, D. R. Blythe, M. Funkenhauser, & R. C. Holt, “Tunis: A Distributed Multiprocessor Operating System,” *USENIX Association Conference Proceedings*, pp. 247–254, June 1985.
- **Holt, 1983.** R. C. Holt, *Concurrent Euclid, the UNIX System, and Tunis*, Addison-Wesley, 1983.
- **Hubbard, 2004.** J. Hubbard, “A Brief History of FreeBSD,” *FreeBSD Handbook*, section 1.3.1, March 2004.
- **ISO, 1999.** ISO, *ISO/IEC 9899 Programming Language C Standard*, ISO 9899, December 1999.
- **Joy, 1980.** W. N. Joy, “Comments on the Performance of UNIX on the VAX,” Technical Report, University of California Computer Systems Research Group, Berkeley, April 1980.
- **Jung, 1985.** R. S. Jung, “Porting the AT&T Demand Paged UNIX Implementation to Microcomputers,” *USENIX Association Conference Proceedings*, pp. 361–370, June 1985.
- **Kashtan, 1980.** D. L. Kashtan, “UNIX and VMS: Some Performance Comparisons,” Technical Report, SRI International, Menlo Park, CA, February 1980.
- **Kernighan & Ritchie, 1978.** B. W. Kernighan & D. M. Ritchie, *The C Programming Language*, Prentice-Hall, Englewood Cliffs, NJ, 1978.
- **Kernighan & Ritchie, 1989.** B. W. Kernighan & D. M. Ritchie, *The C Programming Language*, 2nd ed., Prentice-Hall, Englewood Cliffs, NJ, 1989.
- **Linzner & MacDonald, 1993.** J. Linzner & M. MacDonald, *University of California at Berkeley versus Unix System Laboratories Inc.*, June 1993.
- **McKusick et al., 1989.** M. K. McKusick, M. Karels, & K. Bostic, “The Release Engineering of 4.3BSD,” *Proceedings of the New Orleans Usenix Workshop on Software Management*, pp. 95–100, April 1989.
- **Miller, 1978.** R. Miller, “UNIX—A Portable Operating System,” *ACM Operating System Review*, vol. 12, no. 3, pp. 32–37, July 1978.
- **Miller, 1984.** R. Miller, “A Demand Paging Virtual Memory Manager for System V,” *USENIX Association Conference Proceedings*, pp. 178–182, June 1984.
- **Mohr, 1985.** A. Mohr, “The Genesis Story,” *UNIX Review*, vol. 3, no. 1, p. 18, January 1985.
- **Organick, 1975.** E. I. Organick, *The Multics System: An Examination of Its Structure*, MIT Press, Cambridge, MA, 1975.
- **P1003.1, 1988.** P1003.1, *IEEE P1003.1 Portable Operating System Interface for Computer Environments (POSIX)*, Institute of Electrical and Electronic Engineers, Piscataway, NJ, 1988.
- **Peirce, 1985.** N. Peirce, “Putting UNIX in Perspective: An Interview with Victor Vyssotsky,” *UNIX Review*, vol. 3, no. 1, p. 58, January 1985.
- **Presotto & Ritchie, 1985.** D. L. Presotto & D. M. Ritchie, “Interprocess Communication in the Eighth Edition UNIX System,” *USENIX Association Conference Proceedings*, pp. 309–316, June 1985.
- **Richards & Whitby-Strevens, 1980.** M. Richards & C. Whitby-Strevens, *BCPL: The Language and Its Compiler*, Cambridge University Press, Cambridge, U.K., 1980, 1982.
- **Ritchie, 1978.** D. M. Ritchie, “A Retrospective,” *Bell System Technical Journal*, vol. 57, no. 6, pp. 1947–1969, July–August 1978.
- **Ritchie, 1984a.** D. M. Ritchie, “The Evolution of the UNIX Time-Sharing System,” *AT&T Bell Laboratories Technical Journal*, vol. 63, no. 8, pp. 1577–1593, October 1984.
- **Ritchie, 1987.** D. M. Ritchie, “Unix: A Dialectic,” *USENIX Association Conference Proceedings*, pp. 29–34, January 1987.
- **Ritchie, 1984b.** D. M. Ritchie, “Reflections on Software Research,” *Communications of the ACM*, vol. 27, no. 8, pp. 758–760, 1984.
- **Ritchie, 2004.** D. M. Ritchie, *Documents on Unix System Laboratories Inc. versus Berkeley Software Design Inc.*, March 2004.
- **Ritchie et al., 1978.** D. M. Ritchie, S. C. Johnson, M. E. Lesk, & B. W. Kernighan, “The C Programming Language,” *Bell System Technical Journal*, vol. 57, no. 6, pp. 1991–2019, July–August 1978.
- **Rosler, 1984.** L. Rosler, “The Evolution of C—Past and Future,” *AT&T Bell Laboratories Technical Journal*, vol. 63, no. 8, pp. 1685–1699, October 1984.
- **Tanenbaum, 1987.** A. S. Tanenbaum, *Operating Systems: Design and Implementation*, Prentice-Hall, Englewood Cliffs, NJ, 1987.
- **Tuthill, 1985.** B. Tuthill, “The Evolution of C: Heresy and Prophecy,” *UNIX Review*, vol. 3, no. 1, p. 80, January 1985.
- **Wilson, 1985.** O. Wilson, “The Business Evolution of the UNIX System,” *UNIX Review*, vol. 3, no. 1, p. 46, January 1985.
- **X/OPEN, 1987.** X/OPEN, *The X/OPEN Portability Guide (XPG), Issue 2*, Elsevier Science, Amsterdam, Netherlands, 1987.
- [https://www.tuhs.org/Archive/Documentation/Unix_Review/unixreview_1985jan.pdf?utm_source=chatgpt.com](https://www.tuhs.org/Archive/Documentation/Unix_Review/unixreview_1985jan.pdf?utm_source=chatgpt.com)
- https://www.tuhs.org/
- https://www.ukuug.org/newsletter/
- https://www.usenix.org/publications/login/
- [Perez De Rosso, S., & Jackson, D. (2013). What’s wrong with git? A conceptual design analysis. Proceedings of the 2013 ACM International Symposium on New Ideas, New Paradigms, and Reflections on Programming & Software, 37–52.](Perez%20De%20Rosso,%20S%20,%20&%20Jackson,%20D%20(2013)%20What%E2%80%99s%20wro%20178598edb79080668cf3d129fa8a0792.md)
- [‣](https://app.notion.com/p/3bcc0f5171ec80c2bf3acdde768399ec?pvs=21)
- [Mechanism](https://app.notion.com/p/Mechanism-305598edb79080f3b8d9d8fcda9b6d94?pvs=21)
- Accetta, M. J., Baron, R. V., Bolosky, W. J., Golub, D. B., Rashid, R. F., Tevanian, A., & Young, M. W. (1986). Mach: A new kernel foundation for UNIX development. *Proceedings of the Summer 1986 USENIX Conference*, 93–113.
-
