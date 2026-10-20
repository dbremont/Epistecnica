# Structure Concurrency


> Structured concurrency is a programming paradigm that ensures that multiple concurrent operations (like threads or tasks) are organized in a well-defined and manageable hierarchy, making the program easier to reason about and safer to execute.
> 

## Strategies

Here is a table summarizing various "Structured Concurrency" strategies, their definitions, and key features:

| **Strategy** | **Definition** | **Key Features** |
| --- | --- | --- |
| **Task Scoping** | Concurrency is managed by defining explicit scopes for tasks, ensuring they start and finish together. | Helps in tracking task lifecycles, simplifies error handling, and improves resource management. |
| **Parent-Child Tasks** | Tasks are structured in a hierarchy where parent tasks can await the completion of their child tasks. | Ensures that child tasks do not outlive their parent tasks, enhancing control and predictability. |
| **Cancellation Propagation** | Cancellations are propagated through task hierarchies, ensuring that if a parent task is cancelled, all its child tasks are also cancelled. | Facilitates clean shutdown of concurrent operations and avoids orphaned tasks. |
| **Exception Handling** | Structured concurrency includes mechanisms for propagating and handling exceptions across task boundaries. | Ensures that exceptions in child tasks are handled or propagated to parent tasks for coordinated recovery. |
| **Resource Management** | Resources are allocated and deallocated in a structured manner, tied to the lifecycle of tasks. | Prevents resource leaks by ensuring resources are properly released when tasks complete. |
| **Join Patterns** | Structured concurrency often employs join patterns where tasks can be awaited collectively or individually. | Simplifies synchronization and coordination between multiple concurrent tasks. |
| **Synchronization** | Provides structured ways to synchronize tasks, often using primitives like barriers or latches. | Ensures tasks reach certain points of execution together, avoiding race conditions and ensuring coherence. |
| **Task Composition** | Tasks can be composed in a structured way, enabling the combination of multiple concurrent operations into higher-level constructs. | Enhances modularity and reusability of concurrent code. |
| **Time-bounded Execution** | Supports setting time limits on tasks, ensuring they do not run indefinitely and can be terminated if they exceed their allocated time. | Helps in managing time-sensitive operations and avoiding runaway tasks. |
| **Structured Futures/Promises** | Futures or promises are used in a structured manner, ensuring they are resolved within the scope of their originating tasks. | Provides a reliable mechanism for asynchronous task completion and result propagation. |

This table provides a structured overview of various strategies used in structured concurrency, emphasizing their definitions and key features.

## References

- https://news.ycombinator.com/item?id=16921761
- https://news.ycombinator.com/item?id=36559030
- https://news.ycombinator.com/item?id=34664373
- https://news.ycombinator.com/item?id=25032133
- https://blog.yoshuawuyts.com/tree-structured-concurrency/
- https://openjdk.org/jeps/453
- https://en.wikipedia.org/wiki/Structured_concurrency
- Janicki, Ryszard, and Maciej Koutny. "Structure of concurrency." Theoretical Computer Science 112.1 (1993): 5-52.
- [Structured Concurrency in High-level Languages](https://250bpm.com/blog:124/index.html)
- [Structured Concurrency Cross-language Forum](https://250bpm.com/blog:145/index.html)
- [A Badass Way to Connect Programs Togther](https://joearms.github.io/published/2016-01-28-A-Badass-Way-To-Connect-Programs-Together.html)