# Typescript: Memory Model

> **Ownership and borrowing**: Rust’s ownership and borrowing system ensures that values have a single owner and prevents multiple ownership or aliasing, which can lead to difficult-to-debug bugs like use-after-free and data races.
> 

> **Lifetimes**: Rust’s lifetime system ensures that references to values are valid for the lifetime of the referenced value, preventing dangling references and other memory safety issues.
> 

> **Ownership transfer (Move Semantics)**: Values can be moved between owners using the “move” keyword, which transfers ownership and prevents the original owner from accessing the value.
> 

> The ***items*** of a program are those functions, modules, and types that have their value calculated at compile-time and stored uniquely in the memory image of the rust process. Items are neither dynamically allocated nor freed.
> 

> The ***heap*** is a general term that describes boxes.  The lifetime of an allocation in the heap depends on the lifetime of the box values pointing to it. Since box values may themselves be passed in and out of frames, or stored in the heap, heap allocations may outlive the frame they are allocated within. An allocation in the heap is guaranteed to reside at a single location in the
heap for the whole lifetime of the allocation - it will never be relocated as
a result of moving a box value.
> 

> A *variable* is a component of a stack frame, either a named function parameter,
an anonymous [temporary](https://doc.rust-lang.org/reference/expressions.html#temporaries), or a named local variable.
> 

## References

- [Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [Memory model](https://doc.rust-lang.org/reference/memory-model.html#memory-model)
- …