---
tags: [problem]
---

# Join


> 

| **Join Algorithm** | **Description** | **Best for** | **Time Complexity** | **Notes** |
| --- | --- | --- | --- | --- |
| **Nested Loop Join** | Compares each row from the first table with every row in the second table. | Small datasets, no indexes | **O(m × n)** | Simple but slow for large tables. |
| **Indexed Nested Loop Join** | Uses an index on the inner table to speed up lookups. | When the inner table has an index. | **O(m × log n)** | Efficient if the index is well-optimized. |
| **Sort-Merge Join** | Sorts both tables, then merges them like in merge sort. | Sorted inputs or large datasets. | **O(m log m + n log n)** | Performs well when data is already sorted. |
| **Hash Join** | Uses a hash table to quickly match records. | Large, unsorted datasets. | **O(m + n)** (average case) | Fast but requires extra memory for the hash table. |
| **Grace Hash Join** | A hash join optimized for disk-based operations. | Disk-based databases, large datasets. | **O(m + n)** | Works in multiple passes when memory is limited. |
| **Hybrid Hash Join** | Optimizes Grace Hash Join by keeping a portion in memory. | Large datasets with limited memory. | **O(m + n)** | Reduces disk I/O compared to Grace Hash Join. |
| **Block Nested Loop Join** | Processes blocks of data at a time to reduce disk I/O. | Large datasets without indexes. | **O(m × (n / B))** | Faster than simple Nested Loop Join. |
| **Broadcast Join** | Broadcasts a small table to all nodes in distributed systems. | Distributed databases, when one table is small. | **O(m + n)** | Used in Spark and BigQuery. |
| **Shuffle Hash Join** | Partitions data across multiple nodes using hashing. | Large distributed joins (e.g., Spark, Hadoop). | **O(m + n)** | Avoids data skew but requires network communication. |