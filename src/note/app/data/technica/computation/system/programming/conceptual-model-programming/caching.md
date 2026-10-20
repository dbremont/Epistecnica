---
tags: [technique]
---

# Caching


> **Caching** in computer science refers to a performance optimization technique that stores copies of data or computations in a **faster-access storage layer** (the *cache*) to reduce the cost (in time, energy, or computational resources) of repeated access to the same data or operation results.
> 

> **Caching** is the use of a **temporal storage layer** located closer (in terms of latency and/or bandwidth) to the execution context than the original data source, which holds **redundant or derived representations** of data or computations. The cache operates under a **coherence policy** (to ensure data correctness) and an **eviction policy** (to manage finite space), and can be applied across storage hierarchies (e.g., memory caches, disk caches), computation levels (e.g., memoization), or system layers (e.g., DNS, CPU, HTTP).
> 

## 📑 Structure

> What is the common structure of a cache subsystem?
> 

| **Component** | **Description** |
| --- | --- |
| **Write Policy** | Determines when data is written to cache and backing store (e.g., write-through, write-back). |
| **Cache Key** | The identifier used to index into the cache (e.g., memory address, URL, function arguments). |
| **Cache Value** | The stored result (e.g., data block, object, output of a function). |
| **Lookup Policy** | Defines how the system checks for a cached result (e.g., associative mapping, direct mapping). |
| **Eviction Policy** | Manages what data to remove when the cache is full (e.g., LRU, LFU, FIFO). |
| **Coherence Policy** | Ensures consistency between cache and source data (important in shared memory systems). |
| **Invalidation Mechanism** | Ensures cache correctness by removing or updating stale entries in response to mutations in the backing data source. Can be explicit, time-based (TTL), event-driven, or snooping-based in hardware systems. |

### **Eviction**

| **Technique** | **Description** | **Notes** |
| --- | --- | --- |
| **LRU (Least Recently Used)** | Evicts the item that was accessed least recently | Common in in-memory caches where recently used items are more likely to be accessed again (e.g., Caffeine, Ehcache) |
| **LFU (Least Frequently Used)** | Evicts the item with the lowest access frequency | Useful when certain items are consistently popular over time |
| **FIFO (First In, First Out)** | Evicts the oldest item in the cache | Simple to implement; not always optimal for access patterns |
| **Random Eviction** | Evicts a random item when space is needed | Simple and avoids expensive tracking of usage; used in distributed caches |
| **TTL / Expiry-based Eviction** | Items are automatically evicted after a fixed time-to-live | Helps control staleness; widely used in Redis, Memcached |
| **Size-based Eviction** | Evicts items when cache exceeds a maximum size or memory limit | Often combined with LRU/LFU policies to maintain memory constraints |
| **Segmentation / Multi-tiered Eviction** | Divides cache into segments (e.g., window + main) and applies different policies per segment | Used in high-performance caches like Caffeine for near-optimal eviction |
| **Write-through / Write-back Triggers** | Eviction occurs when underlying storage is written to, depending on cache policy | Ensures consistency between cache and persistent storage |

### Invalidation

> **Cache Invalidation** is the process of **removing or updating stale entries** in the cache to maintain consistency with the original data source. This is a key challenge in cache design due to trade-offs in performance and correctness.
> 

| **Technique** | **Description** | **Notes** |
| --- | --- | --- |
| **Explicit Invalidation** | Application or system explicitly removes entries from the cache. | `cache.delete(key)` in Redis, Ehcache, or Caffeine. |
| **Time-to-Live (TTL)** | Cached entries expire automatically after a fixed duration. | `cache.put(key, value, ttl=60s)`; reduces staleness but allows temporary inconsistency. |
| **Write-Invalidate Protocols** | Used in multiprocessor cache coherence; marks copies in other caches as invalid when updated. | MESI, MOESI protocols in CPU caches; relevant in distributed caches too. |
| **Callback / Observer Invalidation** | Backend notifies the cache when data changes, triggering invalidation. | Database triggers, Redis keyspace notifications, Hazelcast listener events. |
| **Lazy Invalidation** | Cache checks validity only when the data is accessed. | On-demand refresh or validation in Guava LoadingCache or custom caches. |

## Tool

| **Category** | **Tool** | **Description** |
| --- | --- | --- |
| **CPU / Hardware** | **L1/L2/L3 Caches** | Multi-level hardware caches in modern CPUs; store frequently accessed memory blocks to reduce main memory latency. |
|  | **TLB (Translation Lookaside Buffer)** | Caches recent virtual-to-physical memory address translations to speed up memory management unit (MMU) lookups. |
|  | **Branch Prediction Cache** | Caches results of recent branch outcomes to improve speculative execution. |
| **Operating System** | **Page Cache** | Caches file system pages in RAM to avoid repeated disk I/O on reads and writes. |
|  | **dentry/inode cache** | Caches filesystem metadata (directory entries and inodes) in the VFS layer. |
| **Web / Networking** | **CDNs (e.g., Cloudflare, Akamai)** | Globally distributed edge caches that store and serve static or cached dynamic web content. |
|  | **Browser Cache** | Client-side HTTP cache storing assets like CSS, JS, and images for fast reloads. |
|  | **Varnish Cache** | HTTP reverse proxy that caches web server responses to reduce backend load. |
|  | **Nginx FastCGI Cache** | Stores FastCGI responses from backend (e.g., PHP) to serve them quickly. |
|  | **Squid Proxy** | Caching and forwarding HTTP proxy server used to reduce bandwidth and improve latency. |
| **Application Layer** | **Memcached** | In-memory key-value store used for caching database query results, session data, or API responses. |
|  | **Redis** | Advanced in-memory data structure store supporting key expiry, LRU eviction, pub/sub, and cache invalidation mechanisms. |
|  | **Ehcache** | Java-based caching library for general-purpose application data (often used with Spring). |
|  | **Caffeine** | High-performance Java caching library using LRU, time-based expiration, and async loading. |
| **Database** | **PostgreSQL Buffer Cache** | Caches frequently used disk blocks in memory to speed up reads. |
|  | **MySQL Query Cache** | (Deprecated) Cached SELECT query results to reduce parsing and planning overhead. |
|  | **Redis as a Cache Layer** | Used in front of relational or NoSQL databases to cache expensive read operations. |
| **Build Systems / DevOps** | **ccache** | Caches compiler output to avoid recompiling unchanged source code in C/C++ builds. |
|  | **Bazel Remote Cache** | Distributed build artifact cache to accelerate builds across environments. |
|  | **Docker Layer Cache** | Caches intermediate container image layers to speed up rebuilds. |
| **Machine Learning / Data** | **DVC (Data Version Control)** | Caches intermediate data artifacts, models, and results for reproducibility and pipeline speed. |
|  | **Torch Hub / Hugging Face Cache** | Stores pretrained models locally to avoid repeated downloads. |
|  | **Joblib.Memory** | Python library that caches results of expensive computations (e.g., in scikit-learn pipelines). |

## **Benchmark**

> See more in [**Benchmarking**](note.html?n=technica/computation/system/evaluation/benchmarking.md).
> 

### 🎯 Metric

| Metric | What It Measures |
| --- | --- |
| 🕒 **Latency (ms/µs)** | Time per cache GET/SET under various load levels |
| ⚡ **Throughput (ops/sec)** | Operations handled per second under sustained concurrency |
| 🎯 **Hit Rate (%)** | Proportion of successful cache hits versus total lookups |
| 🚮 **Eviction Rate** | Frequency of item eviction under memory pressure |
| 🧠 **Memory Usage** | Memory overhead vs cache capacity and object size |
| 🔁 **Serialization Overhead** | Latency incurred due to (de)serialization of objects |

### 🧪 Workload

> The set of operations the cache will handle during the benchmark.
> 

| **Workload** | **Characteristics** | **Notes** | **Typical Use Case** |
| --- | --- | --- | --- |
| **Read-heavy** | >80% reads, <20% writes | Measures cache efficiency under mostly retrieval operations | Content delivery, session retrieval |
| **Write-heavy** | >50% writes, frequent updates | Tests cache write performance and eviction handling | Logging systems, real-time analytics |
| **Mixed / Balanced** | 50/50 or configurable read/write ratio | Simulates realistic application usage | General-purpose web applications |
| **Uniform Access** | Keys accessed uniformly at random | Tests baseline performance without hotspots | Stress tests, microbenchmarks |
| **Zipfian / Hotspot** | Some keys are accessed much more frequently | Evaluates cache hit ratio under skewed access patterns | Web caches, recommendation systems |
| **Sequential / Streaming** | Keys accessed in increasing/decreasing order | Measures eviction under sequential data patterns | Time-series caching, streaming data |
| **Random Large Objects** | Variable-size keys/values, often large | Tests memory usage and eviction strategies | Media caches, large object storage |
| **Burst / Spike** | Short periods of very high load | Measures system behavior under sudden traffic spikes | Flash sales, sudden analytics queries |
| **Temporal / TTL-sensitive** | Keys have varying TTLs, expire quickly | Evaluates expiration handling and eviction efficiency | Session caches, short-lived data |
| **Concurrency-heavy** | High number of concurrent clients | Measures throughput, contention, and locking behavior | Distributed caches, multi-threaded applications |

## Why Cached?

- **Performance Improvement** – Serving data from memory is much faster than retrieving it from disk or a remote system.
- **Reduce Load on Backend Systems** – Frequent requests can be served from cache, lowering database or service stress.
- **Intrinsic Requirement of the Computation** – Some systems rely on local storage or in-memory caching to function efficiently, such as web applications using local storage or in-browser caches.

## ✅  Checklist

| Category | Item | Description |
| --- | --- | --- |
| ⚡ Performance | Cache Hot Data | Identify frequently accessed data and cache it to reduce latency. |
| 🗄️ Storage | Choose Storage Type | Decide between in-memory, disk, or hybrid cache based on data size and access patterns. |
| ⏱️ Expiration | TTL / Eviction Policy | Define Time-to-Live (TTL) or eviction strategy (LRU, LFU) to avoid stale data. |
| 🔄 Consistency | Invalidation Strategy | Plan how and when to invalidate cached data (explicit, write-through, write-back). |
| 📊 Metrics | Monitor Cache | Track hit rate, miss rate, and eviction count to tune performance. |
| 🔒 Security | Sensitive Data | Avoid caching sensitive or private information unless encrypted or safe. |
| 🌐 Scalability | Distributed Cache | Consider distributed caching if multiple nodes need access to the same data. |

## ⚠️ Pitfalls

| Pitfall | Description | Impact |
| --- | --- | --- |
| ❌ Stale Data | Cached data may become outdated if invalidation is not properly handled. | Inconsistent application state. |
| 🐢 Over-Caching | Caching too much data can overwhelm memory and reduce performance. | Memory pressure and potential crashes. |
| 🔄 Inconsistent Invalidation | Some caches may be updated while others are stale. | Data inconsistencies across services. |
| ⏳ Long TTL | Data remains cached longer than necessary. | Users see outdated information. |
| 🛑 Ignoring Writes | Write-through or write-back not configured properly. | Lost updates or extra backend load. |
| 📉 Poor Monitoring | Lack of metrics leads to unoptimized caching. | Missed opportunities for performance tuning. |
| 🏗️ Complexity | Distributed cache adds network overhead and complexity. | Harder maintenance and debugging. |

## 🔁 **Use Case**

| **Category** | **Use Case** | **Description** |
| --- | --- | --- |
| **Web Applications** | Session Storage | Store user session data in memory to reduce DB access and improve response time. |
|  | Page / Fragment Caching | Cache rendered HTML fragments or pages to speed up delivery of dynamic content. |
|  | Query Result Caching | Cache database query results to reduce load on relational or NoSQL DBs. |
|  | Authentication / Token Cache | Cache authentication tokens or OAuth sessions to speed up repeated requests. |
| **Distributed Systems** | Shared State | Maintain a shared, in-memory state across microservices for fast read/write access. |
|  | Leader Election / Coordination | Use ephemeral keys for distributed coordination in cluster systems (e.g., Redis, etcd). |
|  | Distributed Locking | Cache-based locks for critical sections in distributed applications. |
| **Data Analytics / Big Data** | Intermediate Result Cache | Cache intermediate computation results to avoid recomputation in ETL pipelines or Spark jobs. |
|  | Hot Data Cache | Keep frequently accessed rows, columns, or blocks in memory for fast analytics queries. |
|  | Streaming Data Cache | Maintain sliding-window caches for real-time processing of streams. |
| **API / Microservices** | Rate Limiting / Throttling | Cache counters or tokens to enforce API rate limits efficiently. |
|  | Response Caching | Cache API responses to reduce backend load and latency. |
| **E-commerce / Retail** | Product Catalog Cache | Cache product information, prices, and availability for fast lookup. |
|  | Shopping Cart Cache | Store user carts in memory to handle high-volume traffic efficiently. |
|  | Flash Sale / Spike Handling | Use cache to handle burst traffic without hitting DB, often combined with TTL and LRU eviction. |
| **Content Delivery / Media** | CDN / Edge Cache | Cache static assets (images, videos, CSS, JS) close to users to reduce latency. |
|  | Video / Media Chunk Cache | Cache frequently accessed video or media chunks in memory for streaming services. |
| **Machine Learning / AI** | Feature Cache | Cache precomputed features to speed up model inference. |
|  | Model / Embedding Cache | Keep frequently used embeddings or small models in memory for low-latency predictions. |
| **Networking / Systems** | DNS Cache | Cache resolved DNS entries to avoid repeated network lookups. |
|  | ARP / Routing Table Cache | Cache network layer information to improve packet routing efficiency. |
| **Mobile / Edge Computing** | Local Offline Cache | Store recent or frequently accessed data on mobile/edge devices for offline usage. |
|  | Sensor / IoT Data Buffer | Temporarily cache IoT sensor data before sending to central servers. |
| **Transactional Systems / Finance** | Account / Balance Cache | Cache frequently queried account balances to reduce DB load in high-frequency trading or banking apps. |
|  | Payment Session Cache | Cache transaction sessions to prevent repeated DB access and speed up checkout. |
| **Persistence / Storage Optimization** | Read-Through / Write-Through | Cache acts as intermediary for persistent storage to speed up reads/writes. |
|  | Disk / File Cache | Cache frequently accessed file blocks or disk sectors in memory. |
| **Security** | Captcha / Anti-bot Cache | Temporarily cache user interaction tokens or verification results. |
|  | Fraud Detection / Blacklist Cache | Keep frequently accessed blacklists or risk scores in memory for low-latency checks. |
| **Gaming** | Player State Cache | Store player stats, inventory, and game state in memory to reduce DB hits. |
|  | Leaderboard Cache | Maintain frequently accessed leaderboards or rankings in memory for fast retrieval. |

## 🗂️ Case Study

| Category / Problem | Description | Solution(s) |
| --- | --- | --- |
| 🌐 Web Content | High latency serving dynamic web pages (e.g., news site, e-commerce catalog) | Use **CDNs** for static assets, **edge caching**, **page fragment caching** for dynamic content. |
| 🏪 Database Load | Backend DB overwhelmed by repeated queries for popular data | Implement **in-memory caches** (Redis, Memcached), **query result caching**, **read-through/write-through caching**. |
| 📦 E-commerce Inventory | Frequently changing inventory causes high DB reads | **Cache inventory snapshots** with short TTL, **use event-driven invalidation** on stock updates. |
| 🎮 Gaming / Leaderboards | Real-time scoring queries generate heavy DB traffic | Use **in-memory leaderboard cache**, periodically **sync with DB**, **write-behind caching** for updates. |
| 📊 Analytics / BI | Repeated aggregation queries slow down reporting | **Precompute and cache aggregates**, **materialized views**, **memoization for complex computations**. |
| 🔄 API Rate Limiting | High volume of identical API requests | **Cache API responses** with TTL, **use reverse proxies** to reduce redundant processing. |
| 💳 Payment / Transaction Systems | Frequent validation of repeated transactions | **Cache validation results temporarily**, **ensure expiration** to maintain consistency and compliance. |
| 🧠 Machine Learning Features | Online feature retrieval slows model predictions | **Feature caching** in memory or Redis, **lazy recomputation** for rarely updated features. |
| 🛠️ Microservices | High inter-service call volume | **Local caches per service**, **distributed cache for shared data**, **cache-aside pattern**. |
| 🖼️ Media Delivery | Serving large images/videos repeatedly | **CDN edge caching**, **chunked caching**, **object storage caching**. |

## QA

- What are the theoretical performance limits of in-memory caching?
- …

## References

- https://en.wikipedia.org/wiki/Cache_(computing)
- [**In-Memory Data Grid (IMDG)**](note.html?n=technica/computation/data-system/data-system-conceptual-model/in-memory-data-grid-imdg.md)
- https://github.com/dbremont/system-design-labs/tree/main
- [ ]  https://cache2k.org/benchmarks.html
- [ ]  https://github.com/xeoncross/go-cache-benchmark
- [ ]  https://github.com/ben-manes/caffeine/wiki/benchmarks
- [ ]  https://adriacabeza.github.io/2024/07/12/caffeine-cache.html
- [ ]  https://news.ycombinator.com/item?id=8631898
- [ ]  https://news.ycombinator.com/item?id=13429314
- [ ]  https://news.ycombinator.com/item?id=21588893
- [ ]  https://news.ycombinator.com/item?id=18106847
- [ ]  https://news.ycombinator.com/item?id=33749677
- [ ]  https://news.ycombinator.com/item?id=19188642
- [ ]  https://news.ycombinator.com/item?id=16317613
- [ ]  https://news.ycombinator.com/item?id=21023949
- [ ]  https://news.ycombinator.com/item?id=33427349
- [ ]  https://news.ycombinator.com/item?id=3609011
- [ ]  https://news.ycombinator.com/item?id=39956327
- [ ]  https://news.ycombinator.com/item?id=14147226
- [ ]  https://news.ycombinator.com/item?id=11387540
- [ ]  https://news.ycombinator.com/item?id=5144325
- [ ]  https://news.ycombinator.com/item?id=26686770
- [ ]  https://news.ycombinator.com/item?id=42907488
- [ ]