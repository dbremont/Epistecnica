---
tags: [storage]
---

# File System


> A **file system** is a structured method for organizing,  storing, retrieving, and managing data on a storage device (e.g., disk,  SSD, or memory). It provides an abstraction layer between the physical  storage medium and the operating system or applications, enabling  efficient data access, storage, and manipulation. A file system defines  how data is stored, indexed, and accessed, including the layout of  files, directories, metadata, and control structures.
> 

> A file system is a structured set of sections on a storage device that are managed by the system to store, organize, and access files and metadata. The same storage device an have several file systems.
> 

## Feature Space

> What features does File System Offer? Which are the keys of abstractions they enable or support?
> 

| **Category** | **Feature** | **Description** |
| --- | --- | --- |
| **Concepts** | File | Fundamental unit of data and metadata. |
|  | Directory | Hierarchical container for files and directories. |
|  | Link | Alias/reference to another file or directory. |
|  | Device (Special File) | Represents hardware or special I/O (block/char devices). |
|  | Mount Point (Root) | Entry point of filesystem in global namespace. |
|  | Metadata (Attribute) | Properties of files or directories (permissions, timestamps, size). |
| **Hierarchy & Organization** | Directory Structure | Organizes files in tree-like paths. |
|  | Hard Links | Multiple names pointing to same inode. |
|  | Soft Links / Symlinks | References to other files or directories. |
| **Storage Management** | Block Allocation | Manages assignment of storage blocks to files. |
|  | Extents | Contiguous block allocation for large files. |
|  | Free Space Tracking | Tracks available storage. |
| **Metadata** | Inodes / File Descriptors | Stores file metadata (permissions, ownership, timestamps, pointers). |
|  | Journaling / Logs | Records metadata operations before committing. |
| **Access & Security** | Permissions / ACLs | Read/write/execute controls per user/group. |
|  | Ownership | Associates files with user and group IDs. |
|  | Encryption | On-disk file content encryption. |
| **Reliability (Integrity)** | Checksums / CRC | Data integrity verification. |
|  | Snapshots | Point-in-time filesystem state. |
|  | Replication / Mirroring | Copies data across devices or nodes. |
| **Performance & Optimization** | Caching / Page Cache | Temporarily stores frequently accessed data in RAM. |
|  | Read-Ahead / Prefetch | Predictive loading of blocks. |
|  | Compression | On-disk data reduction. |
| **Specialized Features** | Copy-on-Write (CoW) | Writes changes to new blocks rather than overwriting. |
|  | Overlay / Union Mounts | Merges multiple filesystems into one view. |
|  | Network Transparency | Remote filesystem access over network. |
|  | In-memory / tmpfs | Filesystem entirely in RAM. |

## Taxonomy

> How can we classify file systems?
> 

| **File System** | **Description** | **Use** | **Tags** |
| --- | --- | --- | --- |
| **ext4** | Journaling Linux filesystem, reliable and mature. | General-purpose Linux storage. | Linux, journaling, mature, stable |
| **XFS** | High-performance 64-bit journaling filesystem. | Large files and high-throughput systems. | Linux, high-performance, journaling, scalable |
| **Btrfs** | Copy-on-write, snapshot-capable Linux filesystem. | Advanced storage with snapshots, RAID, and compression. | Linux, CoW, snapshots, RAID, compression |
| **ZFS** | Combined filesystem and volume manager, CoW, snapshots, and data integrity. | Enterprise storage, NAS, data integrity-focused systems. | CoW, snapshots, integrity, scalable, enterprise |
| **NTFS** | Windows journaling filesystem supporting ACLs and large files. | Windows system drives, external storage with Windows compatibility. | Windows, journaling, ACLs, large files |
| **FAT32** | Simple, widely compatible filesystem, 32-bit addressing. | USB drives, cross-platform small storage. | Cross-platform, legacy, simple, small files |
| **exFAT** | Extended FAT, supports large files and modern storage. | SD cards, external drives, cross-platform. | Cross-platform, large files, modern, external media |
| **APFS** | Apple’s modern filesystem with snapshots and encryption. | macOS and iOS drives. | Apple, snapshots, encryption, SSD-optimized |
| **HFS+** | Legacy Apple filesystem with journaling. | Older macOS volumes. | Apple, journaling, legacy |
| **ReFS** | Microsoft resilient filesystem with integrity streams. | Windows Server, large-scale storage. | Windows, resilience, integrity, enterprise |
| **JFS** | IBM’s journaling filesystem optimized for low CPU usage. | Linux servers requiring low overhead. | Linux, journaling, low CPU |
| **tmpfs** | In-memory filesystem, volatile storage. | Temporary files, runtime data. | Linux, RAM, volatile, temp storage |
| **ramfs** | Minimal in-memory filesystem, unlimited growth. | Temporary data, system RAM usage. | Linux, RAM, volatile, temp storage |
| **procfs** | Virtual filesystem exposing kernel and process info. | Access system/process information. | Linux, virtual, kernel, process info |
| **sysfs** | Virtual filesystem exposing kernel device and driver info. | Device management, sysadmin tools. | Linux, virtual, kernel, devices |
| **NFS** | Network filesystem protocol for Unix systems. | Shared storage over LAN. | Network, Unix, distributed |
| **SMB/CIFS** | Network filesystem protocol for Windows/Unix interoperability. | File sharing across networks, Windows-compatible. | Network, Windows, cross-platform |
| **GlusterFS** | Distributed filesystem for scalable storage clusters. | Cloud storage, large-scale distributed storage. | Distributed, scalable, Linux |
| **CephFS** | POSIX-compliant filesystem on top of Ceph object store. | Scalable and fault-tolerant storage clusters. | Distributed, scalable, fault-tolerant, Linux |
| **F2FS** | Flash-optimized filesystem using log-structured design. | NAND flash devices, SSDs, eMMC storage. | Flash-optimized, Linux, SSD |
| **UBIFS** | Journaling filesystem for raw flash memory. | Embedded devices with raw NAND flash. | Embedded, flash, Linux, CoW |
| **ISO 9660** | Standard for optical disc filesystems (CDs). | CDs, read-only media. | Optical media, read-only, legacy |
| **UDF** | Universal Disk Format, replacement for ISO 9660. | DVDs, Blu-ray, cross-platform optical media. | Optical media, cross-platform, rewritable |
| **SquashFS** | Compressed, read-only filesystem for Linux. | Embedded systems, live CDs, container images. | Linux, compressed, read-only, embedded |
| **OverlayFS** | Union filesystem combining multiple layers. | Containers, live systems, temporary overlays. | Linux, union, containers, CoW |
| **Lustre** | Parallel distributed filesystem for HPC. | High-performance computing clusters. | HPC, parallel, distributed, Linux |
| **GFS2** | Clustered filesystem for Linux with journaling. | Shared storage in clustered servers. | Linux, clustered, journaling, enterprise |

## Structure

> What is the Structure of File System (**ext4, OverlayFS**)?
> 

> Note: This is  a general structure - there is some variation in between File Systems.
> 

| **Layer** | **Implements** | **Role** |
| --- | --- | --- |
| **Storage Organization Layer** | Storage Organization | Divides the device into addressable units (blocks, sectors, clusters) and manages their layout. |
| **Metadata Layer** | Metadata Management | Stores file and directory metadata: permissions, ownership, timestamps, file size, and pointers to data blocks. |
| **Directory Layer** | Directory Hierarchy | Organizes files and directories in a tree-like hierarchy; enables path-based access. |
| **Allocation Layer** | Data Allocation | Manages allocation/deallocation of storage using methods like contiguous, linked, indexed, or extent-based allocation. |
| **Access Control Layer (Security)** | Access Control | Enforces permissions and security policies (read/write/execute) for users and processes. |
| **Fault-Tolerance Layer (Reliability)** | Fault Tolerance | Provides mechanisms like journaling, checksums, snapshots, replication to ensure integrity and recoverability. |

## Implementation

> How do filesystems integrate with the operating system? How do filesystems communicate with the hardware?
> 

### Model

| **Model** | **Description** | **Case(s)** |
| --- | --- | --- |
| **Disk-Based System** | Traditional file systems are designed to store data on magnetic disks, focusing on efficient space utilization and data access. | Ext4, NTFS, HFS+ |
| **Network System** | Designed to allow multiple clients or systems to access shared files over a network, treating remote files as if they are local. | NFS, SMB/CIFS, AFP |
| **Journaling System** | Include mechanisms to maintain a journal of changes that help quickly recover from crashes by replaying the journal. | Ext3, Ext4, XFS, ReiserFS, JFS |
| **Distributed System** | Manage files across multiple machines, providing fault tolerance and redundancy, often used in clustered environments. | GlusterFS, Ceph, Hadoop Distributed File System |
| **Flash-Based System** | It is optimized for the characteristics of flash memory, such as solid-state drives, managing wear leveling, and write amplification. | YAFFS, F2FS, JFFS2 |
| **Database System** | Treat file metadata as a database, allowing more complex queries and relationships, and can include versioning and fine-grained permissions. | WinFS (discontinued), Reiser4 |
| **Log-Structured System** | Write all modifications to disk sequentially in a log-like structure, which enhances performance but requires periodic cleaning. | LogFS, NILFS |
| **Virtual File System** | Provide an abstraction layer over various file systems, allowing the OS kernel to interface uniformly with different underlying file systems. | VFS (used in Linux, Unix-like systems) |
| **Union-Based System** | Layer multiple file systems to present them as a cohesive file system, merging their contents for unified access. | UnionFS, OverlayFS, aufs (Another UnionFS) |
|  |  |  |

### File

> How it’s the file abstraction implemented?
> 

> How a process represents a file?
> 

> A file is an abstraction that represents a collection of related data stored on a storage device. The file abstraction allows applications to read, write, and organize data without needing to manage the underlying hardware directly.
> 

> **Note:** In Linux, a file is a very **abstract notion**. While there are actual storage files on disk, many other resources—such as sockets, pipes, and devices—are also **represented or modeled as files**. The phrase “everything is a file” captures this underlying philosophy: the **implementation and rules of interaction may differ** depending on the type of file, but the kernel provides a **uniform abstraction** for accessing diverse resources.
> 

**Implementation Details (For File System - Files):**

1. **Metadata (Inodes / File Descriptors):** Stores file attributes such as size, owner, permissions, timestamps, and pointers to the data blocks on disk.
2. **Data Blocks:** The actual contents of the file are stored in contiguous or non-contiguous blocks on the storage device.
3. **File System Layer:**
    - The file system manages the mapping from file names to metadata and from metadata to data blocks.
    - Provides operations like `open`, `read`, `write`, `close`, and `delete`.
4. **Kernel Abstraction:** The OS kernel exposes the file interface to applications while handling block I/O, caching, and consistency behind the scenes.

### File Types

| File Type | Description | Symbol (`ls -l`) |
| --- | --- | --- |
| Regular File | User data | `-` |
| Directory | Contains files | `d` |
| Symbolic Link | Points to another file | `l` |
| Character Device | Serial devices, keyboard, etc. | `c` |
| Block Device | Disks, USB drives | `b` |
| FIFO / Named Pipe | IPC (first-in, first-out) | `p` |
| Socket | Network/IPC | `s` |

### Technique

> **Note:** Techniques are not overarching guides or templates — they are specific ways to achieve a particular goal.
> 

> What are the key techniques used in file system implementation and abstraction?
> 

| **Category** | **Technique** | **Description** | **Goal** |
| --- | --- | --- | --- |
| **Storage Management** | Block Allocation | Assigns storage blocks to files, either contiguously or in fragments. | Efficient use of disk space and fast access. |
|  | Extents | Allocates large contiguous ranges of blocks for a file. | Reduce fragmentation and improve sequential I/O performance. |
|  | Free Space Tracking | Maintains a record of available blocks (bitmap, free lists, or B-trees). | Quickly locate free storage for new files. |
| **Metadata Management** | Inodes / File Descriptors | Stores file metadata (permissions, timestamps, ownership, block pointers). | Separate file content from metadata for efficient access and management. |
|  | Journaling / Write-Ahead Logging | Records metadata updates before committing them to disk. | Ensure consistency and recovery after crashes. |
|  | Directory Indexing | Structures directories using hash tables, B-trees, or tries. | Enable fast file lookup and directory traversal. |
| **Caching & Performance** | Page Cache / Buffer Cache | Caches file data in memory for faster access. | Reduce disk I/O latency and improve system responsiveness. |
|  | Read-Ahead / Prefetching | Loads anticipated blocks into cache before they are requested. | Minimize I/O wait time for sequential access patterns. |
|  | Delayed Allocation | Postpones block allocation until data is flushed to disk. | Reduce fragmentation and optimize write patterns. |
| **Consistency & Recovery** | Checkpointing | Periodically writes consistent metadata snapshots to disk. | Simplify recovery and maintain file system integrity. |
|  | Copy-on-Write (CoW) | Writes updated data to new blocks instead of overwriting. | Enable snapshots, atomic updates, and crash safety. |
| **Access & Security** | Permission Enforcement | Implements access control using user/group/other bits or ACLs. | Ensure correct access rights and security. |
|  | Quotas | Limits storage usage per user or group. | Prevent resource abuse and enforce fair allocation. |
| **Abstraction Techniques** | Virtual File System (VFS) | Provides a uniform interface to multiple underlying file systems. | Enable portability and modularity of file system implementations. |
|  | Mount Points | Maps a file system into a directory tree. | Allow hierarchical composition and access of multiple storage devices. |
|  | Device Abstraction | Separates hardware details from file system logic. | Make file systems independent of specific storage devices. |

## File System Security

> How is the security enforce?
> 

### Permision Model

**File Permission Concepts**

- **Read (r)**: Allows the user to read the contents of the file or directory.
- **Write (w)**: Allows the user to modify the file or directory (e.g., adding/deleting files in a directory).
- **Execute (x)**: Allows the user to run the file (if it is executable) or access the contents of a directory.

`rwxr-xr--`:

- **Owner**: First 3 characters (`rwx`) represent the file owner’s permissions.
- **Group**: Next 3 characters (`r-x`) represent the group's permissions.
- **Others**: Last 3 characters (`r--`) represent permissions for others.

### Enforcement Model

| **Mechanism** | **Where Enforced** | **How It Works** |
| --- | --- | --- |
| **Permissions & Ownership** | Kernel (VFS layer) | Checks inode metadata (owner, group, permission bits) on every file access; denies unauthorized operations. |
| **Access Control Lists (ACLs)** | Kernel / Filesystem | Extended attributes specify additional user/group permissions; kernel enforces them on access. |
| **Mandatory Access Control (MAC)** | Kernel | SELinux, AppArmor, or Smack policies restrict process actions regardless of standard permissions. |
| **Mount Options** | Kernel / Filesystem | Options like `ro`, `noexec`, `nosuid`, `nodev` restrict filesystem behavior for all access attempts. |
| **Encryption** | Kernel / User-space | File or disk data is encrypted; kernel or libraries handle decryption for authorized access only. |
| **File Integrity Monitoring** | User-space | Tools like AIDE/Tripwire compare file hashes to detect unauthorized changes. |
| **Auditing** | Kernel / User-space | `auditd` logs file access, modifications, and deletions for accountability. |
| **Process-Level Checks** | Kernel | Every system call (`open`, `read`, `write`, `execve`) triggers security checks across all layers; access denied if any check fails. |

## Mounting

> **Mounting a file system** means making it accessible to the operating system by associating it with a specific directory (mount point) in the file system hierarchy.
> 

Types:

- **Manual Mounting**: Using `mount` to temporarily attach a file system.
- **Automatic Mounting**: Configured in `/etc/fstab` for persistent mounting.
- **Loopback Mounting**: Mounting disk images (`.iso`, Snap, AppImage) as virtual file systems.

## File System Comparison

> How can file systems be compared, including their performance characteristics?
> 

| **Dimension** | **Ext4** | **XFS** | **Btrfs** | **ZFS** |
| --- | --- | --- | --- | --- |
| **Sequential Throughput** | High | Very High (large files) | Moderate | Moderate |
| **Random I/O / Latency** | Low | Low | Moderate | Moderate |
| **Small File Performance** | Moderate | Moderate | Moderate | Moderate |
| **Metadata Performance** | High | High | Moderate | Moderate |
| **Journaling / Consistency** | Metadata-only | Metadata-only | Full (CoW) | Full (CoW) |
| **Snapshots** | ❌ | ❌ | ✅ | ✅ |
| **Copy-on-Write (CoW)** | ❌ | ❌ | ✅ | ✅ |
| **Compression Support** | ❌ | ❌ | ✅ | ✅ |
| **Deduplication** | ❌ | ❌ | ❌ | ✅ |
| **Directory Indexing** | H-tree | B-tree | B-tree | B-tree |
| **Max File Size** | 16 TiB | 8 EiB | 16 EiB | 16 EiB |
| **Max Volume Size** | 1 EiB | 8 EiB | 16 EiB | 256 ZiB |
| **CPU Overhead** | Low | Low | Medium | High |
| **Crash Recovery** | Fast | Fast | Moderate | Moderate |
| **Suitable Workload** | General-purpose, small/medium files | Large files, high-throughput | Snapshots, CoW workloads | Enterprise, data integrity, large storage |

## Performance

> How to benchmark a File System?
> 

### Feature

| Feature | Impact on Performance | Notes |
| --- | --- | --- |
| Journaling | Can add write overhead but improves crash recovery | Some FS allow journaling only metadata or full data journaling |
| Copy-on-Write (CoW) | Increases write amplification but enables snapshots | e.g., Btrfs, ZFS |
| Extents | Reduces fragmentation, improves sequential throughput | Ext4, XFS |
| Caching / Prefetching | Reduces read latency and improves sequential access | OS-dependent but FS can optimize patterns |
| Compression / Deduplication | Reduces storage footprint, may add CPU overhead | Trade-off between I/O and CPU |
| Directory Indexing | Faster lookup in large directories | e.g., B-trees in XFS, H-trees in Ext4 |
| Encryption | Protects data but adds CPU overhead | Can be hardware-accelerated |
| Snapshot Support | Can slow writes due to CoW overhead | Available in CoW file systems (Btrfs, ZFS) |
| RAID / Multi-Device Support | Striping improves throughput, mirroring may reduce it | FS-dependent; may require underlying device support |
| File Size & Directory Limits | Very large files or directories can increase metadata overhead | Depends on FS design and max inode count |
| Metadata Performance | Affects file creation, deletion, and directory operations | Depends on inode structure, caching, and indexing |

### Metric

| Metric | Description | Why it Matters |
| --- | --- | --- |
| **Throughput** | Amount of data read/written per unit time (MB/s, GB/s) | Measures bulk I/O efficiency |
| **Latency** | Time to complete a single operation (read/write/create/delete) | Measures responsiveness, critical for small files or interactive workloads |
| **IOPS (I/O Operations Per Second)** | Number of I/O operations completed per second | Important for workloads with many small files or database applications |
| **CPU Overhead** | Amount of CPU used for file system operations | Indicates efficiency of FS implementation |
| **Scalability** | Performance as the number of files or size of storage grows | Important for large-scale storage systems |

### Workload

> 

| Workload | Key Metrics | FS Considerations |
| --- | --- | --- |
| Sequential read/write | Throughput | Extents, prefetching, large block size |
| Random read/write | IOPS, latency | Journaling overhead, small block handling |
| Small files / many files | Metadata performance | Directory indexing, inode allocation |
| Mixed workload | Combination of metrics | CoW, caching, journaling policies |

### Benchmark

> 
1. **Benchmarking Tool**
    - `fio` – flexible I/O benchmarking for various workloads
    - `bonnie++` – measures file I/O and metadata performance
    - `iozone` – tests sequential and random performance
2. **Controlled Test Environment**
    - Same hardware, caching, and disk configuration
    - Repeat tests under cold/warm cache conditions
3. **Consider Realistic Workload Mix**
    - Database operations, web server files, or user home directories
    - Include both read-heavy and write-heavy patterns

## Tool

> Note: In this section we will only explore Linux Utils?
> 

> Which do we have to ‘operation - interact’ with File Systems?
> 

| **Category** | **Tool** | **Purpose** |
| --- | --- | --- |
| **Command-Line Utility** | `ls` | List files and directories |
|  | `cp` | Copy files and directories |
|  | `mv` | Move or rename files and directories |
|  | `rm` | Remove files or directories |
|  | `mkdir` | Create directories |
|  | `rmdir` | Remove empty directories |
|  | `find` | Search for files/directories matching criteria |
|  | `du` | Show disk usage of files/directories |
|  | `df` | Show filesystem disk space usage |
| **Management Tool** | `mount` | Mount a filesystem at a directory |
|  | `umount` | Unmount a filesystem |
|  | `fsck` | Check and repair filesystem integrity |
|  | `mkfs` | Create a new filesystem on a device |
|  | `tune2fs` | Adjust parameters of ext2/3/4 filesystems |
|  | `xfs_admin` | Adjust parameters of XFS filesystems |
|  | `btrfs` commands | Manage and tune Btrfs filesystems |
| **Disk Tool** | `fdisk` | Partition disks interactively |
|  | `parted` | Partition disks non-interactively and interactively |
|  | `lsblk` | List block devices and their properties |
|  | `blkid` | Show block device UUIDs and types |
| **Programming Interface** | `open()` | Open a file descriptor |
|  | `read()` | Read data from a file descriptor |
|  | `write()` | Write data to a file descriptor |
|  | `close()` | Close a file descriptor |
|  | `stat()` | Get file metadata |
|  | `mkdir()` | Create a directory programmatically |
|  | `unlink()` | Remove a file programmatically |
| **Virtual File System (VFS) Layer** | Kernel abstraction | Provides uniform access to all filesystem types |
| **Network FS Tool** | `sshfs` | Mount remote filesystem over SSH |
|  | `mount -t nfs` | Mount remote NFS filesystem |
|  | `smbclient` | Access SMB/CIFS network shares |
| **Graphical File Manager** | Nautilus | GUI file navigation and operations |
|  | Dolphin | GUI file navigation and operations |
|  | Thunar | GUI file navigation and operations |
| **Monitoring Tool** | `lsof` | List open files and their processes |
|  | `stat` | Show detailed file information |
|  | `inotifywait` | Wait for filesystem events |
|  | `iotop` | Monitor I/O usage per process |
|  | `df` | Show filesystem disk space usage |
|  | `du` | Show disk usage of files/directories |

## QA

- What is the page cache?
- What determines the `performace` of a file system?
- How stdin really works?
- What is a stream really?
- How stdout really works?
- What can become a file and how?
- How the file abstraction really works?

### How to create a User Space File System?

> By using the **FUSE framework**, which lets you implement filesystem logic in user space through callbacks for file operations, mounted via the kernel’s FUSE module.
> 

### How to load a new file System to the Kernel?

> A new filesystem is loaded into the Linux kernel by compiling it as a module or built-in and then loading it (e.g., with `modprobe` or automatically on `mount`).
> 

| **Method** | **Description** | **Note** |
| --- | --- | --- |
| **Built-in (static)** | Filesystem is compiled directly into the kernel and available at boot. | `make menuconfig` → select `[*] ext4` |
| **Loadable Kernel Module (manual)** | Filesystem is compiled as a `.ko` module and manually loaded. | `insmod myfs.ko` or `modprobe ext4` |
| **Auto-load on Mount** | Kernel auto-loads the filesystem module via `kmod` when a device is mounted. | `mount -t ext4 /dev/sda1 /mnt/data` |

### How a process represents a file?

> See [Linux Process Management Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-process-management-stack.md).
> 

> A file is a **resource**; it is not directly represented in a process. Its representation exists at multiple levels: **File System → Kernel → Driver → Disk**. A process **refers to it** through a **file descriptor** or **handle**.
> 

> A **process does not interact with a file directly on disk**; it uses an **abstract handle** provided by the operating system. This is usually called a **file descriptor** (in Unix/Linux) or a **file handle** (in Windows).
> 

**Key Points:**

1. **File Descriptor / Handle:**
    - An integer (Unix/Linux) or opaque object (Windows) that uniquely identifies an open file for a process.
    - Example in Unix: `0` = stdin, `1` = stdout, `2` = stderr.
2. **File Table / Kernel Structures:**
    - When a process opens a file, the kernel creates an entry in the **system-wide file table** containing:
        - Pointer to the file’s metadata (inode)
        - Current file offset (read/write position)
        - Access mode (read/write)
        - Reference count (how many processes share it)
3. **Process File Descriptor Table:**
    - Each process has its **own table** mapping file descriptors to the system-wide file table entries.
    - This allows multiple processes to share the same file with independent offsets and permissions.
4. **Operations:**
    - System calls like `open()`, `read()`, `write()`, `lseek()`, `close()` operate on the **file descriptor**, letting the kernel handle the underlying disk I/O.

### What happens when we Open a File?

> This is for file system files?
> 

When a process executes an `open()` (or equivalent) system call:

1. **File Name Resolution:** The kernel translates the file path into a **directory entry** and locates the file’s **metadata** (inode in Unix/Linux).
2. **Access Checks:** The kernel checks the process’s **permissions** against the file’s access control (read, write, execute).
3. **System File Table Entry:** The kernel creates (or reuses) an entry in the **system-wide file table** containing:
    - Pointer to the file’s metadata (inode)
    - Current file offset (position for read/write)
    - Access mode (read/write)
    - Reference count
4. **Process File Descriptor Table Update:** The kernel assigns a **file descriptor** (integer) to the process that points to the system file table entry.
5. **Device/Driver Preparation:** If the file resides on a disk or special device, the **driver may prepare buffers, cache metadata**, or set device-specific state.
6. **Return to Process:** The system call returns the **file descriptor**, which the process can now use for `read()`, `write()`, `lseek()`, or `close()`.

### What type of file is `stdin`?

> **stdin is a file *descriptor* (fd 0) that represents a byte stream — its underlying “file” can be a terminal character device, a pipe/FIFO, a socket, or a regular file depending on how you invoked the process.**
> 

### How to used the same open - `file` of another process?

> You **cannot just “use” a file descriptor from another unrelated process** unless you explicitly pass it (via Unix domain sockets or `/proc/<pid>/fd` trick).
> 

> File descriptors are **per-process kernel objects**, so direct access isn’t normally allowed across processes.
> 

## References

- - [ ]  [**CSBB: File System**]
- https://en.wikipedia.org/wiki/File_system
- Practical File System Design with the Be File System [http://www.nobius.org/dbg/practical-file-system-design.pdf](http://www.nobius.org/dbg/practical-file-system-design.pdf)
- [A Collection of Bash Utilities for Everyday Tasks](https://app.notion.com/p/A-Collection-of-Bash-Utilities-for-Everyday-Tasks-195c0f5171ec805a8caed838d363d3e8?pvs=21)