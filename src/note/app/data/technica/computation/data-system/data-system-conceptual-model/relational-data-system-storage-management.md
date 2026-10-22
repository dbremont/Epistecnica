# Relational Data System Storage Management

- [Heap File Organization](note.html?n=technica/computation/data-system/data-system-conceptual-model/heap-file-organization.md), [Buffer Manager](note.html?n=technica/computation/data-system/data-system-conceptual-model/buffer-manager.md)

> Relational Data System (RDS) Storage Management is the **component of a relational database system responsible for organizing, allocating, accessing, and maintaining data and metadata on storage media** (disk, SSD, or memory). It ensures that tuples, pages, and tables are stored efficiently, retrieved quickly, and kept consistent and durable according to transactional semantics.
> 

> It encompasses both **logical and physical storage**, including structures such as tables, indexes, pages, tuples, and auxiliary storage (e.g., overflow pages, undo/redo logs). Storage management is critical for database performance, reliability, and scalability.
> 

## Storage Hierarchy

> See more in [Storage System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/storage-system.md).
> 

> **Random access** on non-volatile storage is almost always slower than **sequential access**.
> 

![image.png](../assets/note/technica/computation/data-system/data-system-conceptual-model/relational-data-system-storage-management/image.png)

![image.png](../assets/note/technica/computation/data-system/data-system-conceptual-model/relational-data-system-storage-management/image-1.png)

## File Storage

> A **database system stores data** in files on the **operating system**.
> 

> A **database file** is a file on a disk that contains data for a database. Database engines use it to store data in a structured and organized manner, allowing for efficient and reliable access to the data.
> 

> A **database file** may contain one or more tables, indexes, views, and other database objects. Each object is stored in a specific part of the file, such as a table being stored in a dedicated section of the file, and an index being stored in another section.
> 

> Database files are typically stored on a disk or a storage device, and the database engine manages the reading and writing of data to and from the file. The file may be divided into pages, which are the units of storage used by the database engine to store data on disk.
> 

| **Aspect** | **Description** |
| --- | --- |
| **Storage Unit** | Data is stored in structured units: pages/blocks (smallest I/O unit), extents (contiguous pages), and segments (collection of extents for an object). |
| **File Type** | Includes **data files** (actual table/index data), **log/transaction files** (for recovery and durability), **control/metadata files** (database structure info), and **temporary files** (intermediate results). |
| **Data Organization** | Can be **heap (unordered)**, **clustered/sorted** (physical order by key), or **partitioned** (split across multiple files/disks). |
| **Index Storage** | Indexes are separate structures (B-tree, bitmap, etc.) stored in their own segments or files to optimize query access. |
| **Tablespaces  (Logical Grouping)** | Logical grouping of files to manage storage placement, improve I/O performance, and simplify administration. |
| **I/O Strategy** | Pages/blocks are read into memory buffers; frequent pages are cached; log writes are sequential to ensure durability. |
| **File Management Strategy** | Can use **file-per-table** (simplifies backup), **shared-file storage** (reduces file overhead), and disk strategies (RAID, SSDs) to optimize performance. |
| **Durability & Recovery** | Transaction logs and backup files ensure data integrity and allow recovery in case of failures. |
| **Scalability** | Supports growth by adding files, partitions, or tablespaces without major reorganization. |
| **Performance Considerations** | Physical layout, page size, extent allocation, and I/O patterns directly affect query speed and storage efficiency. |

### Vendor

**Database files** can come in various formats, depending on the database engine being used. Some popular **database file formats** include:

- **SQL Server** database files (MDF and LDF) used by Microsoft SQL Server
- **Oracle** database files (DBF) used by Oracle Database
- **PostgreSQL** database files (PGDATA) used by PostgreSQL
- **MySQL** database files (MYD and MYI) used by MySQL

### File

- **Header**: The header is the first part of the database engine file and contains information about the file itself, such as the file format, version number, and size.
- **Data pages**: Data pages are the units of storage used by the database engine to store data. Each page typically contains a fixed number of bytes, such as 4KB or 8KB, and may be allocated to store a single record or multiple records.
- **Index pages**: Index pages are used to store index data, which is used by the database engine to quickly locate records based on the value of one or more fields.
- **Free space**: Free space is used to store data that has been deleted or moved from the file. The database engine may reuse free space to store new data as needed.
- **Allocation structures**: Allocation structures, such as bitmaps or linked lists, are used to keep track of which pages or extents are currently in use and which are free.
- **Transaction logs**: Transaction logs are used to record changes to the data in the database engine file. This can be used to recover data in the event of a system failure or other problem.
- **Backup information**: Backup information may be stored in the database engine file to allow for easy backup and restore operations.

## Page Storage

> A **page** is a fixed-size block of data. - It can contain tuples, meta-data, indexes, log records…  Most systems do not mix page types. - Some systems require a page to be self-contained. - Each page is given a unique identifier. The DBMS uses an indirection layer to map page IDs to physical locations.
> 

> These pages contain the actual data stored in the database, such as rows in a table. They may be organized in different ways depending on the storage engine, but they usually store fixed-length or variable-length records.
> 

> Page size is usually fixed (e.g., 4 KB, 8 KB, 16 KB) and varies by DBMS.
> 

> Understanding page types is crucial for performance tuning, indexing strategies, and transaction management.
> 

> There are three different notions of “pages” in a DBMS: - Hardware Page (usually 4KB) - OS Page (usually 4KB) - Database Page (512B-16KB).
> 

### Type

| **Page Type** | **Description** |
| --- | --- |
| **Data Page** | Stores actual table row data (tuples). Most common page type. May contain multiple rows, depending on the page size and row size. |
| **Index Page** | Stores index entries to facilitate quick lookups. Can include B-tree index pages, bitmap index pages, or other structures depending on the DBMS. |
| **LOB  (Large Object Page)** | Stores large objects such as BLOBs (binary large objects) or CLOBs (character large objects) that do not fit in normal data pages. |
| **Free Space (Free List Page)** | Tracks free space available in data pages for efficient insertion of new rows. |
| **Overflow Page** | Used when a row, index entry, or LOB does not fit in its designated page. Holds the “overflow” portion of the data. |
| **Transaction (Undo) (Rollback Page)** | Maintains undo or rollback information for transaction management, enabling rollback of incomplete transactions. |
| **Transaction Log Page** | Stores log records for write-ahead logging (WAL), including changes to data, for recovery and durability. |
| **System (Metadata Page)** | Holds database metadata like schema definitions, page maps, allocation tables, and system catalogs. |
| **Pointer (Mapping Page)** | Maintains pointers or mapping between logical storage structures (like tables or partitions) and physical pages. |
| **Temporary (Work Page)** | Used for intermediate computations like sorting, joining, or temporary tables. Often stored in temp tablespaces. |

### **(Layout) Data Page**

> What is the layout of a **Data Page?**
> 

> Every **page* contains a *header* of metadata about the page’s contents. - Page Size - Checksum - DBMS Version - Transaction Visibility - Compression Information - Some systems require pages to be selfcontained (e.g., Oracle).
> 

Aspect:

> How to characterize a database data page?
> 

| **Category** | **Value** | **Description** |
| --- | --- | --- |
| **Type** | Heap | Stores records in no particular order; new records are appended. |
|  | Clustered | Stores records ordered by a clustering key (usually a primary key). |
|  | Index | Stores index entries (e.g., B-tree, bitmap) pointing to data records. |
|  | Overflow / Overflow Chain | Used for variable-length or large records that don’t fit in primary pages. |
|  | Temporary / Scratch | Used for intermediate operations, e.g., sorting or joins. |
| **Size** | Fixed | Page size is fixed by DBMS; affects I/O and storage efficiency. |
|  | Variable | Page size can vary depending on records or DBMS settings. |
| **Access Method** | Sequential | Accessed via sequential scan or append mode. |
|  | Random | Accessed via index or direct row lookup. |
| **Usage** | Data | Stores actual table records. |
|  | Metadata | Stores system metadata like headers, free space info, or page directory. |
| **Compression** | Compressed | Data stored in page is compressed to save space. |
|  | Uncompressed | Data stored as-is. |
| **Content** | Homogeneous | Contains records of the same table or type. |
|  | Mixed | Contains multiple types of records or system info. |
| **Capacity** | Full | Page is filled to near maximum capacity. |
|  | Partial | Page has free space for future inserts or updates. |
| **Identity** | Page ID | Unique identifier for the page within the storage structure. |
| **Linkage** | Linked | Part of a chain or list (e.g., overflow chain, free list). |
|  | Unlinked | Standalone page, not part of any chain. |
| **Concurrency Control** | Locked | Page is under a lock (shared/exclusive) for concurrency management. |
|  | Unlocked | Page is not currently locked. |
| **Update** | In-place | Records are updated directly within the same page. |
|  | Out-of-place / Versioned | Updates create new versions elsewhere; old version remains. |
| **Recovery Info** | WAL / Redo | Page contains logging info for recovery in case of crash. |
|  | None | No recovery info stored in page. |
| **Fragmentation Behavior** | High | Tends to fragment due to variable-length records, deletions, or updates. |
|  | Low | Maintains contiguous free space; minimal fragmentation. |
| **Durability** | Persistent | Changes survive crashes after commit. |
|  | Temporary | Page content is ephemeral; discarded on session end or crash. |
| **Layout** | Tuple-Oriented | Each page stores multiple complete tuples; traditional relational storage. |
|  | Log-Structured | Pages store data as an append-only log; optimized for write-heavy workloads. |
|  | Index-Organized | Data is stored in the order of a primary index; pages combine index and data. |

**Layout:**

| **Section** | **Description** |
| --- | --- |
| **Page Header** | Small fixed-size area at the beginning of the page. Contains metadata like page ID, type (data/index), LSN (log sequence number), checksum, free space offset, slot count, etc. |
| **Row Data Area** | Stores the actual table rows (tuples). Rows are written sequentially from the top of the page downward. Each row usually has: row header (with status bits, length, transaction info) + actual column data. |
| **Free Space** | A variable-sized area between the row data and the slot directory. Used for inserting new rows or expanding variable-length columns (if possible). |
| **Slot Directory (Row Offsets)** | Located at the end of the page, grows upward. Each slot contains a pointer (offset) to the beginning of a row in the Row Data Area. Enables row movement inside the page without changing external references (row IDs). |

Data Page Storage Model:

| **Data Page Storage Model** | **Description** | **Case Study** |
| --- | --- | --- |
| **Heap File Organization** | Pages are unordered; new records go into the first page with space (or a new page). Fast inserts, slower lookups (full scan). | PostgreSQL heap tables (default). Good for append-heavy workloads. |
| **Sequential / Sorted File Organization (ISAM-like)** | Records kept sorted by key physically. Good for range scans and batch reads. Insertions may require page splits or reorganizations. | Early ISAM-based DBMS; read-mostly systems (e.g., banking batch systems). |
| **Clustered (Ordered) Storage** | Data pages are physically ordered by a clustering key. Enables fast range scans and ordered retrieval without extra sorting. | InnoDB tables (MySQL) where primary key is clustered. |
| **Hash-Organized Storage (Static)** | Hash function maps records directly to data pages (buckets). Constant-time lookup if hash is uniform. | Simple hash-based storage engines. |
| **Extendible Hashing Storage** | Directory-based dynamic hashing; can grow/shrink the number of data pages as needed. | DB2 hash-organized tables. |
| **Linear Hashing Storage** | Incrementally splits buckets/pages to handle growth, avoiding large rehash operations. | Used in some research DBMS and embedded KV stores. |
| **Columnar Data Page Layout** | Pages store column values contiguously, not rows. Great compression and fast column scans. | Parquet, ORC, and column stores (Vertica, Redshift). |
| **Log-Structured / Append-Only Pages** | Data written sequentially into new pages (immutable). Old versions cleaned up later (compaction). | Write-heavy systems (Cassandra SSTables, PostgreSQL heap with VACUUM). |
| **Packed / Reorganized Storage** | Periodically rewrites data pages to eliminate fragmentation and pack records tightly. | SQLite (after VACUUM), embedded DBs. |

**Data Page Size Tradeoff Model:** 

| **Factor** | **Small Page Size (e.g., 4 KB)** | **Large Page Size (e.g., 16–32 KB)** | **Tradeoff (Effect)** |
| --- | --- | --- | --- |
| **I/O Granularity** | Reads/writes fewer bytes per I/O — good if you only need a few rows (OLTP). | Reads/writes more bytes per I/O — good for range scans or sequential access (OLAP). | Choose based on access pattern: random vs. sequential. |
| **Memory Utilization** | Better cache efficiency for point lookups — less wasted buffer space. | Fewer pages in buffer cache, each page holds more rows. Can increase cache hit rate for full scans but waste memory for sparse access. | Affects buffer pool design. |
| **Concurrency** | More pages → finer-grained latching/locking → more parallelism. | Fewer pages → coarser-grained locking → may cause contention under high concurrency. | Important for highly concurrent OLTP workloads. |
| **Row Density** | Fewer rows per page, so more pages overall → larger page table / index overhead. | More rows per page → smaller indexes, fewer page reads for the same number of rows. | Big impact on index depth and scan performance. |
| **Fragmentation Sensitivity** | Fragmentation less damaging (small gaps). | Fragmentation more expensive (more wasted space per page). | Matters for frequent deletes/updates. |
| **Network / Storage Bandwidth** | Transmits smaller blocks — lower latency for single-row fetches. | More efficient use of bandwidth for bulk fetches. | Relevant for distributed databases. |
| **Compression Efficiency** | Less benefit from page-level compression (small sample). | Better compression (more redundancy across rows). | Big in columnar storage or compressed rowstores. |
| **Update / Insert Overhead** | Inserts cause more page splits (more pages). | Inserts may cause fewer splits, but each split is more expensive. | Impacts write amplification. |

## Tuple Storage

> How to store tuples in a page?
> 

> N**ote:**This is basically part of the Page Storage Model.
> 

> All **attributes in a tuple** must be word aligned to enable the **CPU** to access it without any unexpected behavior or additional work. Use **passing** - to make sure that the data is align with the CPU Word Size; or used **re-ordering**.
> 

The **DBMS** needs a way to keep track of individual tuples. Each tuple is assigned a unique record identifier.

- Most common: `page_id` + `offset/slot`
- Can also contain file location info. An application cannot rely on these IDs to mean anything.

Storage Model:

| **Model** | **Description** | **Case Study** |
| --- | --- | --- |
| **Heap (Unordered Storage)** | Tuples are stored in no specific order. New tuples are appended to the first available free space. Suitable for OLTP workloads with frequent inserts. | PostgreSQL default table storage; SQL Server heap tables. |
| **Slotted Page / Slot Directory** | Each page has a header (slot directory) storing offsets to tuple locations. Allows variable-length tuples and efficient insert/delete without shifting entire page. | PostgreSQL, IBM DB2. |
| **Contiguous / Fixed-Length Tuples** | Tuples of fixed size are stored sequentially; easy to calculate offsets. Fragmentation is minimal, but space is wasted if tuples are smaller than the fixed size. | Oracle fixed-length column tables; older DB2 tables. |
| **Variable-Length Tuples** | Tuples may vary in size (e.g., VARCHAR columns). Page stores an offset table or directory to track tuple locations. Allows flexible schemas but requires more management for fragmentation. | PostgreSQL, MySQL InnoDB, Oracle. |
| **Log-Structured / Append-Only** | Tuples are appended sequentially; updates create new tuple versions instead of overwriting. Optimized for write-heavy workloads and crash recovery. | LSM-tree databases like RocksDB, LevelDB; Cassandra. |
| **Index-Organized / Clustered** | Tuples are stored in the order of a clustering key; pages act both as data storage and index. Enables fast range scans and sequential access by key. | Oracle Index-Organized Tables (IOT), SQL Server Clustered Index Tables. |
| **Compressed / Column-Oriented** | Tuples are split into columns stored in compressed form; page may store multiple tuples but in column format. Optimized for analytic workloads with large scans. | SAP HANA, Oracle Hybrid Columnar Compression, Vertica. |
| **Overflow / TOASTed Tuples** | Large tuples that don’t fit in a page are stored in overflow pages, with a pointer from the main page. | PostgreSQL TOAST; Oracle LOB storage. |

**Tuple Layout**

> A tuple is essentially a sequence of bytes.
> 

> It’s the job of the DBMS to interpret those bytes into attribute types and values.
> 

> Each tuple is prefixed with a header that contains meta-data about it. - Visibility info (concurrency control) - Bit Map for NULL values. - We do not need to store meta-data about the schema.
> 

| **Component** | **Description** | **Notes** |
| --- | --- | --- |
| **Tuple Header / System Info** | Metadata for the tuple: transaction ID, versioning info (MVCC), row status, length. | PostgreSQL uses `xmin`, `xmax` for MVCC; Oracle has rowid pointers. |
| **Null Bitmap / Flags** | Indicates which columns are NULL; supports variable-length columns. | A bitmap or bitmask; allows efficient storage of nullable columns. |
| **Fixed-Length Column Values** | Values for columns with fixed size (INT, DATE, CHAR(n)). | Stored sequentially in the tuple. |
| **Variable-Length Column Values** | Values for columns with variable size (VARCHAR, BLOB, TEXT). | May include length prefix; can be stored inline or in overflow pages. |
| **Optional Padding / Alignment** | Extra bytes to satisfy CPU/memory alignment requirements. | Depends on DBMS and page architecture. |
| **Overflow / TOAST Reference** | Pointer to external storage if the tuple has very large values. | PostgreSQL TOASTed TEXT or BLOB fields. |

**Tuple Data**

> ¿How to encode data?
> 

> DBMS can physically denormalize (e.g., “pre join”) related tuples and store them together in the same page. - Potentially reduces the amount of I/O for common workload patterns. - Can make updates more expensive.
> 

> Attributes are typically stored in the order that you specify them when you create the table.
> 

- Integer / BigInt / SmallInt / TinyInt
- Float / Real vs. Numeric / Decimal
- Varchar / Varbinary / Text / Blob
- Time / Date / Timesampt
- Large Values: Overflow Storage Pages
- Files: Links to Externals Files (Not Transaction Guaranties).
- Null Data Types: Null Column Bitmap Header,  Special Values and Per Attribute Null Flag.
- External Storage Values

## QA

- How to represent the database in files in disk?
- How to compute over files in disk - using memory? How to move data back-and-forth from disk?

## References

- Zeng, Xinyu, et al. "NULLS!: Revisiting null representation in modern columnar formats." Proceedings of the 20th international workshop on data management on new hardware. 2024.
- Sears, Russell, Catharine Van Ingen, and Jim Gray. "To blob or not to blob: Large object storage in a database or a filesystem?." arXiv preprint cs/0701168 (2007).