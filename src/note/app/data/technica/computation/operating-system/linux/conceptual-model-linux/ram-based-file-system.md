---
tags: [storage]
---

# Ram Based File System

- [initramfs](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/initramfs.md)

> A **RAM-based file system** is a volatile storage mechanism that utilizes a portion of the system's **Random Access Memory (RAM)** to create a temporary file system, enabling high-speed read and write operations by storing files and directories directly in memory rather than on persistent storage devices. It is typically implemented using **tmpfs** or **ramfs** in Linux and provides fast access to data but loses all contents upon system shutdown or reboot due to the volatile nature of RAM.
> 

## References

- https://en.wikipedia.org/wiki/Tmpfs
- https://wiki.debian.org/ramfs
- https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html