---
tags: [signal]
---

# SIGPROF

- [Signal](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/signal.md)

> The **`SIGPROF`** signal is a **Unix signal** that is used primarily for **profiling** purposes, and it is directly related to **timed sampling** in profiling tools like `gprof`.
> 

## **How `SIGPROF` Works?**

> **`SIGPROF`** is triggered by a **timer interrupt**, commonly at 100 Hz, but can be adjusted at the system level.
> 

> It is used in profiling tools to periodically collect program state, typically for performance analysis.
> 

> Programs can **ignore, handle, or catch** the signal, and when profiling is enabled (e.g., with `gprof`), it helps record function call data.
> 

1. **Timer Interrupt**
    - `SIGPROF` is typically delivered by a **timer interrupt**. The system generates this signal at regular intervals, which is commonly set to **100 Hz** (100 times per second), but this frequency can be adjusted depending on the system or the profiling tool being used.
2. **Triggering the Signal**
    - When the timer interrupt fires, the operating system sends a **`SIGPROF` signal** to the running process.
    - This interrupt can be used to profile a program by periodically pausing its execution and recording relevant information, such as the **program counter** or the **call stack** at that moment.
3. **Usage in Profiling**
    - Profiling tools like **`gprof`**, **`perf`**, or other performance analysis tools often use **`SIGPROF`** to periodically interrupt the target program and collect **execution state** (e.g., which function is currently being executed).
    - The profiler can then analyze the data from these periodic samples to create a statistical representation of program performance (such as hot spots in the code).
4. **Behavior of the Signal**
    - When the signal is received, the program can be configured to either:
        - **Ignore** the signal (which is typically the case for most programs unless a profiler or specific handler is in place).
        - **Catch** and handle the signal, often by using a signal handler that records the program state or performs profiling tasks.
        - **Terminate** the program, although this is rare with profiling signals, as it is typically used to collect information, not to stop execution.
5. **Profiler Response**
    - In **`gprof`**, for instance, when a program is compiled with the `pg` option, a function `mcount()` is called whenever `SIGPROF` is received. The `mcount()` function logs the current function's entry, and this data is later used to generate a call graph and performance statistics.
6. **Relation to Other Signals**
    - **`SIGPROF`** is similar to other signals like `SIGALRM` (which is also used for timed events) but is typically associated with profiling tools and often has lower priority compared to `SIGALRM`.

## **How to Control `SIGPROF` Frequency?**

The frequency of `SIGPROF` is typically tied to the system's **timer interrupt** frequency, and to change this frequency, you would have to:

- Modify system settings (e.g., adjust the system timer or kernel settings).
- Use a different profiling tool that provides more direct control over sampling frequency, such as `perf` or `gperftools`.