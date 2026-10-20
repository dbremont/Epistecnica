---
tags: [storage]
---

# Storage System

- [Linux  File Systems Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-file-systems-stack.md)

> **Physical storage media** refers to the physical devices, such as hard disk drives, solid-state drives, magnetic tapes, and optical disks, used to store data in a computer system.
> 

> **Computer storage** is the hardware and technology used to retain digital data persistently or temporarily, enabling data access, retrieval, and manipulation by a computing system.
> 

> A **storage system** refers to the combination of hardware and software components designed to store, manage, and retrieve data efficiently and securely.
> 

> Data Degradation: …
> 

![](https://pbs.twimg.com/media/DnzGVX0XoAY7dnH.jpg)

Latency Numbres

![](https://diveintosystems.org/book/C11-MemHierarchy/_images/MemoryHierarchy.png)

QA:

- How to benchmark a disk?
- How to explore the content of a **storage device** without mounting it?
- How Linux models a **`hardware storage device`**? Which are those abstractions that the OS utilize to proxy the **`hardware storage device`**?
- How to list my disk sectors size? How to get the numbers of sector of my disk? [How to list my disk sectors size? How to get the numbers of sector of my disk?](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/storage-system.md)

## Devices

Here is a list of computer storage devices:

- **Cache**: A small amount of very fast memory that is used to temporarily store data that is frequently accessed by the processor.
- **Main Memory (RAM)**: The main memory of a computer system, which is used to store data and instructions that are currently being used by the processor.
- **Hard Disk Drive (HDD)**: A non-volatile storage device that uses spinning disks to store data magnetically.
- **Solid-State Drive (SSD)**: A non-volatile storage device that uses flash memory to store data.
- **Optical Discs**: Storage devices that use laser technology to read and write data on plastic discs, such as CD-ROMs, DVDs, and Blu-ray discs.
- **Magnetic Tape**: A sequential storage medium that uses magnetic strips to store data.
- **USB Flash Drive**: A small portable storage device that uses flash memory to store data.
- **Memory Cards**: Small portable storage devices that are commonly used in digital cameras, mobile phones, and other portable devices.
- **Network-Attached Storage (NAS)**: A dedicated storage device that is attached to a network and provides storage space for multiple users and devices.
- **Cloud Storage**: A type of online storage that allows users to store and access data over the internet from remote servers.

This is not an exhaustive list, but it covers some of the most commonly used computer storage devices.

## Non-Volatile Storage Access Methods

Random access on non-volatile storage, such as hard disk drives (HDDs) and solid-state drives (SSDs), is usually much slower than sequential access due to the physical limitations of the storage medium.

In the case of HDDs, data is stored on spinning disks that must rotate to the correct location before the data can be read or written. Accessing data at random locations requires the disk to spin and the read/write head to move to the correct position, which can take a significant amount of time compared to sequential access, where the data is stored in contiguous blocks and can be read or written without moving the read/write head.

Similarly, in the case of SSDs, data is stored on flash memory chips that can only be accessed in blocks. Reading or writing data at random locations requires the controller to locate the correct block and read or write the desired data, which can take more time than sequential access, where the blocks are read or written in a continuous stream.

Therefore, sequential access is usually faster than random access on non-volatile storage due to the physical limitations of the storage medium.

## Methods

- Log Structure
- Block Storage

## Logs

[Intent Log](https://en.wikipedia.org/wiki/Intent_log)

## Content-Addressable File System (CAFS)

A **content-addressable file system (CAFS)** is a type of file system that uses content-based addressing to identify and access files. Instead of using a traditional hierarchical file path, files in a CAFS are identified and accessed based on their content. Here are some benefits of using a CAFS:

- **Data Integrity**: A CAFS can provide strong guarantees of data integrity because files are identified and accessed based on their content, rather than their location. This means that if a file is modified, its content address will change, and the modified file will be stored as a new object, ensuring the original file remains unchanged.
- **Deduplication**: Because files are identified and stored based on their content, duplicate files are automatically identified and stored as a single object. This reduces storage requirements and can improve performance by reducing the number of duplicate files that need to be managed.
- **Immutable Data**: A CAFS can store data in an immutable format, meaning that once a file is written, it cannot be modified or deleted. This provides a high degree of data security and can be useful in applications that require regulatory compliance or strong data protection.
- **Scalability**: A CAFS can be highly scalable because it does not rely on a traditional file path, which can become unwieldy and difficult to manage as the number of files grows. Instead, files are identified and accessed based on their content, making it easier to manage large numbers of files.
- **Versioning**: Because files are stored as immutable objects, a CAFS can easily provide versioning support, allowing users to track changes to files over time and revert to previous versions if necessary.

Overall, a content-addressable file system can provide significant benefits in terms of data integrity, deduplication, scalability, and versioning. While CAFS may not be appropriate for all use cases, it can be a powerful tool for managing large amounts of data in a secure and efficient manner.

## SSD

[Your SSD lies and that is ok](https://twitter.com/hnasr/status/1661701014700048385)

| **Category** | **Subcategory** | **Examples** | **Key Characteristics** |
| --- | --- | --- | --- |
| **Volatility** | Volatile Storage | RAM (DRAM, SRAM), CPU Cache | Fast but loses data on power loss |
|  | Non-Volatile Storage | SSDs, HDDs, Flash, Tape | Retains data without power |
| **Access Method** | Random Access Storage | RAM, SSDs, NVMe | Data can be accessed in constant time |
|  | Sequential Access Storage | HDDs, Tape Drives | Data must be accessed in order |
| **Medium** | Semiconductor Memory | Flash (NAND, NOR), MRAM, ReRAM | Fast, solid-state storage |
|  | Magnetic Storage | HDDs (Platter-based), Tape | Moving parts, lower speed |
|  | Optical Storage | CD, DVD, Blu-ray | Read via laser, archival use |
|  | Hybrid Storage | SSHD (HDD+SSD), ZNS SSDs | Combines speed and capacity |
| **Interface & Bus** | SATA-Based Storage | SATA SSDs, HDDs | Common in consumer devices |
|  | PCIe-Based Storage | NVMe SSDs, Intel Optane | High-speed storage for enterprise and gaming |
|  | SCSI-Based Storage | SAS HDDs, Enterprise SSDs | High-performance, datacenters |
|  | USB-Based Storage | USB Flash Drives, External SSDs | Portable, plug-and-play |
|  | Network-Based Storage | NAS, SAN, iSCSI, Fibre Channel | Remote access, cloud storage |
| **Use Case** | Consumer Storage | HDDs, SATA SSDs, USB Drives | Personal computing, gaming |
|  | Enterprise Storage | NVMe SSDs, SAS HDDs, SAN | High-performance, redundancy |
|  | Embedded Storage | eMMC, UFS, NOR Flash | IoT, mobile devices |
|  | Cold Storage | Tape, QLC SSDs, Optical Discs | Long-term archival |
|  | High-Speed Storage | Intel Optane, Persistent Memory | Low-latency, fast access |
| **Emerging Tech** | Storage-Class Memory (SCM) | Intel Optane (3D XPoint) | Faster than NAND SSDs |
|  | MRAM (Magnetoresistive RAM) | Persistent RAM | Non-volatile, high endurance |
|  | ReRAM (Resistive RAM) | Alternative to NAND SSDs | Low power, high endurance |
|  | PCM (Phase-Change Memory) | Potential replacement for NAND | Fast, non-volatile |
|  | DNA Storage | Molecular storage | High-density, ultra-long-term |

## How to explore the content of a **storage device** without mounting it?

- **`sudo blkid /dev/sda`**: Displays information about the file systems on the specified device (e.g., `/dev/sda`). This includes the UUID, file system type, and partition label, without mounting the device.
- **`sudo fdisk -l /dev/sda`**: Lists the partition table for the specified device (e.g., `/dev/sda`). It shows the partitions, their sizes, types, and starting/ending points but doesn't mount them.
- **`sudo parted /dev/sda print`**: Prints the partition table of the specified device (e.g., `/dev/sda`). Unlike `fdisk`, it supports both MBR and GPT partition schemes and provides a more user-friendly interface.
- **`sudo hexdump -C /dev/sda | less`**: Displays the raw byte content of the device (e.g., `/dev/sda`) in hexadecimal format. The output can be piped through `less` for easy scrolling and navigation.
- **`sudo testdisk /dev/sda`**: Runs `testdisk` on the specified device (e.g., `/dev/sda`). This tool is used for partition recovery and analysis, allowing you to explore the partition structure and attempt recovery of lost partitions or files.
- **`sudo mount -o loop /path/to/disk-image.iso /mnt`**: Mounts a disk image (e.g., `.iso` or `.img` file) as a loopback device without needing to extract or burn it to physical media. The file system of the image is accessible at `/mnt`.
- **`lsblk /dev/sda`**: Lists information about the block devices attached to the system, including partitions, their sizes, and mount points. It doesn't mount anything but provides a clear overview of the devices.
- **`sudo debugfs /dev/sda1`**: Opens the `debugfs` tool for inspecting an `ext4` file system (e.g., `/dev/sda1`) without mounting it. This tool allows you to examine file system structures, browse directories, and retrieve file contents interactively.
- **`sudo mount -o ro /dev/sda1 /mnt`**: Mounts the specified device (e.g., `/dev/sda1`) in **read-only** mode at the specified mount point (e.g., `/mnt`). This allows you to explore the contents of the file system without the risk of modifying data.

## Hardware Storage Device Model

> 

### Storage

- A **sector** is the smallest unit of data that can be read from or written to on a physical storage device, such as a hard disk, SSD, or optical disk. Typically, a sector is 512 bytes in size, though newer drives may use 4KB sectors (Advanced Format).
- A **cluster** (also known as an **allocation unit**) is a group of sectors that the file system uses as the smallest unit of space for file storage. Clusters are a **higher-level abstraction** compared to sectors and are typically a multiple of the sector size (e.g., 4 KB, 8 KB, etc.).

### **Block Device Abstraction**

- **Block Device**: In Linux, storage devices (like hard disks) are treated as **block devices**. This abstraction allows the OS to read and write data in fixed-size blocks (typically 512 bytes or 4 KB). A file system interacts with the block device via these block-level I/O operations.
- **Character Devices**: Though not the primary abstraction for storage, character devices are sometimes used for certain types of storage or communication with hardware.

### **Logical Block Addressing (LBA)**

- **LBA** is a common method used to abstract physical storage locations on the disk. The OS presents a **linear address space** (logical blocks) rather than dealing with specific physical sectors, tracks, or cylinders on the disk.
- File system drivers access storage through logical block addresses, without needing to know the physical layout or geometry of the disk.

### **Storage Device Interfaces (e.g., ATA, SCSI, NVMe)**

- While each storage device may use different **interfaces** (e.g., **SATA**, **SCSI**, **NVMe**, **USB**, **UFS**, etc.), most modern operating systems provide a **generic interface** to communicate with these devices, abstracting the specifics of the underlying hardware.
- Linux provides kernel drivers and subsystems that handle these interfaces, such as the **SCSI subsystem** for many devices and the **NVMe driver** for solid-state drives.

### **The Linux I/O Stack**

- Linux abstracts disk I/O through a layered stack:
    - **Device Drivers**: Low-level drivers specific to the disk hardware (e.g., SCSI, ATA, NVMe).
    - **Block Layer**: Handles operations like read, write, and direct access to block devices.
    - **File Systems**: Operates on top of the block layer and interacts with block devices via the block layer’s API (e.g., ext4, Btrfs, XFS).

### **Device Mapper**

- The **device-mapper** framework in Linux provides a way to create virtual block devices. This can be used for things like software RAID, LVM (Logical Volume Management), and encryption, which layer on top of physical disks.
- The file system does not need to understand the specifics of the underlying virtual device — it only interacts with a block device through the block layer.

### **UDEV and Device Nodes**

- **UDEV** is responsible for managing device nodes in the `/dev` directory, which are used to represent devices (such as hard disks) in the file system. For instance, `/dev/sda` represents the first hard disk, and `/dev/nvme0n1` represents an NVMe drive.
- File system drivers use these device nodes to access storage devices, but the device driver manages the actual communication with the hardware.

### **Virtual File System (VFS)**

- The **VFS** is a key abstraction in Linux that provides a common interface for interacting with different file systems. It abstracts file operations (open, read, write, etc.) from the underlying file system driver, allowing multiple file systems to coexist and be used by the OS without the application needing to know which one it’s interacting with.
- VFS acts as a middle layer between the user space and the file system drivers, ensuring that file system drivers can be written independently of the device driver specifics.

### **SCSI Block Layer**

- **SCSI** and **ATA** are widely used in storage devices, and the **SCSI block layer** abstracts commands and responses between the kernel and the device. This block layer is crucial for file system interaction because it provides a standard API to access data on various disk types.

## How to list my disk sectors size? How to get the numbers of sector of my disk?

1. **`lsblk -o NAME,SIZE,ROTA,TYPE,SECTORS`**: Lists block devices along with the number of sectors and other relevant information.
2. **`sudo fdisk -l /dev/sda`**: Displays partition details, including sector size and total number of sectors for the specified disk (`/dev/sda`).
3. **`sudo parted /dev/sda unit s print`**: Shows disk information in sectors, including sector size and the total number of sectors for the disk (`/dev/sda`).
4. **`sudo hdparm -I /dev/sda | grep "Sector size"`**: Queries low-level disk information to display the sector size for the specified disk (`/dev/sda`).
5. **`sudo blockdev --getsize64 /dev/sda`**: Displays the total number of sectors on the disk (`/dev/sda`).
6. **`sudo blockdev --getss /dev/sda`**: Retrieves the sector size (in bytes) for the specified disk (`/dev/sda`).
    
    ## **Storage / File Format**
    
    > A **storage format** refers to the specific way data is organized, encoded, and stored on a storage medium to optimize access, retrieval, and efficiency.
    > 
    
    ## Storage Models
    
    | Storage Format | Description | Common Use Cases |
    | --- | --- | --- |
    | **SSTable (Sorted String Table)** | Immutable key-value storage format where keys are stored in a sorted order. | LSM (Log-Structured Merge) trees, databases like Cassandra |
    | **Parquet** | Columnar storage format designed for efficient data processing and compression. | Big data processing, Hadoop, Spark, data warehousing |
    | **ORC (Optimized Row Columnar)** | Columnar storage format optimized for large-scale data processing. | Data warehousing, Hive, Hadoop |
    | **Avro** | Row-based storage format designed for data serialization. | Data interchange between systems, Hadoop, Kafka |
    | **JSON** | Text-based format for storing structured data using key-value pairs. | Web APIs, NoSQL databases, configuration files |
    | **CSV (Comma-Separated Values)** | Plain text format for tabular data where each line corresponds to a row, and columns are separated by commas. | Data import/export, spreadsheets, simple data storage |
    | **HDF5 (Hierarchical Data Format version 5)** | File format and set of tools for managing complex data. | Scientific data, numerical data analysis |
    | **Protocol Buffers** | Language-neutral, platform-neutral extensible mechanism for serializing structured data. | Inter-service communication, data storage |
    | **Apache Arrow** | Columnar in-memory format optimized for analytical processing and data interchange. | Data analytics, machine learning, big data processing |
    | **Feather** | Lightweight binary columnar format for data frames. | Fast data interchange between Python and R |
    | **SQLite** | Lightweight, self-contained SQL database engine with a file-based storage format. | Mobile applications, embedded systems |
    | **Page-Oriented** | Organizes data into fixed-size pages, optimizing for random access. | General-purpose databases, OLTP (Online Transaction Processing) |
    | **Column-Oriented** | Stores data by columns rather than rows, optimizing for read-heavy operations. | OLAP (Online Analytical Processing), data warehousing |
    | **Object-Based** | Stores data as objects, which include the data itself, metadata, and a unique identifier. | Cloud storage, large-scale unstructured data management |
    | **File-Based** | Manages data as files within a hierarchical file system. | Traditional file systems, document management |
    
    ## Tools
    
    > 
    
    | **Category** | **Subcategory** | **Description** |
    | --- | --- | --- |
    | **File Systems** | Local File Systems | Manages data storage on a single device (e.g., **ext4**, **NTFS**, **HFS+**). |
    |  | Distributed File Systems | Provides access to files across multiple machines (e.g., **NFS**, **GlusterFS**, **CephFS**). |
    |  | Clustered File Systems | Supports concurrent access across nodes (e.g., **Lustre**, **IBM GPFS**). |
    |  | Journaling File Systems | Logs changes before applying them to prevent corruption (e.g., **ext4**, **XFS**). |
    |  | Log-Structured File Systems | Writes data sequentially to optimize performance (e.g., **F2FS**, **LFS**). |
    |  | Flash File Systems | Designed for NAND flash storage (e.g., **YAFFS**, **UBIFS**). |
    | **Block Storage Systems** | Local Block Storage | Directly manages block devices for efficient data access (e.g., **LVM**, **ZFS**, **Btrfs**). |
    |  | Distributed Block Storage | Spreads block storage across multiple nodes (e.g., **Ceph RBD**, **Sheepdog**). |
    | **Object Storage Systems** | Cloud Object Storage | Stores data as objects with metadata and unique IDs (e.g., **Amazon S3**, **Google Cloud Storage**). |
    |  | On-Premises Object Storage | Local object storage for high-scale workloads (e.g., **MinIO**, **Ceph Object Gateway**). |
    | **Database Storage Systems** | Relational Databases | Structured storage using tables and SQL (e.g., **PostgreSQL**, **MySQL**, **SQLite**). |
    |  | NoSQL Databases | Flexible schema storage for unstructured data (e.g., **MongoDB**, **Cassandra**). |
    |  | NewSQL Databases | Combines SQL and NoSQL benefits (e.g., **CockroachDB**, **Google Spanner**). |
    |  | Time-Series Databases | Optimized for sequential data (e.g., **InfluxDB**, **Prometheus**). |
    |  | Graph Databases | Designed for relationship-based queries (e.g., **Neo4j**, **ArangoDB**). |
    | **Software-Defined Storage (SDS)** | Storage Virtualization | Abstracts physical storage for flexible management (e.g., **OpenStack Cinder**, **VMware vSAN**). |
    |  | Hyperconverged Storage | Integrates compute, storage, and networking (e.g., **Nutanix**, **ScaleIO**). |
    | **Backup & Archival Storage** | Backup Software | Automates data backup (e.g., **Bacula**, **Veeam**, **Restic**). |
    |  | Archival Storage | Long-term, infrequent-access storage (e.g., **Amazon Glacier**, **IBM Tivoli Storage Manager**). |
    | **Caching & Performance Optimization** | Distributed Caching | Speeds up access to frequently used data (e.g., **Redis**, **Memcached**). |
    |  | Storage Tiering | Moves data between different types of storage for cost optimization (e.g., **DMCache**, **Intel CAS**). |

## References

- Ousterhout, John, et al. "The RAMCloud storage system." *ACM Transactions on Computer Systems (TOCS)* 33.3 (2015): 1-55.
- Stonebraker, Michael. The design of the Postgres storage system. University of California, Berkeley, College of Engineering, Electronics Research Laboratory, 1987.
- [Storage System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/storage-system.md)
- [Linux  File Systems Stack](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/linux-file-systems-stack.md)
- https://dl.acm.org/toc/tos/2025/21/2
- [Datas Storage](https://www.wikiwand.com/en/Data_storage)
- [Dive Into Systems](https://diveintosystems.org/book/index.html)
- [Introduction to File Locking in Linux](https://www.baeldung.com/linux/file-locking)
- https://en.wikipedia.org/wiki/Computer_data_storage
- https://en.wikipedia.org/wiki/Data_degradation