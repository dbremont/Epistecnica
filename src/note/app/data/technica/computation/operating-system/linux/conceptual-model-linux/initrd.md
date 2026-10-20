---
tags: [initialization]
---

# initrd

- [Init System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/init-system.md)

> The **"initrd" method** (Initial RAM Disk) is a technique  used in **Linux boot processes** to load a temporary root filesystem into  memory during the system's startup.
> 

> The `initrd` is a small filesystem image that is loaded into memory by the bootloader (e.g., GRUB, SYSLINUX, or directly by QEMU).
> 

> It contains essential files, drivers, and tools needed to initialize the system and mount the actual root filesystem.
> 

> The "initrd" (initial RAM disk) method is a technique used in the boot process of Linux and other Unix-like operating systems. It involves loading a temporary root file system into memory (RAM) during the system's startup. This temporary file system contains essential drivers, tools, and scripts needed to mount the actual root file system and complete the boot process.
> 

QA:

- …

## **How It Works**

- During boot, the bootloader (e.g., GRUB) loads both the kernel and the initrd image into memory.
- The kernel unpacks the initrd image into a **RAM-based file system** and uses it as its initial root file system.
- The initrd contains scripts and utilities to detect hardware, load necessary kernel modules, and prepare the system to mount the real root
file system.
- Once the real root file system is mounted, the **initrd is discarded**, and the system switches to the actual root file system.

## **Types of initrd**

- **Traditional initrd**: A compressed file system image (e.g., `initrd.img`) that is loaded into memory and used as a temporary root file system.
- **initramfs**: A more modern approach that replaces the traditional initrd. It is a
compressed CPIO archive that is directly integrated into the kernel image or loaded separately. It is more flexible and efficient than the traditional initrd.

## Reference

- https://en.wikipedia.org/wiki/Initial_ramdisk
- …