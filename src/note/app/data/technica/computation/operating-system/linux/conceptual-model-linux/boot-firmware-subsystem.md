---
tags: [firmware]
---

# Boot Firmware Subsystem

- [Firmware](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/firmware.md), [Booting (Initialization)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/booting-initialization.md)

> In this note we will explore the **Boot Firmware Subsystem.**
> 

> What type of software is the ‘**Boot Firmware Subsystem’? What is the interaction topology? Which are the instances of this class?**  How to characterized each instance?
> 

## What type of software is the ‘**Boot Firmware Subsystem’?**

> The **Boot Firmware Subsystem (BFS)** is a **low-level privileged system software subsystem** embedded in platform firmware.
> 

```bash
Physical hardware
↓
Boot Firmware Subsystem
↓
Bootloader / Operating System
```

## How to characterized a **Boot Firmware Subsystem (BFS)?**

| Property | Description |
| --- | --- |
| Architecture | x86 / ARM / RISC-V / Power |
| Storage medium | ROM / SPI flash / EEPROM |
| Startup CPU mode | real mode / protected mode / long mode |
| Initialization scope | CPU only / full platform |
| Boot mechanism | MBR / GPT / direct kernel |
| Execution model | monolithic / modular |
| Driver model | none / firmware drivers / extensible |
| Runtime services | yes/no |
| Security model | none / measured boot / secure boot |
| Extensibility | fixed / pluggable |
| Open vs proprietary | open-source / vendor-specific |
| Handoff protocol | boot sector / EFI / direct kernel handoff |

## **What is the interaction topology? What is the functional role?**

### Typical responsibilities include:

- CPU reset vector handling
- chipset bring-up
- DRAM initialization / memory training
- interrupt controller setup
- PCI / PCIe enumeration
- device discovery
- ACPI table generation
- SMBIOS exposure
- power-management initialization
- secure boot / trust validation
- selecting boot device
- loading next-stage boot software

### Interaction topology:

```bash
Power applied
   ↓
CPU reset
   ↓
Reset vector executes firmware
   ↓
Firmware initializes hardware
   ↓
Firmware discovers boot device
   ↓
Firmware loads bootloader / kernel image
   ↓
Control transferred to bootloader or kernel
```

## **Which are the instances of this class?**

| Instance | Description | Note |
| --- | --- | --- |
| BIOS | Legacy PC boot firmware responsible for POST, device initialization, and bootstrapping the OS | Traditional x86 firmware; executes in 16-bit real mode; commonly tied to MBR boot |
| UEFI | Modern modular firmware interface for platform initialization and OS loading | Current dominant firmware standard on PCs and servers; supports GPT, Secure Boot, runtime services |
| coreboot | Lightweight open-source platform firmware that performs hardware initialization and launches a payload | Often used as a replacement for vendor BIOS/UEFI; optimized for speed and openness |
| SeaBIOS | Open-source implementation of legacy BIOS interfaces | Frequently used as a payload with coreboot or in QEMU/KVM virtual machines |
| LinuxBoot | Firmware implementation where a Linux kernel executes as part of the boot firmware stage | Common in servers/datacenters; allows rich scripting and diagnostics during boot |
| Open Firmware | Firmware architecture based on a device-tree model and Forth interpreter | Historically used on SPARC, PowerPC, and older Apple systems |
| Das U-Boot | Widely used embedded boot firmware/bootloader for ARM and embedded systems | Common in SoCs, development boards, routers, and industrial hardware |
| EDK II | Open-source implementation framework for building UEFI firmware | Used by many vendors as a base for UEFI development |

## References

- https://en.wikipedia.org/wiki/BIOS
- https://en.wikipedia.org/wiki/UEFI
- How to replace the `firmware`?