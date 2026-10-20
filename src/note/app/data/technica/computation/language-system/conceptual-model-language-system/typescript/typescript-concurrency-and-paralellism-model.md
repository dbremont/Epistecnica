# Typescript: Concurrency and Paralellism Model

> **Rust** is a **systems programming language** renowned for its focus on safety and performance, and its approach to concurrency is no exception. Rust's ownership and type systems are designed to prevent race conditions at compile time, offering a robust foundation for writing safe concurrent code.
> 

Here's a table outlining the concurrency models in Rust:

| Concurrency Model | Description | Example |
| --- | --- | --- |
| Threads | OS-level threads that execute independently, allowing concurrent execution of multiple tasks. | `std::thread::spawn` |
| Mutexes & Locks | Mutual exclusion locks allow safe concurrent access to shared data by synchronizing access with locking mechanisms. | `std::sync::Mutex` and `std::sync::RwLock` for shared state. |
| Atomic Types | Primitive types with atomic operations allow safe concurrent access and modification without locking. | `let counter = AtomicUsize::new(0); counter.fetch_add(1, Ordering::Relaxed);` |
| Channels | Communication primitives for message passing between concurrent tasks, enabling safe data transfer and synchronization. | `let (sender, receiver) = channel(); sender.send(42).unwrap();` |
| Futures | An asynchronous programming model is based on non-blocking futures, allowing tasks to be executed concurrently without blocking the main thread. | `async fn example() { /* Async code */ }` |
| Actors | Concurrent programming model based on actors, where independent actors communicate via message passing, encapsulating state and behavior. | `actix::Actor` framework |

This table provides an overview of the concurrency models available in Rust. Each offers different approaches to concurrent programming and synchronization.

## References

- [Asynchronous Programming in Rust](https://rust-lang.github.io/async-book/)
- [Fearless Concurrency](https://doc.rust-lang.org/book/ch16-00-concurrency.html)
- …