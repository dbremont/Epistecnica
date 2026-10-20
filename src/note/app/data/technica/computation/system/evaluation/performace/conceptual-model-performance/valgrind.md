---
tags: [tool]
---

# Valgrind

- [LTTng](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/lttng.md), [Profiler](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/profiler.md)

> Valgrind is a versatile suite of tools for debugging and profiling programs. **Callgrind** is one of its powerful tools specifically designed for call graph generating and program profiling.
> 

> [Callgrind](perf.data) collects data about the program's function call history and the cost associated with each function, where "cost" can refer to the number of instructions executed, cache misses, or other metrics.
> 

QA:

- How to test Valgrind accuracy?
- …

## Install

```bash
sudo apt-get install valgrind # Install
```

## Use

Create a simple C program that will serve as the target for profiling. Here’s an example program, `example.c`:

```c
#include <stdio.h>

void print_count(int n) {
    for (int i = 0; i < n; i++) {
        printf("%d\\n", i);
    }
}

int main() {
    print_count(10);
    return 0;
}

```

```bash
gcc -g example.c -o example # Compile
valgrind --tool=callgrind ./example # Run callgrind
kcachegrind callgrind.out.1078739
```

## References

- [Valgrind](https://valgrind.org/)
- Nethercote, Nicholas, and Julian Seward. "Valgrind: a framework for heavyweight dynamic binary instrumentation." ACM Sigplan notices 42.6 (2007): 89-100.
- Nethercote, Nicholas, and Julian Seward. "Valgrind: A program supervision framework." Electronic notes in theoretical computer science 89.2 (2003): 44-66.
- Becker, Martin, and Samarjit Chakraborty. "A Valgrind Tool to Compute the Working Set of a Software Process." *arXiv preprint arXiv:1902.11028* (2019).
-