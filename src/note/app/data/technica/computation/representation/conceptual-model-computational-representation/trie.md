---
tags: [data-structure]
---

# Trie


> A **Trie** (pronounced *“try”*) is a **tree-like data structure** used to store a dynamic set of strings, usually for **retrieval and prefix-based operations**. It’s also called a **prefix tree** because keys are stored by their common prefixes.
> 

## Formulation

A **Trie** is a multi-way tree where:

- Each **node** represents a single character (or part of a key).
- The **path from the root to a node** represents a prefix of the stored keys.
- **Keys (strings) are stored implicitly** in the paths from the root to leaf nodes.
- Leaf nodes (or nodes marked with a special flag) indicate the **end of a valid key**.

## Performance

> Which are the performance characteristics of **Trie**?
> 

| **Dimension** | **Description** | **Notes** |
| --- | --- | --- |
| **Lookup Time** | Time to find a key or value. | Typically, O(k), where k is the length of the key; independent of the number of keys stored. Very fast for prefix searches. |
| **Insertion Time** | Time to insert a new key/value pair. | O(k), proportional to key length. Each character may create a new node if it does not exist. |
| **Deletion Time** | Time to remove a key/value. | O(k), may require pruning nodes if they no longer lead to any key. |
| **Memory (Space Usage)** | Amount of memory required to store the structure. | Can be high due to nodes for every character; sparse tries waste memory unless compressed (e.g., Patricia Trie). |
| **Load Distribution** | How evenly data is distributed across nodes (for distributed systems). | Not inherently balanced; can lead to uneven tree depth if keys share long common prefixes. |
| **Fault Tolerance  (Redundancy)** | Ability to handle node failures or data loss. | Standard Tries to have no redundancy; distributed tries can replicate nodes for fault tolerance. |
| **Scalability** | How performance changes as the dataset or network grows. | Lookup/insertion scales with key length, not number of keys; memory usage may become a limiting factor for very large datasets. |
| **Network Overhead** | Amount of network communication required (for distributed structures). | Depends on distribution strategy; prefix-based partitioning may reduce network hops, but naive distribution can increase overhead. |
| **Concurrency & Contention** | Ability to handle multiple simultaneous accesses. | Fine-grained locking possible at node level; read-heavy workloads scale well. |
| **Cache (Locality Effects)** | How well the structure utilizes memory hierarchy. | Poor spatial locality for sparse tries; compressed tries or path compression improve cache performance. |

## Implementation

| **Language** | **Library** | **Description** |
| --- | --- | --- |
| Python | `pygtrie` | Google’s Trie library; supports prefix search, insertion, deletion, and iterators; easy to use for dynamic Tries. |
| Python | `datrie` | Double-Array Trie for Unicode strings; memory-efficient, fast lookups; suitable for static dictionaries. |
| Python | `marisa-trie` | MARISA-based static Trie; very memory-efficient and fast for read-heavy workloads. |
| Java | Apache Commons Collections – `PatriciaTrie` | Compressed Trie / Radix Tree; supports key/value mapping and prefix operations. |
| Java | `Trie4J` | High-performance Java Trie; supports multiple search types, memory-efficient. |
| Java | `datrie-java` | Java binding for Double-Array Trie; efficient for large Unicode datasets. |
| C++ | `marisa-trie` | Efficient static Trie; optimized for fast lookups and memory usage. |
| C++ | `cpp-trie` | Simple, flexible Trie for string keys; good for dynamic operations. |
| C++ | `DAWG` | Directed Acyclic Word Graph; memory-efficient, optimized for prefix searches. |
| JavaScript / TypeScript | `prefix-trie-ts` | TypeScript Trie library; supports insertion, search, and prefix matching. |
| JavaScript | `dawg-lookup` | DAWG-based Trie for fast dictionary lookups; memory-efficient. |

## Case Study

> Suppose we store the words: `"cat"`, `"car"`, `"cap"`:
> 

```bash
        (root)
        / 
       c
       |
       a
     / | \
    t  r  p
```

## References

- https://github.com/pytries/marisa-trie
- https://en.wikipedia.org/wiki/Trie
- https://commons.apache.org/proper/commons-collections/apidocs/org/apache/commons/collections4/trie/PatriciaTrie.html
- https://github.com/google/pygtrie/tree/master