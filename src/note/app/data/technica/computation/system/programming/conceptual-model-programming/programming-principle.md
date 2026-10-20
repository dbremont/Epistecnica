---
tags: [principle]
---

# Programming Principle


> A **Programming Principle** is a **guiding normative rule** that informs design, implementation, and maintenance decisions in software systems. It constrains how code should be structured, composed, and evolved in order to achieve properties such as modularity, clarity, robustness, or scalability.
> 

## Taxonomy

> List of Software Design Principles.
> 

> **Note:** This list is incomplete.
> 

| **Category** | **Principle** | **Description** |
| --- | --- | --- |
| **🧩 Modularity** | **Separation of Concerns** | Divide a system into distinct sections, each addressing a specific concern. |
|  | **Modularity** | Structure software into interchangeable, composable, independent components. |
|  | **Information Hiding** | Hide design and implementation details to reduce system complexity. |
| **🧠 Responsibility Design** | **Single Responsibility Principle (SRP)** | Each module/class should have one, and only one, reason to change. |
|  | **Open/Closed Principle (OCP)** | Software should be open for extension, but closed for modification. |
|  | **Liskov Substitution Principle (LSP)** | Subtypes must be substitutable for their base types without breaking behavior. |
|  | **Interface Segregation Principle (ISP)** | Clients should not be forced to depend on interfaces they do not use. |
|  | **Dependency Inversion Principle (DIP)** | High-level modules should not depend on low-level modules—both depend on abstractions. |
| **♻ Reuse & Consistency** | **DRY (Don’t Repeat Yourself)** | Eliminate duplication by abstracting repeated logic into a single representation. |
|  | **KISS (Keep It Simple, Stupid)** | Simplicity should be a design goal; avoid unnecessary complexity. |
|  | **YAGNI (You Ain’t Gonna Need It)** | Don’t implement features until they are needed. |
|  | **Law of Demeter** | "Talk only to your immediate friends." Promotes minimal knowledge principle. |
| **🔗 Coupling & Cohesion** | **Loose Coupling** | Reduce interdependencies between components to allow easier evolution. |
|  | **High Cohesion** | Group related functionality together to improve readability and maintainability. |
| **🔒 Encapsulation** | **Encapsulation** | Protect internal states by exposing only necessary behaviors or interfaces. |
| **🎭 Abstraction** | **Abstraction** | Simplify usage and hide complexity through abstract interfaces. |
| **📈 Scalability** | **Scalability** | Design systems that can grow to handle increasing load or size efficiently. |
| **⚡ Performance** | **Asynchronous Processing** | Use non-blocking mechanisms to improve responsiveness and throughput. |
|  | **Caching** | Store frequently used data to avoid recomputation or fetching delays. |
|  | **Load Balancing** | Evenly distribute load across multiple nodes to optimize resource utilization. |
| **🛠 Reliability** | **Fail Fast** | Detect and handle errors immediately to avoid cascading failures. |
|  | **Graceful Degradation** | Maintain partial functionality when parts of the system fail. |
|  | **Fault Tolerance** | Design systems to continue functioning despite failures or errors. |
| **🔍 Observability** | **Observability** | Enable understanding of internal state through logs, metrics, and traces. |
| **🔄 Compatibility** | **Backward Compatibility** | Ensure new changes don't break existing clients or systems. |
| **✅ Quality Assurance** | **Automated Testing** | Use test automation to ensure code quality, prevent regressions, and validate behavior. |
|  | **Continuous Integration (CI)** | Integrate code frequently and test continuously to catch issues early. |
| **🛡 Security** | **Least Privilege Principle** | Give components/users only the access necessary to perform their function. |
|  | **Defense in Depth** | Layer multiple defensive mechanisms to reduce system vulnerabilities. |
|  | **Secure by Design** | Integrate security considerations from the start, not as an afterthought. |
| **🧪 Evolvability** | **Design for Change** | Build with change in mind—optimize for flexibility, not premature optimization. |
|  | **Design for Testability** | Architect components in a way that facilitates easy testing and isolation. |
| **⏳ Distributed Systems** | **Eventual Consistency** | In distributed environments, data may not be instantly consistent—accept delay. |
|  | **Backpressure** | Handle overloads by signaling producers to slow down (e.g., in stream processing). |
|  | **Time Is a First-Class Concern** | Account for time drift, delays, and asynchrony in distributed systems. |
| **🧱 OOP (Object-Oriented)** | **Polymorphism** | Design objects to share behaviors and override them as needed via interfaces. |
|  | **Inheritance** | Enable a class to derive properties and behaviors from a parent class. |
|  | **Composition Over Inheritance** | Favor combining simple objects over inheriting behavior through complex hierarchies. |
|  | **Message Passing** | Objects communicate via well-defined interfaces and method calls. |

## Reflections

### **The Fallacy of Perfect Abstraction**

> *Abstractions fail; design for evolvability, not perfection.*
> 
- **Leaky Abstractions**: No abstraction hides all complexity (e.g., ORMs sometimes generate inefficient SQL).
- **Law of Demeter**: "Don’t talk to strangers"—loose coupling reduces ripple effects.
- **Hyrum’s Law**: With enough users, all observable behaviors become depended upon.

### **Trade-offs Are Everywhere**

> *Every design decision is a compromise—know what you’re sacrificing.*
> 
- **CAP Theorem**: You can’t have Consistency, Availability, and Partition Tolerance simultaneously.
- **Performance vs. Correctness**: Optimizing too early can introduce bugs.
- **Simplicity vs. Flexibility**: Over-engineering kills maintainability.

### **Time Is a First-Class Problem**

> *Time and order are illusions in distributed systems—design accordingly.*
> 
- **Eventual Consistency**: The real world is async—embrace it.
- **Out-of-Order Events**: Distributed systems must handle time skew (e.g., Lamport clocks).
- **Backpressure**: Systems must handle load gracefully (e.g., Kafka, Reactive Streams).

### **Concurrency Is Hard (But Manageable)**

> *The real challenge isn’t speed—it’s managing complexity in parallel execution.*
> 
- **Amdahl’s Law**: Parallelism has diminishing returns.
- **Immutability**: Shared mutable state is the root of all evil (e.g., functional programming).
- **Actor Model**: Isolate state in independent actors (e.g., Erlang, Akka).

### **The Two Hard Problems in CS**

> *The hardest problems are often the simplest to overlook.*
> 
- **Naming Things**: Poor naming increases cognitive overhead.
- **Cache Invalidation**: Stale data causes subtle bugs.
- **Off-by-One Errors**: Edge cases dominate system failures.

### **Designing for Failure**

> *Assume everything will fail—design for it.*
> 
- **Chaos Engineering**: Netflix’s Chaos Monkey teaches resilience.
- **Circuit Breakers**: Fail fast instead of cascading failures.
- **Idempotency**: Retries should be safe (e.g., payment processing).

### **The Human Factor**

> *Software is a social construct—design for people, not just machines.*
> 
- **Cognitive Load**: Code should minimize mental effort to understand.
- **Conway’s Law**: Organizations design systems that mirror their communication structure.
- **Bike-Shed Effect**: Teams obsess over trivial decisions while ignoring hard ones.

### **The Myth of "One-Size-Fits-All"**

> *The best designs emerge from constraints, not dogma.*
> 
- **No Silver Bullet**: No language/framework solves all problems (Fred Brooks).
- **Right Tool for the Job**: SQL vs. NoSQL, monolith vs. microservices.
- **YAGNI (You Aren’t Gonna Need It)**: Avoid speculative generality.

### **Software Ages Like Milk, Not Wine**

> *Design for change—software outlives its original purpose.*
> 
- **Technical Debt**: Quick hacks accumulate interest.
- **Bit Rot**: Unmaintained systems decay.
- **The Lindy Effect**: Good designs survive; bad ones get rewritten.

**The Unreasonable Effectiveness of Hashing**

> *Hashing transforms chaos into order—turning O(n) problems into O(1) magic.*
> 
- **Consistent Hashing**: Enables scalable distributed systems (e.g., Dynamo, Cassandra).
- **Bloom Filters**: Probabilistic data structures for efficient membership tests (used in databases, caches).
- **Merkle Trees**: Detect inconsistencies in distributed data (e.g., Git, blockchain).

### **The Log: The Heart of Distributed Systems**

> *All state is just a snapshot of history—logs are the source of truth.*
> 
- **Write-Ahead Log (WAL)**: Durability in databases (e.g., PostgreSQL, Kafka).
- **Event Sourcing**: Reconstruct state by replaying logs (e.g., financial systems).
- **LSM Trees**: Log-structured storage for high write throughput (e.g., RocksDB).

### **The CAP Theorem’s Dirty Secrets**

> *You can’t "solve" CAP—you can only shift the trade-off.*
> 
- **PACELC**: Refinement of CAP (what happens when there’s no partition?).
- **CRDTs (Conflict-Free Replicated Data Types)**: Eventually consistent data structures that always converge.
- **CALM Theorem**: Consistency *as logical monotonicity* (e.g., deterministic merges).

**Why it’s deep**:

### **The Myth of Deterministic Systems**

> *Computers are not mathematical abstractions—they’re physical systems with chaos.*
> 
- **Heisenbugs**: Bugs that disappear when observed (e.g., race conditions).
- **Quirks of Floating-Point**: `0.1 + 0.2 ≠ 0.3` due to IEEE 754.
- **Compiler Optimizations**: Code ≠ execution (e.g., memory reordering).

### **The Power of Two Choices**

> *Randomness + minimal coordination often beats complex algorithms.*
> 
- **Load Balancing**: Picking 2 random servers cuts tail latency exponentially.
- **The Birthday Paradox**: Why hash collisions happen sooner than you think.

### **The Hidden Cost of Garbage Collection**

> *Memory management isn’t free—it’s a tax on every operation.*
> 
- **Stop-the-World Pauses**: Why GC hates low-latency systems.
- **Reference Counting vs. Tracing**: Cyclic references vs. unpredictable pauses.
- **Off-Heap Memory**: How Kafka avoids GC entirely.

### **The Curse of Generality**

> *Abstraction boundaries are rigid—design for extension is hard.*
> 
- **The Expression Problem**: Can you add new types *and* operations without recompiling?
- **Type Erasure**: Java generics vs. C++ templates.
- **The Visitor Pattern**: A workaround for OOP’s limitations.

### **The Physics of Databases**

> *Databases are just clever ways to cheat the speed of light.*
> 
- **B-Trees vs. LSM Trees**: Disk seeks vs. sequential writes.
- **The Five-Minute Rule**: Cache what’s accessed every 5 mins (still relevant?).
- **NVMe & Persistent Memory**: How hardware changes everything.

### **10. The Butterfly Effect in Distributed Systems**

> *Distributed systems are nonlinear—small changes have catastrophic effects.*
> 
- **Cascading Failures**: One retry storm can take down a continent (e.g., AWS outages).
- **TCP Incast**: Too many requests at once cause collapse.
- **Tail Latency Amplification**: A few slow calls can doom a system.

### **The Philosophy of Testing**

> *Tests can’t prove absence of bugs—only presence.*
> 
- **Hypothesis Testing**: QuickCheck (property-based testing) > unit tests.
- **Fuzzing**: How AFL finds bugs humans never could.
- **Formal Verification**: TLA+ for proving designs correct (e.g., AWS).

### **The Illusion of Local Reasoning**

> *In complex systems, nothing is truly local.*
> 
- **Side Effects**: How functional programming tries (and fails) to eliminate them.
- **Effect Systems**: Rust’s borrow checker as a compromise.
- **Distributed Tracing**: Why observability > debugging.

## References

- Haoyu, Wang, and Zhou Haili. "Basic design principles in software engineering." *2012 Fourth International Conference on Computational and Information Sciences*. IEEE, 2012.
- [‣](https://app.notion.com/p/10e598edb79081b3a2e7c6c2f92d2317?pvs=21)