# QEMU (Quick Emulator)


> In this note we will render intelligible the Quick Emulator (QEMU).
> 

> **Note:** QEMU’s goals are realized through a set of executable tools such as `qemu-system-x86_64`, `qemu-img`, and `qemu-nbd`.
> 

> NOTE:  I AM NOT SASTIFY WITH THIS TECHNICAL ONTIC DECOMPOSITION -  MECHANISM, CAPABILTY,  TECHNICAL PRINCIPLE, ETC.
> 

QEMU (Quick Emulator): Conceptual Model

## Formulation

> How to organize the `conceptual map` of that renders QEMU intelligible? To render QEMU intelligible, you need a **multi‑layered conceptual map** that separates **what** the virtual machine is (its static definition) from **how** it behaves (dynamic emulation) and **how** it connects to host resources.
> 

> What is QEMU? QEMU is a software-defined hardware platform constructor capable of instantiating executable virtual machines by composing CPU models, memory maps, firmware, buses, and device emulations.
> 

> What is `QEMU` **main abstraction**?  The idea of a **Virtual Machine.**
> 

## Virtual Machine

> A **Virtual Machine (VM)** is a software-instantiated computer system that reproduces the structural and behavioral properties of a physical machine, allowing software to execute as if it were running on dedicated hardware.
> 

### Part Set

> **Virtual Device Set:** Collection of emulated peripherals available to the guest machine. Examples include disks, NICs, serial ports, USB controllers, GPUs, timers, etc.
> 

> **Virtual Input Devices:** Keyboard, mouse, tablet, serial console, or other input mechanisms attached to the guest.
> 

| **Category** | **Part** | **Description** |
| --- | --- | --- |
| Compute | **Virtual CPU (vCPU)** | Software-defined processor exposed to the guest system. Executes guest instructions either through emulation or hardware-assisted virtualization. Includes registers, privilege modes, interrupt handling, and ISA semantics. |
| Memory System | **Virtual Memory** | Addressable memory made visible to the guest. Simulates RAM, ROM, memory regions, and mappings used by programs, kernel, and devices. |
| Memory System | **Virtual Storage** | Emulated block storage presented as HDD, SSD, CD-ROM, or flash device. Often backed by host files such as `.qcow2` or raw disk images. |
| Network System | **Virtual Network Interface** | Emulated network adapter allowing packet exchange between guest and host/external network. |
| Graphics System | **Virtual Display Adapter** | Graphics output device exposed to the guest. May emulate VGA, VirtIO GPU, framebuffer, etc. |
| **Firmware** | **Virtual Firmware** | Boot firmware responsible for early initialization of the machine and transfer of execution to the bootloader or kernel. Examples: BIOS, UEFI, OpenBIOS, U-Boot. |
| Interrupt System | **Interrupt System** | Mechanism through which devices signal events to the CPU. Includes interrupt controllers and routing logic. |
| Time System | **Timer System** | Provides timekeeping, scheduling ticks, timers, and temporal signals used by the guest OS. |
| Runtime State | **Execution State** | Runtime state of the VM while running: CPU register values, RAM contents, device state, timers, interrupt queues, etc. |
|  | **Persistent Machine State** | State that can be saved/restored via snapshots, migration, suspend/resume, or checkpoints. |
| **Virtual Input Device** | Keyboard |  |
|  | … |  |
|  | … |  |

### Structural Set

| Element | Description |
| --- | --- |
| **Machine Topology** | Overall organization of the machine: which components exist and how they are connected. |
| **Memory Map** | Spatial organization of the guest address space. |
| **Interrupt Topology** | Routing structure for interrupts. |
| **Boot Order** | Ordered sequence used during startup to locate boot target. |
| **Device Attachment Model** | Defines where devices are mounted (PCI, USB, VirtIO, etc.). |
| **Machine Type** | Overall machine blueprint describing which devices exist and how they are wired together. Examples include `pc`, `q35`, `virt`, `raspi`. |
| **Virtual Bus Topology** | Internal interconnect structure that links CPU, memory, and devices. Defines communication paths between components. |

## Virtual Machine Interface

> The **Virtual Machine Interface** is the externally observable control and interaction layer of a virtual machine. It defines how users, tools, and orchestration systems construct, configure, control, and inspect the VM without directly manipulating its internal state.
> 

### Core Functionality Set

| Function | Description |
| --- | --- |
| **Machine Definition** | Specification of VM composition: CPU type, memory size, devices, firmware, topology. |
| **VM Creation (Instantiation)** | Allocation and construction of a virtual machine instance from a machine definition. |
| **Boot / Start Execution** | Transition from reset state into firmware execution and OS boot process. |
| **Stop / Shutdown** | Controlled termination of VM execution, preserving or discarding state. |
| **Reset** | Reinitialization of VM state to power-on condition. |
| **Suspend / Resume** | Pause execution while preserving runtime state, then restore execution. |
| **Snapshot** | Capture of full or partial machine state for later restoration. |
| **Migration** | Transfer of VM execution state to another host while maintaining continuity. |
| **Device Configuration** | Dynamic attachment, removal, or configuration of virtual devices. |
| **Resource Allocation Control** | Adjustment of CPU cores, memory size, and device limits (if supported). |
| **State Inspection** | Query of machine state (CPU registers, memory regions, device status). |

### Auxiliary  Functionality Set

> These are **non-essential but operationally important services** that support usability, observability, debugging, and integration.
> 

| Function | Description |
| --- | --- |
| **Monitoring** | Observation of performance metrics (CPU usage, I/O throughput, latency, memory pressure). |
| **Debugging Interface** | Access to low-level execution introspection (breakpoints, step execution, register inspection). |
| **Logging System** | Recording of VM events, device activity, and system messages. |
| **Console Access** | Text-based interaction channel (serial console, monitor interface). |
| **Graphical Output Interface** | Display redirection via framebuffer, SPICE, VNC, or host windows. |
| **Input Injection** | Injection of keyboard, mouse, or other input events into the VM. |
| **Network Bridging Control** | Configuration of how VM networking is connected to host or external networks. |
| **Device Hotplug Support** | Runtime insertion/removal of devices without reboot. |
| **Performance Tuning Controls** | Adjustments of scheduling, CPU pinning, caching, or emulation speed. |
| **Security Controls** | Isolation configuration, sandboxing, privilege separation, and device access restrictions. |

### Tool Set

| **Tool** | **Purpose** | **Use Cases** |
| --- | --- | --- |
| **qemu-system-<arch>** | Full system emulator for specific architectures (e.g., x86, ARM, RISC-V). | Running complete operating systems on emulated hardware. |
| **qemu-img** | Disk image manipulation tool. | Creating, converting, and managing disk images (e.g., qcow2, raw, vmdk). |
| **qemu-nbd** | Network Block Device (NBD) server for QEMU disk images. | Exporting QEMU disk images over the network. |
| **qemu-io** | Disk image inspection and testing tool. | Testing and debugging disk images. |
| **qemu-monitor** | Command-line interface to the QEMU monitor. | Interacting with a running QEMU instance (e.g., changing settings, taking snapshots). |
| **qemu-ga** | QEMU Guest Agent. | Communication between the host and guest for tasks like freezing filesystems or querying info. |
| **qemu-pr-helper** | Persistent reservation helper for SCSI devices. | Managing SCSI persistent reservations in virtualized environments. |
| **qemu-bridge-helper** | Helper for setting up network bridges. | Configuring network bridges for QEMU virtual machines. |
| **qemu-storage-daemon** | Daemon for managing QEMU storage features. | Providing storage services (e.g., NBD, vhost-user) to QEMU instances. |
| **qemu-keymap** | Keyboard mapping tool. | Configuring keyboard layouts for QEMU VMs. |
| **qemu-trace-stap** | SystemTap tracing tool for QEMU. | Tracing QEMU events and performance using SystemTap. |
| **qemu-edid** | EDID (Extended Display Identification Data) generator. | Generating EDID data for virtual displays. |
| **qemu-options** | Documentation for QEMU command-line options. | Understanding and configuring QEMU command-line parameters. |
| **qemu-kvm** | … | … |
|  |  |  |

### **Interaction Interface: qemu-system-<arch>**

> `qemu-system-x86_64  --help`
> 

> **Note:** The QEMU command-line interface is **not fully orthogonal**. It provides multiple syntactic mechanisms with overlapping functionality and different levels of abstraction, such as `-hda` and `-drive` for disks, and `-nic` and `-device` for networking. These options are not simply independent primitives; some are convenience or higher-level interfaces that configure underlying devices and subsystems.
> 

#### Option Set Category

| **Category** | **Description** | **Option Set** |
| --- | --- | --- |
| **Machine** | Select and configure the virtual machine platform and chipset. | `-machine` |
| **CPU** | Configure the virtual CPU model and features. | `-cpu`, `-smp` |
| **Memory** | Configure guest RAM and memory backing. | `-m`, `-mem-path`, `-mem-prealloc`, `-object` |
| **Acceleration** | Select hardware or software virtualization acceleration. | `-accel`, `-enable-kvm` |
| **Boot** | Control how and from where the guest boots. | `-boot`, `-kernel`, `-initrd`, `-append` |
| **Storage** | Configure virtual disks and block-storage backends. | `-drive`, `-blockdev`, `-cdrom`, `-hda`, `-hdb` |
| **Networking** | Configure virtual network interfaces and network backends. | `-nic`, `-netdev`, `-net`, `-device` |
| **Devices** | Add and configure virtual hardware devices. | `-device`, `-global`, `-usb`, `-usbdevice` |
| **Display** | Configure the guest graphical display. | `-display`, `-vga`, `-nographic`, `-curses` |
| **Remote Display** | Provide graphical access through remote-display protocols. | `-vnc`, `-spice` |
| **Console (Serial)** | Configure serial ports, parallel ports, and character-device backends. | `-serial`, `-parallel`, `-chardev` |
| **Monitor (Management)** | Configure QEMU's management and control interfaces. | `-monitor`, `-qmp` |
| **Audio** | Configure virtual audio hardware and audio backends. | `-audiodev`, `-device` |
| **Filesystem Sharing** | Share host filesystems with the guest. | `-fsdev`, `-virtfs` |
| **Firmware** | Configure BIOS, UEFI, and firmware-related storage. | `-bios`, `-pflash`, `-L`, `-fw_cfg` |
| **Clock (RTC)** | Configure the guest's real-time clock and time behavior. | `-rtc`, `-clock` |
| **Debugging** | Configure debugging, GDB access, startup state, and debug output. | `-s`, `-gdb`, `-S`, `-d` |
| **Snapshots** | Control temporary disk changes and VM snapshots. | `-snapshot`, `-loadvm` |
| **Runtime (Process)** | Control how the QEMU process itself runs. | `-daemonize`, `-pidfile`, `-no-reboot`, `-no-shutdown` |
| **Security (Isolation)** | Restrict QEMU's capabilities and resource behavior. | `-sandbox`, `-realtime`, `-overcommit` |
| **Device Defaults** | Control QEMU's automatically created devices. | `-nodefaults` |
| **Guest Identity** | Assign identity information to the virtual machine. | `-name`, `-uuid` |

#### Option Set Space

| **Flag** | **Purpose** | **Instance** |
| --- | --- | --- |
| **`-hda <file>`** | Specify the first hard disk image (IDE). | `-hda disk.img` |
| **`-hdb <file>`** | Specify the second hard disk image (IDE). | `-hdb disk2.img` |
| **`-kernel <file>`** | Specify a kernel image to boot. | `-kernel vmlinuz` |
| **`-drive <options>`** | Define a drive with specific options (e.g., `file`, `format`, `if`). | `-drive file=disk.img,format=qcow2,if=virtio` |
| **`-boot <order>`** | Set the boot order (e.g., `c` for hard disk, `d` for CD-ROM). | `-boot order=d` |
| **`-m <size>`** | Set the amount of RAM for the guest. | `-m 2048` (2 GB of RAM) |
| **`-cdrom <file>`** | Specify a CD-ROM image (IDE). | `-cdrom ubuntu.iso` |
| **`-smp <n>`** | Set the number of CPU cores. | `-smp 4` (4 CPU cores) |
| **`-initrd <file>`** | Specify an initial RAM disk (initrd) for the kernel. | `-initrd initrd.img` |
| **`-append <cmdline>`** | Pass kernel command-line arguments. | `-append "root=/dev/sda1 console=ttyS0"` |
| **`-netdev <type>,id=<name>,...`** | Configure a network backend. | `-netdev user,id=net0` |
| **`-device <driver>,...`** | Add a device to the guest (e.g., network card, USB device). | `-device e1000,netdev=net0` |
| **`-nographic`** | Disable graphical output and use the terminal for input/output. | `-nographic` |
| **`-curses`** | Use a text-based interface for the display. | `-curses` |
| **`-vga <type>`** | Specify the type of VGA card to emulate. | `-vga std` (standard VGA) |
| **`-display <type>`** | Specify the display backend (e.g., `sdl`, `gtk`, `none`). | `-display sdl` |
| **`-monitor <type>`** | Specify the monitor interface (e.g., `stdio`, `telnet`). | `-monitor stdio` |
| **`-serial <device>`** | Redirect the serial port to a device (e.g., `stdio`, `telnet`). | `-serial stdio` |
| **`-parallel <device>`** | Redirect the parallel port to a device. | `-parallel /dev/parport0` |
| **`-usb`** | Enable USB support. | `-usb` |
| **`-usbdevice <device>`** | Add a USB device (e.g., `mouse`, `tablet`). | `-usbdevice tablet` |
| **`-soundhw <model>`** | Enable sound hardware (e.g., `hda`, `ac97`). | `-soundhw hda` |
| **`-enable-kvm`** | Enable KVM (Kernel-based Virtual Machine) for hardware acceleration. | `-enable-kvm` |
| **`-cpu <model>`** | Specify the CPU model to emulate. | `-cpu host` (use the host CPU model) |
| **`-accel <type>`** | Enable an acceleration method (e.g., `kvm`, `tcg`). | `-accel kvm` |
| **`-s`** | Start a GDB server on port 1234. | `-s` |
| **`-gdb <device>`** | Start a GDB server on a specific device (e.g., `tcp::1234`). | `-gdb tcp::26000` |
| **`-S`** | Pause the CPU at startup (useful for debugging). | `-S` |
| **`-d <options>`** | Enable debug output (e.g., `cpu`, `int`, `mmu`). | `-d cpu,int` |
| **`-snapshot`** | Run in snapshot mode (changes to disk images are not saved). | `-snapshot` |
| **`-loadvm <snapshot>`** | Load a VM snapshot at startup. | `-loadvm snapshot1` |
| **`-net <type>,...`** | Configure a network interface (legacy option, prefer `-netdev`). | `-net user,hostfwd=tcp::2222-:22` |
| **`-fsdev <type>,...`** | Configure a file system device (e.g., `local`, `proxy`). | `-fsdev local,id=fs1,path=/shared,security_model=none` |
| **`-virtfs <options>`** | Configure a virtual file system (e.g., `local`, `proxy`). | `-virtfs local,path=/shared,mount_tag=host0,security_model=none` |
| **`-bios <file>`** | Specify a custom BIOS file. | `-bios bios.bin` |
| **`-pflash <file>`** | Specify a parallel flash image (e.g., for UEFI). | `-pflash uefi.img` |
| **`-L <path>`** | Specify the directory for BIOS, VGA BIOS, and keymaps. | `-L /usr/share/qemu` |
| **`-vnc <display>`** | Start a VNC server for remote display. | `-vnc :1` |
| **`-spice <options>`** | Enable SPICE remote desktop protocol. | `-spice port=5900,addr=127.0.0.1` |
| **`-rtc <options>`** | Configure the real-time clock (e.g., `base=utc`). | `-rtc base=utc` |
| **`-clock <options>`** | Configure the clock source (e.g., `rt`, `vm`). | `-clock rt` |
| **`-name <name>`** | Set the name of the guest (displayed in the window title). | `-name "My VM"` |
| **`-uuid <uuid>`** | Set the UUID of the guest. | `-uuid 550e8400-e29b-41d4-a716-446655440000` |
| **`-machine <options>`** | Select the emulated machine type and its properties (like virtualization acceleration, memory backends, or firmware). | -machine q35,accel=kvm |
| -nic <options> | Configure a complete virtual NIC and network backend in one option | -nic user,model=e1000 |
| -chardev <backend>,... | Define a character-device backend used by serial, monitor, etc. | -chardev stdio,id=char0 |
| -object <type>,... | Create an object such as a memory backend, iothread, secret, etc. | -object memory-backend-ram,id=mem1,size=4G |
| -mem-path <path> | Use a specific host memory backing path | -mem-path /dev/hugepages |
| -mem-prealloc | Preallocate guest memory | -mem-prealloc |
| -nodefaults | Disable QEMU's default devices | -nodefaults |
| -no-reboot | Do not automatically reboot after guest shutdown/crash | -no-reboot |
| -no-shutdown | Keep QEMU running after the guest shuts down | -no-shutdown |
| -daemonize | Run QEMU as a daemon | -daemonize |
| -pidfile <file> | Write QEMU's PID to a file | -pidfile qemu.pid |
| -qmp <device> | Configure the QEMU Machine Protocol interface | -qmp unix:qmp.sock |
| -monitor <device> | Configure the QEMU monitor | -monitor stdio |
| -serial <device> | Configure serial-port redirection | -serial stdio |
| -drive-mirror | Drive mirroring during operation | varies |
| -blockdev <options> | Define block-storage nodes explicitly | -blockdev driver=file,... |
| -audiodev <options> | Configure an audio backend | -audiodev driver=none,id=audio0 |
| -device <driver>,... | Instantiate a virtual device | -device virtio-net,netdev=net0 |
| -global <property=value> | Set global device properties | -global ICH9-LPC.disable_s3=1 |
| -fw_cfg <name>,... | Pass firmware configuration data | -fw_cfg name=opt/foo,string=bar |
| -bios <file> | Specify firmware/BIOS | -bios bios.bin |
| -pflash <file> | Attach a flash device/image | -pflash OVMF_VARS.fd |
| -kernel_irqchip <value> | Configure kernel interrupt-controller support | -kernel_irqchip on |
| -realtime <mlock=on|off> | Configure realtime behavior | -realtime mlock=on |
| -overcommit <options> | Configure host resource overcommit | -overcommit mem-lock=on |
| -sandbox <options> | Configure QEMU's sandbox restrictions | -sandbox on |

## Virtual Machine Implementation

> How is the virtual Machine Implemented?
> 

> A **Virtual Machine Implementation** is the set of mechanisms that realize a virtual machine model on a host system. It translates abstract machine definitions (CPU, memory, devices, firmware, topology) into executable behavior using emulation, virtualization, and host resource mapping.
> 

Were are  going to describe the implementation as a set of layers:

- **Model layer** → defines the machine
- **Execution layer** → runs it
- **Host layer** → grounds it in physical resources
- **Control layer** → manages lifecycle
- **State layer** → preserves continuity

### Which are the general mechanisms & implementation elements?

> Note: This are general - or mechanism that underlies the implementation of others mechanism in QEMU.
> 

| Mechanism (Element) | Description | Role in the System |
| --- | --- | --- |
| **VirtIO** | A **paravirtualized device interface specification** used between guest OS and hypervisor. Defines standardized “virtual devices” (net, block, rng, etc.) that avoid full hardware emulation. | Reduces device emulation overhead by letting the guest use optimized drivers instead of pretending to be real hardware. It is the **primary abstraction layer for fast virtual devices**. |
| **VFIO** | A **kernel framework for safe, userspace-controlled device passthrough**. It exposes physical PCI devices directly to a VM while enforcing isolation via IOMMU. | Enables near-native performance by giving the VM **direct access to real hardware devices** (GPU, NIC, NVMe). It is the core mechanism for **device passthrough virtualization**. |
| **IOMMU** | Hardware + kernel-managed **address translation unit for DMA operations** (e.g., Intel VT-d, AMD-Vi). Translates device DMA addresses into guest-allowed physical memory. | Provides **memory isolation and security boundary for VFIO and passthrough devices**, ensuring devices cannot access arbitrary host memory. |
| **vhost** | A **kernel offload backend for VirtIO devices**. Moves the datapath (especially networking/block I/O) from QEMU userspace into the kernel. | Improves VirtIO performance by eliminating userspace round-trips. It is a **performance accelerator for VirtIO, especially network and storage I/O**. |
| **vhost-user** | A **userspace protocol for implementing VirtIO backends outside QEMU**, typically used with DPDK or custom I/O servers. Communicates via Unix sockets or shared memory. | Enables **high-performance userspace I/O stacks** while still using VirtIO in the guest. Common in NFV (network function virtualization) and cloud dataplanes. |
| **Object Model (QOM)** | A C-based object system providing inheritance, composition, properties, and runtime typing for devices and machine components. | **Primary structural foundation of QEMU.** Enables hardware to be composed as an object graph (devices, buses, machines). Everything hardware-like is a QOM object. |
| **Accelerator Abstraction** | Pluggable interface selecting execution backend: TCG, KVM, HVF, WHPX. | Defines the **CPU execution substrate boundary**—decouples QEMU from specific virtualization hardware or DBT engines. |
| Device Model Framework | Implementation layer of virtual hardware devices (PCI, USB, storage controllers, NICs) built on QOM. | Encodes **hardware semantics (register behavior, interrupts, DMA logic)**. |

### How is the machine implemented?

Each “Part” is implemented by translating a **virtual abstraction into one of three mechanisms**:

- **Direct execution** (hardware virtualization for CPU)
- **Software simulation** (device + firmware emulation)
- **Mapping layer** (memory, storage, network, I/O bridging)

So the VM is not a single program—it is a **coordinated set of execution, emulation, and mapping subsystems layered over the host OS and CPU virtualization extensions**.

| **Part** | **Implementation** |
| --- | --- |
| **Virtual CPU (vCPU)** | Implemented via **hardware virtualization (KVM, HVF, WHPX)** or **dynamic binary translation (TCG)**. Maintains CPU state structures (registers, flags, MMU) and executes guest instructions either natively or through translation into host instructions. |
| **Virtual Memory** | Implemented using **host virtual memory mapping + address translation layer**. Guest physical memory is backed by host RAM regions; access is mediated via page tables, shadow paging, or EPT/NPT hardware support. |
| **Memory Map** | Implemented as a **memory region graph** (e.g., `MemoryRegion` tree) that maps guest physical addresses to RAM, ROM, or MMIO handlers. |
| **Virtual Storage** | Implemented via **block device layer** mapping virtual disks to host files or block devices (e.g., qcow2, raw images, LVM, NVMe passthrough). |
| **Virtual Network Interface** | Implemented via **network backends** such as TAP, bridge, socket, or user-mode networking. Packet processing is routed between guest NIC emulation and host networking stack. |
| **Virtual Display Adapter** | Implemented via **framebuffer emulation or GPU virtualization layers**, with rendering forwarded to host display systems (GTK, SDL, VNC, SPICE, VirtIO-GPU pipelines). |
| **Virtual Input Devices** | Implemented via **event injection subsystem**, mapping host input events (keyboard/mouse/touch) into guest device queues or interrupt signals. |
| **Virtual Firmware** | Implemented as **ROM image loading + execution redirection at reset vector**, with firmware binaries (BIOS/UEFI like SeaBIOS or OVMF) mapped into guest address space. |
| **Interrupt System** | Implemented using **virtual interrupt controllers (PIC/APIC/GIC models)** that route device events to vCPU interrupt lines and inject exceptions. |
| **Timer System** | Implemented using **host timers + virtual clock abstraction**, translating host time into guest time progression and scheduling periodic interrupts. |
| **Execution State** | Implemented as **in-memory runtime structures** holding CPU state, device state, and memory snapshots, continuously updated during execution cycles. |
| **Persistent Machine State** | Implemented via **serialization engine**, capturing CPU state, memory pages, device states, and timers into snapshot files for restore or migration. |
| **Machine Construction (Topology)** | Implemented via **object model + device graph (QOM-like system)** that instantiates CPUs, buses, and devices and connects them into a coherent system graph. |
| **Bus / Interconnect System** | Implemented as **device bus frameworks (PCI, USB, VirtIO, etc.)** managing address spaces, enumeration, and message routing between components. |
| Machine Initialization Model | Board-level system definition (chipset, memory map, firmware, devices, buses). |
| Main Event Loop (glib-based loop) | Central scheduler using epoll/poll/timers integrated with GLib. |
| Device Lifecycle System | Runtime mechanism for adding/removing CPUs, memory, PCI devices, and buses. |

### How is the structural layer implemented?

> The **structural layer** is the part of the VM system that *constructs and organizes the virtual machine as a coherent machine graph* before and during execution.
> 

> It does **not execute instructions directly**. Instead, it defines *what exists* and *how components are connected*.
> 

| **Element** | **Implementation** |
| --- | --- |
| **Machine Builder** | Implemented as a **configuration parser + instantiation engine** (e.g., QEMU CLI, libvirt XML, machine presets). It creates and wires all VM components at startup. |
| **Object Model (Component Graph)** | Implemented via an **object system (e.g., QOM - QEMU Object Model)** that represents CPUs, devices, buses, and memory regions as interconnected runtime objects. |
| **Device Model Framework** | Implemented as a **device abstraction API** where each device is a software object exposing standardized interfaces (MMIO handlers, IRQ lines, DMA callbacks). Often built on `qdev`-like frameworks. |
| **Memory Region System** | Implemented as a **hierarchical memory mapping tree** (e.g., `MemoryRegion` + `AddressSpace`) that maps guest physical addresses → host memory or device callbacks. |
| **Bus / Interconnect Graph** | Implemented as a **dynamic graph of bus objects** (PCI, USB, VirtIO, etc.) managing device attachment, enumeration, and address assignment. |
| **Machine Type Definition** | Implemented as a **predefined machine template / class registry** that encodes default topology, chipset configuration, and device layout (e.g., `pc`, `q35`, `virt`). |
| **Firmware Loader (Structural Role)** | Implemented as a **ROM mapping + image placement subsystem** that injects firmware binaries into memory regions and defines reset entry points. |
| **Interrupt Topology Definition** | Implemented as an **interrupt routing graph** connecting devices → interrupt controllers → CPUs (APIC/GIC models). |
| **Address Space Layout Engine** | Implemented as a **mapping compiler** that resolves overlapping memory regions, assigns MMIO windows, and builds final guest physical layout. |
| **Device Attachment System** | Implemented as a **plug-in graph construction mechanism** that connects devices to buses using slots, ports, and capabilities (PCI slots, USB ports, VirtIO channels). |
| **Dependency Resolver (Initialization Order)** | Implemented as a **topological initialization scheduler** ensuring devices are created and linked in correct dependency order (CPU → memory → chipset → devices). |

### How is the host integration layer implemented?

> This layer connects the virtual machine to real hardware and OS resources.
> 

| Component | Description |
| --- | --- |
| **CPU Thread Mapping** | Maps vCPUs to host threads. |
| **Memory Allocation Layer** | Allocates host RAM regions backing guest memory. |
| **Block Device Backend** | Maps virtual disks to files, partitions, or raw block devices. |
| **Network Backend** | Connects virtual NICs to TAP, bridge, NAT, or socket networks. |
| **Graphics Backend** | Routes display output to GTK, SDL, VNC, SPICE, etc. |
| **Input Backend** | Maps host input devices to guest input channels. |

### How is the control  interface Implemented?

> This layer controls execution and lifecycle.
> 

| Mechanism | Description |
| --- | --- |
| **VM Monitor Interface (QMP/HMP)** | External control protocol for VM operations. |
| **Lifecycle Controller** | Handles start, stop, reset, pause, resume. |
| **Snapshot Engine** | Serializes and restores full VM state. |
| **Migration Engine** | Transfers execution state between hosts. |
| **Hotplug Manager** | Dynamically adds/removes devices during runtime. |

### Dependency Set

> QEMU (Quick Emulator) has various dependencies that vary depending on the features and target platforms you want to support. Here’s a general table of the key dependencies for building and running QEMU:
> 

| **Dependency** | **Description** | **Required for** |
| --- | --- | --- |
| **GCC** | The GNU Compiler Collection, used for compiling QEMU. | Essential for building QEMU. |
| **Make** | A build automation tool. | Used to compile QEMU from source. |
| **pkg-config** | Helps in checking the availability of libraries. | Used for detecting dependencies like libglib2.0, libpixman, etc. |
| **glib2** | A low-level core library that provides data structures and utilities. | Required for QEMU's internal operations (e.g., event loops, memory management). |
| **libpixman** | A library for low-level pixel manipulation. | Required for graphics acceleration in QEMU. |
| **zlib** | Compression library. | Required for file compression (e.g., for disk images). |
| **libssl** | Secure Socket Layer (SSL) and Transport Layer Security (TLS) libraries. | For encrypted connections in QEMU (e.g., TLS for VNC, HTTPS). |
| **SDL2** | Simple DirectMedia Layer 2, a cross-platform graphics library. | Used for graphical display output in QEMU (optional). |
| **GTK3** | A multi-platform toolkit for creating graphical user interfaces. | Used for QEMU's GUI (optional). |
| **Spice** | A remote desktop protocol used by QEMU for virtualized environments. | Required for enhanced graphical performance and remote access. |
| **libusb** | Library for USB device access. | Required for USB passthrough support in QEMU. |
| **libcurl** | A library for transferring data with URLs. | Used for network protocols (e.g., HTTP for firmware downloads). |
| **libfdt** | Device tree library. | Required for working with device trees, especially on ARM-based systems. |
| **libvirt** | A toolkit for managing virtualized platforms. | Provides integration with libvirt for VM management (optional). |
| **Cairo** | 2D graphics library for vector graphics. | Used for certain rendering and display features in QEMU. |
| **libncurses** | A library for creating text-based user interfaces. | Used for the QEMU monitor interface and text-based VM management. |
| **bzip2** | Compression library, faster than zlib in some cases. | Used for compressed disk image formats. |
| **python3** | Python is often used for scripting QEMU-related tasks (e.g., device models, tests). | Required for some scripting tasks and building the test suite. |
| **systemd** | System and service manager for Linux systems. | Optional for managing QEMU as a service on Linux systems. |

| **Library** | **Purpose** |
| --- | --- |
| **TCG (Tiny Code Generator)** | QEMU's built-in Just-In-Time (JIT) translation engine for translating guest code to host instructions. |
| **glib** | General utilities like data structures, event loops, and memory management. |
| **libffi** | Foreign Function Interface for calling C functions dynamically. |
| **zlib** | Compression support (e.g., for disk images). |
| **libpixman** | Pixel manipulation (used for graphical output in QEMU). |
| **SDL or GTK** | Graphical frontend support for QEMU GUI. |
| **SPICE** | Enhances remote desktop performance for virtual machines. |
| **libusb** | USB passthrough support. |
| **liburing** | Async I/O handling with io_uring (optional). |
| **capstone** | Disassembly framework used in some QEMU builds for debugging. |
| **lzo / zstd** | Compression for disk image formats (e.g., QCOW2). |
| **GMP & Nettle** | Cryptographic operations for TPM and other security features. |
| **LLVM (optional)** | Some builds use LLVM for JIT optimizations. |
| **libslirp** | User-mode networking support. |
| **meson & ninja** | Modern build system used by QEMU. |

## Practice

> 

### Scope

> What QEMU can do?
> 

> The **scope of QEMU** defines the full set of capabilities it provides as a system-level machine constructor, emulator, and virtualization runtime.
> 

> See  [Virtual Machine Interface](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/qemu-quick-emulator.md).
> 

### Use Set

| **Use Case** | **Description** |
| --- | --- |
| **Full System Emulation** | It emulates an entire computer system, including CPU, memory, and peripherals. |
| **User-Mode Emulation** | Runs programs compiled for one architecture on another architecture. |
| **Virtualization** | Acts as a hypervisor to run virtual machines (VMs) on x86 hardware. |
| **Debugging and Development** | Enables debugging of operating systems, firmware, and user-space programs. |
| **Firmware Development** | Emulates hardware for firmware development (e.g., BIOS, UEFI). |
| **Embedded Systems Development** | Emulates embedded systems for development and testing. |
| **Security Research** | Provides a sandboxed environment for analyzing malware and vulnerabilities. |
| **Education and Training** | Used in academic settings to teach operating systems, computer architecture. |
| **Cross-Platform Testing** | Tests software on multiple architectures without requiring physical hardware. |
| **Cloud and Virtualization** | Used as a backend for cloud platforms and virtualization tools (e.g., KVM). |
| **Custom Hardware Simulation** | Simulates custom hardware configurations for research and development. |

### Limit Set

> The **Limit Set of QEMU** defines the fundamental boundaries on what the system can accurately represent, execute, or simulate. These limits arise from physics (host hardware), abstraction (model fidelity), and implementation constraints (software architecture).
> 

```bash
QEMU Limit Set =
  (No cycle-accurate hardware simulation)
+ (No physical/electrical modeling)
+ (Host-dependent execution constraints)
+ (Partial device coverage)
+ (Performance vs fidelity tradeoffs)
```

## QA

### Is the `Firmware` part of the `Virtual Machine` - or the Implementation Layer?…

> 

### What types of `-kernel` can QEMU load?

| Type | Case | Works with `-kernel` |
| --- | --- | --- |
| ELF kernel | `vmlinux` | ✔ yes |
| Linux x86 compressed | `bzImage` | ✔ yes |
| ARM kernel | `Image` | ✔ yes |
| Raw binary | `kernel.bin` | ⚠ architecture-specific |
| Multiboot ELF | `kernel.elf` | ✔ yes |
| ISO / disk images | `*.iso`, `*.qcow2` | ❌ no |

### What is the difference between **qemu-system-<arch>’**'s `-drive` and `-hda` options, and when should I use one instead of the other?

> In QEMU, **`-hda`** is a legacy convenience option that attaches an image as the first virtual hard disk, while **`-drive`** is the modern, more explicit option that lets you specify properties such as the image file, format, interface, and device configuration. For example, `-drive file=freebsd.qcow2,format=qcow2` is preferred because it explicitly declares the disk image and its format.
> 

### Which are the options of the   **qemu-system-<arch>’**s `-drive` command?

| Option | Meaning | Use |
| --- | --- | --- |
| `file` | Disk-image filename | `file=disk.qcow2` |
| `format` | Image format | `format=qcow2` |
| `if` | Interface/bus type | `if=virtio` |
| `media` | `disk` or `cdrom` | `media=cdrom` |
| `index` | Device index | `index=0` |
| `readonly` | Make drive read-only | `readonly=on` |
| `cache` | Host caching mode | `cache=none` |
| `snapshot` | Use temporary snapshot | `snapshot=on` |
| `discard` | Discard/TRIM behavior | `discard=unmap` |

## References

- https://www.qemu.org/
- https://gitlab.com/qemu-project/qemu
- https://qemu-project.gitlab.io/qemu/system/gdb.html
- https://zserge.com/posts/kvm/
- https://qemu-project.gitlab.io/qemu/about/index.html
- https://wiki.qemu.org/Documentation/Architecture
- [KV M HOST IN A FEW LINES OF CODE](https://zserge.com/posts/kvm/)
- Bellard, Fabrice. “QEMU, a fast and portable dynamic translator.” USENIX annual technical conference, FREENIX Track. Vol. 41. 2005.
- Bartholomew, Daniel. “Qemu: a multihost, multitarget emulator.” Linux Journal 2006.145 (2006): 3.
- Guillon, Christophe. “Program instrumentation with qemu.” 1st International QEMU Users’ Forum. Vol. 1. 2011.
- Sampath, Pradyumna, and B. Rachana Rao. “Efficient embedded software development using QEMU.” 13th Real Time Linux Workshop. 2011.
- Bugnion, Edouard, et al. Hardware and software support for virtualization. Morgan & Claypool, 2017.
- Smith, Jim, and Ravi Nair. Virtual machines: versatile platforms for systems and processes. Elsevier, 2005.
- Smith, James E., and Ravi Nair. “The architecture of virtual machines.” Computer 38.5 (2005): 32-38.
- Spinellis, Diomidis, and Georgios Gousios. Beautiful architecture: leading thinkers reveal the hidden beauty in software design. " O’Reilly Media, Inc.", 2009.
- [DynamoRIO](https://github.com/DynamoRIO/dynamorio)
- [Frida](https://frida.re/)
- [Ghidra](https://ghidra-sre.org/)
- https://www.qemu.org/docs/master/devel/index-tcg.html
- [xv6](note.html?n=technica/computation/operating-system/xv6.md)
- [KVM](note.html?n=technica/computation/platform/virtualization/virtualization-conceptual-model/kvm.md)
- [**Firmware**](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/firmware.md)
- [Linux Virtualization Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-virtualization-stack.md)
- [GDB (GNU Project Debugger)](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger.md)
- https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF
- https://www.qemu.org/docs/master/user/main.html