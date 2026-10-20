# Data Partition Model

- [Replication Model](note.html?n=technica/computation/data-system/data-system-conceptual-model/replication-model.md)

> **Data partitioning** is the process of dividing a large dataset into smaller, manageable **segments (partitions)** that can be stored, processed, and queried independently, either **within a single system or across multiple systems or nodes**.
> 

> **Partitioning is not replication**, but they can and often do **work together**.
> 

## Partition Model

| Strategy | Description | Advantages | Limitations | Common Use Cases |
| --- | --- | --- | --- | --- |
| **Horizontal Partitioning (Sharding)** | Divides rows across partitions based on a key (e.g., user ID) | Enables scale-out; smaller data per node; local reads | Cross-shard joins are complex; key design is critical | Large user bases, SaaS platforms, global apps |
| **Vertical Partitioning** | Splits columns across tables or servers (e.g., user profile vs. login info) | Reduces row size; isolates frequently used columns | More joins needed; may degrade performance on wide queries | Column-heavy databases, analytics |
| **Range Partitioning** | Data is split by value range (e.g., dates, numeric IDs) | Simple logic; effective for time-series data | Uneven distribution ("hot shards") if ranges aren’t balanced | Time-series DBs, logs, financial data |
| **Hash Partitioning** | Applies a hash function to a key to assign rows to partitions | Uniform distribution; avoids hotspots | Difficult to predict placement; resharding is complex | User-based systems, balanced load apps |
| **List Partitioning** | Partitions are based on discrete values (e.g., country = US, DE, IN) | Good for categorical data; easy to control placement | Impractical with many values; manual maintenance | Region-specific data, compliance (GDPR, etc.) |
| **Composite Partitioning** | Combines multiple strategies (e.g., range + hash) | Balances benefits of both strategies | Increased complexity; requires careful design | Complex enterprise DBs, hybrid transactional systems |
| **Round-Robin Partitioning** | Rows distributed sequentially to each partition | Simple; balanced if data is homogeneous | No data locality; poor query optimization | Parallel processing frameworks (e.g., Spark) |
| **Key/Modulo Partitioning** | Key % N → partition | Fast computation; even distribution if keys are uniform | Requires resharding when N changes; may ignore data semantics | Cache systems (e.g., Redis clusters), legacy systems |
| **Geographical Partitioning (Geo-Sharding)** | Based on user or data location (e.g., EU, US, APAC) | Low latency; regulatory compliance | Cross-region queries; increased ops complexity | Global apps, regulatory compliance, CDN-backed apps |
| **Manual Partitioning** | Explicit rules/code define where each row goes | Full control | Error-prone, inflexible; hard to scale | Legacy systems, early-stage apps |

| Strategy | Description | Advantages | Limitations | Common Use Cases |
| --- | --- | --- | --- | --- |
| **Horizontal Partitioning (Sharding)** | Divides rows across partitions based on a key (e.g., user ID) | Enables scale-out; smaller data per node; local reads | Cross-shard joins are complex; key design is critical | Large user bases, SaaS platforms, global apps |
| **Vertical Partitioning** | Splits columns across tables or servers (e.g., user profile vs. login info) | Reduces row size; isolates frequently used columns | More joins needed; may degrade performance on wide queries | Column-heavy databases, analytics |
| **Range Partitioning** | Data is split by value range (e.g., dates, numeric IDs) | Simple logic; effective for time-series data | Uneven distribution ("hot shards") if ranges aren’t balanced | Time-series DBs, logs, financial data |
| **Hash Partitioning** | Applies a hash function to a key to assign rows to partitions | Uniform distribution; avoids hotspots | Difficult to predict placement; resharding is complex | User-based systems, balanced load apps |
| **List Partitioning** | Partitions are based on discrete values (e.g., country = US, DE, IN) | Good for categorical data; easy to control placement | Impractical with many values; manual maintenance | Region-specific data, compliance (GDPR, etc.) |
| **Composite Partitioning** | Combines multiple strategies (e.g., range + hash) | Balances benefits of both strategies | Increased complexity; requires careful design | Complex enterprise DBs, hybrid transactional systems |
| **Round-Robin Partitioning** | Rows distributed sequentially to each partition | Simple; balanced if data is homogeneous | No data locality; poor query optimization | Parallel processing frameworks (e.g., Spark) |
| **Key/Modulo Partitioning** | Key % N → partition | Fast computation; even distribution if keys are uniform | Requires resharding when N changes; may ignore data semantics | Cache systems (e.g., Redis clusters), legacy systems |
| **Geographical Partitioning (Geo-Sharding)** | Based on user or data location (e.g., EU, US, APAC) | Low latency; regulatory compliance | Cross-region queries; increased ops complexity | Global apps, regulatory compliance, CDN-backed apps |
| **Manual Partitioning** | Explicit rules/code define where each row goes | Full control | Error-prone, inflexible; hard to scale | Legacy systems, early-stage apps |

## 🔄 Partitioning vs. Replication

| Concept | Description |
| --- | --- |
| **Partitioning** | Breaks data into **different** subsets |
| **Replication** | Creates **copies** of the same dataset |
| 🔁 Together | Each partition can also be **replicated** for high availability |

## References

- https://news.ycombinator.com/item?id=17567122
- https://en.wikipedia.org/wiki/Shard_(database_architecture)