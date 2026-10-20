# Recovery


> **Algorithms for Recovery** typically refer to methods used in computing systems to ensure data consistency and system state integrity following failures, focusing on techniques like logging **(write-ahead, redo, undo)**, **checkpointing**, and shadow paging to effectively restore data to a valid state.
> 

## Recovery Model

> Here’s a table comparing the main database recovery models, highlighting key aspects such as logging behavior, recovery capabilities, and typical use cases.
> 

> This comparison helps in choosing the right recovery model based on the specific requirements of a database environment.
> 

| Recovery Model | Logging Details | Recovery Capabilities | Typical Use Cases |
| --- | --- | --- | --- |
| **Simple Recovery** | Only logs transactional changes; does not log bulk operations. | No point-in-time recovery; supports only recovery up to the last full or differential backup. | Suitable for non-critical data or systems where data can be easily recreated, and point-in-time recovery is not required. |
| **Full Recovery** | Logs all transactions and bulk operations fully. | It supports point-in-time recovery and allows recovery to an exact point before a failure. | Ideal for environments where data loss is unacceptable, such as financial systems or critical applications. |
| **Bulk-Logged Recovery** | Logs minimal details for bulk operations but full details for regular transactions. | It allows for efficient bulk operations and supports point-in-time recovery, but only if no bulk operations have occurred since the last backup. | This is useful for systems performing large bulk operations where performance during these operations is critical, yet some form of crash recovery is needed. |
| **Snapshot Recovery** | It depends on the technology used; it generally does not involve transaction logging. | Allows quick reversion to the snapshot state; unsuitable for point-in-time recovery beyond snapshots. | Often used in development and testing environments where rapid restoration to a known state is valuable. |
| **Continuous Data Protection** | Continuous log changes as they occur, either at the block level or using real-time replication. | It enables recovery to virtually any point but is limited only by data retention policies and storage. | Best for high-value applications where even minimal data loss is detrimental and rapid recovery is essential. |

This table outlines the strengths and limitations of each database recovery model, aiding in the decision-making process to match recovery capabilities with organizational needs and risk tolerance.

## Recovery Strategies

> Database recovery strategies are crucial for maintaining data integrity and availability, especially in the event of system failures or data corruption.
> 

> Below is a table summarizing key database recovery strategies or algorithms typically used in managing and restoring data:
> 

| Strategy/Algorithm | Description |
| --- | --- |
| **Immediate Update** | Writes changes to disk immediately, before the transaction commits, using log records to roll back if needed. |
| **Deferred Update** | Writes changes to a log and only applies them to the central database after committing the transaction. |
| **Checkpointing** | Regularly saves the state of the database at specific points, reducing the amount of log data to process during recovery. |
| **Log Sequence Numbers (LSN)** | It uses a unique identifier for each log entry to restore transactions in the correct order. |
| **Write-Ahead Logging (WAL)** | Ensures that all log records for changes are written to disk before the data pages are written, facilitating consistent recovery states. |
| **Two-Phase Commit** | Coordinates all parts of a distributed transaction into two distinct phases (prepare and commit/abort) to ensure all or none of the transaction is committed. |
| **Aries Algorithm** | It uses a combination of WAL, redo, and undo logging and maintains consistency through three phases: analysis, redo, and undo during recovery. |
| **Shadow Paging** | Maintains a shadow copy of the entire database or pages, which gets updated with changes upon transaction commit, preserving the old data until it's certain the new data is correctly written. |
| **Flashback Technology** | Allows the database to be rolled back or reverted to a previous point, utilizing historical data logs and snapshots. |
| **Replication** | It keeps copies of data on multiple machines or storage systems so that if one fails, the data can be recovered from another location. |

These strategies encompass a range of techniques, from basic logging to more complex systems involving multi-phase commits and replication. Each strategy has strengths and is chosen based on specific requirements such as real-time recovery, ensuring data consistency, or the performance overhead each method introduces.

## References

- Mohan, Chandrasekaran, et al. "ARIES: A transaction recovery method supporting fine-granularity locking and partial rollbacks using write-ahead logging." ACM Transactions on Database Systems (TODS) 17.1 (1992): 94-162.
- [The disaggregated write-ahead log](https://news.ycombinator.com/item?id=39282054) (2023) ([schmizz.net](http://schmizz.net/))
- Alagappan, Ramnatthan, et al. "Protocol-aware recovery for consensus-based distributed storage." ACM Transactions on Storage (TOS) 14.3 (2018): 1-30.
- [The Leadership Myth in Replicated Databases](https://maheshba.bitbucket.io/blog/2023/05/06/Leadership.html)
- [https://pulsar.apache.org/docs/3.1.x/administration-zk-bk/#bookkeeper](https://pulsar.apache.org/docs/3.1.x/administration-zk-bk/#bookkeeper)
- Maryanski, Fred J., and Kirk A. Norsworthy. "A model of the performance of a rollback algorithm." *Proceedings of the 1979 annual conference*. 1979.