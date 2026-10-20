---
tags: [effect-system]
---

# Coroutine

- [Continuation](note.html?n=technica/computation/language-system/conceptual-model-language-system/continuation.md)

> **Coroutine** is a component that generalizes a subroutine to allow multiple entry points for suspending and resuming execution at certain locations. Unlike subroutines, coroutines can exit by calling other coroutines, which may later return to the point where they were invoked in the original coroutine.
> 

> **Coroutine Model**: Coroutines are lightweight, cooperative concurrency units that allow functions to yield control back to a scheduler and later resume from where they left off. They are commonly used in asynchronous programming.
> 

QA:

- Does an `async` function must have some internal await?
- Does an `async` function must be awaited?

## Case Studies

### Python Coroutine

> Note A Coroutine (async def compute()) must always be awaited (await compute()); if not error.
> 

> In Python, a **coroutine** is a special type of **function** that can *pause* its execution and *yield control back to the event loop*, allowing other tasks to run concurrently in a cooperative multitasking fashion.
> 

> A generator-like function declared with async def that returns a coroutine object when called, and whose execution can be suspended and resumed using the await keyword.
> 

Coroutines are:

- Coroutines are **awaitable**.
- They are **non-blocking** and **asynchronous**.
- Core to Python’s `asyncio` framework.
- Require an **event loop** to run.

🔬 Coroutine vs Generator (Key Differences)

| Feature | Coroutine (`async def`) | Generator (`def` + `yield`) |
| --- | --- | --- |
| Declared with | `async def` | `def` with `yield` |
| Returns | Coroutine object | Generator object |
| Resume with | `await` | `next()`, `.send()` |
| Use case | Asynchronous IO, concurrency | Lazy iteration, pipelines |
| Syntax | `await some_async_func()` | `yield value` |

📌 Coroutine Lifecycle

1. **Defined with** `async def`
2. **Called** → returns a coroutine object (but doesn’t execute)
3. **Awaited** → begins/resumes execution
4. **Suspends on** `await`, returns control to the event loop
5. **Resumes** when awaited task is done
6. **Terminates** with `return` or end of function

Case Study:

```python
import asyncio

async def compute():
    await asyncio.sleep(1)
    return 42

async def main():
    result = await compute()
    print(result)

asyncio.run(main())
```

Implementation:

> Coroutines in Python are implemented as **stateful objects** built on top of Python’s **generator protocol**, extended with `async`/`await` syntax and a supporting runtime in `asyncio`. Here's a deep technical breakdown:
> 

1. 🧱 **Syntax-Level Desugaring**

- A function defined with `async def` is transformed by the interpreter into a special kind of **generator-like function**.
- Instead of yielding values (`yield`), it **awaits** other awaitable objects (like coroutines or futures).

```python
async def coro():
    await some_async_func()

```

is internally similar in structure to:

```python
def coro():
    yield from some_async_func().__await__()

```

The `__await__()` method returns an **iterator**, and Python drives it with a **suspension-resumption protocol**, similar to `yield from`.

2. ⚙️ **Coroutine Objects**

When you call an `async def` function, Python creates a **coroutine object** (not a generator). These objects:

- Are **awaitable** (they implement the `__await__()` method).
- Maintain an **execution frame** and internal **state machine**.
- Are driven by the **event loop** which repeatedly resumes them.

```python
import inspect

async def foo():
    return 42

coro = foo()
print(inspect.iscoroutine(coro))  # True

```

3. 🔁 **Awaitable Protocol**

Any object implementing `__await__()` returning an iterator can be awaited:

```python
class MyAwaitable:
    def __await__(self):
        yield
        return 42

async def my_coro():
    result = await MyAwaitable()

```

---

4. ⚡ **Driving Execution: The Event Loop**

Coroutines must be **scheduled and executed** by an **event loop** (e.g., `asyncio`):

- The loop maintains a queue of coroutine objects and resumable tasks.
- When a coroutine hits an `await`, it yields control, returning to the loop.
- When the awaited object is ready (e.g., after I/O), the coroutine is resumed.

```python
async def task():
    await asyncio.sleep(1)  # suspension point

asyncio.run(task())

```

---

5. 🧬 Internals: Bytecode and Frame State

Python compiles `async def` functions into a **co_coroutine** code object.

- Uses opcodes like `GET_AWAITABLE`, `YIELD_FROM`, and `AWAIT`.
- Execution is paused with `YIELD_FROM`, and resumed later.
- Coroutine’s frame (`PyFrameObject`) stores the state, locals, and instruction pointer.

You can inspect this using the `dis` module:

```python
import dis

async def f(): await g()

dis.dis(f)

```

6. 🛠️ Coroutine State Machine

Each coroutine object can be in one of several states:

- **Created**: Before first `await` (not yet started)
- **Running**: Currently executing
- **Suspended**: Waiting at an `await` point
- **Completed**: Finished execution (either normally or via exception)

7. 💥 Exceptions and Cancellation

- Exceptions propagate through `await` like regular Python calls.
- Coroutines can be **cancelled** via `.cancel()` on the task.
- Cleanup logic is handled using `try/finally`.

```python
async def worker():
    try:
        await asyncio.sleep(10)
    finally:
        print("Cleanup")

```

## References

- https://en.wikipedia.org/wiki/Coroutine