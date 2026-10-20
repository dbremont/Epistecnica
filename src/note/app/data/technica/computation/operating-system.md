# Operating System

> An **operating system** is a privileged, event-driven, resource-managing software layer that abstracts, schedules, and mediates access to hardware and system resources (CPU, memory, I/O, devices) for concurrently executing user and kernel-space processes through a combination of protected mode execution, system calls, interrupt handling, and virtual memory management.
> 

> An Abstract note - on **Operating System**.
> 

> A **conceptual map** for parsing the elements related to operations systems, production systems, and operational processes.
> 

> Our study of the **OS Systems** will be organized in terms of the study of ([Linux](note.html?n=technica/computation/operating-system/linux.md)).
> 

> **Note:** A useful way to study a computer system from the ground up is by using a virtualization system like [QEMU (Quick Emulator)](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/qemu-quick-emulator.md).
> 

## Formulation

> How a OS is structure? What is the abstract template?
> 

### What type of technical element is a `OS`?

> A Technical System is an organized set of interacting Technical Objects, relationships, mechanisms, and interfaces that collectively realizes one or more Technical Functions within an operational environment.
> 

> An **Operating System is an organized Technical System** composed of interacting software components, mechanisms, and interfaces that collectively manage computational resources, control program execution, and provide services to other software and users.
> 

> See more in [Philosophia Artium Technicarum et Operis](https://app.notion.com/p/Philosophia-Artium-Technicarum-et-Operis-355c0f5171ec808b82f8d7a85e8134cd?pvs=21).
> 

### Which are ideas that can ground the study of OS Systems?

- Technical Problem
    - **Technical Specification**
    - **Technical Capability: What can this system enable an agent to do?**
- Hardware
- Hardware Abstract Layer
    - Hardware Abstract Module
- **Technical Interface:** How can the consumer access the service?
    - **Technical Service:** What capability does the system make available to consumers?
- **Technical Mechanism:** How is the capability technically realized?
- Technical Module:  A **structural unit** that organizes implementation.
- Technical Layer:  A structural level within a technical system that groups technical elements according to their **architectural position, implementation boundary, and relationship to other technical elements**.

### How should an Operating System be mapped onto a Technical Ontology?

> See 🌐.
> 

## Firmware

> Actually firmware ( [**Firmware**](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/firmware.md)) it’s the software that intermediates the interaction with the hardware.
> 

> Alongside firmware there are also the drivers.
> 

## Kernel

> **Kernel:** $K : H \rightarrow H_{vm}$ is the privileged system component that transforms the physical hardware substrate $H$ into a (**projection layer of H**) -  abstract machine $H_{vm}$ capable of program execution,  where $H$ means **Hardware**, and $H_{vm}$ means **Hardware Model**.
> 

> The only goal of the OS kernel is to construct a virtual computational substrate from hardware and expose it to user applications in a way that enables safe, concurrent, and abstract computation without requiring direct interaction with physical devices - they also implement many other functionality (like virtualization, monitoring mechanism, etc) but this are secondary.
> 

> How to model the **Hardware**?
> 

> How to formulate the $H_{vm}$? How does it **abstracts hardware**?
> 

> How is  $H_{vm}$ implemented?
> 

### Abstract Machine Interface

> What is the structure  of the `Abstract Machine Interface` exposed by the OS? Which are the elements? How are they used?
> 

| **Interface Element** | **Description** | **Semantics (What it provides)** | **Reference Implementation** |
| --- | --- | --- | --- |
| Process / Thread | Execution abstraction of a program | Independent flow(s) of execution with scheduling context | `task_struct`, PCB, kernel stack, context switch logic, scheduler queues |
| Virtual Address Space | Per-process memory abstraction | Continuous, isolated memory model | MMU, page tables, `mm_struct`, TLB, paging subsystem |
| System Calls | Controlled entry points into kernel | Safe invocation of privileged operations | syscall instruction (trap), syscall table, dispatcher, ABI layer |
| Files / File Descriptors | Uniform I/O abstraction | Device-independent data access model | VFS layer, `file`, `inode`, `dentry`, FD table per process |
| Signals / Events | Asynchronous notification mechanism | Interrupt-like communication to processes | signal subsystem, `sigaction`, pending signal queues, interrupt delivery paths |
| IPC (pipes, sockets, queues) | Inter-process communication channels | Data exchange between isolated processes | pipe buffers, UNIX domain sockets, message queues, shared memory (shm), networking stack |
| Scheduling Abstraction | Execution time-sharing model | Illusion of parallel execution | scheduler (CFS or similar), runqueues, timer tick, load balancing |
| Device Abstractions | … | … | … |
| Time Abstraction | Logical system time | Monotonic or wall-clock time | hardware timers (TSC/APIC), timekeeping subsystem, `ktime`, `jiffies`, clocksource |
| Permissions / Protection Model | Security abstraction layer | Access control over resources | UID/GID model, capability system, ACLs, LSM (SELinux/AppArmor), MMU privilege rings |

### Abstract Machine Implementation

> How is the abstract machine implemented? Which are the techniques, mechanisms - that is implementation elements? What is there role  Which set of interface element does they support?
> 

| **Category** | **Implementation Mechanism** | **Description** | **Supports Which Interface Elements** |
| --- | --- | --- | --- |
| **Scheduling** | Scheduler | Selects runnable execution contexts based on policy (CFS, RT, etc.), enforcing fairness, priority, and CPU allocation. | Processes, threads, scheduling abstraction |
| **Execution Control** | Context Switching | Saves/restores CPU state (registers, stack, MMU context) between execution contexts. | Process abstraction, thread abstraction |
| **Memory Management** | MMU + Page Tables | Hardware-assisted translation from virtual to physical memory addresses. | Virtual address space |
| **Control Transfer** | Trap/Interrupt Handler | Entry point for asynchronous events and synchronous traps into kernel mode. | System calls, signals, hardware events |
| **System Interface** | System Call Dispatcher | Routes syscall numbers to kernel service routines. | System calls |
| **File Abstraction** | VFS (Virtual File System) | Uniform interface over heterogeneous filesystem implementations. | File abstraction, file descriptors |
| **Hardware Abstraction** | Device Drivers | Translate kernel I/O requests into device-specific operations. | Device abstractions |
| **Interrupt Management** | Interrupt Controller (PIC/APIC) | Routes, prioritizes, and delivers hardware interrupts to CPU cores. | Signals, interrupts, timers |
| **Communication** | IPC Subsystem | Mechanisms for inter-process communication (pipes, queues, shared memory). | IPC abstractions |
| **Time Management** | Timer Subsystem | Provides system time, scheduling ticks, and time events. | Time abstraction, scheduler |
| **Protection Model** | Security Module (DAC/MAC) | Enforces discretionary and mandatory access control policies. | Protection model |
| **Privilege Model** | Kernel Mode / Privilege Levels | Hardware-enforced separation between user and kernel execution domains. | All system calls + hardware access |
| **Memory Management** | Virtual Memory Manager (VMM) | Manages address spaces, mappings, and memory isolation policies. | Process memory isolation, VM abstraction |
| **Fault Handling** | Page Fault Handler | Resolves invalid or missing memory accesses (demand paging, copy-on-write). | Virtual memory semantics |
| **Physical Memory** | Physical Memory Allocator (buddy/slab/slub) | Allocates and frees physical pages/objects efficiently. | Kernel memory allocation, buffering |
| **Storage I/O** | Block I/O Layer | Standardizes block device requests and request merging. | Disk/storage abstraction |
| **I/O Optimization** | I/O Scheduler | Orders and merges I/O requests for latency/throughput optimization. | Storage performance abstraction |
| **Caching** | Page Cache / Buffer Cache | Caches file and block data in memory to reduce I/O latency. | File system performance layer |
| **Direct Memory Access** | DMA Subsystem | Allows devices to read/write memory without CPU intervention. | High-performance I/O abstraction |
| **Networking** | TCP/IP Stack | Implements full network protocol stack (L2–L4 typically in kernel). | Network sockets abstraction |
| **Networking Hardware** | Network Device Subsystem | Manages NIC drivers and packet I/O pipelines. | Network interface abstraction |
| **Networking QoS** | Packet Scheduler (qdisc) | Controls queuing, shaping, and prioritization of network packets. | Network traffic control |
| **Signal Handling** | Signal Delivery Engine | Dispatches signals to processes/threads based on events. | Signal abstraction |
| **Synchronization** | Spinlocks | Busy-wait locks for short critical sections in kernel. | Concurrency control primitives |
| **Synchronization** | Mutexes / Semaphores | Blocking synchronization primitives for mutual exclusion and signaling. | Thread synchronization abstraction |
| **Synchronization** | RCU (Read-Copy-Update) | Lock-free read-mostly synchronization mechanism. | High-performance concurrent reads |
| **User-Kernel Boundary** | Futex | Fast user-space mutex with kernel fallback only on contention. | Lightweight thread synchronization |
| **Boot & Initialization** | Bootloader Interface | Transfers control from firmware/bootloader to kernel entry point. | System initialization |
| **Hardware Discovery** | Device Enumeration (ACPI/Device Tree) | Detects and describes hardware topology and devices. | Hardware model construction |
| **Bus Architecture** | PCI/Bus Subsystem | Manages device discovery, enumeration, and configuration over buses. | Device topology abstraction |
| **Timing Precision** | High-resolution timers (hrtimers) | Provides fine-grained timing events beyond system tick. | Timers, scheduling precision |
| **Time Coordination** | Time synchronization (NTP support in kernel/user) | Aligns system clock with external time sources. | System time consistency |
| **Virtualization** | Virtualization Layer (KVM/Xen interface) | Exposes hardware-assisted virtualization to guest OSes. | Virtual machines abstraction |
| **Containers** | Container primitives integration | Implements namespaces, cgroups, and isolation primitives. | Process isolation environments |
| **Security Hooks** | Security enforcement hooks (LSM hooks) | Pluggable security framework for enforcing policies (SELinux, AppArmor). | Security policy enforcement |
| **Interrupt Dispatch (Real Mode Legacy)** | Interrupt vector table (IVT) | A fixed memory-resident table at physical address `0x0000:0x0000` mapping interrupt numbers (0–255) to 16-bit far pointers (CS:IP). On `int n`, the CPU uses this table to transfer control to firmware/handler routines (typically BIOS in real mode). It is initialized by firmware and serves as the earliest hardware-software control transfer mechanism in x86 systems. | Hardware interrupts, BIOS services (e.g., video, disk), boot-time control transfer, legacy system calls |
| **Interrupt Dispatch (Protected/Long Mode)** | Interrupt Descriptor Table (IDT) | A CPU-managed table referenced via the `IDTR` register that maps interrupt vectors (0–255) to gate descriptors (interrupt/trap/task gates). Each entry encodes handler address, privilege level (DPL), segment selector, and type. Unlike IVT, it is not a flat pointer table but a protected descriptor structure enabling privilege separation and controlled entry into kernel mode. | Hardware interrupts, exceptions (page faults, divide error), system calls (via `int`, `syscall`, `sysenter` legacy paths), CPU traps, fault handling |
| **Display Output** | Framebuffer (fbdev) | Memory-backed pixel buffer representing a display surf. Writing bytes into this mapped memory changes pixels on screen. Historically exposed as `/dev/fb0`. | Display abstraction, pixel output, console graphics |
| **Display Mode Setting** | Kernel Mode Setting (KMS) | Controls display resolution, refresh rate, timings, and monitor configuration directly in kernel space. Replaced userspace mode setting in modern Linux graphics. | Display configuration, monitor output abstraction |
| **Graphics Memory Management** | GEM / TTM | Manages GPU memory objects such as textures, buffers, framebuffers, command buffers, and mappings between CPU/GPU memory domains. | GPU buffer abstraction, rendering resources |
| **Graphics Rendering Interface** | DRM (Direct Rendering Manager)  (API - That Drivers Must Implement) | Core kernel graphics subsystem managing GPUs, command submission, buffer sharing, synchronization, and display pipelines. | GPU abstraction, rendering devices, display pipeline |
| **Display Composition** | Display Controller / Scanout Engine | Hardware pipeline that reads framebuffer memory and converts it into a video signal sent to monitor connectors (HDMI, DisplayPort, eDP). | Final screen output |
| **Console Rendering** | Virtual Terminal (VT) / Framebuffer Console (`fbcon`) | Renders kernel text consoles onto framebuffer devices when no graphical server is running. | TTY display, terminal output |
| **2D/3D Acceleration** | GPU Driver Command Submission Engine | Builds and submits command streams to the GPU for rasterization, compositing, shaders, texture processing, etc. | Hardware graphics acceleration |
| **Media Processing** | Video4Linux (V4L2) | Kernel subsystem for camera/video capture, encoding/decoding pipelines, webcams, tuners, image sensors. | Video capture abstraction |
| **Audio Output** | ALSA Kernel Sound Subsystem | Low-level kernel framework for audio playback, recording, mixers, DMA audio buffers, codec drivers. | Audio device abstraction |
| **Audio Scheduling** | PCM Buffer Engine | Streams audio samples through ring buffers to hardware DACs using DMA. | Audio playback/recording streams |
| **Multimedia Synchronization** | DMA-BUF | Zero-copy shared buffer mechanism between GPU, display, video decoder, and other devices. | Shared multimedia buffers |
| **Hardware Video Decode/Encode** | Media Codec Driver | Kernel interface to hardware encoders/decoders (H.264, HEVC, AV1, VP9, etc.). | Video acceleration abstraction |
| **Input/Display Integration** | Input Subsystem + Evdev | Handles keyboards, mice, touchscreens, stylus devices feeding events to graphical systems. | Interactive multimedia I/O |
| **Display Composition (Userspace Interface)** | Wayland/DRM Buffer Presentation Path | Kernel exposes display buffers that compositors present to outputs using page flips and atomic commits. | Desktop graphics presentation |

### Hardware Model

> See more in [(Hardware) Physical Substrate](note.html?n=technica/computation/platform/hardware-physical-substrate.md).
> 

## Evaluation

> How to evaluate a OS?
> 

| Category | Metric | Description | Interpretation |
| --- | --- | --- | --- |
| Performance | Throughput | Number of tasks/processes completed per unit time (CPU, I/O, system calls). | Higher is better; indicates system capacity under load. |
|  | Latency | Time taken to complete a single operation (syscall, I/O request, scheduling decision). | Lower is better; reflects responsiveness. |
|  | Context Switch Overhead | Cost (time/CPU cycles) of switching between execution contexts. | Lower improves efficiency under multitasking. |
|  | CPU Utilization | Fraction of time CPU is actively executing useful work. | High is generally good, but must avoid saturation/overcommit. |
|  | I/O Throughput | Rate of disk/network/device data transfer. | Higher indicates efficient I/O subsystem design. |
|  | Memory Bandwidth Utilization | Effective usage of memory subsystem bandwidth. | High without thrashing indicates good memory management. |
|  | Cache Hit Ratio | Fraction of memory accesses served from cache (page cache, CPU cache effects). | Higher reduces latency and improves throughput. |
| Scalability | Multi-core Scaling Efficiency | Performance gain as CPU cores increase. | Near-linear scaling indicates low contention and good parallel design. |
|  | Lock Contention Rate | Frequency of synchronization conflicts (spinlocks, mutexes). | Lower indicates better concurrency design. |
|  | NUMA Efficiency | Performance locality across NUMA nodes. | Higher locality efficiency improves large-socket systems. |
|  | Max Concurrent Processes | Maximum stable number of processes/threads supported. | Higher indicates stronger kernel scalability. |
| Fairness | Scheduling Fairness Index | Measure of equitable CPU allocation across processes. | Balanced distribution avoids starvation. |
|  | Starvation Incidents | Occurrence of processes not receiving CPU/I/O time. | Zero is ideal. |
|  | Priority Inversion Frequency | Cases where low-priority tasks block high-priority ones. | Lower indicates correct scheduling + locking design. |
| Reliability | Crash Rate | Frequency of kernel panic, system crash, or hard freeze. | Lower indicates stronger stability. |
|  | Uptime | Continuous system operation time without reboot/failure. | Higher reflects system robustness. |
|  | Recovery Time | Time to recover from failure (crash, restart, service failure). | Lower improves resilience. |
|  | Fault Isolation Strength | Ability to contain faults within subsystems/processes. | Strong isolation reduces systemic failure propagation. |
| Memory Management | Page Fault Rate | Frequency of page faults per workload unit. | Lower (after warm-up) indicates efficient memory management. |
|  | Thrashing Index | Degree of excessive paging activity. | Lower is essential for stable performance. |
|  | Allocation Latency | Time to allocate kernel/user memory. | Lower improves responsiveness of all subsystems. |
| I/O System | Disk Utilization Efficiency | Ratio of useful I/O vs total issued I/O. | Higher means less wasted I/O operations. |
|  | Queue Depth Stability | Stability of I/O request queues under load. | Stable queues prevent latency spikes. |
| Networking | Packet Loss Rate | Fraction of packets dropped in transmission. | Lower indicates reliable network stack. |
|  | TCP Retransmission Rate | Frequency of retransmitted packets. | Lower implies better congestion control and stability. |
|  | Network Latency | Time for packet round-trip or delivery. | Lower improves interactive performance. |
| Security | Attack Surface Size | Number of exposed interfaces, syscalls, services. | Smaller reduces exploitability. |
|  | Privilege Escalation Incidents | Successful unauthorized elevation of privileges. | Zero is required for secure systems. |
|  | Policy Enforcement Accuracy | Correctness of DAC/MAC/LSM enforcement. | High accuracy prevents leakage or bypass. |
|  | Isolation Strength | Degree of containment between processes/users/containers. | Strong isolation is fundamental for multi-tenancy. |
| Energy Efficiency | Power Consumption | Energy used under defined workloads. | Lower is better for mobile/large-scale systems. |
| Energy Efficiency | Performance per Watt | Work completed per unit energy. | Higher indicates efficient resource utilization. |
| Usability (System Level) | System Responsiveness | Perceived delay in user-visible operations. | Lower improves user experience. |
| Usability (System Level) | Boot Time | Time from power-on to usable system state. | Lower is better for usability and embedded systems. |
| Determinism | Jitter | Variability in response times under repeated operations. | Lower is essential for real-time systems. |
| Determinism | Worst-case Latency | Maximum observed delay for critical operations. | Critical for RTOS guarantees. |

## System Space

[In](note.html?n=technica/computation/operating-system/in.md)

🌐

[xv6](note.html?n=technica/computation/operating-system/xv6.md)

[x86](note.html?n=technica/computation/operating-system/x86.md)

[seL4](note.html?n=technica/computation/operating-system/sel4.md)

[Linux](note.html?n=technica/computation/operating-system/linux.md)

[Mach](note.html?n=technica/computation/operating-system/mach.md)

[Plan 9](note.html?n=technica/computation/operating-system/plan-9.md)

[CTSS](note.html?n=technica/computation/operating-system/ctss.md)

[MINIX](note.html?n=technica/computation/operating-system/minix.md)

[Multics](note.html?n=technica/computation/operating-system/multics.md)

[Android](note.html?n=technica/computation/operating-system/android.md)

[Amoeba](note.html?n=technica/computation/operating-system/amoeba.md)

[MS-DOS](note.html?n=technica/computation/operating-system/ms-dos.md)

[FreeBSD](note.html?n=technica/computation/operating-system/freebsd.md)

[**Unikernel**](note.html?n=technica/computation/operating-system/unikernel.md)

[BSD Unix](note.html?n=technica/computation/operating-system/bsd-unix.md)

[**MS Windows**](note.html?n=technica/computation/operating-system/ms-windows.md)

[Unix (PDP-11)](note.html?n=technica/computation/operating-system/unix-pdp-11.md)

[OpenHarmony](note.html?n=technica/computation/operating-system/openharmony.md)

[**BusyBox Linux**](note.html?n=technica/computation/operating-system/busybox-linux.md)

[Linux Distribution](note.html?n=technica/computation/operating-system/linux-distribution.md)

## History Timeline

> See more in https://encyclopedia.pub/entry/32956.
> 

## Research Frontier

> See more in https://pk.org/articles/big-ideas-os.html
> 

## QA

### Are OS Disk related elements like page cache, and `I/O` scheduling managed by the file system, or are they independent kernel components?

File System:

```bash
User read()
  ↓
VFS (file system interface layer)
  ↓
File system (ext4, xfs)
  ↓
Page cache (memory subsystem)
  ↓
Block I/O layer
  ↓
I/O scheduler
  ↓
Driver
  ↓
Disk
```

### How does the OS used the Firmware? What is the role of the Firmware?

> 

### What is the relationship between Nvidea open source driver and DRM?

> 

## References

- https://github.com/dbremont/os-labs
- [Virtualization](note.html?n=technica/computation/platform/virtualization.md)
- [(Hardware) Physical Substrate](note.html?n=technica/computation/platform/hardware-physical-substrate.md)
- [‣](https://app.notion.com/p/368598edb79080918a2ad2e8f419e88e?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081bfa9b8ee29f0e3a6c5?pvs=21)