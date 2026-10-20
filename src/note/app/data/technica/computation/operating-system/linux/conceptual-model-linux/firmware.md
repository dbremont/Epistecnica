---
tags: [firmware]
---

# Firmware

- [Boot Firmware Subsystem](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/boot-firmware-subsystem.md), [Booting (Initialization)](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/booting-initialization.md)

> In this note we will explore a class of software, firmware software.
> 

> Firmware is very low-level software that provides an abstraction and control layer over a hardware component.
> 

> **Note:** The term **Firmware Layer** refers to the aggregate set of firmware present in a computer system, comprising the firmware associated with each hardware component.
> 

## How is firmware related with the elements (components) of a computer system?

```bash
Computer System
│
├── CPU
│    └── microcode
│
├── Motherboard
│    └── BIOS / UEFI
│
├── GPU
│    └── GPU firmware
│
├── SSD / HDD
│    └── storage controller firmware
│
├── NIC
│    └── network adapter firmware
│
├── Keyboard / Mouse
│    └── peripheral firmware
│
├── Embedded Controller
│    └── EC firmware
│
└── TPM
     └── security firmware
```

## Is `firmware` a unit - or they are many firmware systems in one computer system?

> A computer typically contains **multiple firmware systems**, not a single one.
> 

## How does the kernel or other software talks to firmware?

| Firmware | Interaction Actor Set | Interaction Description |
| --- | --- | --- |
| UEFI / BIOS | Kernel ↔ platform firmware | Through firmware-defined runtime interfaces, boot tables, configuration structures, and platform service calls. The kernel reads information such as memory maps, ACPI tables, SMBIOS data, and may invoke runtime services like time, variable storage, or reboot. |
| Microcode | Kernel ↔ CPU firmware | Through CPU instructions or model-specific registers (MSRs). The kernel may load microcode updates during boot and control processor behavior via privileged instructions. |
| GPU firmware | GPU driver ↔ GPU firmware | Through MMIO registers, command submission queues, DMA descriptors, mailbox protocols, or firmware command processors. The driver sends commands; firmware schedules and executes internal GPU operations. |
| SSD firmware | Storage driver ↔ SSD firmware | Through storage protocols such as SATA, AHCI, or NVMe. The OS issues commands like read/write/flush; the controller firmware translates them into flash operations. |
| NIC firmware | Network driver ↔ NIC firmware | Through device registers, DMA rings, interrupts, admin queues, or command mailboxes. The driver configures the device and exchanges packet buffers. |
| Embedded controller firmware | Kernel / ACPI subsystem ↔ EC | Through ACPI EC interfaces, I/O ports, or vendor-specific controller commands. Used for battery state, thermal sensors, fan control, lid switches, etc. |
| USB peripheral firmware | USB stack ↔ device firmware | Through USB protocol transactions (control transfers, bulk transfers, interrupt transfers). |
| TPM firmware | Kernel / security subsystem ↔ TPM | Through TPM command protocols over LPC, SPI, I²C, or memory-mapped interfaces. |

## Can a component’s firmware be changed or updated? How?

> What is flashing? **Flashing** is the process of **writing new firmware into a device’s non-volatile memory**.
> 

| **Component** | **Change Status** | **Description** |
| --- | --- | --- |
| UEFI / BIOS | Yes — commonly updatable | Updated by “flashing” a new firmware image to the motherboard’s SPI flash chip. Usually done from the firmware setup utility, a vendor updater tool, or a bootable USB image. |
| Microcode | Yes — partially updatable | CPU microcode can often be patched by the firmware during boot or loaded by the operating system early in startup. Usually temporary unless stored by platform firmware. |
| GPU firmware / VBIOS | Yes | Updated using vendor flashing tools or driver-distributed firmware packages. Common for bug fixes, compatibility, or performance tuning. |
| SSD firmware | Yes | Updated via SSD vendor tools or OS utilities. Usually improves stability, controller behavior, or fixes data-handling bugs. |
| NIC firmware | Yes | Updated through vendor tools or operating-system firmware loaders. Common in servers and enterprise networking hardware. |
| Embedded controller firmware | Yes | Usually updated together with laptop/motherboard firmware. Controls battery, fans, keyboard, thermal logic, etc. |
| TPM firmware | Sometimes | Some TPM implementations support firmware updates through vendor utilities; many are tightly controlled because of security requirements. |
| USB peripheral firmware (keyboard, mouse, webcam, etc.) | Sometimes | Depends on the device. Many modern peripherals allow firmware updates through vendor software. Some are fixed at manufacture. |
| Simple fixed-function controllers | No or rarely | Some components contain firmware stored in mask ROM and cannot realistically be updated after manufacturing. |

## Which security exploits target firmware, and how are they carried out?

| Exploit Class | Target Firmware | High-Level Mechanism | Description |
| --- | --- | --- | --- |
| Bootkit | UEFI / BIOS | Firmware image modification | Malicious code is inserted into platform firmware so it executes before the OS during boot. |
| SPI flash overwrite | Motherboard firmware | Unauthorized reflashing | Attacker replaces or alters firmware stored in the motherboard flash chip. Often requires privileged access or a platform protection failure. |
| Persistent firmware implant | Device firmware (GPU / NIC / SSD) | Malicious firmware replacement | A device’s onboard firmware is modified to create persistence below the OS layer. Survives reinstalling the operating system. |
| Secure Boot bypass | UEFI boot chain | Trust-chain subversion | The attacker interferes with signature verification or abuses misconfiguration so unauthorized code loads during boot. |
| Option ROM abuse | PCI/PCIe device firmware | Malicious pre-boot device code | Expansion devices expose boot-time code (Option ROM) executed by firmware before the OS loads. |
| Microcode abuse / microarchitectural exploitation | Microcode | CPU behavior manipulation or hardware vulnerability abuse | Targets CPU internal behavior, speculative execution, or processor control paths. |
| Embedded controller compromise | EC firmware | Reprogramming embedded controller logic | Attacker targets battery/fan/keyboard controller firmware to gain persistence or covert hardware control. |
| Storage firmware implant | SSD firmware | Controller firmware modification | Malicious firmware alters controller behavior beneath the file system and block layer. |
| Network adapter firmware compromise | NIC firmware | Malicious firmware or DMA misuse | Attacker abuses network controller firmware or privileged DMA capabilities. |
| Malicious firmware update channel | Any updatable firmware | Compromised updater / signed-package abuse | The firmware update path itself is abused to deliver malicious code. |
| Supply-chain firmware compromise | Any firmware-bearing device | Malicious firmware introduced before deployment | Device arrives already modified during manufacturing, assembly, or distribution. |
| Firmware rootkit | Multiple firmware layers | Persistent low-level implant | Long-lived malware embedded below the operating system and difficult to detect from software alone. |

## In which type of hardware is the firmware store?

> Firmware is usually stored in **non-volatile memory**, meaning memory that retains contents when power is removed.
> 

| **Component** | **Typical  Storage Mechanism** |
| --- | --- |
| Motherboard | SPI flash chip |
| CPU | internal ROM / microcode storage |
| GPU | onboard flash ROM |
| SSD | controller flash / embedded flash |
| NIC | EEPROM or flash |
| Keyboard / mouse | microcontroller internal flash |
| Router | NOR/NAND flash |

## How to  to map the system components and it’s Firmware in Linux?

| Component | Linux tool | Firmware type |
| --- | --- | --- |
| Motherboard | `dmidecode` | BIOS / UEFI |
| CPU | `/proc/cpuinfo` | microcode |
| GPU | `dmesg`, `/lib/firmware` | GPU firmware blob |
| Wi-Fi | `dmesg` | `.ucode` |
| NIC | `ethtool`, `dmesg` | NIC firmware |
| NVMe SSD | `fwupdmgr` | SSD controller firmware |
| USB devices | `lsusb` | embedded firmware |
| Embedded Controller | `fwupdmgr` | EC firmware |
| Thunderbolt | `fwupdmgr` | controller firmware |

## References

- https://en.wikipedia.org/wiki/Firmware