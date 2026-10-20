# MS Windows

> Microsoft Windows is a **hybrid-kernel, NT-based, POSIX-incompatible** operating system designed for multi-user, multi-tasking environments. It implements **preemptive multitasking, virtual memory management, user-mode/kernel-mode separation, and a highly extensible driver architecture**.
> 

## **Kernel Architecture**

- **Hybrid Kernel**: Not purely monolithic or microkernel; combines monolithic performance with microkernel modularity.
- **Windows NT Kernel**:
    - **Executive Layer** (Handles memory management, process management, security, and I/O).
    - **Kernel Mode Subsystems** (Scheduler, dispatcher, synchronization, object manager).
    - **HAL (Hardware Abstraction Layer)** (Abstracts hardware differences).
- **Thread Scheduling**:
    - **Preemptive, priority-based scheduler** using **a 32-level priority system** (0–15 for user mode, 16–31 for real-time tasks).
    - **CPU affinity & NUMA-aware scheduling** for optimized multi-core processing.

## **Memory Management**

- **Virtual Memory**:
    - **Demand-paged virtual memory** with **copy-on-write (COW)**.
    - **Per-process 4GB (x86) or 128TB (x64) address space**.
- **Paging Mechanism**:
    - **Page Frame Number (PFN) database** tracks physical memory.
    - **Lazy allocation & trimming via working set manager**.
- **Memory Protection**:
    - **DEP (Data Execution Prevention)** – Hardware-enforced non-executable memory pages.
    - **ASLR (Address Space Layout Randomization)** – Mitigates memory-based exploits.
    - **VBS (Virtualization-Based Security)** – Isolates security-sensitive code in a hypervisor-protected region.

## **File System**

- **NTFS (New Technology File System)**:
    - **Journaling with redo/undo logs** for crash recovery.
    - **B+ tree directory structure** for efficient lookups.
    - **Transactional NTFS (TxF)** allows atomic file operations.
    - **Sparse files, reparse points, junctions, and symbolic links**.
- **Additional File Systems**:
    - **ReFS (Resilient File System)** for high-reliability storage.
    - **FAT32/exFAT** for legacy and removable media support.
    - **SMB, NFS, WebDAV support** for networked storage.

## **Security Model**

- **User-Mode & Kernel-Mode Separation**:
    - **Ring 3 (User Mode) & Ring 0 (Kernel Mode)**.
    - **Process isolation enforced via object-based security**.
- **Authentication & Access Control**:
    - **Access Control Lists (ACLs)** define fine-grained security permissions.
    - **LSA (Local Security Authority)** manages user authentication.
    - **SSPI (Security Support Provider Interface)** supports Kerberos, NTLM, and TLS.
- **Integrity Mechanisms**:
    - **UAC (User Account Control)** prevents unauthorized elevation.
    - **Secure Boot & TPM integration** ensure firmware integrity.
    - **BitLocker** provides full-disk encryption.

## **Process & Thread Management**

- **Processes & Threads**:
    - **Thread-based scheduling** (not process-based).
    - **Each process has at least one primary thread**; threads share memory space.
- **Inter-Process Communication (IPC)**:
    - **LPC (Local Procedure Call)** for fast intra-kernel messaging.
    - **Named pipes, shared memory, sockets** for cross-process communication.
    - **Job Objects** allow managing multiple processes as a unit.

## **Device & Driver Model**

- **Windows Driver Model (WDM)**:
    - Implements a **layered approach (User Mode <-> Kernel Mode <-> Hardware Abstraction Layer)**.
    - **IRP (I/O Request Packets)** propagate through driver stack.
    - **Plug and Play (PnP) & Power Management (ACPI-compliant)**.
- **Windows Driver Frameworks (WDF)**:
    - **Kernel-Mode Driver Framework (KMDF)**.
    - **User-Mode Driver Framework (UMDF)**.

## **Graphics & UI Subsystem**

- **DirectX Graphics Kernel (DXGK)**:
    - **Direct3D, Direct2D, WDDM (Windows Display Driver Model)**.
    - **Hardware-accelerated GUI rendering**.
- **Window Manager (DWM)**:
    - Uses **GPU-based composition** for rendering windows.
    - Implements **VSync, anti-tearing, and per-pixel alpha blending**.
- **User Interface Frameworks**:
    - **Win32 API** (low-level GUI operations).
    - **GDI+ (Graphics Device Interface)**.
    - **UWP (Universal Windows Platform)**.
    - **Windows Terminal supports GPU-accelerated text rendering**.

## **Networking Stack**

- **Winsock API**:
    - Supports **IPv4, IPv6, TCP, UDP, QUIC, and SCTP**.
- **Networking Features**:
    - **QoS (Quality of Service)** for traffic prioritization.
    - **SMB (Server Message Block) for file sharing**.
    - **Firewall & packet filtering via Windows Filtering Platform (WFP)**.
    - **VPN, IPsec, DNS-over-HTTPS (DoH)** support.

## **Virtualization & Containers**

- **Hyper-V**: Type-1 hypervisor for full virtualization.
- **Windows Sandbox**: Lightweight, disposable VM.
- **Windows Subsystem for Linux (WSL 2)**:
    - **Full Linux kernel running inside a Hyper-V VM**.
    - **Supports ELF64 binaries and system calls**.

## **Power Management**

- **ACPI-compliant power states**:
    - **S0 (Running), S1-S3 (Sleep states), S4 (Hibernate), S5 (Shutdown)**.
    - **Modern Standby (low-power instant-on mode)**.
- **Processor Power Management (PPM)**:
    - **Dynamic Voltage and Frequency Scaling (DVFS)**.
    - **Core Parking for reducing active cores on low-load systems**.

## **Software Packaging & Deployment**

- **Traditional EXE/MSI Installers**.
- **Microsoft Store/UWP Apps**.
- **Appx & MSIX Containerization**.
- **WinGet Package Manager** (CLI-based software management).

## **Crash Dump & Debugging Tools**

- **WinDbg & kd (Kernel Debugger)**.
- **Event Tracing for Windows (ETW)** for system-wide telemetry.
- **MiniDump & Full Kernel Dump Analysis**.

## **Supported Architectures**

- **x86 (32-bit, deprecated)**.
- **x86-64 (64-bit, primary target)**.
- **ARM64 (Windows on ARM)**.

## References

- https://en.wikipedia.org/wiki/Microsoft_Windows
- https://www.microsoft.com/en-us/software-download/windows11