---
tags: [clock]
---

# Clock


> In distributed systems, a **clock** is a mechanism or  service that provides a consistent and ordered notion of time across  multiple nodes, enabling synchronization, event ordering, and 
coordination despite the absence of a global physical clock.
> 

## Taxonomy

| **Clock Type** | **Description** |
| --- | --- |
| **System Clock** | The system clock, or real-time clock (RTC), is integrated into a computer's motherboard. It tracks the current date and time, referencing time-related operations in the OS and software applications. |
| **Logical Clocks** | Abstract models are used in distributed systems to order events and maintain a partial ordering of events across different processes or nodes without necessarily representing real-time. |
| **Vector Clocks** | Track causal relationships and order events in distributed systems. This ensures consistent views of events across multiple nodes and aids in synchronization and conflict resolution. |
| **Lamport Timestamps** | Logical clocks that order events in a distributed system maintain causality between events and determine the global order across distributed nodes. |
| **Monotonic Clocks** | Provide a continuous, ever-increasing time value unaffected by system clock changes or synchronization adjustments. It is commonly used for measuring time intervals and scheduling tasks. |
| **Wall Clocks** | Represent the real-world time, typically provided by the system clock. Display the current date and time to users and timestamp events. |

## References

- [Time](note.html?n=technica/computation/miscelanea/time.md)