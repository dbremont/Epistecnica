# Vector Data System

- [Vector Data Model](note.html?n=technica/computation/data-system/data-system-conceptual-model/vector-data-model.md)

> 

> **Vector databases** support a wide range of search types for various applications, and the supported search types depend on the specific use case and the types of vectors (e.g., text, image, audio) stored in the database.
> 

> A **"Vector Search Engine"** is a technology that enables efficient searching and retrieval of data by representing items as vectors in a multidimensional space, facilitating similarity comparisons for tasks like content recommendation and image retrieval.
> 

> Note: Vector Search Engine used vector databased.
> 

## Index

Here's a list of **expected search types** that **vector databases** can support:

- **Exact Matching Search**: Retrieve vectors that match the query vector exactly.
- **Nearest Neighbors Search**: Find the most similar vectors to a query vector. This is often performed using similarity measures like cosine similarity or Euclidean distance.
- **Range Search**: Retrieve vectors that fall within a specific range of similarity to a query vector.
- **K-Nearest Neighbors (K-NN) Search**: Retrieve the K vectors most similar to a query vector. K-NN search is a type of nearest neighbor search.
- **Approximate Nearest Neighbors (ANN) Search**: Find an approximate set of nearest neighbors that may not be the absolute nearest but are within an acceptable error margin. This is useful for improving search efficiency in high-dimensional spaces.
- **Similarity Threshold Search**: Retrieve vectors with a similarity greater than or equal to a predefined threshold.
- **Semantic Search**: Perform searches based on the meaning or semantics of the vectors. For example, find vectors that are semantically related to a query.
- **Recommendation Search**: This type of search recommends items or content based on user preferences or similar items. Collaborative filtering and content-based recommendations are examples.
- **Time Series Search**: Search for similar time series data patterns. This is commonly used in applications like anomaly detection and forecasting.
- **Geospatial Search**: Retrieve vectors related to specific geographic locations. Useful for location-based services and geospatial data analysis.
- **Tag-Based Search**: Find vectors associated with specific tags or labels. Common in image and video search.
- **Category-Based Search**: Retrieve vectors that belong to specific predefined categories or classes.
- **Multimodal Search**: This technique combines vectors from different modalities (e.g., text and images) for searching and retrieval. It is often used in cross-modal search applications.
- **Fuzzy Search**: Find vectors similar to a query but not necessarily an exact match.
This is useful for handling typographical errors or approximate matches.
- **Complex Query Search**: Perform searches based on complex queries that involve multiple criteria or conditions.
- **Streaming Search**: Continuously search and retrieve vectors from a real-time data stream.
- **Time-Based Search**: Search for vectors based on time-specific criteria, such as creation or modification timestamps.
- **Composite Search**: Combine multiple search types or criteria to find vectors that satisfy complex conditions.

## Data Model

> 

| **Data Model** | **Description** | **Use Case** | **Storage Format** |
| --- | --- | --- | --- |
| **Vector Space Model** | Represents data points as high-dimensional vectors. | Text, image, and document similarity search. | Dense matrices, embedding tables. |
| **Inverted Index with Vectors** | Combines keyword index with vector representations. | Hybrid search (keyword + semantic). | Inverted index, dense matrix for vectors. |
| **ANN Indexes (HNSW, IVF)** | Efficient structures for approximate nearest neighbor search. | Large-scale, high-dimensional vector search. | Tree-based or graph-based index structures. |
| **Embedding Table** | Stores embeddings of entities in a table. | NLP, image recognition. | Dense matrices or binary embeddings. |
| **Vector Database (Milvus, Pinecone)** | Managed systems optimized for vector similarity search. | Large-scale production search systems. | Vector indexes, HNSW, IVF, or other ANN algorithms. |
| **Graph-Based Model** | Represents knowledge as nodes/edges with vectors for semantic relationships. | Knowledge graph-based applications. | Graph databases (e.g., Neo4j) with embedded vectors. |
| **Dense Matrices** | Stores vectors in matrix form for efficient computation. | Embedding storage for ML tasks. | Dense matrices (e.g., NumPy arrays, HDF5, TFRecord). |

## References

- [What is a vector search engine?](https://dev.to/asmitbm/what-are-vector-search-engines-3lp1)
- [‣](https://app.notion.com/p/2d6d05682f2844a7b7ead9307b4bbeeb?pvs=21)
- [‣](https://app.notion.com/p/03e70c9866124cf5883b6b771e2b3a20?pvs=21)
- [‣](https://app.notion.com/p/ba87d043299946f0889e4422a120a3a8?pvs=21)

## Case Study

| **Data System** | **Description** |
| --- | --- |
| **Milvus** | Open-source vector database designed for efficient similarity search and analytics of large-scale vector data. |
| **Pinecone** | Fully managed vector database optimized for similarity search in large datasets. |
| **Weaviate** | Open-source vector search engine that supports semantic search and knowledge graph integration. |
| **FAISS (Facebook AI Similarity Search)** | A library developed by Facebook for efficient similarity search and clustering of dense vectors. |
| **Vespa** | Open-source search engine optimized for vector search and machine learning. |
| **Qdrant** | Vector search engine optimized for machine learning applications and embeddings. |
| **Chroma** | Open-source vector database designed for high-performance vector search. |
| **Zilliz Cloud** | Managed vector database offering cloud-based solutions for fast similarity search. |
| **PGVector** | … |

## References

- https://blog.wilsonl.in/corenn/