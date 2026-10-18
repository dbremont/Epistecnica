---
tags: [learning-system]
---

# Kanerva Machine


> A Kanerva Machine is a neural network designed to efficiently store and retrieve high-dimensional patterns.  Pentti Kanerva first proposed it in 1988.
> 

> The **Kanerva Machine** is particularly useful for storing and retrieving high-dimensional patterns, such as images or text, with low memory requirements and fast retrieval times. It has been used in various applications, including content-addressable memory, recommendation systems, and natural language processing.
> 

> Here is a simplified overview of how a Kanerva Machine works:
> 

| **Step** | **Description** |
| --- | --- |
| **Encoding** | Encodes high-dimensional input patterns into sparse binary vectors using a random projection technique called "count sketch," mapping the input vector to a lower-dimensional space. |
| **Storage** | Stores the sparse binary vectors as “anchors” in a lookup table, where each anchor represents a unique high-dimensional pattern. |
| **Retrieval** | Retrieves the closest anchor to a new input pattern by computing the Hamming distance (bit differences) between the input pattern and all stored anchors, selecting the closest one. |
| **Reconstruction** | Reconstructs the original input pattern by mapping the retrieved anchor back to the high-dimensional space using the count sketch. |
| **Learning** | Learns new patterns by creating and storing a new anchor when presented with an input pattern sufficiently different from all existing anchors. |

## References

- https://en.wikipedia.org/wiki/Sparse_distributed_memory
- [‣](https://app.notion.com/p/d44e77b60e094316bd30ced82d579740?pvs=21)
- Anderson, M. L. (2003). Embodied cognition: A field guide. 149(1), 91–130.
