---
tags: [domain]
---

# Representation Problem: Dataset (Structured)


> **Domain**: A dataset is a structured collection of data, typically organized into rows (observations) and columns (variables), representing a specific set of observations or measurements.
> 

> **Data Model** is a collection of tools for modelling the real world, the molled is called a database. Examples: Relational, Key/Value, Graph, Document / Object, Wide-Column / Column-family, Array / Matrix / Vectors, Hierarchical, Network, Multi-Value. Note : Sometimes the database is also called a data model.
> 

## Representations Systems

Here's an exploration of different data models for distributed systems presented in a table format:

| Data Model | Description | Examples |
| --- | --- | --- |
| Relational Data Model | Organizes data into tables with rows and columns, following the principles of relational algebra and ensuring data integrity through constraints and relationships between tables. Queries are performed using SQL (Structured Query Language). | MySQL, PostgreSQL, Oracle Database |
| Document Data Model | Document databases store data as flexible and self-contained documents, typically in JSON or BSON format. They allow for nested structures and dynamic schemas. Document databases offer high flexibility and scalability, making them suitable for semi-structured and unstructured data. | MongoDB, Couchbase, Firebase |
| Key-Value Data Model | Data represents a collection of key-value pairs, providing efficient storage and retrieval of individual records. Due to their simplicity and high throughput, key-value stores are often used for caching, session management, and distributed data storage. | Redis, Amazon DynamoDB, Riak |
| Graph Data Model | Graph databases model data as a network of nodes and edges, where nodes represent entities and edges represent relationships between entities. They excel at querying complex relationships and traversing graph structures efficiently, making them suitable for social networks, recommendation engines, and network analysis applications. | Neo4j, Amazon Neptune, ArangoDB |
| Wide-Column Data Model | Organizes data into tables with rows and columns, similar to the relational model, but allows for column families with columns that vary from row to row, offering flexibility in schema design. Wide-column stores are optimized for read-and-write performance, making them ideal for time-series data, analytics, and content management systems. | Apache Cassandra, Apache HBase, ScyllaDB |
| Time-Series Data Model | The specialized data model is optimized for storing and analyzing time-stamped data points, such as sensor readings, log entries, and financial market data. Time-series databases provide efficient storage, indexing, and querying capabilities tailored to time-series data, enabling real-time analytics and monitoring applications. | InfluxDB, Prometheus, TimescaleDB |
| Replicated Data Model | Distributes copies of data across multiple nodes or datacenters, ensuring redundancy and fault tolerance. Replicated data models can use various consistency and replication strategies, such as eventual consistency, strong consistency, and quorum-based replication, depending on the application's requirements. | Multi-master replication, Active-passive replication, Consistent hashing, CRDTs (Conflict-free Replicated Data Types) |
| Sharded Data Model | Divides data into partitions or shards distributed across multiple nodes, allowing horizontal scaling and improved performance. Sharded data models require partitioning schemes and coordination mechanisms to distribute queries and maintain data consistency across shards. | Horizontal partitioning, Range partitioning, Hash partitioning, Consistent hashing |
| Hybrid Data Model | Combines multiple data models to address diverse requirements and use cases within a single system. Hybrid data models leverage the strengths of different data models, such as relational, document, and graph, to support complex data structures and relationships while maintaining scalability and flexibility. | Polyglot persistence, Multi-model databases |
|  **CRDT (Conflict-free Replicated Data Types)** | CRDTs are data structures designed for distributed systems, allowing multiple replicas to converge to a consistent state without centralized coordination. They enable seamless updates and operations in real-time, even in the presence of network partitions or conflicts. |  |
| **Spark DataFrame** | DataFrame is a distributed collection of data organized into named columns, similar to a table in a relational database. DataFrame API provides a higher-level, more structured, and optimized approach to work with structured and semi-structured data. DataFrames support various data formats, such as CSV, JSON, and Parquet, and enable SQL-like querying capabilities.  |  |
| **Spark Resilient Distributed Dataset (RDD)** | RDD is the fundamental data structure in Apache Spark. It represents an immutable distributed collection of objects that can be processed parallel across a cluster. RDDs offer fault tolerance through lineage information, which allows them to recover lost data.  |  |
| **Distributed Hash Tables (DHTs)** | DHTs are data structures that distribute and organize data across a network of nodes. They provide efficient lookup and retrieval of data in real-time distributed systems. - **OT (Operational Transformation)**: OT is a technique that maintains consistency in collaborative real-time editing environments. It is commonly employed in collaborative text editing tools, document editing platforms, and collaborative drawing applications. OT works by transforming operations on shared data so that they are executed in the correct order, even if multiple users make simultaneous changes. This ensures that the changes made by different users are correctly integrated and avoid conflicts. |  |
| No SQL | Key/Value - Graph - Document - Column-family |  |
| Array / Matrix / Vector | … |  |
| Datalog | … |  |

## Data Exchange Formats

Here's an exploration of different data exchange formats, including Apache Avro, JSON, and XML, presented in a table format:

| Data Exchange Format | Description | Example Use Cases |
| --- | --- | --- |
| Apache Avro | Avro is a binary serialization format that provides compact, fast, and schema-based data serialization. It supports rich data structures, schema evolution, and language independence, making it suitable for efficient data exchange and storage in distributed systems and message-passing frameworks. | Apache Kafka, Apache Hadoop, Apache Spark, Inter-process communication, Log aggregation |
| JSON (JavaScript Object Notation) | JSON is a lightweight, human-readable, and language-independent data interchange format representing data as key-value pairs, arrays, and nested objects. Due to its simplicity, flexibility, and ease of parsing and generation, it is widely used for web APIs, configuration files, and inter-process communication. | Web APIs (RESTful services), Configuration files, Message payloads, AJAX (Asynchronous JavaScript and XML) requests, Data serialization and deserialization |
| XML (eXtensible Markup Language) | XML is a markup language for encoding documents in a human-readable and machine-readable format. It uses tags to define data structures and hierarchies, allowing for flexible and extensible data representation. XML is commonly used for data interchange, configuration files, and structured document representation. | Web services (SOAP), RSS feeds, Configuration files, Document storage, Legacy systems integration |
| Protocol Buffers (protobuf) | Google developed a binary serialization format for efficient and language-neutral serialization of structured data. Protocol Buffers use a schema to define message types, enabling backward and forward compatibility, efficient encoding, and fast serialization and deserialization. They are used for inter-service communication, data storage, and RPC (Remote Procedure Call) frameworks. | Google APIs, gRPC (Remote Procedure Call), Google Bigtable, Distributed systems communication, Inter-process communication |
| MessagePack | MessagePack is a binary serialization format that efficiently packs data into a compact binary format, reducing message size and improving serialization and deserialization performance. It supports various data types and is designed for high-performance data exchange in distributed systems and message-passing frameworks. | Distributed systems communication, High-throughput messaging systems, Inter-process communication, Serialization libraries |
| CSV (Comma-Separated Values) | CSV is a simple text format for representing tabular data in plain text. Each line represents a record, and commas or other delimiters separate fields. Due to their simplicity and ease of parsing, CSV files are widely used for data interchange between spreadsheets, databases, and other software systems. | Spreadsheet data exchange, Database imports and exports, Log files, Configuration files |
| **Apache Arrow** | A cross-language development platform for in-memory data that facilitates efficient data interchange between different systems. |  |
| **FlatBuffers** | FlatBuffers is an open-source data serialization library that allows fast and memory-efficient data access without parsing, making it suitable for performance-critical applications. |  |
| **BSON** | BSON (Binary JSON) is a binary representation of JSON-like documents commonly used in MongoDB for efficient data storage and retrieval. |  |
| **ORC (Optimized Row Columnar)** | A high-performance columnar storage file format used in Hadoop-based systems. |  |
| **Parquet** | A columnar storage file format is used for efficient data storage and processing in big data environments. |  |
| **Feather** | A lightweight and efficient file format for data interchange in data science workflows. |  |
| … | … |  |

## Representation of Data Models

Here's a list of representation mechanisms commonly used in data systems, including Heap File, presented in a table format:

| Representation Mechanism | Description |
| --- | --- |
| Heap File | A primary storage mechanism where records are stored sequentially without any particular order. Records are appended to the file as they are created, resulting in minimal overhead for insertion and deletion but potentially leading to fragmentation and slower retrieval times for unordered queries. |
| Sorted File | Stores records in sorted order based on one or more keys. Sorted files enable efficient retrieval using binary search or other search algorithms, as well as range queries and joins. However, maintaining sorted order may require additional overhead during insertion and deletion operations. |
| Hashing | It uses a hash function to map keys to locations in a data structure, such as a hash table or hash file. Hashing provides fast retrieval and insertion times for exact-match queries but may suffer from collisions, requiring collision resolution techniques like chaining or open addressing. |
| B-Tree | B-trees are a self-balancing tree data structure that maintains sorted data and allows for efficient insertion, deletion, and retrieval operations. They are commonly used in databases and file systems to store indexes and facilitate range queries, providing logarithmic time complexity for most operations. |
| B+ Tree | Like B-trees, B+ trees have additional properties designed to improve performance and disk I/O efficiency. They separate keys from data, maintain a linked list of leaf nodes for range queries, and ensure a balanced distribution of keys across nodes, making them well-suited for database indexing. |
| LSM Tree | A log-structured merge-tree data structure optimized for write-heavy workloads and disk-based storage systems. LSM trees buffer incoming writes in memory and periodically merge them with on-disk structures, reducing the number of disk writes and improving write throughput at the expense of increased read latency. |
| Bitmap Index | Represents sets of values using a bitmap, where each bit corresponds to a unique value or range of values. Bitmap indexes enable fast set-based operations like AND, OR, and NOT, making them efficient for certain types of queries such as data warehousing and OLAP (Online Analytical Processing). |
| Columnar Storage | Columnar storage stores data in a column-oriented format rather than a row-oriented format. It improves query performance for analytics workloads by reducing I/O overhead and allowing for efficient compression and column-level operations, such as aggregations and filtering. Columnar databases are commonly used in data warehouses. |
| Log-Structured Storage | Organizes data as a sequence of log records written sequentially to disk. Log-structured storage optimizes for write throughput and crash recovery by batching writes and ensuring sequential I/O, making it suitable for applications with high write rates and append-only workloads. |

## References

- Athanassoulis, Manos, Stratos Idreos, and Dennis Shasha. "Data 
Structures for Data-Intensive Applications: Tradeoffs and Design 
Guidelines." *Foundations and Trends® in Databases* 13.1-2 (2023): 1-168.
- Shah, Gauri (2003). Distributed Data Structures for Peer-to-Peer Systems (PDF) (Ph.D. thesis). Yale University.