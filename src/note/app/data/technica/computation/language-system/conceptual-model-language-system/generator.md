---
tags: [effect-system]
---

# Generator


> A **generator** is a **computational entity** that implements the **iterator interface** and produces a sequence of values **on demand** by **suspending and resuming execution**, preserving internal state **across invocations**, typically using a `yield` construct or equivalent continuation mechanism.
> 

> This is a mechanism to deal with infinite data structure; and also implement **Lazy Evaluation**.
> 

## **Interface Contract**

> In most languages (e.g., Python, C#, JavaScript), generators conform to the **iterator protocol**, providing: `next(): T | raises StopIteration` where `T` is the next yielded value.
> 

## Implementation

### **Resumable Continuation**

Unlike regular functions, generators maintain **execution context** (program counter and local bindings) between calls. This is commonly implemented using:

- **stack reification**
- **continuation-passing style (CPS)**
- or **compiler-generated state machines**.

### **Execution Semantics**

A generator is a form of **stateful coroutine** that encapsulates a **control flow frame** with:

- an instruction pointer (IP) for resumption,
- an activation record (stack frame) storing local variables,
- and optionally a heap or closure for captured values.

## Case Studies

### Python Generators

> In **Python**, **generators** are implemented using **compiler-generated state machines**, built on top of the **Python Virtual Machine (PVM)**. Here's a deep dive into how Python implements generators at the language and runtime level.
> 

1. **At the Language Level**

When the Python parser encounters a `yield` statement inside a function:

- It compiles that function into a **generator function**, not a regular function.
- Calling the function does **not** execute the body immediately; instead, it returns a **generator object**.

```python
def gen():
    yield 1
    yield 2

```

- This is compiled into Python bytecode that includes the `YIELD_VALUE` opcode.
- The generator object conforms to the **iterator protocol** (`__iter__`, `__next__`).

2. **Compilation to Bytecode**

Use the `dis` module to see how Python rewrites it:

```python
import dis

def gen():
    yield 1
    yield 2

dis.dis(gen)

```

**Output:**

```
  3           0 LOAD_CONST               1 (1)
              2 YIELD_VALUE
              4 POP_TOP
  4           6 LOAD_CONST               2 (2)
              8 YIELD_VALUE
             10 POP_TOP
             12 LOAD_CONST               0 (None)
             14 RETURN_VALUE

```

- `YIELD_VALUE` suspends execution and returns control to the caller.
- The function’s state (stack frame, instruction pointer, local variables) is saved.

3. **The Generator Object**

Calling `gen()` returns a `generator` object with:

- A reference to the function’s **code object**
- A **frame object** holding:
    - The instruction pointer (which bytecode to run next)
    - Local variables (`co_varnames`)
    - The operand stack

It supports:

```python
.__next__()
.send(value)
.throw(exc)
.close()

```

Internally, calling `next(generator)` resumes execution from the **last saved instruction pointer** until the next `yield`.

4. **State Machine Model**

Python turns your generator into a **state machine**, with:

- **States**: Created, Running, Suspended, Completed
- Transitions: `next()`, `send()`, `throw()`

5. **How Suspension Works**

Each time a `yield` is executed:

- The current **frame** is frozen.
- Local state (variables, instruction pointer) is stored.
- The **generator object** retains this frame for resumption.

This is fundamentally different from threads or coroutines—**no parallel execution**, just **cooperative control transfer**.

6. **Under the Hood (C level)**

In **CPython**, generator support is implemented in:

- `Python/ceval.c`: handles bytecode execution.
- `Objects/genobject.c`: defines the `PyGenObject` type.
- `YIELD_VALUE` in `ceval.c` saves the frame state and returns to the caller.

```c
// Rough sketch of YIELD_VALUE in CPython source
TARGET(YIELD_VALUE) {
    retval = POP();
    f->f_stacktop = stack_pointer;
    why = WHY_YIELD;
    goto fast_yield;
}

```

7. **Performance Note**

- Generators are **much more lightweight** than threads.
- They allow Python to **simulate coroutines** and **asynchronous I/O**, especially in `async def` / `await` patterns (which extend the generator concept via `asyncio` and `awaitable` objects).

## References

- https://en.wikipedia.org/wiki/Generator_(computer_programming)