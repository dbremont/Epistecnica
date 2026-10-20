---
tags: [initialization]
---

# Booting (Initialization)

- [GRUB: GNU GRand Unified Bootloader](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/grub-gnu-grand-unified-bootloader.md), [Boot Firmware Subsystem](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/boot-firmware-subsystem.md), [Firmware](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/firmware.md)

> In this note we will explore the booting (initialization)  process of a computer system.
> 

> **Booting (Initialization)** can be conceived as the staged initialization process in which a collection of hardware and firmware components cooperate to transform a powered hardware substrate into an operational execution environment capable of loading and running software.
> 

## Formulation

> Which are the stages of the booting process? Which are the elements that participates?
> 

| Stage | Description | Actor Set |
| --- | --- | --- |
| **Power Application** | Electrical power is applied to the platform and voltage rails stabilize. | Power supply unit (PSU), motherboard power circuitry, VRMs, CPU, RAM |
| **Reset Assertion / CPU Release** | CPU exits reset state and begins execution from the reset vector. | CPU, reset controller, chipset / platform controller |
| **Firmware Entry** | Platform firmware gains control and starts early machine initialization. | BIOS or UEFI, CPU |
| **POST / Hardware Self-Test** | Basic validation of CPU, RAM, timers, buses, and critical hardware presence. | Firmware, memory controller, CPU, chipset |
| **Platform Hardware Initialization** | Hardware controllers are configured into usable operational state. | Firmware, DRAM controller, interrupt controller, PCIe root complex, storage controllers |
| **Device Enumeration** | System scans buses and discovers connected devices. | PCI Express bus, USB controllers, SATA/NVMe controllers, firmware |
| **Memory Map Construction** | Physical address space is laid out; RAM, MMIO, reserved firmware regions are defined. | Firmware, CPU MMU structures, memory controller |
| **Boot Device Discovery & Selection** | Firmware determines where the executable boot payload lives. | UEFI/BIOS boot manager, storage device, network PXE stack |
| **Bootloader Loading** | Boot executable is copied into RAM and execution transfers to it. | GRUB / other bootloader, storage subsystem, firmware |
| **Kernel Loading** | OS kernel image and optional initramfs are loaded into memory. | Bootloader, kernel image, RAM |
| **Kernel Early Initialization** | Kernel establishes paging, interrupts, schedulers, allocators, and driver subsystems. | Linux kernel, CPU, MMU, interrupt controller |
| **Driver & Device Activation** | Kernel binds drivers to detected devices and activates them. | Kernel drivers, GPU, NIC, storage devices, USB devices |
| **Userspace Initialization** | First userspace process starts and system services are launched. | systemd / init process |
| **Operational State** | System becomes usable for interactive or service workloads. | Shell, desktop environment, daemons, user applications |

## **Bootloader (Kernel Loading Tool)**

> What is a Bootloader?  Why is the term ‘Bootloader’  semantics match the semantics of the parts boot and loader? What will be a better term?
> 

> A **bootloader** is the system software component responsible for loading an executable payload—typically an operating system kernel—into memory and transferring execution control to it.
> 

> A better term will be  a ‘Boot Transition Manager’ or a Kernel Launch Manager.
> 

> 
> 
> 
> **Bootloader = bootstrap loader -** a program that starts the machine startup sequence by loading the next executable stage (typically the operating system kernel) into memory and transferring control to it.
> 

### Function Set

> Which are the functions - roles of a bootloader?
> 

| Function | Description |
| --- | --- |
| **Payload Discovery** | Finds a bootable executable payload (usually a kernel image) in a boot medium such as disk, flash, USB, or network. |
| **Executable Loading** | Reads the kernel or next-stage program from storage and copies it into RAM. |
| **Memory Placement** | Places the loaded payload at the correct physical or virtual memory location expected by the executable format or architecture. |
| **Machine-State Preparation** | Configures the CPU into the required execution mode before handing off control (e.g. real mode → protected mode → long mode on x86). |
| **Memory Information Export** | Collects and passes the system memory map to the kernel (usable RAM, reserved regions, MMIO ranges, firmware regions). |
| **Hardware Context Passing** | Supplies platform metadata needed by the kernel such as ACPI tables, device tree blobs, SMBIOS data, framebuffer info, or boot services data. |
| **Kernel Parameter Injection** | Passes boot arguments / command-line parameters to the kernel. |
| **Initramfs / Initrd Loading** | Loads an auxiliary RAM disk containing early userspace files, drivers, or scripts needed before the root filesystem mounts. |
| **Execution Transfer** | Jumps to the kernel entrypoint and hands over CPU execution control. This is its defining operation. |
| **Boot Target Selection** | Chooses which operating system, kernel version, partition, or boot entry to execute. |
| **Configuration Parsing** | Reads boot configuration files, boot entries, kernel paths, timeout settings, etc. |
| **Filesystem Access** | Implements minimal filesystem readers to access files from FAT, ext4, ISO9660, etc. |
| **User Interaction / Boot Menu** | Presents menu UI allowing boot selection, recovery mode, alternate kernel choice, timeout selection, etc. |
| **Chainloading** | Loads another bootloader rather than directly loading a kernel. Common in multiboot setups. |
| **Integrity / Signature Verification** | Verifies cryptographic signatures or integrity of boot artifacts before execution (used in UEFI Secure Boot). |
| **Recovery / Rescue Booting** | Provides fallback boot paths when normal boot fails. |
| **Diagnostics / Debug Output** | Emits serial output, boot logs, error messages, or debug info during early startup. |

### Implementation Set

> Which are the implementation of the bootloader system concept?
> 

> **Bootloader** is a **functional concept**, while **GRUB**, **U-Boot**, **systemd-boot**, etc. are **concrete implementations** of that concept.
> 

| Bootloader System | Description | Note |
| --- | --- | --- |
| GRUB | General-purpose multistage bootloader used widely on Linux systems. Supports filesystems, menus, multiboot, kernel parameters, chainloading. | Most common on desktop/server Linux |
| systemd-boot | Minimal UEFI-native boot manager that loads EFI executables directly. | Common on modern UEFI Linux systems |
| U-Boot | Highly portable embedded bootloader used in embedded boards and ARM systems. | Dominant in embedded Linux |
| LILO | Early Linux bootloader that predates GRUB. Loads kernels from fixed disk sectors. | Historically important; mostly obsolete |
| SYSLINUX | Lightweight bootloader family for FAT filesystems, USB media, PXE, and live systems. | Common in installers/live USBs |
| rEFInd | Graphical UEFI boot manager for discovering and launching EFI boot entries. | Popular in multi-OS systems |
| Windows Boot Manager | Microsoft boot manager used to launch Microsoft Windows boot environments. | Standard on Windows |
| iPXE | Network bootloader capable of downloading boot images over HTTP, TFTP, iSCSI, etc. | Used in PXE/network boot |
| coreboot | Open-source firmware that performs platform initialization and often chains into a payload loader. | Firmware + boot-stage hybrid |
| Das U-Boot SPL | Tiny first-stage loader that initializes DRAM and loads full U-Boot. | Common in constrained embedded hardware |

## Booting Mechanism Set

> How to implement a bootloader?
> 

| Mechanism | Description | Usage |
| --- | --- | --- |
| **Entry Point Definition** | Defines the first instruction executed when firmware jumps into the bootloader. | Starting execution |
| **Executable Binary Format** | Binary layout understood by firmware or previous stage (raw binary, ELF, PE/COFF, etc.). | Packaging bootloader image |
| **Firmware Interface** | Mechanism for interacting with BIOS or UEFI services. | Console output, disk access, memory services |
| **CPU Initialization** | Setup of processor state before loading the next stage. | Register setup, stack setup, execution mode switching |
| **Stack Initialization** | Allocates and points the stack pointer to usable RAM. | Function calls, local variables |
| **Memory Addressing** | Mechanism to read/write physical memory. | Loading kernel into RAM |
| **Disk / Block I/O Access** | Reading sectors or files from storage media. | Load kernel image from disk/USB |
| **Filesystem Reader** | Parser for FAT, ext4, ISO9660, etc. | Reading `/boot` files |
| **Partition Parser** | Reads MBR/GPT metadata to locate partitions. | Selecting boot partition |
| **Executable Parser** | Parses kernel image format (ELF, bzImage, PE). | Extract kernel sections |
| **Memory Relocation** | Moves code/data to required runtime address. | Kernel placement |
| **Kernel Parameter Passing** | Passes command line/options to kernel. | `root=`, `console=`, debug args |
| **Boot Metadata Construction** | Provides memory map, framebuffer info, ACPI pointers, etc. | Kernel startup context |
| **Initramfs Loading** | Loads early RAM filesystem if used. | Early userspace |
| **Console Output** | Basic text output via serial/UART/framebuffer. | Debugging boot process |
| **Configuration Parsing** | Reads boot config file/menu entries. | Multi-boot or kernel selection |
| **Integrity Verification** | Optional hash/signature verification. | Secure boot / trusted boot |
| **Execution Handoff** | Final jump into kernel entrypoint. | Boot completion |

## References

- https://en.wikipedia.org/wiki/Bootloader
- https://en.wikipedia.org/wiki/GNU_GRUB
- https://en.wikipedia.org/wiki/Booting
- [http://wiki.osdev.org/System_Initialization_(x86)](http://wiki.osdev.org/System_Initialization_(x86))