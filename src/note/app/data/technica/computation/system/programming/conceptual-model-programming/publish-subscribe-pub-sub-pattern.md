---
tags: [design-idiom]
---

# Publish-Subscribe (Pub-Sub) Pattern


> A **messaging pattern** where senders of messages, called publishers, do not program the messages to be sent directly to specific receivers, called subscribers.
> 

> **Note:** Other topics, such as how to observe these systems, monitoring, and related concerns, are not covered.
> 

## Implementation

| **Method** | **Operation** | **Description** | **Complexity** |
| --- | --- | --- | --- |
| **Hash Map + List** | `subscribe(e, s)` | Append subscriber `s` to list for event `e`. | O(1) amortized |
|  | `unsubscribe(e, s)` | Remove subscriber `s` from list (linear scan). | O(k) |
|  | `publish(e)` | Notify all `k` subscribers. | O(k) |
|  | `get_subscribers(e)` | Return list of subscribers for event `e`. | O(1) |
|  | `get_events(s)` | Not supported without reverse mapping. | — |
| **Hash Map + Set** | `subscribe(e, s)` | Add subscriber `s` to set for event `e`. | O(1) average |
|  | `unsubscribe(e, s)` | Remove subscriber `s` from set. | O(1) average |
|  | `publish(e)` | Notify all `k` subscribers. | O(k) |
|  | `get_subscribers(e)` | Return set of subscribers for event `e`. | O(1) |
|  | `get_events(s)` | Not supported without reverse mapping. | — |
| **Bidirectional Mapping** | `subscribe(e, s)` | Update both event→subscribers and subscriber→events. | O(1) |
|  | `unsubscribe(e, s)` | Remove subscriber from both mappings. | O(1) |
|  | `publish(e)` | Notify all `k` subscribers. | O(k) |
|  | `get_subscribers(e)` | Return subscribers for event `e`. | O(1) |
|  | `get_events(s)` | Return events subscribed by `s`. | O(1) |
| **Event Bus w/ Filtering** | `subscribe(e, s, f)` | Register `s` with optional filter `f(data)`. | O(1) |
|  | `unsubscribe(e, s)` | Remove subscriber and its filter from event `e`. | O(1) |
|  | `publish(e, data)` | Evaluate filters and notify matching subscribers. | O(k · cf), cf = filter cost |
|  | `get_subscribers(e)` | Return list of `(subscriber, filter)` pairs. | O(1) |
|  | `get_events(s)` | Requires scanning or indexing over all events. | O(m) worst case |

## Uses

> Pub-Sub systems are ideal when the **producer of information should not know who the consumers are**, and vice versa. This architectural pattern supports **asynchronous, scalable, and decoupled communication**.
> 

### 🧭 Decision Model

> When a system or sub-system can be model as a “Pub-Sub”?
> 

> Model your system as Pub-Sub if it benefits from decoupled, event-driven communication that is scalable, dynamic, and asynchronous, especially when many components need to communicate without tight dependencies.
> 

Use a **pub-sub pattern** if you need:

- ✔ **Loose coupling** between producers and consumers
- ✔ **Scalable fan-out** to many consumers
- ✔ **Asynchronous** event handling
- ✔ **Dynamic and many-to-many** communication
- ✔ **Topic or content-based routing**
- ✔ **Multicast or broadcast semantics**

Use **enhanced pub-sub** (e.g., with filtering or partitioning) if:

- You need **selective consumption** (e.g., `filter(data) → notify`)
- You need **consumer groups** or **stream processing**
- You have **high-volume, ordered, or replayable logs**

### Don’t Use For This

> Pub-sub systems are **not a good fit** when you need:
> 

| **Requirement** | **Why Not** |
| --- | --- |
| **Synchronous RPC-style results** | Pub-sub is inherently async; no direct response path |
| **Strong delivery guarantees** | Most pub-sub systems default to **at-most-once** without external support |
| **Total ordering of events** | Needs extra work or different architecture (e.g., queues with strict FIFO) |
| **Request tracing / debugging** | Hard to trace end-to-end without instrumentation |
| **Exact-once delivery** | Non-trivial; requires idempotency or transactional message systems |
| **Small systems with static flow** | Overkill for simple workflows—use direct calls or queues |

## ⚙️ Effects of Pub-Sub Architecture on a System

| **Impact / Effect** | **Benefit** | **Trade-off / Challenge** |
| --- | --- | --- |
| **Loose Coupling** | Components evolve independently, easier maintenance | Harder to trace flows and debug due to indirect interaction |
| **Scalability & Load Distribution** | Efficient multicast and horizontal scaling | Potential message floods; need for throttling/backpressure |
| **Asynchronous Communication** | Improved responsiveness and throughput | Complex handling of eventual consistency and race conditions |
| **Eventual Consistency** | Suitable for distributed systems with relaxed consistency | Temporary inconsistencies; requires design for convergence |
| **Increased Complexity** | Enables flexible messaging patterns and decoupling | Adds operational overhead; more complex monitoring/debugging |
| **Fault Tolerance & Reliability** | Configurable guarantees, resilient event delivery | Higher latency and resource use for durability |
| **Flexibility in Communication Patterns** | Supports one-to-many, many-to-many, dynamic subs | Complexity in ordering, filtering, message correlation |
| **Latency Considerations** | Asynchronous delivery can improve throughput | Added latency compared to direct synchronous calls |
| **Monitoring & Observability Challenges** | Encourages sophisticated instrumentation and tracing | Indirect paths complicate tracing and diagnostics |

## Similar Systems

> **Pub-Sub systems** share similarities or overlap with other messaging and event-driven architectures. Understanding these can help choose the right tool or pattern.
> 

| **System Type** | **Description** | **Key Differences** |
| --- | --- | --- |
| **Message Queues** | Point-to-point messaging where each message is consumed by a single consumer. | Ensures message ordering and guaranteed delivery to one consumer only. |
| **Event Streaming** | High-throughput ordered streams of events (e.g., Kafka, Pulsar). | Focuses on durable storage, replay, and stream processing capabilities. |
| **Observer Pattern** | Object-oriented pattern where observers register to listen to changes in a subject. | Usually in-memory and synchronous, often single-process scope. |
| **Notification Services** | Cloud services (e.g., AWS SNS, Google Pub/Sub) that deliver messages across distributed apps. | Provide managed pub-sub with integration to cloud ecosystems. |
| **Callback Mechanisms** | Functions passed as parameters to be executed on event occurrence. | Usually tightly coupled and synchronous within the same process. |
| **Reactive Streams** | Asynchronous stream processing with backpressure support (e.g., RxJava, Reactor). | Provides advanced flow control and composable asynchronous data flows. |
| **Dataflow Systems** | Systems that model computations as directed graphs of operations on data streams. | Often used for complex event processing and analytics pipelines. |
| **Publish-Subscribe Middleware** | Middleware solutions that abstract message routing and delivery (e.g., MQTT brokers). | Often support specific protocols or QoS levels for IoT or mobile devices. |

## Case Studies

| **Domain** | **Example System** | **Why Pub-Sub Fits** |
| --- | --- | --- |
| **Microservices** | Event-driven microservices (e.g., Order Service publishing events consumed by Billing, Shipping) | Services decoupled, communicate asynchronously via events. |
| **UI Frameworks** | Frontend event buses (e.g., React’s context, Redux middleware, Angular event emitters) | Components subscribe to UI events and update reactively. |
| **IoT Platforms** | MQTT-based sensor networks | Sensors publish data; many monitoring/processing apps subscribe. |
| **Real-Time Messaging** | Chat applications (e.g., Slack, Discord) | Messages published to channels, multiple subscribers receive them. |
| **Logging & Monitoring** | Centralized log aggregation (e.g., ELK stack, Fluentd pipelines) | Log producers send events to broker; multiple consumers process logs. |
| **Financial Trading Systems** | Market data distribution systems | Price tickers broadcast updates to many trading clients. |
| **Notification Systems** | Push notification services (e.g., Firebase Cloud Messaging) | Events push notifications to many clients asynchronously. |
| **Distributed Caches** | Cache invalidation events | Changes in one cache instance publish invalidation events to others. |
| **Gaming** | Multiplayer game state synchronization | Server publishes game state events; clients subscribe and update UI. |
| **Content Delivery Networks** | Cache refresh and purge events | Invalidate or update caches globally via events. |
| **Continuous Integration** | Pipeline events and status updates | Build and deploy stages communicate asynchronously. |
| **Blockchain Networks** | Transaction and block propagation | Nodes publish new blocks and transactions to the network. |

## References

- https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern
- Lazzari, L., & Farias, K. (2022). An exploratory study on the effects of event-driven architecture on software modularity. [https://arxiv.org/abs/2110.14699](https://arxiv.org/abs/2110.14699)
- Lu, W., Liu, Y. (2011). Research of Event-Driven Enterprise Application Integration Base on Service Oriented Architecture. In: Zeng, D. (eds) Applied Informatics and Communication. ICAIC 2011. Communications in Computer and Information Science, vol 224. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-642-23214-5_5](https://doi.org/10.1007/978-3-642-23214-5_5)
- John, V., & Liu, X. (2017). A Survey of Distributed Message Broker Queues. [https://arxiv.org/abs/1704.00411](https://arxiv.org/abs/1704.00411)
- Ferretti, S. (2012). Publish-Subscribe Systems via Gossip: a Study based on Complex Networks. [https://arxiv.org/abs/1112.0416](https://arxiv.org/abs/1112.0416)
- Gómez, A., Rodríguez, R.J., Cambronero, ME. et al. Profiling the publish/subscribe paradigm for automated analysis using colored Petri nets. Softw Syst Model 18, 2973–3003 (2019). [https://doi.org/10.1007/s10270-019-00716-1](https://doi.org/10.1007/s10270-019-00716-1)
- Nasirifard, P., & Jacobsen, H.-A. (2022). A Serverless Publish/Subscribe System. [https://arxiv.org/abs/2210.07897](https://arxiv.org/abs/2210.07897)
- Tools
    - https://news.ycombinator.com/item?id=44413809 https://github.com/kelindar/event/tree/master
    - …