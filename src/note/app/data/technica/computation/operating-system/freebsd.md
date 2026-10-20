# FreeBSD

> FreeBSD is a **Unix-like operating system** derived from the Berkeley Software Distribution (**BSD**) and is developed as an open-source, **monolithic**, **preemptive**, and **multiprocessing-capable** kernel. It provides a **POSIX-compliant userland** and supports multi-threading, virtual memory, and a wide range of hardware architectures.
> 

## Technical Element Map

> How should the **technical system** “FreeBSD” be decomposed?
> 

| Technical Element | FreeBSD instances |
| --- | --- |
| **Technical Capability** | **Hardware management**; CPU management; CPU scheduling; processor topology management; memory management; physical-memory management; virtual-memory management; address-space management; process execution; thread execution; multitasking; scheduling; synchronization; **storage management**; block I/O; storage abstraction; disk management; filesystem management; file management; pathname management; mounting; **networking**; network communication; packet processing; routing; bridging; firewalling; network address translation; tunneling; network interface management; **audio**; audio capture/playback; **graphics/display**; GPU access; display management; rendering support; input-device management; keyboard; mouse; HID; **USB**; **Bluetooth**; PCI; ACPI; power management; thermal management; device management; device discovery; interrupt management; DMA; **virtualization**; virtual-machine execution; hardware-assisted virtualization; virtual CPU execution; virtual memory virtualization; virtual device emulation; **IPC**; pipes; FIFOs; Unix-domain communication; shared memory; message queues; signals; sockets; synchronization primitives; terminal communication; pseudo-terminals; **security**; authentication support; authorization; access control; credentials; privilege management; cryptography; integrity protection; auditing; mandatory access control; sandboxing/isolation; **jails**; resource isolation; resource accounting; process/resource limits; system boot; kernel loading; module loading; device initialization; system configuration; service initialization; system monitoring; performance monitoring; tracing; logging; accounting; system diagnostics; timekeeping; timers; clock management; user/account management; group management; session management; environment management; locale support; internationalization; random-number generation; entropy management; kernel debugging; crash handling; core dumps; system recovery; compatibility; binary execution; executable loading; shared-library loading; system administration; package/software management support; filesystem export; network service hosting; kernel extensibility |
| **Technical Interface** | **System calls**; POSIX API; C library interfaces; ABI; executable/binary interfaces; socket API; network socket interface; routing socket; packet-filter interface; `/dev`; `/proc`; `/sys` where applicable; `sysctl`; sysctl MIBs; `ioctl`; `kqueue`; `kevent`; signal interface; process-control interfaces; resource-limit interfaces; VFS interface; vnode interface; filesystem interfaces; mount interfaces; file-descriptor interface; device-driver interfaces; Newbus interfaces; kernel-module interfaces; kernel linker interfaces; CAM interfaces; GEOM interfaces; network-interface interfaces; network-stack interfaces; TTY interface; PTY interface; terminal interface; PTY master/slave interface; IPC interfaces; shared-memory interfaces; semaphore interfaces; message-queue interfaces; POSIX shared-memory interfaces; jail interfaces; MAC-framework interfaces; audit interfaces; crypto interfaces; random-device interface; timer interfaces; clock interfaces; tracing/profiling interfaces; debugging interfaces; virtualization interfaces; `/dev/vmm/*`; bhyvectl interfaces; VM management interfaces; configuration files; `rc.conf` interface; loader configuration interface; sysctl configuration interface; device configuration interface |
| **Technical Mechanism** | **CPU scheduling**; priority scheduling; load balancing; CPU affinity; context switching; thread dispatch; process creation; `fork`; `exec`; process termination; signal delivery; exception handling; trap handling; system-call dispatch; privilege-level transitions; virtual-memory translation; page tables; paging; page fault handling; copy-on-write; demand paging; memory mapping; memory allocation; kernel memory allocation; buffer management; caching; write-back; read-ahead; asynchronous I/O; synchronous I/O; interrupt handling; interrupt routing; interrupt threading; DMA; bus transactions; device discovery; device probing; device attachment; device I/O; character I/O; block I/O; storage queuing; storage scheduling; block transformation; storage layering; filesystem operations; pathname resolution; directory lookup; vnode operations; inode management; journaling; copy-on-write filesystems; snapshots; checksumming; compression; deduplication; replication; packet processing; protocol processing; routing; forwarding; packet filtering; firewall rule evaluation; NAT; socket buffering; congestion control; packet queuing; network interrupt processing; link-layer processing; synchronization; mutexes; spinlocks; rwlocks; condition variables; atomic operations; reference counting; credential checking; privilege checking; access-control enforcement; MAC policy enforcement; capability/resource accounting; resource limits; namespace/isolation mechanisms; jail enforcement; cryptographic primitives; key handling; entropy collection; random-number generation; logging; event tracing; accounting; performance counters; timer management; clock synchronization; module loading/linking; executable loading; dynamic linking; virtual-machine entry/exit; VM traps; VM exits; vCPU scheduling; guest-memory mapping; virtual interrupt injection; device emulation; virtual disk I/O; virtual network I/O |
| **Technical Module** | **Kernel core**; process subsystem; process-management subsystem; thread subsystem; scheduler; VM subsystem; physical-memory subsystem; memory allocator; IPC subsystem; signal subsystem; synchronization subsystem; syscall subsystem; executable-loader subsystem; dynamic-linking support; VFS; vnode subsystem; UFS; ZFS; NFS; NFS client/server; tmpfs; devfs; procfs; GEOM; CAM; storage subsystem; disk subsystem; ATA/SATA support; NVMe support; SCSI support; storage drivers; network stack; socket subsystem; routing subsystem; routing protocols; network-interface subsystem; Ethernet subsystem; wireless networking; firewall subsystem; packet-filter subsystem; bridge subsystem; VLAN subsystem; tunneling subsystem; USB subsystem; Bluetooth subsystem; PCI subsystem; ACPI subsystem; audio subsystem; sound drivers; DRM/graphics subsystem; GPU drivers; display subsystem; input subsystem; HID subsystem; keyboard subsystem; mouse subsystem; TTY subsystem; pseudo-terminal subsystem; console subsystem; device-driver framework; **Newbus**; bus subsystem; interrupt subsystem; DMA subsystem; power-management subsystem; thermal-management subsystem; crypto subsystem; cryptographic accelerators; random/entropy subsystem; MAC framework; jail subsystem; security subsystem; audit subsystem; credential subsystem; privilege subsystem; kernel module subsystem; kernel linker; virtualization subsystem; **VMM/bhyve subsystem**; vCPU subsystem; virtual-device subsystem; resource-accounting subsystem; resource-limit subsystem; timer subsystem; clock subsystem; timekeeping subsystem; logging subsystem; tracing subsystem; profiling subsystem; debugging subsystem; crash-dump subsystem; kernel configuration subsystem |
| **Technical Layer** | **Physical hardware**; CPU hardware; memory hardware; storage hardware; network hardware; GPU/display hardware; audio hardware; input hardware; USB hardware; PCI hardware; firmware; ACPI/UEFI firmware interfaces; boot firmware; **bootloader**; kernel-loading layer; hardware-abstraction layer; bus layer; device-driver layer; interrupt/DMA layer; kernel core; kernel subsystems; virtualization layer; system-call/interface layer; kernel-exposed device/interface layer; kernel-supported facilities; **FreeBSD base system**; system libraries; libc; runtime libraries; shared libraries; system utilities; command-line utilities; administrative utilities; daemons; service-management layer; configuration layer; initialization/rc layer; shell environment; userland; package-management layer; Ports Collection; third-party software; applications |
| **Constitutive Technical Object** | **Kernel**; CPU; CPU core; hardware thread; CPU topology; physical memory; memory page; physical frame; virtual address; virtual address space; page table; process; thread; credential; user; group; session; process ID; thread ID; file descriptor; file; directory; pathname; inode; vnode; filesystem; mount; mount point; disk; partition; slice; volume; block device; character device; storage controller; storage namespace; storage queue; bus; PCI device; USB device; Bluetooth device; network interface; network adapter; interface address; route; routing table; packet; frame; socket; socket buffer; connection; port; protocol endpoint; firewall rule; VLAN; tunnel; bridge; audio device; audio stream; graphics device; GPU; display; framebuffer; input device; keyboard; mouse; HID device; terminal; console; PTY; pipe; FIFO; shared-memory object; semaphore; message queue; signal; timer; clock; interrupt; interrupt vector; DMA buffer; kernel module; kernel object; jail; security credential; access-control rule; MAC policy; audit record; log record; trace event; performance counter; VM; vCPU; guest physical memory; guest virtual address space; virtual disk; virtual NIC; virtual console; virtual device; VM state; kernel configuration; system configuration; boot environment; kernel image; executable; shared library; daemon; system service |
| **Technical Artifact** | Kernel image; kernel module; device driver; executable; shared library; configuration file; `rc.conf`; loader configuration; sysctl configuration; filesystem image; disk image; VM image; boot environment; crash dump; core dump; log; audit record; trace; system database; account database; package; Ports build artifact |
| **Technical Resource** | CPU time; physical memory; virtual memory; address space; storage capacity; storage bandwidth; I/O bandwidth; network bandwidth; network address; network port; file descriptor; process ID; thread; kernel memory; DMA buffer; socket buffer; filesystem space; inode; ZFS dataset; ZFS pool; GEOM provider; device node; entropy; timer; VM; vCPU; guest memory; virtual disk; virtual network interface |
| **Technical Constraint** | CPU limits; memory limits; process limits; thread limits; file-descriptor limits; storage capacity limits; filesystem quotas; ZFS quotas; network bandwidth limits; socket limits; connection limits; jail resource limits; privilege restrictions; MAC policies; device-access restrictions; address-space limits; kernel configuration constraints; hardware compatibility constraints; driver constraints; ABI constraints; resource exhaustion constraints |
| **Technical Configuration** | Kernel configuration; device configuration; boot configuration; loader configuration; `rc.conf`; `sysctl.conf`; network configuration; interface configuration; routing configuration; firewall configuration; filesystem/mount configuration; storage configuration; ZFS configuration; jail configuration; user/group configuration; service configuration; power-management configuration; virtualization/VM configuration |
| **Technical Control Mechanism** | Kernel configuration; sysctl controls; resource limits; `rlimit`; quotas; jail controls; MAC policies; firewall rules; routing configuration; device permissions; filesystem permissions; ACLs; capabilities/privileges; scheduler controls; CPU affinity; VM controls; module loading/unloading; service startup/shutdown; system configuration; administrative commands |

## How to install FreeBSD  with QEMU?

```bash
## Install QEMU
sudo apt update
sudo apt install qemu-system-x86 qemu-utils
```

```bash
## Download FreeBSD
mkdir -p ~/qemu/freebsd/{iso,vm}
cd ~/qemu/freebsd/iso

wget https://download.freebsd.org/releases/amd64/amd64/ISO-IMAGES/15.1/FreeBSD-15.1-RELEASE-amd64-disc1.iso
```

```bash
## Create the virtual disk
cd ~/qemu/freebsd/vm
qemu-img create -f qcow2 freebsd.qcow2 20G
```

```bash
## Boot the installer
## How does (-nic user,model=e1000) works?
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=freebsd.qcow2,format=qcow2 \
    -cdrom ../iso/FreeBSD-15.1-RELEASE-amd64-disc1.iso \
    -nic user,model=e1000 \
    -boot d
```

```bash

### Boot the installed system
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=freebsd.qcow2,format=qcow2 \
    -nic user,model=e1000
```

```bash
## Use

qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=freebsd.qcow2,format=qcow2 \
    -nic user,model=e1000
```

```bash
# debug
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=freebsd.qcow2,format=qcow2 \
    -nic user,model=e1000 \
    -S -s

## No Graphic
qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=freebsd.qcow2,format=qcow2 \
    -nic user,model=e1000 \
    -nographic

qemu-system-x86_64 \
    -machine q35 \
    -m 4G \
    -smp 4 \
    -drive file=freebsd.qcow2,format=qcow2 \
    -nic user,model=e1000,hostfwd=tcp::2222-:22
    
## gdb
## Use  also gdb-multiarch
## kernel.debug can be extracted using ssh 
## (remember that in order ot use root - need to change the configs to allow it).

gdb
target remote :1234
set osabi none
file kernel.debug
```

## Does FreeBSD have a graphical shell?

> No—FreeBSD does not provide a graphical shell as a core OS facility; its native command interpreters (`sh`, `csh`, `tcsh`) are terminal-based, while graphical environments such as Xorg/Wayland plus KDE, GNOME, or Xfce run as separate userland components above the kernel and expose graphical terminal emulators rather than replacing the shell itself.
> 

## References

- https://www.freebsd.org/
- https://github.com/freebsd/freebsd-src
- [Berkeley Socket](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)
- [QEMU (Quick Emulator)](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/qemu-quick-emulator.md)