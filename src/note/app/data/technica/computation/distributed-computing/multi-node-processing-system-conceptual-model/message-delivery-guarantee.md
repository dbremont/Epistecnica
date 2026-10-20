# Message Delivery Guarantee


> **Message Delivery Guarantee** refers to the assurance that a message will be delivered to its intended recipient with a specified level of reliability, such as "at-most-once," "at-least-once," or "exactly-once," regardless of potential network failures or system crashes.
> 

Here's a table outlining the different types of **message delivery semantics** and their characteristics:

| **Semantics** | **Description** | **Pros** | **Cons** | **Use Case** |
| --- | --- | --- | --- | --- |
| **At-most-once** | Messages are delivered either once or not at all. | No duplicates, Fast processing | Risk of message loss,  No retries | Non-critical systems where speed is prioritized over reliability |
| **At-least-once** | Messages are guaranteed to be delivered at least once, but may be delivered multiple times. | Guaranteed delivery, Reliable | Risk of duplicate messages, Requires idempotent handling on the receiver | Systems where reliability is critical, but duplicate processing is acceptable |
| **Exactly-once** | Messages are delivered and processed once and only once, even in the presence of failures or retries. | No duplicates, Guaranteed consistency | Complex to implement,  Higher resource overhead | Financial systems, critical data processing, distributed transaction systems |

## References

- https://exactly-once.github.io/posts/exactly-once-delivery/
- …