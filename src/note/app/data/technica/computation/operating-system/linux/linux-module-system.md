# Linux Module System


> The "Linux Module System" consists of dynamically loadable kernel modules that allow functionality to be added to the operating system kernel without needing to reboot or recompile the kernel, enhancing flexibility and efficiency by loading drivers and extensions as needed.
> 

> The **Linux Module System** is a crucial aspect of the Linux kernel, allowing for dynamic loading and unloading of modules at runtime. This system enhances flexibility and modularity, which is particularly useful for managing device drivers, file systems, and network protocols without requiring a full system reboot.
> 

> **Module: Loadable kernel** objects can be loaded and unloaded into the kernel as needed, extending its functionality without the need for a reboot.
> 

QA:

- …
- How to **interact** with a **kernel module**?
- How to know which kernel modules are being used?

## List of Kernel Module(s)

| Module | Description | Approx. Introduction |
| --- | --- | --- |
| **zram** | Compressed RAM-based block device (swap in RAM) | ~3.14+ |
| **zswap** | Compressed swap cache in RAM before disk swap | ~3.11+ |
| **zcache** | Deprecated compressed cache layer | ~3.x (experimental era) |
| **ext4** | Default Linux journaling filesystem | ~2.6.28 |
| **ext3** | Older journaling filesystem | ~2.4–2.6 era |
| **xfs** | High-performance scalable filesystem | ~2.4+ |
| **btrfs** | CoW filesystem with snapshots | ~2.6.29 |
| **vfat** | FAT32/FAT16 filesystem support | Early Linux (2.0+) |
| **ntfs** | Windows NT filesystem driver (read/write improved over time) | ~2.6+ (stable write later) |
| **nfs** | Network File System client/server | Early Linux |
| **cifs/smbfs** | Windows SMB/CIFS network filesystem | ~2.6+ |
| **overlay** | Overlay filesystem (container layers) | ~3.18 |
| **fuse** | Filesystem in userspace bridge | ~2.6.14 |
| **loop** | Loopback block device (files as disks) | Early Linux |
| **dm_mod** | Device mapper (LVM, crypt, snapshots) | ~2.6+ |
| **cryptd** | Crypto offload daemon | ~2.6+ |
| **aesni_intel** | AES-NI hardware crypto acceleration | ~3.x |
| **kvm** | Kernel-based virtual machine core | ~2.6.20 |
| **kvm_intel / kvm_amd** | CPU-specific virtualization support | ~2.6.20 |
| **vboxdrv** | VirtualBox kernel driver | external module |
| **e1000** | Intel gigabit Ethernet driver | ~2.4+ |
| **e1000e** | Newer Intel NIC driver | ~2.6.27 |
| **igb** | Intel server NIC driver | ~2.6+ |
| **ixgbe** | 10GbE Intel NIC driver | ~2.6+ |
| **r8169** | Realtek Ethernet driver | ~2.6+ |
| **iwlwifi** | Intel Wi-Fi driver | ~2.6.27+ |
| **ath9k** | Atheros Wi-Fi driver | ~2.6.27+ |
| **brcmfmac** | Broadcom Wi-Fi (fullmac) driver | ~3.x |
| **snd_hda_intel** | Intel HD Audio driver | ~2.6+ |
| **snd_usb_audio** | USB audio support | Early |
| **usbcore** | Core USB subsystem | Early |
| **xhci_hcd** | USB 3.0 controller driver | ~2.6.31+ |
| **ehci_hcd** | USB 2.0 controller driver | ~2.6+ |
| **ohci_hcd** | USB 1.1 controller driver | Early |
| **uhci_hcd** | Intel USB controller driver | Early |
| **i915** | Intel integrated GPU driver | ~2.6+ |
| **amdgpu** | AMD GPU driver (modern) | ~4.2+ |
| **radeon** | Legacy AMD GPU driver | ~2.6+ |
| **nvidia (nouveau)** | Open-source NVIDIA driver | ~2.6.33 |
| **nvidia proprietary** | NVIDIA closed driver | external |
| **drm** | Direct Rendering Manager core | ~2.6+ |
| **evdev** | Input event subsystem | ~2.6+ |
| **hid** | Human Interface Device core | Early |
| **usbhid** | USB keyboard/mouse support | Early |
| **i2c-core** | I2C bus subsystem | Early |
| **spi-core** | SPI subsystem | ~2.6+ |
| **gpio** | General Purpose IO framework | ~2.6+ |
| **rtc** | Real-time clock subsystem | Early |
| **watchdog** | System watchdog timers | Early |
| **thermal** | Thermal management framework | ~2.6+ |
| **intel_pstate** | Intel CPU frequency scaling | ~3.9+ |
| **cpufreq** | CPU frequency scaling core | ~2.6+ |
| **acpi** | ACPI power management | ~2.6+ |
| **battery** | Laptop battery subsystem | Early |
| **snd** | ALSA sound core | ~2.6+ |
| **bluetooth** | Bluetooth stack | ~2.6+ |
| **btusb** | Bluetooth USB transport | ~2.6+ |
| **nf_conntrack** | Netfilter connection tracking | ~2.6+ |
| **iptables/x_tables** | Packet filtering framework | ~2.4–2.6 |
| **nftables** | Modern packet filtering | ~3.13+ |
| **ip_tables** | Legacy firewalling | Early |
| **bridge** | Ethernet bridging | Early |
| **bonding** | NIC bonding/teaming | ~2.4+ |
| **tun/tap** | Virtual network interfaces | Early |
| **veth** | Virtual Ethernet pairs (containers) | ~2.6.24 |
| **macvlan** | Virtual MAC interfaces | ~2.6+ |
| **ipv6** | IPv6 protocol stack | ~2.4+ |
| **tcp_bbr** | BBR congestion control | ~4.9 |
| **sch_fq_codel** | Queueing discipline | ~3.5+ |
| **md_mod** | Software RAID (MD) | Early |
| **raid0/1/5/6** | RAID personalities | Early |
| **nvme** | NVMe SSD driver | ~3.3+ |
| **ahci** | SATA AHCI controller | ~2.6+ |
| **sd_mod** | SCSI disk driver layer | Early |
| **scsi_mod** | SCSI core subsystem | Early |
| **libata** | SATA/ATA subsystem | ~2.6+ |
| **sr_mod** | SCSI CD-ROM driver | Early |
| **loop** | Loopback device driver | Early |
| **mac80211** | Wi-Fi stack core | ~2.6.22+ |
| **cfg80211** | Wireless configuration API | ~2.6.30+ |

## Module Management Commands

> 

| **Command** | **Function** | **Usage Example** |
| --- | --- | --- |
| **`lsmod`** | Displays currently loaded kernel modules. | `lsmod` |
| **`modprobe`** | Adds or removes modules from the Linux kernel, handling dependencies. | `modprobe <module_name>` |
| **`insmod`** | Inserts a module into the Linux kernel without handling dependencies. | `insmod <path_to_module>` |
| **`rmmod`** | Removes a module from the Linux kernel, assuming no active dependencies. | `rmmod <module_name>` |
| **`modinfo`** | Displays information about a kernel module. | `modinfo <module_name>` |

## Capability

> 

Here’s the table with an added **structure** to show what types of **data structures** or **interfaces** may be involved in the functionality of each kernel module. This gives a more detailed breakdown of what elements you might work with in the kernel module development.

| **Functionality** | **Description** | **Examples** |
| --- | --- | --- |
| **Device Drivers** | Manages communication with hardware devices. | - Block Device Drivers (HDDs, SSDs)  - Character Device Drivers (Mouse, Keyboard) |
| **File System Modules** | Implements file systems or adds support for different types. | - NTFS, exFAT, Btrfs, ext4 drivers |
| **Memory Management** | Manages memory allocation and virtual memory handling. | - Custom memory allocators  - Page fault handlers |
| **System Calls** | Adds new system calls to the kernel. | - Custom system calls for new functionality |
| **Inter-process Communication (IPC)** | Provides mechanisms for communication between processes. | - Message queues, semaphores, shared memory |
| **Scheduler Modules** | Customizes the process scheduler to modify task scheduling policies. | - Real-time scheduling  - Custom task schedulers |
| **Security Modules** | Implements or enhances security features in the kernel. | - SELinux, AppArmor, Cryptographic algorithms |
| **Networking and Protocols** | Implements or modifies networking protocols and device drivers. | - TCP/UDP protocols, firewall rules, network interface drivers |
| **Interrupt Handling** | Handles hardware interrupts and manages communication between the kernel and devices. | - IRQ handlers for mouse, keyboard, network devices |
| **Power Management** | Implements power-saving features for the kernel. | - CPU frequency scaling, device power state transitions |
| **Hardware Abstraction Layers (HAL)** | Provides an abstraction layer for interacting with hardware. | - Drivers for custom hardware  - Virtualization modules |
| **Event Handling and Logging** | Handles system events and logs specific actions. | - Event handling for device hot-plug  - Logging system events |
| **Timers and Delayed Work** | Implements timers and deferred tasks within the kernel. | - Periodic tasks  - Delayed work queues |
| **Custom Hardware Interfaces** | Interfaces with custom or non-standard hardware. | - I2C/SPI communication  - GPIO handling |
| **System Resource Management** | Manages resources like CPU, memory, and devices. | - CPU load balancing  - Resource usage tracking |
| **Virtualization Support** | Provides support for running virtual machines or containers. | - KVM, Xen, Docker modules |

## Limits

> **Kernel Data Structure Access**: Modules typically interact with kernel data structures and functions. These structures can change with kernel updates, making modules dependent on the specific kernel version.
> 

> **Kernel Address Space Layout Randomization (KASLR)**: Modern kernels use KASLR to randomize kernel memory addresses, which can make it difficult for modules to locate critical kernel structures (such as the syscall table or interrupt descriptor table) unless KASLR is disabled.
> 

> ??
> 

## References

- https://linux-kernel-labs.github.io/refs/heads/master/labs/kernel_modules.html
- https://en.wikipedia.org/wiki/Loadable_kernel_module