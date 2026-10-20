---
tags: [storage-system]
---

# SSTable

- [Memtable](note.html?n=technica/computation/data-system/data-system-conceptual-model/memtable.md)

> An **SSTable** (Sorted String Table) is a persistent, ordered, immutable data structure used in distributed storage systems to store large amounts of structured data in a sorted sequence, enabling efficient lookups and range scans.
> 

> An **SSTable** provides a persistent, ordered immutable map from keys to values, where both
keys and values are arbitrary byte strings.
> 

> Internally, each **SSTable** contains a sequence of blocks (typically each block is **64KB** in size, but this is conﬁgurable). A **block index** (stored at the end of the **SSTable**) is used to **locate blocks**; the index is loaded into memory when the **SSTable** is opened.
> 

## References

[Key-Value Data Model](note.html?n=technica/computation/data-system/data-system-conceptual-model/key-value-data-model.md)