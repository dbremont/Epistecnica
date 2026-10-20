---
tags: [domain]
---

# Representation Problem: Associative Data

- [Lock-Free Data Structure](note.html?n=technica/computation/representation/conceptual-model-computational-representation/lock-free-data-structure.md), [Concurrent Map](note.html?n=technica/computation/representation/conceptual-model-computational-representation/concurrent-map.md)

> Associative data is a general technique (and family of data structures) to organize information around keys rather than positions, enabling efficient, semantic, and decoupled access to values.
> 

## Associative Data Specific

| **Data Structure** | **Description** | **Use(s)** |
| --- | --- | --- |
| **Hash Table** | Uses a hash function to map keys to buckets, enabling expected constant-time insertion, lookup, and deletion. | Symbol tables, caches, fast lookup, runtime environments |
| **Map * Associative Array (ADT)** | Abstract key–value mapping interface independent of implementation details. | General data modeling, configuration storage, object representation |
| **Tree-Based Map (Ordered Map)** | Stores key–value pairs in a balanced tree structure, preserving key order. | Range queries, ordered traversal, database and filesystem indexes |
| **Trie / Radix Tree** | Decomposes structured keys (e.g., strings, bit sequences) into prefix paths. | Dictionaries, autocomplete, routing tables, prefix lookup |
| **Graph** | Represents entities as nodes and associations as edges, optionally labeled or weighted. | Network modeling, dependencies, knowledge graphs |
| **Semantic Network** | Graph with typed nodes and labeled relations emphasizing conceptual meaning. | Ontologies, knowledge representation, expert systems |
| **Multidimensional Map** | Maps composite keys (tuples or vectors) to values across multiple dimensions. | OLAP systems, scientific data, sparse tensors, feature stores |
| **Piecewise Map** | Domain is partitioned into regions, each governed by a distinct mapping rule. | Control systems, rule engines, numerical methods, dispatch logic |
| **Interval / Segment Tree** | Tree structure mapping intervals to values or sets of values. | Scheduling, range queries, piecewise functions |
| **Decision Tree** | Hierarchical conditional mapping from input attributes to outputs. | Classification, policy evaluation, rule-based decisions |
| **Relational Index** | Auxiliary structure mapping attribute values to row identifiers in tables. | Database query optimization, fast joins |
| **Content-Addressable Store** | Associates values via hashes of their content rather than symbolic keys. | Version control, deduplication, immutable data storage |

## Performance

> Which are the abstract and concrete performance characteristics?
> 

## References

- https://en.wikipedia.org/wiki/Associative_array