# Data System

> A **data system (database management system (dbms))**  is a structured framework of hardware, software, and protocols designed to collect, store, process, manage, and retrieve data efficiently to support various applications and decision-making processes.
> 

> A database is an organized collection of interrelated data that models some aspect of the real world. Note: It represents only the current state of the modeled domain, not its full history or potential future states.
> 

## External-Memory Model (EMM) of Computation

> **The External-Memory Model (EMM) of Computation** is an organizing model for computation in data systems in which algorithms that are straightforward to express when their data fits in RAM must be **reformulated for execution over data that exceeds RAM capacity**. The computation is realized through a sequence of operations over **bounded portions of the data resident in RAM**, together with transfers of data between RAM and external memory.
> 

> See more in [External Memory Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/external-memory-model-of-computation.md).
> 

## Data System Space

> A **data system** is an organized framework—comprising software, storage, and processing components—designed to **collect, store, manage, transform, and make accessible data** for specific operational, analytical, or decision-making purposes.
> 

> A **computational management system** that implements an external-memory model of computation to enable the storage, retrieval, organization, transformation, and governance of datasets whose scale exceeds primary memory capacity. See
> 

> A database engine is a software component that manages the storage, retrieval, and manipulation of data in a database.
> 

> Systems: Algorithms + Data Structures.
> 

> System: Declarative Interfaces + Data Processing Engine.
> 

> A data system stores data and provides access to data.
> 

> A data system is a massive collection of data structures, algorithms, data flow, and caching policies. It should all play nice with the hardware. We should always make the right choice about which data structure, algorithm, data flow, and caching method we use. Ideally, users/apps should also be just to use it. A data system has two parts a declarative interface (data model) and engine that implements the interface.
> 

> A database: Organized collection of inter-related data that models some aspect of the real world. It’s a model of a small, finite subset of the real world. We expect some correspondance between the real world and the constructs of the database.
> 

> Database Management System(DBMS): It’s software that allows applications to store and analyze information in a database. A general-purpose DMBS supports the definition, creation, querying, update, and administration of databases with some data model.
> 

> Data Model is a collection of tools for modelling the real world, the molled is called a database. Examples: Relational, Key/Value, Graph, Document / Object, Wide-Column / Column-family, Array / Matrix / Vectors, Hierarchical, Network, Multi-Value. Note : Sometimes the database is also called a data model.
> 

> Process Model: A Process Model is a visual or abstract representation that describes the sequence of tasks, activities, and interactions within a system or business process.
> 

> Data Oriented Proces-Model: A data-oriented process model is an approach to modeling and designing systems or processes that places a strong emphasis on data flows, transformations, and interactions, with a primary focus on how data moves through the system and how it is processed and transformed at various stages.
> 

> A schema: is a description of a particular data collection using a given data model.
> 

> Normalization: The task of re-factor a database schema to store data without redundancy.
> 

> Data: A data, aka datum, is a set of symbols that models certain aspects of reality. Etimology datum / “dado” means “given”.
> 

> Fundamental Dogma: - Facts for Querying - Data Processing
> 

> Representation (Modelling): - Dynamic Model (Process Representation) (BPM) - Static Model (Data Representation) (Registers Store)
> 

| **System Type** | **Description** | **Role** | **Instance(s)** | **System Type Tree Path** |
| --- | --- | --- | --- | --- |
| **Data System** | System whose defining function is the persistent storage and management of data | Store and manage data | — | **Data System** |
| **Data Storage System** | Data System specialized in storing data according to a particular storage organization | Persistent data storage | — | **Data System → Data Storage System** |
| **File Data System** | Data Storage System that stores data as files organized within a file namespace | File-oriented storage | Filesystem, HDFS | **Data System → Data Storage System → File Data System** |
| **Object Storage Data System** | Data Storage System that stores data as independently addressable objects with associated metadata | Object-oriented storage | Amazon S3, MinIO | **Data System → Data Storage System → Object Storage Data System** |
| **Database System** | Data Storage System that stores structured or semi-structured data according to a defined data model and provides operations for accessing and modifying it | General-purpose structured data storage | PostgreSQL, MongoDB | **Data System → Data Storage System → Database System** |
| **Relational Database System** | Database System based on the relational data model | Relational data storage and management | PostgreSQL, MySQL | **Data System → Data Storage System → Database System → Relational Database System** |
| **Operational Database System** | Relational Database System optimized for frequent transactional reads and writes | Operational data storage | PostgreSQL, MySQL | **Data System → Data Storage System → Database System → Relational Database System → Operational Database System** |
| **Analytical Database System** | Relational Database System optimized for large-scale analytical queries and aggregations | Analytical data storage | Snowflake, BigQuery | **Data System → Data Storage System → Database System → Relational Database System → Analytical Database System** |
| **NoSQL Database System** | Database System using a non-relational data model | Flexible/distributed data storage | MongoDB, Cassandra | **Data System → Data Storage System → Database System → NoSQL Database System** |
| **Key–Value Data System** | NoSQL Database System storing data primarily as key–value associations | Fast keyed storage | Redis, DynamoDB | **Data System → Data Storage System → Database System → NoSQL Database System → Key–Value Data System** |
| **Document Data System** | NoSQL Database System storing semi-structured documents | Document-oriented storage | MongoDB | **Data System → Data Storage System → Database System → NoSQL Database System → Document Data System** |
| **Column-Family Data System** | NoSQL Database System organizing distributed data into column families | Large-scale distributed storage | Cassandra, HBase | **Data System → Data Storage System → Database System → NoSQL Database System → Column-Family Data System** |
| **Graph Data System** | Database System storing entities and their relationships as graph structures | Relationship-oriented storage | Neo4j | **Data System → Data Storage System → Database System → Graph Data System** |
| **Time-Series Data System** | Database System optimized for storing observations indexed by time | Temporal data storage | InfluxDB, TimescaleDB | **Data System → Data Storage System → Database System → Time-Series Data System** |
| **Vector Data System** | Database System specialized in storing vector representations and supporting similarity retrieval | Vector storage and similarity retrieval | Milvus, Pinecone | **Data System → Data Storage System → Database System → Vector Data System** |
| **In-Memory Data System** | Data System whose primary active data representation is maintained in volatile memory | Low-latency data storage | Redis, Memcached | **Data System → Data Storage System → In-Memory Data System** |
| **In-Memory Grid Data System** | In-Memory Data System distributed across multiple computational nodes | Distributed low-latency storage | Hazelcast, Ignite | **Data System → Data Storage System → In-Memory Data System → In-Memory Grid Data System** |
| **Cache Data System** | Data System storing copies of data to reduce access latency | Cached data storage | Redis, Memcached | **Data System → Data Storage System → Cache Data System** |
| **Event Data System** | Data System that persistently stores events as an ordered historical record | Event storage and reconstruction | EventStoreDB | **Data System → Data Storage System → Event Data System** |
| **Search Data System** | Data System that stores data together with structures optimized for efficient query-based retrieval | Search-oriented storage and retrieval | Elasticsearch, Solr | **Data System → Data Storage System → Search Data System** |
| **Analytical Data System** | Data System specialized in storing and processing data for analytical workloads | Analytics and decision support | — | **Data System → Data Storage System → Analytical Data System** |
| **Data Warehouse** | Analytical Data System organized as a managed repository of integrated, structured analytical data | Historical analytics, BI, reporting | Snowflake, BigQuery | **Data System → Data Storage System → Analytical Data System → Data Warehouse** |
| **Data Lake** | Data System designed to retain large quantities of raw and heterogeneous data | Flexible large-scale data storage | S3-based data lake | **Data System → Data Storage System → Data Lake** |
| **Hybrid Data System** | Data System combining characteristics of multiple distinct storage and management architectures | Integrated data storage and management | — | **Data System → Data Storage System → Hybrid Data System** |
| **Data Lakehouse** | Hybrid Data System combining lake-oriented storage with warehouse-oriented data management and analytical capabilities | Unified analytical storage | Databricks Lakehouse | **Data System → Data Storage System → Hybrid Data System → Data Lakehouse** |
|  |  |  |  |  |

## Data Model Space

> A **data model** is a collection of concepts for describing data in a database.
> 

> A **Schema** is a description of a particular collection of data, using a given data model.
> 

> A data model can be captured by **⟨Representation, Operations, Semantics⟩**, such that the representation defines the data structure, operations specify valid manipulations, and semantics assign precise meaning to both.
> 

> Note: Sometimes we adopt a more formal approach and assign a precise mathematical semantics to the data model.
> 

| **Data Model** | **Description** | **Formal Semantics** | **Instance(s)** |
| --- | --- | --- | --- |
| **Relational Data Model** | Organizes data into tables (relations) with rows and columns. Data is stored in structured formats. | Based on **first-order predicate logic** and **relational algebra/calculus**. | MySQL, PostgreSQL, Oracle, SQL Server |
| **Hierarchical Data Model** | Data is organized in a tree-like structure with a parent-child relationship between data elements. | Defined by **tree structures**; formalized with **rooted directed acyclic graphs** and set constraints. | IBM IMS, Windows Registry |
| **Network Data Model** | Similar to the hierarchical model but allows more complex relationships using a graph structure. | Based on **graph theory**; uses **set-oriented record types** and **pointers** for relations. | Integrated Data Store (IDS), TurboIMAGE |
| **Object-Oriented Data Model** | Organizes data using objects, similar to object-oriented programming, combining data and methods. | Formalized by **object calculus** and **semantic data models**; encapsulation and inheritance modeled mathematically. | db4o, ObjectDB, Versant Object Database |
| **Document Data Model** | Stores data in semi-structured formats, typically as documents (e.g., JSON, XML). | Grounded in **tree/graph structures**; formalized by **semi-structured data models** and **XPath/XQuery semantics**. | MongoDB, CouchDB, RavenDB |
| **Columnar Data Model** | Data is stored in columns rather than rows, optimized for analytical queries on specific attributes. | Relational algebra semantics preserved, but storage model defined as **column-oriented decomposition**. | Apache HBase, Apache Cassandra, Google Bigtable |
| **Key-Value Data Model** | Data is stored as key-value pairs, where each key is associated with a specific value. | Formalized as a **mathematical function** (key → value mapping). | Redis, Amazon DynamoDB, Riak |
| **Graph Data Model** | Data is represented as nodes, edges, and properties to capture relationships between entities. | Defined by **graph theory**; formally described by **property graphs** or **RDF triple semantics**. | Neo4j, ArangoDB, Amazon Neptune |
| **Dimensional Data Model** | Organizes data into facts (measurable values) and dimensions (attributes for analysis). | Defined by **star/snowflake schemas**; formally captured using **multi-relational mapping**. | Data Warehouses (e.g., Amazon Redshift, Snowflake) |
| **Multidimensional Data Model (OLAP Cube)** | Organizes data into dimensions and measures for complex analysis and reporting. | Formalized by **multidimensional algebra**; cube operations (slice, dice, roll-up, drill-down). | Microsoft Analysis Services, IBM Cognos, Essbase |
| **Entity-Relationship Model** | Represents data using entities and relationships, often used in database design. | Formalized in terms of **set theory** and **first-order logic** (entities, attributes, relationships). | ERwin Data Modeler, Oracle SQL Developer |
| **Time-Series Data Model** | Optimized for handling data that is collected or indexed in a time order. | Modeled as a **sequence of (time, value) tuples**, often formalized with **temporal logic**. | InfluxDB, Prometheus, OpenTSDB |
| **Vector Data Model** | Stores and queries high-dimensional vector representations (embeddings) of data, optimized for similarity search. | Formalized using linear algebra and metric space theory; similarity often defined via distance functions (e.g., Euclidean, cosine). | Pinecone, Weaviate, Milvus, FAISS |
| **Geospatial Data Model** | Stores and queries spatial/geographic data, representing real-world features like points, lines, and polygons, often with attributes. | Formalized using geometry, topology, and linear algebra; spatial relationships modeled via set theory, vector/raster representations, and spatial predicates (e.g., intersects, contains, distance). | PostGIS, Oracle Spatial, SQL Server Spatial, QGIS |

## Workload

> **A data system workload** refers to the amount and type of operations (such as queries, transactions, and computational tasks) that a system handles during a given period.
> 

| **Workload Type** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **OLTP (Online Transaction Processing)** | Handles fast, frequent, small transactions (CRUD operations). Focuses on low latency and high availability. | MySQL, PostgreSQL, Microsoft SQL Server, Oracle, CockroachDB, TiDB |
| **OLAP (Online Analytical Processing)** | Optimized for complex queries and large-scale data analysis, often used in data warehouses. | Snowflake, Amazon Redshift, Google BigQuery, Apache Druid, ClickHouse |
| **HTAP (Hybrid Transactional/Analytical Processing)** | Combines OLTP and OLAP, allowing real-time analytics on transactional data. | TiDB, SingleStore (MemSQL), Google Spanner, YugabyteDB |
|  |  |  |

## Query Language

> A **query language** is a formal language designed to retrieve, manipulate, and sometimes transform data stored in an information system — most commonly a database. Unlike general-purpose programming languages, query languages are often **declarative**, meaning that users specify *what* data they want, not *how* to compute it.
> 

> See more in
> 

## Storage

> How to store the data in a persistent medium?
> 

> How to store the data in volatile medium?
> 

> How to store the data for the long term?
> 

> See [Representation](note.html?n=technica/computation/representation.md), [Apache Parquet](note.html?n=technica/computation/representation/conceptual-model-computational-representation/apache-parquet.md),  [Data File Format](note.html?n=technica/computation/representation/conceptual-model-computational-representation/data-file-format.md).
> 

## World Simplest Data System

> 

```bash
# World Simplest Data System
#!/bin/bash

db_set () {
   echo "$1, $2" >> database
}

db_get () {
   grep "^$1" database | sed -e "s/^1,//" | tail -n 1
}
```

## Conceptual Model

Data System: Conceptual Model

## QA

### **How can databases carry out computation when all the data cannot fit in working memory?**

> Databases use **external-memory algorithms**, partitioning, streaming, buffering, and temporary disk-based structures so computation can proceed over data larger than available RAM.
> 

> See more in [External Memory Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/external-memory-model-of-computation.md).
> 

### Which operations are particularly difficult to perform when the data exceeds available working memory? Are there any operations that cannot be performed under these conditions?

> **Global operations** such as sorting, duplicate elimination, grouping, joins, and aggregation become I/O-intensive because they may require materializing or partitioning intermediate state, but **no standard relational operation is inherently impossible** provided sufficient secondary storage and execution resources are available.
> 

### What happens to an ongoing computation when the underlying data is modified concurrently?

> 

### Which are the `Models of Computation`  that grounds computation descriptions in a `data system`?

> See more in [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md).
> 

## References

- https://github.com/csiglab/data-system-labs
- https://en.wikipedia.org/wiki/Data_model
- Jia, Zhen, et al. "Characterizing and subsetting big data workloads." 2014 IEEE International Symposium on Workload Characterization (IISWC). IEEE, 2014.
- Tolia, N., Kozuch, M., Satyanarayanan, M., Karp, B., Bressoud, T., & Perrig, A. (2003). Opportunistic Use of Content Addressable Storage for Distributed File Systems.
- To BLOB or Not To BLOB: Large Object Storage in a Database or a Filesystem - https://www.sqlite.org/fasterthanfs.html - https://www.microsoft.com/en-us/research/publication/to-blob-or-not-to-blob-large-object-storage-in-a-database-or-a-filesystem/ - File System Design Approaches https://arxiv.org/pdf/1403.5976.pdf
- Paul, Debjyoti, et al. "Database workload characterization with query plan encoders." arXiv preprint arXiv:2105.12287 (2021).
- [Database of Databases](https://dbdb.io/)
- [Video Streaming at Scale with Kubernetes and RabbitMQ](https://alexandreolive.medium.com/video-streaming-at-scale-with-kubernetes-and-rabbitmq-6e23fd0e75fb)
- [GC for MVCC - MyRocks, InnoDB and Postgres](http://smalldatum.blogspot.com/2023/04/gc-for-mvcc-myrocks-innodb-and-postgres.html)
- [noisepage](https://github.com/cmu-db/noisepage)
- [Scuba: Diving into Data at Facebook](https://research.facebook.com/publications/scuba-diving-into-data-at-facebook/)
- [SplinterDB](https://twitter.com/debasishg/status/1703090961344336370)
    - [How FoundationDB works and why it works](https://blog.the-pans.com/notes-on-the-foundationdb-paper/)
- [Understanding Google’s File System](https://www.micahlerner.com/2020/03/22/understanding-googles-file-system.html)
- [Awesome Big Data](https://github.com/newTendermint/awesome-bigdata)
- [Big Data Storage](https://berthub.eu/articles/posts/big-data-storage/)
- [Log-structured Protocols in Delos](https://www.micahlerner.com/2021/11/23/log-structured-protocols-in-delos.html)
- An Empirical Evaluation of Columnar Storage Formats [pdf] ([vldb.org](http://vldb.org/))
[https://news.ycombinator.com/item?id=40370613](https://news.ycombinator.com/item?id=40370613)
- [https://en.wikipedia.org/wiki/DB-Engines_ranking](https://en.wikipedia.org/wiki/DB-Engines_ranking)
- [Workload](note.html?n=technica/computation/system/design/computer-system-design-conceptual-model/workload.md)
- [Storage System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/storage-system.md)
- OLTP Through the Looking Glass 16 Years Later: Communication is the New Bottleneck /  [https://www.vldb.org/cidrdb/papers/2025/p17-zhou.pdf](https://www.vldb.org/cidrdb/papers/2025/p17-zhou.pdf)z
- Wang, Hao, et al. "LavaStore: ByteDance's Purpose-Built, High-Performance, Cost-Effective Local Storage Engine for Cloud Services." Proceedings of the VLDB Endowment 17.12 (2024): 3799-3812.
- Colle, Romain, et al. "Oracle database replay." Proceedings of the VLDB Endowment 2.2 (2009): 1542-1545.
- https://muratbuffalo.blogspot.com/2025/07/serializable-isolation-for-snapshot.html
- [Are You Sure You Want to Use MMAP in Your Database Management System?](https://db.cs.cmu.edu/mmap-cidr2022/)
- [Updates to the insert benchmark](http://smalldatum.blogspot.com/2023/05/updates-to-insert-benchmark.html)
- [Awesome Database Development](https://github.com/huachaohuang/awesome-dbdev)
- [Outline of databases](https://en.wikipedia.org/wiki/Outline_of_databases)
- [Database of Databases](https://dbdb.io/)
- Kleppmann, M. (2017). Designing data-intensive applications. O’Reilly Media.
- Silberschatz, A., Korth, H. F., Sudarshan, S. (2010). Database System Concepts (6th ed.). McGraw-Hill Professional.
- Petrov, A. (2019). Database internals. O’Reilly UK.
- Hellerstein, J. M., Stonebraker, M., Hamilton, J., Hellerstein, J. M., Stonebraker, M., Hamilton, J. (2007). Architecture of a Database System. Foundations and Trends R in Databases, 1(2), 141–259. https://doi.org/10.1561/1900000002
- Chamberlin, D. D., Astrahan, M. M., Blasgen, M. W., Gray, J. N., King, W. F., Lindsay, B. G., Lorie, R., Mehl, J. W., Price, T. G., Putzolu, F., Selinger, P. G., Schkolnick, M., Slutz, D. R., Traiger, I. L., Wade, B. W., Yost, R. A. (1981). A History and Evaluation of System R. 24(10), 632–646.
- Gray, J., McJones, P., Blasgen, M., Lindsay, B., Lorie, R., Price, T., Putzolu, F., Traiger, I. (1981). The Recovery Manager of the System R Database Manager. ACM Computing Surveys (CSUR), 13(2), 223–242.
- Mohan, C., Lindsay, B., Obermarck, R. (n.d.). Transaction Management in the R* Distributed Database Management System.
- Kent, W. (2012). Data & reality. Technics Publications.
- Things You Should Know About Databases. (n.d.). Retrieved July 12, 2022, from https://architecturenotes.co/things-you-should-know-about-databases/
- [The Design and Implementation of Modern Column-Oriented Database Systems](https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf)
- [Architecture of a Database System](https://perspectives.mvdirona.com/content/binary/ArchitectureOfDatabaseSystem.pdf)
- [The Fourth Paradigm - Data Intesive Scientific Discovery](https://sites.astro.caltech.edu/~george/aybi199/4th_paradigm_book_complete_lr.pdf)
- [Readings in Databases](https://github.com/rxin/db-readings)
- [DBOS: A DBMS-oriented Operating System](https://vldb.org/pvldb/vol15/p21-skiadopoulos.pdf)
- [Lotus: Scalable Multi-Partition Transactions on Single-Threaded Partitioned Databases](https://www.vldb.org/pvldb/vol15/p2939-zhou.pdf)
- [Anti-Caching: A New Approach to Database Management System Architecture](https://www.vldb.org/pvldb/vol6/p1942-debrabant.pdf)
- [How do databases deal with data tables that cannot fit in memory?](https://stackoverflow.com/questions/1725143/how-do-databases-deal-with-data-tables-that-cannot-fit-in-memory)
- - [TAO: [Facebook’s Distributed Data Store for the Social Graph]](https://www.micahlerner.com/2021/10/13/tao-facebooks-distributed-data-store-for-the-social-graph.html)
- [The Seattle Report on Database Research](https://cacm.acm.org/magazines/2022/8/262905-the-seattle-report-on-database-research/fulltext)
- [The Inner Workings of Distributed Databases](https://questdb.io/blog/inner-workings-distributed-databases/)
- [Scaling Databases at Activision [pdf] (sched.com)](https://news.ycombinator.com/item?id=35655910)
- [Database Gyms [pdf] (cidrdb.org)](https://news.ycombinator.com/item?id=36380434)
- [How do databases execute expressions? | notes.eatonphil.com](https://notes.eatonphil.com/2023-09-21-how-do-databases-execute-expressions.html)
- [Linear-time analytical queries in plain Python](https://gist.github.com/pkhuong/69b457af82eeb2bc3ebf1a3e4209ae69)
- [Scaling TiDB To 1 Million QPS. A Flipkart journey | by Sachin Japate | Flipkart Tech Blog](https://blog.flipkart.tech/scaling-tidb-to-1-million-qps-d556aa6a16ef)
- Saving cloud costs by writing our own database ([hivekit.io](http://hivekit.io/))
[https://news.ycombinator.com/item?id=39929185](https://news.ycombinator.com/item?id=39929185)
- https://news.ycombinator.com/item?id=46124205
- https://github.com/apache/iggy
- https://bytebytego.com/guides/7-must-know-strategies-to-scale-your-database/

Courses:

- https://15445.courses.cs.cmu.edu/fall2025/
- https://15721.courses.cs.cmu.edu/spring2024/
- https://ocw.mit.edu/courses/6-830-database-systems-fall-2010/
- [15-826 Multimedia and Data Mining](https://www.cs.cmu.edu/~christos/courses/826.F25/index.html)
- https://15799.courses.cs.cmu.edu/spring2025/
- https://web.stanford.edu/class/cs245/