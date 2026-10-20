---
tags: [data-collection, tool]
---

# tracy


> The Tracy Profiler is a powerful tool that integrates seamlessly into C and C++ applications, providing deep insights into performance through its server-client architecture, instrumentation capabilities, and rich GUI for data visualization. By leveraging its components, developers can effectively monitor and optimize their applications in real time.
> 

### **Tracy Server**

- The central component that runs as a standalone application.
- Receives profiling data from instrumented applications over a network socket.
- Provides a graphical user interface (GUI) to visualize the profiling data.

### **Tracy Client**

- A set of headers and libraries that you integrate into your C/C++ application.
- Provides macros and functions to instrument your code with minimal overhead.
- Automatically sends profiling data to the Tracy server during execution.

### **Instrumentation Macros**

- **ZoneScoped**: Automatically creates a profiling zone that ends when the scope is exited. Useful for measuring the duration of functions or blocks of code.
- **ZoneScopedN("Name")**: Similar to `ZoneScoped`, but allows you to name the zone for easier identification in the GUI.
- **TracyCZone**: A macro for C functions to create a zone for profiling.
- **TracyMessage**: Used for logging custom messages and data points to the profiler.

### **GUI Visualization**

- A real-time visual interface to view the profiling data.
- Displays timelines of function calls, resource usage, and performance metrics.
- Allows filtering and drilling down into specific threads, zones, and function calls for detailed analysis.

### **Thread Support**

- Tracy can profile multi-threaded applications, allowing you to track performance across different threads.
- Supports context switching, enabling analysis of how threads interact and the impact on performance.

### **Memory Profiling**

- Provides insights into memory allocation and deallocation, helping identify memory leaks and excessive usage.
- Can log memory-related events in the application to analyze how memory is utilized over time.

### **Custom Instrumentation**

- Users can define their own custom zones and message types to gather specific profiling information relevant to their applications.
- Supports advanced features like manual zone control and custom event logging.

### **Performance Metrics**

- Tracks various performance metrics, including frame time, CPU usage, and function call durations.
- Helps identify bottlenecks and areas for optimization in the application.

## References

- https://github.com/wolfpld/tracy
- https://davespace.xyz/blog/building-tracy-profiler-on-linux
- https://news.ycombinator.com/item?id=34559993
- [GDB (GNU Project Debugger)](note.html?n=technica/computation/system/evaluation/performace/conceptual-model-performance/gdb-gnu-project-debugger.md)
- - [GCC : GNU Compiler Collection]
- https://www.youtube.com/watch?v=ghXk3Bk5F2U