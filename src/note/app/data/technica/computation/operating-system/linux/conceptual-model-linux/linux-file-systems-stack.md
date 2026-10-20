---
tags: [storage]
---

# Linux  File Systems Stack

- [Storage System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/storage-system.md)

> The **Linux File Systems Stack** is a modular and hierarchical system that facilitates file operations, from user-space requests down to physical disk I/O. It includes the **VFS**, **file system drivers**, **block layer**, **page cache**, and **storage device drivers**, each responsible for specific aspects of file management, storage access, and performance optimization. The stack ensures that different file systems can coexist and interact seamlessly within the Linux environment.
> 

## Terminology

| **Term** | **Description** | **Notes** |
| --- | --- | --- |
| **Mounting** | Process of making a filesystem accessible at a mount point in the directory tree. | `mount /dev/sda1 /mnt/data` |
| **Unmounting** | Detaching a mounted filesystem so it is no longer accessible. | `umount /mnt/data` |
| **Root File System (rootfs)** | Top-level filesystem mounted at `/` containing essential directories and files required for boot and operation. | `/bin`, `/etc`, `/lib` |
| **Mount Point** | Directory where a separate filesystem is attached (mounted). | `/home`, `/mnt/data` |
| **Device Node** | Special file under `/dev` representing a hardware device. | `/dev/sda`, `/dev/nvme0n1` |
| **Filesystem Type** | Format of a filesystem that defines how data is organized and stored. | `ext4`, `xfs`, `btrfs`, `vfat` |
| **Swap Space** | Area on disk or partition used as virtual memory extension when RAM is insufficient. | `/swapfile`, swap partition |
| **Block Device** | Device storing data in fixed-size blocks with random access capability. | SSD, HDD |
| **Character Device** | Device that streams data one character at a time. | `/dev/tty`, `/dev/random` |
| **Mount Options** | Parameters controlling how a filesystem is mounted. | `ro`, `rw`, `noexec`, `nosuid` |
| **Virtual Filesystem (VFS)** | Kernel abstraction layer allowing uniform access to different filesystem types. | Supports `ext4`, `xfs`, `ntfs` transparently |
| **Persistent Storage** | Storage that retains data after power-off. | SSD, HDD, Tape |
| **Volatile Storage** | Storage that loses data when powered off. | RAM |
| **Path** | Sequence of directory names used to locate a file or directory within the filesystem hierarchy. | Absolute: /usr/bin/python, Relative: ../documents/file.txt |
| **Path Resolution** | Process by which the kernel or VFS determines the actual inode corresponding to a given path. | Involves traversing directory entries and following symlinks; uses dentry and inode caches in VFS |
| **Inode** | Data structure used by the filesystem to store metadata about a file or directory (excluding its name or path). | Stores permissions, ownership, timestamps, file size, pointers to data blocks; every file has a unique inode number within a filesystem. |
| **File** | Abstract representation of a sequence of bytes stored on a filesystem, including its data and metadata. | Accessed via a file descriptor in user space; metadata stored in the inode; can be regular file, directory, device file, or special file. |
| File System | Method and data structures an operating system uses to control how data is stored, organized, retrieved, and managed on storage devices. | Provides hierarchical structure (directories, files, metadata); examples: `ext4`, `NTFS`, `FAT32`, `ZFS`. |
| **Partition** | Contiguous region of a storage device treated as a separate logical disk by the operating system. | … |

## Stack Structure

> What is the structure of the Linux File Stack?
> 

> The Linux File Stack is highly complex — a single file read or write triggers a **cascade of interactions across multiple layers**, from user-space libraries to system calls, through the Virtual File System, filesystem-specific drivers, block and I/O scheduling layers, and finally down to the hardware, with caches, locks, and metadata management silently coordinating in the background, making what appears to be a simple operation a **symphony of coordinated subsystems**.
> 

| **Category** | **Component** | **Description** |
| --- | --- | --- |
| **Application Layer** | User Applications | Programs (e.g., editors, shells, DBs) that access files via system calls. |
|  | Libraries | Standard libraries (e.g., glibc) providing file I/O functions like `fopen`, `read`, `write`. |
| **System Call Interface** | VFS API | Kernel interface that abstracts file operations (`open`, `read`, `write`, `close`) for user programs. |
| **Virtual File System (VFS)** | VFS Layer | Provides a unified interface to various filesystem types; manages inodes, dentries, and superblocks. |
|  | Dentries | Directory entries caching for quick path lookup. |
|  | Inodes | Metadata structures representing files (size, ownership, permissions, timestamps). |
|  | Superblocks | Metadata about the filesystem as a whole (type, size, status). |
| **Caching Layer** | Page Cache | Stores recently accessed file data in RAM to reduce disk I/O; used by VFS. |
| **Filesystem Drivers** | Ext4, XFS, Btrfs, NTFS, FAT, etc. | Implementations of specific filesystem types; handle on-disk structures and file operations. |
| **Block Layer** | Block Device Drivers | Drivers that interface with storage hardware (HDD, SSD, NVMe), handle read/write requests. |
|  | Buffer/Block Cache | Kernel caching layer for disk blocks to improve I/O performance. |
| **I/O Scheduling Layer** | I/O Scheduler | Manages and optimizes the order of block I/O requests (CFQ, BFQ, Deadline, NOOP). |
| **Physical Device Layer** | Storage Hardware | Actual disks or storage devices (HDD, SSD, NVMe, RAID arrays). |
|  | Device Controllers | Hardware controllers managing access to storage devices. |

## Implementation

> Which enabling abstractions support the implementation of key file system features (files, directories, etc.)?
> 

> Note: Other Enabling Abstraction are specify in the File Systems Implementation Itself.
> 

| **Abstraction** | **Role** | **What Enables?** |
| --- | --- | --- |
| **Hardware** | Actual disk or storage medium. | Enables **persistent storage of data and physical I/O operations**. |
| RAID | Combines multiple physical disks into a single logical unit with redundancy or performance benefits. | Enables fault tolerance, improved performance, and data redundancy. |
| **Block Device Layer** | Provides read/write access to raw storage blocks. | Enables **hardware-independent block I/O** and abstraction over different storage media. |
| **Page Cache (Buffer Cache)** | Caches file data and metadata in RAM to improve performance. | Enables **faster I/O, reduced disk access, and efficient memory utilization**. |
| **Partition** | Logical division of a physical disk, defined by the partition table (MBR/GPT). | Enables **separation of storage**, multiple OS installations, and independent management of data regions. |
| **Logical Disk (Volume)** | A partition formatted with a filesystem, treated as a logical storage unit by the OS. | Enables **flexible storage management**, resizing, snapshots, and logical abstraction over physical disks. |
| **Virtual File System (VFS)** | OS-level abstraction that provides a uniform interface to different file systems. | Enables **filesystem interoperability** and uniform file API for applications. |
| **File System** | Data structure that organizes and manages files within a volume. | Enables **file and directory organization, metadata management, access control, and efficient storage allocation**. |

### RAID

> **RAID** is a storage technology that combines multiple physical disks into a single logical unit to provide **redundancy, performance improvement, or both**. The OS and filesystem may see a RAID array as a single block device.
> 

### File System

> In Linux, a **File System** is a **structured method and set of data structures used by the kernel to manage how data is stored, organized, and accessed on storage devices**.
> 

> See more in [File System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/file-system.md).
> 

A **File System in Linux** is a **kernel-managed abstraction layer** that:

- Defines how data and metadata are laid out on disk (e.g., inodes, directories, superblocks).
- Provides a **hierarchical namespace** (directories and files) accessible under a single unified tree rooted at `/`.
- Exposes files as the universal interface (regular files, device files, sockets, pipes) following the **"everything is a file"** philosophy.
- Is accessed through the **Virtual Filesystem (VFS)** layer, which standardizes operations (`open`, `read`, `write`, etc.) across different filesystem implementations (ext4, xfs, btrfs, etc.).

## Secondary Storage Hardware

| **Category** | **Technology** | **Year** | **Description** | **Vendor(s)** |
| --- | --- | --- | --- | --- |
| HDD (Hard Disk Drive) | Magnetic storage | 1956 | Uses spinning magnetic disks to store persistent data; high capacity, slower access. | Seagate, Western Digital, Toshiba |
| SSD (Solid State Drive) | Flash-based storage | 1991 | Non-volatile NAND flash storage; faster access and lower latency than HDDs. | Samsung, Western Digital, Intel |
| NVMe SSD | High-speed storage | 2009 | Connects via PCIe for ultra-fast read/write performance. | Samsung, Intel, Western Digital |
| Hybrid Drive (SSHD) | Mixed storage | 2010 | Combines HDD capacity with SSD cache for improved performance. | Seagate, Western Digital |
| Magnetic Tape | Archival storage | 1951 | Sequential access storage for long-term backup and archival purposes. | IBM, Quantum, HPE |
| Optane / 3D XPoint | Persistent memory | 2015 | Non-volatile memory with very low latency, bridging DRAM and SSD speeds. | Intel, Micron |
| eMMC / UFS | Embedded storage | 2000s | Flash storage embedded in mobile devices and embedded systems. | Samsung, Toshiba, Micron |
| HDD Arrays / RAID | Redundant storage | 1980s | Multiple HDDs combined for redundancy or performance (RAID 0/1/5/6/10). | Dell, HPE, NetApp |

## Linux Storage Hardware Communication Model

> ….
> 

## Partition

> What is a disk partition? What is the nature of this abstraction? What partitions exist on a new disk? How is this abstraction implemented? How does the OS detect the partition type?
> 

### Formulation

> A **disk partition** is a logically defined portion of a physical storage device (like an HDD or SSD) that is treated by the operating system as a separate “disk” with its own file system, allowing multiple independent areas for organizing data, installing operating systems, or managing storage.
> 

> The OS treats each partition as a separate logical volume, which can then be formatted with a file system and mounted.
> 

### Implementation

> A **partition table** is the standard data structure stored on a disk that defines how the disk is divided into partitions. It records the start and end points of each partition, their types, and attributes, allowing the operating system to recognize, access, and manage multiple logical storage areas on a single physical disk. There are two formats  - **MBR** and **GPT.**
> 

| Format | Description |
| --- | --- |
| **MBR (Master Boot Record)** | Traditional partitioning scheme stored in the first sector of the disk. Supports up to 4 primary partitions (or 3 primary + 1 extended), up to 2 TB disk size. Contains boot code and partition entries. |
| **GPT (GUID Partition Table)** | Modern partitioning scheme with primary and backup headers. Supports very large disks, many partitions (128+), and uses globally unique identifiers (GUIDs) for partitions. Required for UEFI boot. |

### OS Interaction

> How does the OS detect the partition type?
> 

> The partition table itself is a **low-level abstraction**, while the filesystem is the higher-level abstraction the OS interacts with to manage files.
> 

> The identification is basically It’s this MBR; Its this GPT?
> 

## Root File System

> The **Root File System** is the top-level directory hierarchy of a Linux or Unix-like operating system. It contains all the essential directories, files, and binaries required for the system to boot and operate. It is mounted at the root mount point `/`.
> 

### Implementation

> How is the concept of the **“Root File System”** Implemented?
> 

> The **root file system** is the top-level filesystem mounted at `/` in Linux. It provides the initial filesystem hierarchy from which the kernel and user processes can access files and directories. All other filesystems are mounted **underneath this root**.
> 

> The **root file system** is **not itself a filesystem**; it is a mount point that the kernel uses as the starting point of the directory hierarchy, mapping to an actual underlying filesystem (like ext4, XFS, or tmpfs) on a device or in memory.
> 

> **Rootfs is a kernel abstraction**: The kernel sees the root filesystem as a special VFS (Virtual File System) object. The VFS allows the kernel to **abstract away the details of the underlying storage device**, whether it’s a disk, SSD, or even an initramfs in memory.
> 

> **VFS Layer**: Linux uses the **VFS layer** to represent all filesystems in a unified way. The rootfs is just one of these VFS mount points, but it is **special because all absolute paths start from it**.
> 

> It is a **VFS abstraction**.
> 

> It points to a **real filesystem** that resides on a device, in RAM, or over the network.
> 

> All absolute paths (`/bin`, `/etc`, etc.) are **resolved relative to the rootfs**.
> 

### Path Structure

| **Directory** | **Description** | **Notes** |
| --- | --- | --- |
| `/` | Root of the filesystem hierarchy | Mount point for rootfs |
| `/bin` | Essential command binaries for all users | e.g., `ls`, `cp`, `bash` |
| `/sbin` | Essential system binaries for administration | e.g., `fsck`, `ifconfig` |
| `/etc` | Host-specific configuration files | `passwd`, `fstab`, `network` configs |
| `/lib` | Shared libraries required by `/bin` and `/sbin` | `libc.so`, kernel modules in `/lib/modules` |
| `/usr` | Secondary hierarchy for read-only user data and programs | `/usr/bin`, `/usr/lib`, `/usr/share` |
| `/var` | Variable data like logs, spool files, and caches | `/var/log`, `/var/spool` |
| `/tmp` | Temporary files, usually cleared at boot | Accessible by all users |
| `/home` | User home directories | `/home/alice`, `/home/bob` |
| `/dev` | Device nodes | `/dev/sda`, `/dev/tty`, `/dev/null` |
| `/proc` | Virtual filesystem providing process and kernel info | e.g., `/proc/cpuinfo`, `/proc/meminfo` |
| `/sys` | Kernel object and device information (sysfs) | `/sys/class`, `/sys/block` |
| `/mnt` | Temporary mount points | Often used for manual mounts |
| `/media` | Mount points for removable media | `/media/cdrom`, `/media/usb` |
| `/boot` | Static files for boot loader | Kernel images, `grub` configs |
| `/run` | Runtime variable data since boot | PID files, sockets, locks |

## QA

- How does the boot (initialization) process select and list the OS partitions?
- What mounting a device means?
- What is a disk partition?
- How to map file system with specific hardware disk or storage device?
- Which type of file systems are supported by Linux (**`lsblk -l`**)?
- How a file system is store in disk?
- What is an unmounted file system?
- How to explore unmounted file systems?
- What is the meaning of **mounting** file systems? **Mounting a file system** means making it accessible to the operating system by associating it with a specific directory (mount point) in the file system hierarchy.
- What the OS/Kernel  **`does to mound`** file systems?
- What is the **`root file`** system?
- How to mount a **`file system`** in other file **`system tree`**?
- Does the `OS` have a disk abstraction for many disk technologies? Which are those abstractions?  How a file system is  represented on a disk?
- How to recover corrupted file systems?
- How to print the **`file system’s tree`**?
- What is really a file system from the **`os/kernel`** standpoint? Data Representation + Interaction.
    - How does the kernel choose the correct file system to handle a **file system** operation?
- How to explore the content of a **storage device** without mounting it? Question answer in `Hardware Storage System`.
- How the **root file system** is mounted? [How to root file system is mounted?](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-file-systems-stack.md)
- Which are the disk units of storage?
- Which  are the disk cluster units of storage?
- How can I trace a file's data directly to the disk sectors and read those sectors from my `/dev/sda` disk?
- What `sda` means? It stands for "**SCSI disk A**" for historical reasons, but these days /dev/sdX is also used to denote SATA devices, SD cards and so on.
- How to determine the **file system type** of given path $x$ on Linux?

### How can I trace a file's data directly to the disk sectors and read those sectors from my `/dev/sda` disk?

> To trace a file’s data directly to the disk sectors and read those sectors from the disk (e.g., `/dev/sda`), you’ll need to interact with the file system and the raw disk. The process involves finding the blocks where the file is stored and then accessing those blocks on the disk. Here’s a step-by-step approach:
> 

**Identify the file's inode and blocks:** Files are stored in **blocks** on the disk. To trace a file to its sectors, you need to identify the file's inode and the blocks it uses. You can do this using the `debugfs` tool.

```bash
sudo debugfs /dev/sda1
debugfs:  stat /path/to/your/file
```

**Map file blocks to disk sectors:** File systems like ext4 use logical block addresses (LBAs) which can be mapped to actual disk sectors. The block addresses returned by `debugfs` represent **logical blocks** within the file system. These need to be mapped to the corresponding physical sectors on the disk.

You can use the `blockdev` command to get the physical disk sectors:

```bash
sudo blockdev --getss /dev/sda
```

This will give you the **sector size** (e.g., 512 bytes, 4KB), and you can calculate the physical sector 

addresses by multiplying the logical block addresses by the sector size.

3. **Read the disk sectors directly**

- Once you have the physical sector addresses, you can read them directly using tools like `dd`, `hexdump`, or `cat`. You’ll need to know the sector size and the offset to read from the disk.

Example using `dd`:

```bash
sudo dd if=/dev/sda of=sector_data.bin bs=512 skip=SECTOR_NUMBER count=1

```

Replace `SECTOR_NUMBER` with the appropriate sector number (calculated by multiplying the logical block number by the sector size), and adjust the block size (`bs`) according to your sector size (usually 512 bytes or 4 KB).

Alternatively, you can use `hexdump` to inspect the sector contents:

```bash
sudo hexdump -C /dev/sda | less
```

4. **Automating the process**

- Automating this process may require writing a script that takes the inode information and automatically maps it to sectors, reading the sectors one by one. You would need to handle the block-to-sector mapping and take care of cases like indirect blocks (if the file is large and uses multiple levels of indirection).

### How to determine the **file system** of given path on Linux?

> Let’s call it x**.**
> 

```bash
stat -f -c %T "$x"  # Get the filesystem type of the given path using 'stat'.

df -T "$x"  # Display filesystem type along with disk usage information.

findmnt -no FSTYPE "$x"  # Extract only the filesystem type of the given path using 'findmnt'.

grep " $(df --output=source "$x" | tail -n 1) " /proc/mounts | awk '{print $3}'  
# Find the mounted device corresponding to the path, search for it in /proc/mounts,  
# and extract the filesystem type (third column).

blkid -o value -s TYPE "$(df --output=source "$x" | tail -n 1)"  
# Get the block device for the given path using 'df', then use 'blkid' to retrieve its filesystem type.

```

### How to create a new ‘file system’? that is How to create a new partition an format-it with a given ‘file system’?

> The question (How to create a new ‘file system’?) does not makes sense. Creating a new file system does **not** mean writing a new file system software. In practice, it means creating a new partition on a storage device and **formatting that partition with a file system** (e.g., EXT4, XFS, FAT32) so it can store and organize data.
> 

### How does the root file system is specify?

> The **root file system (rootfs)** is specified during **system boot**, and there are several ways the Linux kernel and bootloader know which device or image to use as `/`.
> 

Here's a **structured explanation**:

| Method | How It Works | Notes |
| --- | --- | --- |
| **Bootloader Kernel Parameter** | The bootloader (GRUB, LILO, etc.) passes the root device to the kernel via the `root=` parameter. | `linux /vmlinuz-linux root=/dev/sda1 ro`Here `/dev/sda1` is used as rootfs. |
| **UUID / LABEL** | Instead of specifying a raw device, a **filesystem UUID** or **label** can be used, which is more robust if devices are reordered. | `root=UUID=123e4567-e89b-12d3-a456-426614174000root=LABEL=rootfs` |
| **Initramfs / Initrd** | A temporary root filesystem loaded into RAM at boot. The kernel mounts it first and later switches to the “real” rootfs on disk. | Common in modern Linux: `/boot/initramfs-linux.img` |
| **Network Root (NFS / iSCSI / NVMe-oF)** | The kernel can mount a root filesystem over the network using protocols like NFS, iSCSI, or NVMe over Fabrics. | `root=/dev/nfs nfsroot=192.168.1.10:/export/rootfs` |
| **Embedded / Read-Only Root** | In embedded systems, rootfs may reside in a read-only partition, flash memory, or even in the kernel image itself. | `/dev/mtdblock0` or initramfs built into the kernel |

### How to root file system is mounted?

The **root file system** is mounted during the **boot process** of a Linux or Unix-like system. Here’s a breakdown of how this typically happens:

1. **BIOS/UEFI Initialization**
    - The **BIOS** or **UEFI** firmware performs the initial hardware checks and hands over control to the bootloader (e.g., **GRUB**).
    - GRUB (or other bootloaders) loads the **kernel** into memory and passes control to it.
2. **Kernel Boot Process**
    - The kernel is loaded into memory by the bootloader and begins execution.
    - During boot, the kernel initializes the system hardware (drivers, device detection) and prepares for mounting the file systems.
3. **Initial RAM Disk (initrd/initramfs)**
    - Before mounting the root file system, the kernel may load a **temporary root file system** called **initramfs** or **initrd**.
    - This is a compressed file system image that contains essential binaries and drivers needed to mount the real root file system.
    - The initramfs includes a minimal environment to allow the kernel to access essential resources, such as drivers for the storage controller (e.g., AHCI, NVMe), encryption keys, or RAID devices.
4. **Mounting the Root File System**
    - Once the kernel has loaded the initramfs, it looks for the **root file system**.
    - The kernel locates the **root device** (partition or disk) by reading information from the **bootloader** or **kernel parameters**. The location of the root file system is typically specified by a parameter like `root=/dev/sda1` or `root=UUID=<UUID>`.
        - **Example**: The bootloader may pass `root=/dev/sda1` as a parameter to the kernel, meaning the root file system is on the `/dev/sda1` partition.
5. **Mounting the Root File System**
    - The kernel mounts the root file system (e.g., `/dev/sda1`) on the **root directory `/`**.
    - The file system type (e.g., `ext4`, `btrfs`, `xfs`) is detected automatically or passed as a parameter.
        - If the file system type is not specified, the kernel uses a default, typically **ext4**.
    - The root file system is now fully available to the system for accessing system files and launching user-space programs.
6. **Switching from initramfs (if used)**
    - Once the real root file system is mounted, the kernel will typically switch from the initramfs to the actual root file system.
    - This switch happens by executing the **init** process (usually `/sbin/init`) from the real root file system.
7. **Finalizing System Initialization**
    - The `init` process (or other initialization systems, such as **systemd**) takes over to set up the system further (e.g., mounting other file systems like `/home`, `/var`, or network drives) and start essential services.

### How does the `system` determine which partitions contain the operating system during boot?

> 

1. **Firmware Stage (BIOS/UEFI)**

- **BIOS:** Reads the **Master Boot Record (MBR)** on the first sector of the first disk.
- **UEFI:** Reads the **EFI System Partition (ESP)**, which contains bootloaders for installed OSes.
- **Goal:** Find a bootloader program that can continue loading the OS.

2. **Bootloader Stage**

- The bootloader is a small program stored in a specific location:
    - **MBR-based systems:** Bootloader resides in the first 512 bytes of the disk.
    - **UEFI systems:** Bootloader is a file (like `bootx64.efi`) on the EFI System Partition.
- The bootloader **knows which partition contains the OS kernel** because:
    - It is **configured with partition information** (often in a configuration file, e.g., GRUB’s `grub.cfg`).
    - It can **scan partitions** for OS kernels if configured to auto-detect.

3. **Kernel Loading Stage**

- Once the bootloader identifies the correct partition:
    - It mounts the partition (usually a minimal filesystem driver in the bootloader itself).
    - It loads the **kernel** and optionally an **initramfs/initrd**.
- The kernel then takes over and mounts the **root filesystem** of the OS.

4. **Mechanisms Used to Identify OS Partitions**

- **Partition Table Entries:** Indicates type (e.g., Linux `83`, Windows `7`/`NTFS`).
- **Bootloader Configuration:** Explicitly points to the partition (e.g., `/dev/sda1` or UUID `e4f9c...`).
- **Filesystem Signatures:** Bootloader or kernel may detect known OS files or markers.
- **UUIDs/Labels:** Universally unique identifiers ensure the correct partition is chosen even if drive order changes.

### How the list the Physical Hard Disk Drive?

> 

### How many filesystems - can a Partition Contain?

> https://askubuntu.com/questions/1463833/can-we-create-two-different-filesystems-on-a-single-partition
> 

> There is much nuance on this answer- bordering philosophy.
> 

> As is the case with advances in technology, the clear borders of old definitions are still becoming more blurred. Traditionally, one partition is formatted with one filesystem - and this is still normally the case.
> 

## References

- [Filesystem in Userspace](https://en.wikipedia.org/wiki/Filesystem_in_Userspace)
- https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
- Ghemawat, S., Gobioff, H., & Leung Google, S.-T. (2003). The Google File System.
- Baker, M. G., Hartman, J. H., Kupfer, M. D., Shirriff, K. W., & Ousterhout, J. K. (1991). Measurements of a distributed file system. ACM SIGOPS Operating Systems Review, 25(5), 198–212. https://doi.org/10.1145/121133.121164
- McKusick, M. K., Joy, W. N., Leffler, S. J., & Fabry, R. S. (1984). A fast file system for UNIX. ACM Transactions on Computer Systems (TOCS), 2(3), 181–197. https://doi.org/10.1145/989.990
- Sweeney, A. (1996, January). Scalability in the XFS File System. https://www.usenix.org/conference/usenix-1996-annual-technical-conference/scalability-xfs-file-system
- Thekkath, C. A., Mann, T., & Lee, E. K. (1997). Frangipani: a scalable distributed file system. ACM SIGOPS Operating Systems Review, 31(5), 224–237. https://doi.org/10.1145/269005.266694
- SantanaRicardo, RangaswamiRaju, TarasovVasily, & HildebrandDean. (2016). A Fast and Slippery Slope for File Systems. ACM SIGOPS Operating Systems Review, 49(2), 27–34. https://doi.org/10.1145/2883591.2883598
- Rosenblum, M., & Ousterhout, J. K. (1992). The design and implementation of a log-structured file system. ACM Transactions on Computer Systems (TOCS), 10(1), 26–52. https://doi.org/10.1145/146941.146943
- Prabhakaran, V., Arpaci-Dusseau, A. C., & Arpaci-Dusseau, R. H. (2005). Analysis and Evolution of Journaling File Systems.
- Lee, C., Sim, D., Hwang, J., & Cho, S. (2015). F2FS: A New File System for Flash Storage. 273–286.
- Hellwig, C. (n.d.). XFS: the big storage file system for Linux.
- Katabi, L., Rhea, R., & Nagaos, C. (n.d.). Experiences with a Distributed, Scalable, Methodological File System: AnalogicFS.
- Griffioen, J., & Appleton, R. (1994, June). Reducing File System Latency using a Predictive Approach. https://www.usenix.org/conference/usenix-summer-1994-technical-conference/reducing-file-system-latency-using-predictive
- Rhea, S., Eaton, P., Geels, D., Weatherspoon, H., Zhao, B., & Kubiatowicz, J. (2003, March). Pond: The OceanStore Prototype. 2nd USENIX Conference on File and Storage Technologies (FAST 03). https://www.usenix.org/conference/fast-03/pond-oceanstore-prototype
- Linux file system explained. https://twitter.com/alexxubyte/status/1666462242613915648
- How to see information inside inode data structure [https://unix.stackexchange.com/questions/279729/how-to-see-information-inside-inode-data-structure](https://unix.stackexchange.com/questions/279729/how-to-see-information-inside-inode-data-structure)
- How the Linux VFS, block layer, and device drivers fit together http://blog.vmsplice.net/2020/04/how-linux-vfs-block-layer-and-device.html
- - [Unionfs: [A Stackable Unification File System]](https://www.fsl.cs.sunysb.edu/project-unionfs.html)
- [Unioning file systems: Architecture, features, and design choices](https://lwn.net/Articles/324291/)
    - [UnionFS](https://en.wikipedia.org/wiki/UnionFS)
- [Gitfs: Version Controlled File System](https://news.ycombinator.com/item?id=28263356)
- Pate, Steve D. UNIX Filesystems: Evolution, Design, and Implementation. John Wiley & Sons, 2003.
- Disk write buffering and its interactions with write flushes ([utoronto.ca](http://utoronto.ca/))
[https://news.ycombinator.com/item?id=39741096](https://news.ycombinator.com/item?id=39741096)
- [Journaling File System](https://en.wikipedia.org/wiki/Journaling_file_system)
- Lee, Eunji, et al. "Shortcut-JFS: A write efficient journaling file system for phase change memory." *2012 IEEE 28th Symposium on Mass Storage Systems and Technologies (MSST)*. IEEE, 2012.
- https://github.com/deepseek-ai/3FS
- https://notes.eatonphil.com/2025-03-27-things-that-go-wrong-with-disk-io.html
- [Berkeley Socket](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/berkeley-socket.md)

[Recovery](note.html?n=technica/computation/data-system/data-system-conceptual-model/recovery.md)