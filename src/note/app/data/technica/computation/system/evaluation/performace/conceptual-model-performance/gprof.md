---
tags: [analysis, tool]
---

# gprof

- [LTTng](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/lttng.md), [Profiler](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/profiler.md)

> **`Gprof`** is a performance analysis tool for Unix-like systems that profiles C, C++, and Fortran programs by collecting execution statistics through instrumentation or sampling, generating call graphs and function-level timing metrics to identify bottlenecks.
> 

QA:

- How to read **`gprof`** outcomes?
- Does **`gprof`** runs the programs? No, **`gprof`** itself does **not run** the program. Instead, it **analyzes** the data collected during the execution of the program.
- How gprof uses `gcc -pg` "mcount”?
- Why gproff needs `prof example gmon.out`?
- How to test **`gcc -pg`** accuracy?
- How to overrride `gcc -pg` wit ld_preload?

## How to read this?

> **% Time**: Percentage of total execution time that the function took.
> 

> **Cumulative Time (seconds)**: Total time taken by this function and all functions above it.
> 

> **Self Time (seconds)**: Time spent in the function itself (excluding children).
> 

> **Calls**: Number of times the function was called.
> 

> **Self ms/call**: Time taken per call in milliseconds (for self time).
> 

> **Total ms/call**: Time taken per call in milliseconds (including children).
> 

> **Name**: The name of the function.
> 

```csharp
Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls  ms/call  ms/call  name    
100.00      0.03     0.03        1    30.00    30.00  function2
  0.00      0.03     0.00        1     0.00     0.00  function1
```

## How to read this?

> **Granularity**: Each sample recorded represents 4 bytes, and 33.33% of the total 0.03 seconds of execution time corresponds to one sample hit.
> 

> **Self Time**: The time spent in the function itself.
> 

> **Children Time**: The time spent in functions called by the current function.
> 

> **Calls**: The number of times the function was called during the execution.
> 

```csharp
granularity: each sample hit covers 4 byte(s) for 33.33% of 0.03 seconds

index % time    self  children    called     name
                0.03    0.00       1/1           main [2]
[1]    100.0    0.03    0.00       1         function2 [1]
-----------------------------------------------
                                                 <spontaneous>
[2]    100.0    0.00    0.03                 main [2]
                0.03    0.00       1/1           function2 [1]
                0.00    0.00       1/1           function1 [3]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[3]      0.0    0.00    0.00       1         function1 [3]
-----------------------------------------------
```

## References

- https://en.wikipedia.org/wiki/Gprof
- https://github.com/lattera/glibc/tree/master/gmon
- - [GCC : GNU Compiler Collection]
- [GCC Instrumentation](note.html?n=technica/computation/language-system/conceptual-model-language-system/gcc-gnu-compiler-collection.md)