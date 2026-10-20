---
tags: [initialization, storage]
---

# initramfs

- [Ram Based File System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/ram-based-file-system.md)

> Note: initramfs despide it’s name, is not a file system.
> 

> **initramfs** (Initial RAM File System) is a **cpio archive** containing a set of files, scripts, and utilities needed during the Linux boot process. When the kernel loads **initramfs**, it unpacks this archive into a **ramfs** or (or its more advanced counterpart, **tmpfs**) instance in memory, which serves as the temporary root filesystem (`/`). This **ramfs** provides the in-memory storage mechanism for the files and directories contained in **initramfs**, enabling the kernel to execute boot-critical tasks before transitioning to the real root filesystem.
> 

> **initramfs** is a **cpio archive**  (compressed using gzip, xz, or other compression algorithms) that is  embedded into or loaded alongside the Linux kernel image. It contains a  minimal set of utilities (e.g., `busybox`), kernel modules, and initialization scripts (`/init`) that are executed by the kernel in user space after the kernel has completed its own initialization.
> 

> The `init`  script is responsible for detecting hardware, loading necessary kernel  modules, and preparing the environment to mount the real root  filesystem. Once the real root filesystem is mounted, the `initramfs` is discarded, and the boot process transitions to the actual root filesystem's `init` system (e.g., `systemd` or `SysVinit`).
> 

QA:

- …

## Key Components

1. **cpio Archive**: A filesystem image packaged in the `cpio` format, often compressed.
2. **/init**: The initial user-space process executed by the kernel from the `initramfs`.
3. **Kernel Modules**: Drivers required to access storage devices or other hardware.
4. **Utilities**: Minimal tools (e.g., `busybox`) for device detection, filesystem mounting, and other boot-time tasks.
5. **Scripts**: Logic to handle complex storage setups, such as unlocking encrypted partitions or assembling RAID arrays.

## Workflow

1. **Bootloader Stage**: The bootloader loads the kernel and `initramfs` into memory.
2. **Kernel Initialization**: The kernel decompresses and unpacks the `initramfs` into a `tmpfs` (in-memory filesystem).
3. **User-Space Execution**: The kernel executes the `/init` script from the `initramfs`.
4. **Root Filesystem Preparation**: The `init` script loads necessary modules, detects hardware, and mounts the real root filesystem.
5. **Handover**: The `initramfs` is unmounted, and control is passed to the `init` system on the real root filesystem.

## Use Cases

- **Encrypted Root Filesystems**: Unlocking LUKS-encrypted partitions.
- **Complex Storage**: Handling LVM, RAID, or network-based root filesystems.
- **Hardware Detection**: Loading drivers for storage controllers or other critical hardware.
- **Custom Boot Environments**: Providing a minimal environment for recovery or system maintenance.

## Example

```bash
# Inspecting an initramfs image
mkdir /tmp/initramfs
cd /tmp/initramfs
zcat /boot/initramfs-linux.img | cpio -idmv

```

## References

- https://www.linuxfromscratch.org/blfs/view/svn/postlfs/initramfs.html