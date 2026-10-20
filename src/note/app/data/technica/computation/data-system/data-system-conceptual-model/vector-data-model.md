---
tags: [data-model]
---

# Vector Data Model

- [Vector Data System](note.html?n=technica/computation/data-system/data-system-conceptual-model/vector-data-system.md)

> A data model can be captured by **⟨Representation, Operations, Semantics⟩**, such that the representation defines the data structure, operations specify valid manipulations, and semantics assign precise meaning to both.
> 

> **Stores** and **queries high-dimensional** vector representations (embeddings) of data, optimized for similarity search.
> 

> **Formalized** using **linear algebra** and metric space theory; similarity often defined via distance functions (e.g., Euclidean, cosine).
> 

## Representation

Data is represented as **multidimensional numeric structures**—vectors (1D), matrices (2D), or higher-order tensors (nD)—that encode features, relationships, or embeddings of objects.

- Each vector, matrix, or tensor corresponds to an entity, document, image, time series, or other complex data item.
- Dense and sparse formats are supported, depending on storage and performance requirements.
- Specialized indexing structures (e.g., hierarchical, graph-based, or quantized indices) are used for efficient similarity search and retrieval.
- The dimensionality and structure capture semantic or relational information, enabling operations like similarity search, transformations, and projections.

## Operator

- **Insertion**: Adding a new vector to the dataset.
- **Deletion**: Removing a vector from the dataset.
- **Similarity Search / k-NN Query**: Finding vectors closest to a query vector according to a distance metric.
- **Distance Computation**: Computing similarity/distance between two vectors (e.g., Euclidean, cosine, Manhattan).
- **Range Query / Threshold Search**: Retrieving all vectors within a certain distance from a query vector.

## Semantic

Semantics are formalized using **linear algebra** and **metric space theory**.

- **Similarity** is defined via a distance function $d(u,v)$ on the vector space, often Euclidean or cosine similarity.
- Operations like k-NN or range queries have precise mathematical definitions based on these distances.
- Guarantees include approximate or exact retrieval, depending on the index and algorithm used (e.g., FAISS, HNSW, Annoy).

## References

- https://github.com/pgvector/pgvector
- [Vector Databases: A Technical Primer](https://news.ycombinator.com/item?id=38971221)
- [Do you need a vector database? (ethanrosenthal.com)](https://news.ycombinator.com/item?id=35550567)