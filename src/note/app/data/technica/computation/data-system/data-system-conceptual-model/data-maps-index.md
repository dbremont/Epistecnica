---
tags: [index]
---

# Data Maps (Index)

- [B-Tree](note.html?n=technica/computation/data-system/data-system-conceptual-model/b-tree.md), [R Tree](note.html?n=technica/computation/data-system/data-system-conceptual-model/r-tree.md), [LSM Tree](note.html?n=technica/computation/data-system/data-system-conceptual-model/lsm-tree.md), [Suffix Tree](note.html?n=technica/computation/data-system/data-system-conceptual-model/suffix-tree.md), [Skip List](note.html?n=technica/computation/data-system/data-system-conceptual-model/skip-list.md), [Hash Index](note.html?n=technica/computation/data-system/data-system-conceptual-model/hash-index.md), [Inverted Index](note.html?n=technica/computation/data-system/data-system-conceptual-model/inverted-index.md)

> Data Maps (Index) refers to a data structure that organizes and facilitates efficient retrieval of data by mapping keys to corresponding values or locations within a dataset.
> 

## Taxonomy

| **Index Type** | **Description** | **Typical Use Cases** | **Data Domain** | **Tag(s)** |
| --- | --- | --- | --- | --- |
| **B-Tree / B+-Tree** | Balanced tree; B+ variant stores values only at leaf nodes for sequential access. | General-purpose indexing for equality and range queries. | Numeric, string, date/time, ordered categorical data | General-purpose, Range, Equality |
| **Hash Index** | Uses hash tables for fast key lookups; unordered. | Equality lookups (`=`), exact matches. | IDs, UUIDs, hashed values | Equality, Key-Value |
| **Bitmap Index** | Uses bitmaps to represent distinct column values; efficient for low-cardinality columns. | Data warehousing, analytical queries. | Boolean, gender, status flags, categorical data | Analytical, Low-cardinality |
| **BRIN (Block Range Index)** | Stores summaries per block instead of every row. | Very large, ordered tables (time-series, logs) | Sequential/correlated data | Large-table, Summary |
| **Full-Text Index** | Maps terms to document locations; supports tokenized text search. | Full-text search, array membership queries. | Text, documents, JSON/arrays | Text, Search, Inverted |
| **GIN (Generalized Inverted Index)** | Inverted index for composite types. | Full-text, arrays, JSONB. | Documents, arrays | Text, Arrays, Composite |
| **GiST (Generalized Search Tree)** | Extensible tree for complex types. | Ranges, spatial, geometric, full-text. | Spatial, range, text | Extensible, Range, Spatial |
| **SP-GiST (Space-Partitioned GiST)** | Space-partitioned tree for non-balanced trees. | Multi-dimensional, hierarchical partitioned data | Spatial, multidimensional | Multi-dimensional, Spatial |
| **Trie (Prefix Tree)** | Stores strings character by character; supports fast prefix search. | Autocomplete, dictionary lookup. | Strings, words, URLs | String, Autocomplete, Dictionary |
| **Suffix Tree (Array)** | Stores all suffixes of a string; supports fast substring search. | Pattern matching, bioinformatics | Text, DNA/protein sequences | Pattern, Substring, Bioinformatics |
| **Skip List** | Probabilistic sorted linked list structure. | Alternative to B-trees for in-memory fast insertion/search | Numeric, string, ordered in-memory datasets | In-Memory, Ordered, Probabilistic |
| **Forward Index** | Maps document/record to terms it contains. | Text engines, search | Text, documents | Text, Search, Forward |
| **R-Tree** | Hierarchical bounding-rectangle tree for spatial objects. | GIS, spatial queries, spatial joins | 2D/3D spatial data | Spatial, GIS, Hierarchical |
| **Quadtree** | Recursive 2D spatial partitioning tree. | Spatial indexing, graphics, collision detection | 2D spatial data | Spatial, 2D, Partitioning |
| **k-d Tree** | Multi-dimensional binary search tree. | Range search, nearest neighbor queries | Multi-dimensional data (points, vectors) | Multi-dimensional, Range, Spatial |

## Related Concept

| **Concept** | **Description** | **Role** | **Type** |
| --- | --- | --- | --- |
| **Unique Index** | Ensures all values in the indexed column(s) are unique. | Enforces data integrity; prevents duplicates. | Constraint / Index Modifier |
| **Clustered Index** | Determines the physical order of table rows based on the key. | Organizes table storage; improves range queries. | Physical / Index Modifier |
| **Composite Index** | Index on multiple columns combined. | Speeds up queries filtering on multiple columns. | Multi-Column Index |
| **Non-Clustered Index** | Separate structure pointing to table rows. | Supports secondary lookups and selective queries. | Secondary Index |
| **Functional / Expression Index** | Index built on the result of a function or expression. | Optimizes queries using computed or transformed values. | Computed / Expression-Based Index |
| **Partial / Filtered Index** | Index that covers only a subset of table rows meeting a condition. | Reduces storage and improves query performance on filtered subsets. | Filtered / Conditional Index |
| **Covering Index** | Index containing all columns needed to satisfy a query. | Avoids accessing table rows for queries. | Query Optimization / Composite Index |
| **Reverse Key / Reversed Index** | Keys are stored in reversed order to reduce hotspotting. | Improves insert/update performance in high-concurrency systems. | Performance / Specialized Index |
| **Bitmap Join / Derived Index** | Index built to optimize join queries, often in data warehouses. | Speeds up joins and analytical queries. | Analytical / Derived Index |
| **Materialized View Index** | Index built on top of precomputed views. | Accelerates queries using pre-aggregated data. | Precomputed / Derived Index |
| **Expression-Based Index Strategy** | Conceptual approach for indexing computed expressions. | Enables efficient querying of derived or transformed values. | Index Strategy / Optimization |

## Evaluation

> How should I evaluate the overall impact  and effectiveness of Index in a database?
> 

| **Aspect** | **Description** |
| --- | --- |
| **Query Performance** | How much the index speeds up query execution. |
| **Index Usage (Hit Rate)** | How frequently the index is actually used by the query planner. |
| **Storage Cost** | Disk space consumed by the index. |
| **Write Overhead** | Impact on insert, update, delete operations. |
| **Maintenance Cost** | Effort required to rebuild, vacuum, or optimize indexes. |
| **Selectivity (Cardinality)** | Ratio of distinct indexed values to total rows. |
| **Coverage (Query Support)** | Whether the index includes all columns needed by queries. |
| **Redundancy (Overlap)** | Existence of duplicate or overlapping indexes. |
| **Access Patterns** | Match between index type and query workload. |
| **Holistic Impact** | Combined effect on read, write, storage, and maintenance. |

## References

- [Quadtree](https://en.wikipedia.org/wiki/Quadtree)
- [A primer on Roaring bitmaps: what they are and how they work](https://vikramoberoi.com/a-primer-on-roaring-bitmaps-what-they-are-and-how-they-work/)
- [Using bitmaps to run interactive retention analyses over billions of events for less than $100/mo](https://vikramoberoi.com/using-bitmaps-to-run-interactive-retention-analyses-over-billions-of-events-for-less-than-100-mo/)
- [8 Key Data Structures That Power Modern Databases](https://www.youtube.com/watch?v=W_v05d_2RTo)

- [Representation Problem: Sequence (Data)]