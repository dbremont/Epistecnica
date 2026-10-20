---
tags: [storage-system]
---

# Memtable

- [SSTable](note.html?n=technica/computation/data-system/data-system-conceptual-model/sstable.md)

> A **Memtable** is an in-memory data structure used in distributed databases to store recent writes and updates before they are flushed to disk as immutable SSTables, facilitating fast write operations and efficient data retrieval.
> 

> In-memory in a sorted buffer called a **memtable**.
> 

## References

- **MemTable /** [https://github.com/facebook/rocksdb/wiki/MemTable](https://github.com/facebook/rocksdb/wiki/MemTable)
- Lambov, Branimir. "Trie memtables in cassandra." *Proceedings of the VLDB Endowment* 15.12 (2022): 3359-3371.
- Build a Database Pt. 2: MemTable / [https://adambcomer.com/blog/simple-database/memtable/](https://adambcomer.com/blog/simple-database/memtable/)