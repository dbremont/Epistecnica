---
tags: [monitoring]
---

# Kernel Monitoring and Tracing Facilities


## Index

Got it! If you're specifically asking about the **kernel services and APIs** related to **tracing** and **monitoring**, without the user-level tools or applications, here’s an overview of the key kernel features and subsystems that provide tracing, monitoring, and performance analysis functionality:

### 1. **ftrace (Function Tracer) API**

The **ftrace** subsystem provides the core framework for tracing kernel functions and events. It allows kernel modules to trace function calls, schedule events, and more. It is the primary mechanism used for function-level tracing in the Linux kernel.

### Key Services:

- **Function Tracing**: Allows tracing of function calls within the kernel using **tracepoints**.
- **Event Tracing**: Tracks kernel events like process context switches, interrupt handling, and more.
- **Dynamic Tracing**: You can enable/disable tracing of functions or events dynamically via the `/sys/kernel/debug/tracing` directory.

### API:

- **tracepoint**: Tracepoints in the kernel code (e.g., `sched_switch`, `irq_handler_entry`).
- **trace_set_*()**: Functions for enabling/disabling events.
- **trace_event()**: API for defining custom trace events.

Example for using the kernel's trace API:

```c
#include <linux/tracepoint.h>

TRACE_EVENT(my_trace_event,
    TP_PROTO(int param),
    TP_ARGS(param),
    TP_STRUCT__entry(
        __field(int, param)
    ),
    TP_fast_assign(
        __entry->param = param;
    ),
    TP_printk("param = %d", __entry->param)
);

```

### 2. **BPF (Berkeley Packet Filter) / eBPF (Extended BPF) API**

eBPF allows for high-performance, low-overhead kernel tracing and monitoring. It's a more general-purpose system for running custom code in response to kernel events.

### Key Services:

- **Tracing**: eBPF can trace kernel events like function calls, system calls, and networking events.
- **Performance Monitoring**: eBPF can be used for CPU performance counters, context switches, and custom metrics.
- **Networking**: eBPF enables advanced network monitoring and manipulation.

### API:

- **bpf() syscall**: Used to load and attach eBPF programs to kernel events.
- **BPF Type Format (BTF)**: eBPF uses BTF for type information, making it more extensible.
- **bpf_trace_printk()**: Used for logging trace output from within eBPF programs.
- **BPF_PROG_ARRAY**: Allows the attachment of multiple eBPF programs to different events.

Example of a simple BPF program:

```c
#include <linux/bpf.h>

SEC("tracepoint/syscalls/sys_enter_execve")
int bpf_prog1(struct trace_event_raw_sys_enter *ctx) {
    bpf_trace_printk("execve system call invoked\n");
    return 0;
}
char _license[] SEC("license") = "GPL";

```

### 3. **Perf Events API**

The **perf events** subsystem provides an API for kernel performance monitoring, allowing you to gather hardware performance counters, software events, and trace kernel events for analysis.

### Key Services:

- **Performance Monitoring**: Tracks CPU cycles, cache hits/misses, branch mispredictions, and other hardware-level counters.
- **Kernel Tracepoints**: Monitors kernel events such as context switches, system calls, and interrupts.
- **Sampling**: Collects periodic samples of CPU activity, including call graphs and stack traces.

### API:

- **perf_event_open()**: Opens a performance event for monitoring.
- **perf_event_read()**: Reads the current value of a performance event.
- **perf_event_attr**: Defines the event type and configuration.

Example usage in kernel (simplified):

```c
#include <linux/perf_event.h>

struct perf_event_attr attr = {
    .type = PERF_TYPE_HARDWARE,
    .config = PERF_COUNT_HW_CPU_CYCLES,
    .size = sizeof(struct perf_event_attr),
};

int fd = sys_perf_event_open(&attr, 0, -1, -1, 0);
if (fd < 0)
    return -1;

long long count;
read(fd, &count, sizeof(count));

```

### 4. **Tracepoints (Kernel Static Instrumentation)**

Tracepoints are static hooks inserted into the kernel that allow tracing of specific events, such as system calls, kernel function entries/exits, and scheduling events. Tracepoints can be configured at runtime to gather specific metrics.

### Key Services:

- **Static Tracepoints**: Kernel developers insert these tracepoints at specific locations in the code to allow runtime tracing.
- **Tracepoint API**: The `tracepoint()` API is used to define and log data for tracepoints.

### API:

- **TRACE_EVENT()**: Used to define custom trace events in the kernel.
- **tracepoint_probe_register()**: Registers a tracepoint handler.

Example of registering a tracepoint handler:

```c
#include <linux/tracepoint.h>

TRACE_EVENT(my_event,
    TP_PROTO(int arg),
    TP_ARGS(arg),
    TP_STRUCT__entry(
        __field(int, arg)
    ),
    TP_fast_assign(
        __entry->arg = arg;
    ),
    TP_printk("arg=%d", __entry->arg)
);

```

### 5. **System Calls and Sysfs for Monitoring**

Sysfs provides a mechanism for exporting kernel internal information to user space, allowing for the dynamic configuration of kernel parameters related to performance.

### Key Services:

- **Sysfs**: Through `/sys`, you can expose various kernel parameters, configuration settings, and status reports for monitoring.
- **Kernel Parameters**: For example, you can monitor CPU usage, network traffic, memory usage, and more via sysfs nodes.

### API:

- **sysfs_create_file()**: Used to create sysfs entries for performance monitoring.

Example usage:

```c
#include <linux/sysfs.h>

sysfs_create_file(kernel_kobj, &my_attribute.attr);

```

### 6. **Kprobes and Uprobes**

**Kprobes** and **Uprobes** allow dynamic instrumentation of kernel and user-space functions, respectively. They enable attaching probes to arbitrary code locations to monitor events or trace function calls.

### Key Services:

- **Kprobes**: Used to insert probes into kernel functions to trace their execution.
- **Uprobes**: Allows tracing of user-space functions or events.

### API:

- **register_kprobe()**: Registers a probe to be placed on a specific kernel function.
- **register_uprobe()**: Registers a probe for user-space function calls.

Example of registering a kprobe:

```c
#include <linux/kprobes.h>

static int handler_pre(struct kprobe *p, struct pt_regs *regs) {
    printk(KERN_INFO "Kprobe: %s\n", p->symbol);
    return 0;
}

static struct kprobe kp = {
    .symbol = "do_sys_open",
    .pre_handler = handler_pre,
};

register_kprobe(&kp);

```

### 7. **CPU Frequency and Power Monitoring API**

The kernel provides interfaces for monitoring and controlling CPU frequency and power consumption.

### Key Services:

- **CPUFreq**: Allows monitoring and adjusting CPU frequency scaling.
- **Power Management**: Provides power consumption information and allows kernel developers to tune power-saving modes.

### API:

- **cpufreq_get()**: Retrieves the current frequency of a CPU.
- **cpufreq_update_policy()**: Updates CPU frequency scaling policy.

Example usage:

```c
#include <linux/cpufreq.h>

unsigned int freq = cpufreq_get(cpu);

```

---

### Conclusion:

The Linux kernel provides a robust set of **tracing** and **monitoring APIs** for developers to instrument and monitor kernel and application behavior. These APIs are part of several subsystems such as **ftrace**, **perf**, **eBPF**, **tracepoints**, and more, allowing for extensive and flexible performance analysis at a granular level.

If you want to implement or work with any of these tracing or monitoring subsystems, you will typically interact with the corresponding **kernel APIs** mentioned above, which offer low-level access to kernel internals and performance metrics.

Let me know if you'd like further details on any specific subsystem!

## Performance Events Subsystem

Linux performance counters provide detailed insights into how the system's hardware and software are performing. These counters can be used to analyze various aspects like CPU performance, memory access, cache hits/misses, and more. You can access and manage performance counters through tools like `perf`, which interfaces directly with the kernel's **Performance Events Subsystem**.

### **🔹 Key Linux Performance Counters:**

1. **CPU Cycles (cycles)**
    - Counts the number of clock cycles.
    - Useful to measure how efficiently a program uses the CPU.
    - Example: `perf stat -e cycles ./your_program`
2. **Instructions (instructions)**
    - Counts the number of instructions executed by the CPU.
    - Helps measure **Instructions Per Cycle (IPC)**, a performance metric indicating how efficiently the CPU executes instructions.
    - Example: `perf stat -e instructions ./your_program`
3. **Cache Hits (L1-dcache-loads)**
    - Counts the number of data cache loads that were served from the L1 data cache.
    - Helps analyze the **cache hit rate** and **locality** of data.
    - Example: `perf stat -e L1-dcache-loads ./your_program`
4. **Cache Misses (L1-dcache-load-misses)**
    - Counts the number of times a data load could not be serviced from the L1 cache and had to be fetched from a higher-level cache or main memory.
    - High miss rates indicate **poor data locality**.
    - Example: `perf stat -e L1-dcache-load-misses ./your_program`
5. **Branch Instructions (branch-instructions)**
    - Counts the number of branch instructions.
    - Useful for evaluating how many branches are being executed in the code.
    - Example: `perf stat -e branch-instructions ./your_program`
6. **Branch Mispredictions (branch-misses)**
    - Counts the number of branch mispredictions (when the CPU guesses the wrong path for a branch).
    - Mispredictions cause pipeline stalls, negatively impacting performance.
    - Example: `perf stat -e branch-misses ./your_program`
7. **Context Switches (context-switches)**
    - Counts the number of context switches between processes.
    - Useful for understanding CPU scheduling and workload balance.
    - Example: `perf stat -e context-switches ./your_program`
8. **Page Faults (page-faults)**
    - Counts the number of page faults that occurred during the execution of a program.
    - High page faults indicate inefficient memory access patterns or insufficient memory.
    - Example: `perf stat -e page-faults ./your_program`
9. **CPU Migration (cpu-migrations)**
    - Counts the number of times a process is migrated from one CPU core to another.
    - Can be useful for tuning NUMA (Non-Uniform Memory Access) systems.
    - Example: `perf stat -e cpu-migrations ./your_program`
10. **Cache References (cache-references)**
    - Counts the number of cache accesses (both hits and misses).
    - Example: `perf stat -e cache-references ./your_program`
11. **Stalled Cycles (stalled-cycles-frontend / stalled-cycles-backend)**
    - Measures the number of cycles the CPU spends waiting for instructions to be fetched (frontend stall) or for execution units to become available (backend stall).
    - Indicates bottlenecks in instruction fetch or execution.
    - Example: `perf stat -e stalled-cycles-frontend ./your_program`
12. **Cycles Per Instruction (CPI)**
    - Measures the number of cycles required to execute an instruction.
    - Lower values indicate more efficient instruction execution.
    - Calculated from `cycles` / `instructions`.

---

### **🔹 Tools to Access Performance Counters:**

### **1. `perf` (Linux Performance Tool)**

`perf` is the most popular tool for accessing hardware performance counters on Linux. Here’s how to use it:

- **Basic Usage**:
    
    `perf stat` provides a summary of performance counter data.
    
    Example:
    
    ```bash
    perf stat -e cycles,instructions,L1-dcache-loads,branch-misses ./your_program
    
    ```
    
    This command will output performance stats for CPU cycles, instructions, L1 cache loads, and branch mispredictions.
    
- **Event Sampling**:
    
    For more detailed, event-level profiling, use `perf record` and `perf report`.
    
    Example:
    
    ```bash
    perf record -e cycles,instructions -p <PID>
    perf report
    
    ```
    

### **2. `perf top`**

`perf top` gives a live, top-like view of the functions consuming the most CPU cycles.

```bash
perf top

```

### **3. `stat` Command (Alternative)**

For simple CPU statistics, you can also use the `stat` command. It can give you some basic insights like CPU time, process statistics, etc.

Example:

```bash
time ./your_program

```

### **4. `tuna` (for NUMA systems)**

`Tuna` can be used for NUMA-related performance analysis by managing CPU affinity and collecting performance data across multiple NUMA nodes.

### **5. `bpftrace` (for advanced tracing)**

`bpftrace` is a powerful tracing tool that uses eBPF (Extended Berkeley Packet Filter) for dynamic tracing. It allows for advanced performance analysis, including network performance, I/O, and system calls.

---

### **🔹 Example: Using `perf` for Analysis**

To analyze CPU performance for a program (`./my_program`), focusing on cycles, instructions, and cache hits/misses:

```bash
perf stat -e cycles,instructions,L1-dcache-loads,L1-dcache-load-misses ./my_program

```

The output might look like this:

```
 Performance counter stats for './my_program':

       1,234,567,890      cycles
       2,345,678,901      instructions
           1,234,567      L1-dcache-loads
             234,567      L1-dcache-load-misses

       1.234567890 seconds time elapsed

```

From this output:

- **Cycles**: The CPU spent 1.2 billion cycles to execute the program.
- **Instructions**: The program executed about 2.3 billion instructions.
- **Cache Stats**: The L1 cache handled 1.2 million loads, but 234K of them missed, meaning the data had to be fetched from a higher-level cache or memory.

---

### **🔹 Conclusion:**

Linux performance counters provide invaluable insights into CPU performance and other hardware-related metrics. Using tools like `perf`, `bpftrace`, and `tuna`, you can identify bottlenecks, optimize code for better cache locality, and ensure efficient use of CPU resources.

Would you like a deeper dive into a specific tool or counter?