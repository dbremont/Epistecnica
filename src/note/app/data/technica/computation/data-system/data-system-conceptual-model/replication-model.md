# Replication Model

- [Data Partition Model](note.html?n=technica/computation/data-system/data-system-conceptual-model/data-partition-model.md)

> …p
> 

## Replication Models

| Replication Model | Description | Data Flow Direction | Consistency Model | Use Cases | Examples / Technologies |
| --- | --- | --- | --- | --- | --- |
| **Master-Slave** | A single master handles writes; replicas (slaves) handle reads | One-way (Master → Slaves) | Eventually consistent | Read-heavy workloads, reporting, backups | MySQL, PostgreSQL, SQL Server |
| **Master-Master** | Multiple masters accept writes and replicate to each other | Bi-directional | Conflict-prone | High availability, multi-region write access | MySQL (with conflict resolution), CouchDB |
| **Peer-to-Peer** | All nodes are equal; each can read and write and syncs with others | Multi-directional | Complex consistency | Decentralized systems, P2P networks | Cassandra, Couchbase |
| **Multi-Master (Clustered)** | Synchronous replication with tight coordination | Synchronous bi-directional | Stronger consistency | High availability with strong guarantees | Galera Cluster for MySQL, Spanner |
| **Log Shipping** | Ships transaction logs to replica and replays them | One-way | Eventually consistent | DR scenarios, low-overhead replication | SQL Server Log Shipping |
| **Snapshot Replication** | Periodic full data copy (snapshot) | One-way | Eventual/point-in-time | Static data, less frequent updates | PostgreSQL (pg_dump + restore) |
| **Statement-Based (SBR)** | Replicates SQL statements to other nodes | One-way or multi-directional | Depends on engine | Simpler SQL workloads, deterministic statements | MySQL with SBR |
| **Row-Based (RBR)** | Replicates actual row changes (DML) | One-way or multi-directional | Depends on engine | Complex or non-deterministic SQL operations | MySQL with RBR |
| **Hybrid Replication** | Mix of row-based and statement-based replication | One-way or multi-directional | Depends | Systems needing flexibility and optimization | MySQL (mixed mode) |
| **Asynchronous** | Changes are queued and applied later | One-way | Eventually consistent | Performance-prioritized replication | Most traditional setups |
| **Synchronous** | Transactions are committed on both master and replica before ACK | Two-way or tightly coupled | Strong consistency | Financial systems, mission-critical data | Spanner, Galera, PostgreSQL (sync) |
| **Logical Replication** | Replicates database-level changes (tables, rows, schema-level) | One-way | Customizable | Selective replication, heterogenous systems | PostgreSQL Logical Replication |
| **Physical Replication** | Block-level replication of disk/data files | One-way | Near exact replica | Full backup, hot standby | PostgreSQL Streaming Replication |

## References

- https://en.wikipedia.org/wiki/Replication_(computing)