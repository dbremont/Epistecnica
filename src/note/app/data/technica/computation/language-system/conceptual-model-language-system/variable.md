---
tags: [linguistic-abstraction]
---

# Variable


> 

## Volatile Variable

> `volatile` has semantics for memory visibility. Basically, the value of a `volatile` field becomes visible to all readers (other threads in particular) after a write operation completes on it. Without `volatile`, readers could see some non-updated value.
> 

> The `volatile` keyword is used to mark a  `variable` as "being stored in main memory"; and not cached (allocated) in registers.
> 

## References

- https://en.wikipedia.org/wiki/Free_variables_and_bound_variables
- https://stackoverflow.com/questions/106591/what-is-the-volatile-keyword-useful-for