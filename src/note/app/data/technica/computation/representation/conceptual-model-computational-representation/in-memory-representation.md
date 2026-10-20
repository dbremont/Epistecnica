---
tags: [data-structure]
---

# In-Memory Representation


> **"In-memory representation"** refers to the way data is stored and structured directly in a computer's main memory (RAM), enabling fast access and manipulation by the processor.
> 

> A type is a set of value and operations allowed o those types.
> 

> A value from a data type is used to represent a piece of information about some aspect of the world / problem domain.
> 

## Taxonomy

| **Category** | **Data Structure** | **Description** | **Use** |
| --- | --- | --- | --- |
| **Linear** | Array | Fixed-size contiguous memory elements of the same type | Random access, static lists, matrix representation |
|  | Dynamic Array / Vector | Resizable array with contiguous memory | Lists requiring dynamic growth, implementing stacks/queues |
|  | Linked List (Singly) | Sequence of nodes with value and pointer to next | Insertions/deletions at arbitrary positions, queues |
|  | Linked List (Doubly) | Nodes have next and previous pointers | Bi-directional traversal, LRU caches |
|  | Circular Linked List | Last node points to first | Round-robin scheduling, circular buffers |
|  | Stack | LIFO (Last In, First Out) collection | Function call management, expression evaluation |
|  | Queue | FIFO (First In, First Out) collection | Task scheduling, BFS traversal |
|  | Deque | Double-ended queue | Sliding window problems, caching |
|  | Skip List | Probabilistic linked structure with multiple levels | Fast search/insert/delete (~O(log n)), ordered sets/maps |
| **Hash** | Hash Table / Hash Map | Key-value store with hash function | Fast lookup, dictionaries, caches |
|  | Cuckoo Hash Table | Hash table with relocation strategy | High-performance hash maps with constant-time lookup |
|  | Bloom Filter | Probabilistic set membership structure | Checking existence with space efficiency, network caches |
|  | Count-Min Sketch | Approximate frequency counting | Streaming analytics, network traffic monitoring |
| **Tree** | Binary Tree | Node with up to two children | Hierarchical data, expression trees |
|  | Binary Search Tree (BST) | Binary tree with left<node<right | Sorted data storage, search operations |
|  | AVL Tree | Self-balancing BST using rotations | Ordered maps/sets with guaranteed O(log n) operations |
|  | Red-Black Tree | Balanced BST with color rules | Standard library implementations (TreeMap, TreeSet) |
|  | B-Tree / B+-Tree | Multi-way search tree for disks | Databases, file systems, range queries |
|  | Trie (Prefix Tree) | Tree for string storage, nodes for characters | Autocomplete, dictionary lookups, IP routing |
|  | Suffix Tree | Compact tree of all suffixes of a string | String matching, bioinformatics, compression |
|  | Segment Tree | Tree for range queries and updates | Range sum/min/max queries in arrays |
|  | Fenwick Tree / BIT | Binary Indexed Tree for cumulative frequency | Efficient prefix sums, frequency counting |
|  | k-d Tree | Multi-dimensional binary tree | Spatial searches, nearest neighbor |
|  | QuadTree | Tree dividing 2D space into quadrants | Image processing, spatial indexing, GIS |
|  | Octree | 3D analog of quad tree | 3D graphics, voxel storage, collision detection |
|  | R-Tree | Spatial indexing tree | GIS, spatial databases, rectangle intersection |
|  | Interval Tree | Stores intervals and allows overlap queries | Scheduling, computational geometry |
| **Graph** | Adjacency Matrix | 2D matrix representing edges | Dense graphs, O(1) edge lookup |
|  | Adjacency List | List of neighbors for each vertex | Sparse graphs, BFS/DFS traversal |
|  | Edge List | List of edges (pairs of vertices) | Graph algorithms, network representation |
|  | Incidence Matrix | Matrix of vertices vs edges | Edge-based graph operations, theoretical graph studies |
| **Heap** | Binary Heap | Complete binary tree satisfying heap property | Priority queues, scheduling |
|  | Fibonacci Heap | Heap supporting fast decrease-key | Dijkstra, Prim’s algorithm, amortized efficient PQ |
|  | Binomial Heap | Heap supporting merge operation efficiently | Advanced priority queue operations |
|  | Pairing Heap | Simplified mergeable heap | Practical priority queue in graphs |
| **Multiset** | Hash Set | Unordered collection of unique items | Membership checks, fast insertion/deletion |
|  | Tree Set | Ordered set using BST | Sorted collections, range queries |
|  | Multiset / Bag | Allows duplicates, tracks count | Frequency counting, histogram |
| **Text** | Rope | Balanced tree for long string manipulation | Efficient concatenation, text editor buffers |
|  | Suffix Array | Array of sorted suffixes | Substring search, pattern matching |
|  | DAWG / Directed Acyclic Word Graph | Compressed automaton of all substrings | Dictionary storage, substring queries |
| **Specialized** | LSM Tree | Log-structured merge tree | High write-throughput databases |
|  | Skip Graph | Probabilistic graph-based ordered structure | Distributed systems, peer-to-peer lookup |
|  | Disjoint Set / Union-Find | Tracks set membership and merges | Kruskal’s algorithm, connected components |
|  | K-ary Heap | Heap with k children per node | Optimized priority queues |
|  | Sparse Table | Preprocessed table for static range queries | Range min/max queries in O(1) |
|  | Treap | Randomized BST using priorities | Balanced BST with probabilistic guarantees |
|  | Van Emde Boas Tree | Supports fast operations on bounded integers | Fast integer priority queues, predecessor queries |
|  | Cartesian Tree | Heap-ordered binary tree | Range queries, RMQ, Cartesian decompositions |
| **Matrix** | Dense Matrix | Standard contiguous storage | Linear algebra, numerical computation |
|  | Sparse Matrix | Only non-zero elements stored | Sparse linear algebra, graph adjacency |
|  | Block Matrix | Matrix split into blocks for efficiency | High-performance computing, parallel algorithms |
| **Hybrid** | Forward Index | Maps documents to terms | Search engines, indexing |
|  | Inverted Index | Maps terms to documents | Full-text search, search engines |
|  | Spatial Hashing | Hashing space for spatial objects | Collision detection, graphics |
|  | Circular Buffer | Fixed-size buffer with wraparound | Streaming data, audio/video processing |
|  | Memory Pool / Arena | Pre-allocated fixed-size memory blocks | Fast allocation/deallocation, embedded systems |
|  | Rope | Tree-based string representation | Efficient string concatenation and splitting |
|  | Zipper | Focused traversal structure | Functional programming, immutable trees |

## References

- [Data structures as topological spaces (2002)](https://news.ycombinator.com/item?id=39396337)
- [Against a Universal Definition of ‘Type’](http://tomasp.net/academic/papers/against-types/against-types.pdf)
- [Types are not sets](https://dl.acm.org/doi/10.1145/512927.512938)
- [The Trouble with Types](https://www.cs.ox.ac.uk/ralf.hinze/WG2.8/31/slides/martin.pdf)
- [The hunt for the missing data type](https://news.ycombinator.com/item?id=39592444)
- [List of Data Structures](https://www.wikiwand.com/en/List_of_data_structures)
- [Data Structure](https://www.wikiwand.com/en/Data_structure)
- [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
- [Data Structures](https://brilliant.org/courses/computer-science-fundamentals/)
- [List of data structures](https://en.wikipedia.org/wiki/List_of_data_structures)
- [Succinct Data Structure](https://en.wikipedia.org/wiki/Succinct_data_structure)
- [6.851: Advanced Data Structures](https://courses.csail.mit.edu/6.851/spring21/)
- [Hyperdimensional Hashing: A Robust and Efficient Dynamic Hash Table](https://bpb-us-e2.wpmucdn.com/sites.uci.edu/dist/4/4834/files/2022/04/HD_Hashing_DAC22.pdf)