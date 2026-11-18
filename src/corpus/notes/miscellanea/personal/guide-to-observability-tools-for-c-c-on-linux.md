---
tags: [note, guia]
---

# Guide to Observability Tools for C/C++ on Linux


> The current implementation doesn't support **multithreading** because it uses a global static array (`stack[MAX_FUNC_STACK]`) that is shared across all threads. To properly support multithreading, we need to use **thread-local storage (TLS)** with `__thread` or `pthread_getspecific()`.
> 

QA:

- How to interprose gmon `mcount`?
- How to profile PostgreSQL? perf, callgrind, or bpftrace ,…
- How to use `finstrument-functions` for instrumentation?
- …

## Index

| **Option** | **Use Case** | **Instrumentation Method** |
| --- | --- | --- |
| `-pg` | Profiling with `gprof` | Inserts `mcount()` calls |
| `-fprofile-arcs -ftest-coverage` | Code coverage with `gcov` | Adds execution counters in each branch |
| `-finstrument-functions` | Custom function tracing | Calls `__cyg_profile_func_enter/exit()` |
| `-fsanitize=` | Injects runtime checks to detect memory errors (`AddressSanitizer`), undefined behavior (`UBSan`), and thread race conditions (`ThreadSanitizer`). |  |

## **Thread-Safe Implementation Using `__thread` (Thread-Local Storage)**

This version ensures that each thread has its own function stack.

```c
#define _GNU_SOURCE
#include <stdio.h>
#include <time.h>
#include <dlfcn.h>
#include <stdint.h>
#include <pthread.h>

typedef struct {
    void *func_addr;
    struct timespec start_time;
} func_entry_t;

// Thread-local storage for function timing stack
#define MAX_FUNC_STACK 1024
static __thread func_entry_t stack[MAX_FUNC_STACK];
static __thread int stack_index = 0;

void __attribute__((no_instrument_function)) __cyg_profile_func_enter(void *func, void *caller) {
    if (stack_index >= MAX_FUNC_STACK) return;

    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);  // Get current timestamp

    stack[stack_index].func_addr = func;
    stack[stack_index].start_time = ts;
    stack_index++;
}

void __attribute__((no_instrument_function)) __cyg_profile_func_exit(void *func, void *caller) {
    if (stack_index <= 0) return;

    struct timespec end_time;
    clock_gettime(CLOCK_MONOTONIC, &end_time);

    stack_index--;
    func_entry_t entry = stack[stack_index];

    if (entry.func_addr != func) return;  // Basic sanity check

    uint64_t duration_ns = (end_time.tv_sec - entry.start_time.tv_sec) * 1000000000ULL +
                           (end_time.tv_nsec - entry.start_time.tv_nsec);

    Dl_info info;
    if (dladdr(func, &info) && info.dli_sname) {
        printf("[Thread %ld] Function %s executed in %lu ns\n", pthread_self(), info.dli_sname, duration_ns);
    }
}

```

---

## **How This Fixes Multithreading Issues**

1. **Each thread has its own function stack**:
    - The `__thread` keyword makes `stack` and `stack_index` **thread-local**, meaning each thread has its own independent copy.
2. **No global shared state**:
    - Avoids data races without needing locks, which keeps performance high.
3. **Thread IDs are included in output**:
    - Uses `pthread_self()` to show which thread executed each function.

---

## **Compiling and Running**

### **Compile the Shared Library**

```bash
gcc -shared -fPIC -o myprofiler.so myprofiler.c -ldl -pthread

```

### **Run Your Program with LD_PRELOAD**

```bash
LD_PRELOAD=./myprofiler.so ./your_program

```

### **Example Output (Multithreaded Program)**

```
[Thread 140582137472768] Function main executed in 123456 ns
[Thread 140582137472960] Function worker_thread executed in 567890 ns

```

---

### **Alternative: Using `pthread_key_t` for Even More Flexibility**

If `__thread` isn't available, we can use `pthread_getspecific()` with a **per-thread stack** stored in `pthread_key_t`. Let me know if you want that version!

Would you like enhancements such as **logging to a file** or **profiling only specific functions**? 🚀

### Profiling S**hortcomings**

The `-pg` / `gmon` profiling method (used with `gprof`) has several **shortcomings** that limit its usefulness in modern performance analysis. Here are the key issues:

**Does Not Profile Multi-Threaded Programs Well**

- `gprof` relies on `mcount()` or `__monstartup()`, which are **not thread-safe**.
- If a multi-threaded program is profiled, the results can be inaccurate because `gmon.out` does not distinguish between different threads.
- Many modern applications use threads (via pthreads or OpenMP), making `gprof` less effective.

**No Precise Call Graph Timing**

- `gprof` can show how many times functions are called, but **it does not accurately measure the time spent in functions**.
- It relies on statistical sampling (via `setitimer()` and `SIGPROF`), which can introduce inaccuracies.
- Inline functions and tail-call optimizations can cause misleading results since `gprof` does not track these properly.

**Excludes System Time and I/O Wait**

- `gprof` only tracks **CPU time spent inside user-space functions**.
- It does not account for:
    - Time spent in kernel-space (e.g., system calls, page faults, context switches).
    - Time spent waiting for I/O operations (e.g., disk access, network requests).
- As a result, if a program spends a lot of time in system calls (e.g., `read()`, `write()`, `poll()`), `gprof` will not capture this.

**High Overhead Due to `mcount()`**

- When compiled with `pg`, each function call triggers a call to `mcount()`, which records profiling data.
- This significantly slows down execution (can be **2-10x slower**).
- Programs with **frequent short function calls** suffer the most from this overhead.

**No Support for Shared Libraries (`.so`)**

- `gprof` does not work well with **dynamically linked shared libraries** (e.g., `.so` files).
- Calls to functions in shared libraries are **not recorded**, making profiling incomplete.

**No Real-Time Profiling**

- `gprof` only provides **post-execution analysis**.
- You must:
    1. Run the program.
    2. Generate `gmon.out`.
    3. Analyze with `gprof`.
- This makes it **impossible to do real-time performance monitoring**, unlike tools like `perf` or `Valgrind`.

**Not Suitable for Large Codebases**

- Large applications with thousands of functions generate **huge `gmon.out` files**.
- The analysis with `gprof` can be **very slow**.
- The reports become harder to interpret due to excessive detail.

**Compiler Optimizations Break Accuracy**

- Modern compilers (GCC, Clang) perform aggressive optimizations like:
    - Function inlining
    - Tail call elimination
    - Loop unrolling
- `gprof` does not properly account for these optimizations, leading to misleading results.

### Alternatives

Here's a table comparing alternatives to `gprof` (`-pg`/`gmon`) for performance profiling:

| **Tool** | **Pros** | **Cons** | **Best For** |
| --- | --- | --- | --- |
| **Linux `perf`** | - Low overhead  - Works on optimized binaries - Profiles CPU & system calls - Supports multi-threading - Kernel and user-space profiling | - Complex output - Requires Linux | System-wide profiling, kernel & user-space performance analysis |
| **Valgrind / Callgrind + KCacheGrind** | - No need for `-pg` recompilation - Precise function timing - Graphical visualization | - Very high overhead - Slows execution significantly | Function-level profiling, visual call graphs |
| **Google `gperftools` (CPU Profiler)** | - Low overhead - Works in multi-threaded apps - Call graph visualization - Can be used in production | - Requires instrumentation - No system-wide profiling | CPU-bound performance issues, production profiling |
| **`strace`** | - Tracks system calls - No recompilation needed | - Slows execution - No CPU profiling | Debugging syscall bottlenecks |
| **`ltrace`** | - Tracks shared library calls - No recompilation needed | - Slows execution - No CPU profiling | Profiling dynamic library calls |
| **Intel VTune Profiler** | - Advanced profiling features - Works on optimized code - Multi-threading & memory analysis | - Requires Intel CPUs - Proprietary software | In-depth CPU, cache, and memory analysis |
| **AMD uProf** | - Detailed CPU profiling for AMD CPUs - Works on optimized code - Thread-aware | - Requires AMD CPUs - Complex UI | Profiling AMD architectures |
| **Flamegraphs (`perf + flamegraph.pl`)** | - Visual representation of performance - Works with many profiling tools - Easy to interpret | - Requires extra setup - Needs large sample size | Identifying CPU hot spots in large applications |

## References

- [GCC Instrumentation](https://app.notion.com/p/GCC-Instrumentation-1c1c0f5171ec8051b457cd79d8ec5369?pvs=21)
- [‣](https://app.notion.com/p/c3742c0a3fb54745906235947e3aa5b7?pvs=21)
- [Perf](https://app.notion.com/p/Perf-c038a059952e410f85ae24bce18752ce?pvs=21)
- [LTTng](https://app.notion.com/p/LTTng-1c1c0f5171ec806aa0c4c0e13727a0af?pvs=21)
- [Profiler](https://app.notion.com/p/Profiler-1c1c0f5171ec80f0ae85c627e8971d92?pvs=21)
- [Valgrind](https://app.notion.com/p/Valgrind-d589e7a83fc44a40953937547cdc50d2?pvs=21)
