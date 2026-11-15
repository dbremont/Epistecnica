---
tags: [note, guia]
---

# A Guide to Standards Computational System Performace Analysis Benchmarks


> Standard set of  benchmarks vary by domain but generally fall into categories such as general-purpose computing, numerical computing, machine learning, and parallel/distributed processing.
> 

## Index

### **General Programming Language Benchmarks**

| **Benchmark** | **Purpose** | **Commonly Used For** |
| --- | --- | --- |
| **SPEC CPU** | Measures CPU and memory performance across languages | C, C++, Fortran, Java |
| **LLVM Test Suite** | Tests compiler optimizations and performance | C, C++, Rust (via LLVM) |
| **Google Benchmark** | Microbenchmarking of functions and libraries | C, C++ |
| **Computer Language Benchmarks Game (CLBG)** | Compares language implementations across tasks | Python, C++, Java, Rust, Go, etc. |

### **Scientific & Numerical Computing Benchmarks**

| **Benchmark** | **Purpose** | **Commonly Used For** |
| --- | --- | --- |
| **LINPACK (HPL)** | Measures floating-point performance, used in TOP500 supercomputers | C, Fortran |
| **NAS Parallel Benchmarks (NPB)** | Evaluates parallel computing performance | MPI, OpenMP, C, Fortran |
| **SPEC OMP** | Tests OpenMP-based parallel workloads | C, Fortran |

### **Machine Learning & AI Benchmarks**

| **Benchmark** | **Purpose** | **Commonly Used For** |
| --- | --- | --- |
| **MLPerf** | Measures AI and deep learning performance | TensorFlow, PyTorch, JAX |
| **DeepBench** | Evaluates deep learning operations like GEMM and RNN performance | CUDA, OpenCL, Python |

### **Parallel & Distributed Computing Benchmarks**

| **Benchmark** | **Purpose** | **Commonly Used For** |
| --- | --- | --- |
| **SPEC MPI** | Evaluates MPI-based distributed workloads | C, Fortran |
| **Graph500** | Measures large-scale graph processing performance | C, MPI |
| **HPCC (HPC Challenge)** | Tests memory bandwidth, latency, and computation in HPC systems | MPI, OpenMP, C, Fortran |

### **Web & Database Performance Benchmarks**

| **Benchmark** | **Purpose** | **Commonly Used For** |
| --- | --- | --- |
| **TPC (TPC-C, TPC-H, TPC-DS)** | Measures transaction processing and analytics in databases | SQL, NoSQL |
| **JetStream 2** | Evaluates JavaScript engine performance in browsers | JavaScript |
| **WebXPRT** | Measures web application performance | JavaScript, WebAssembly |

## References

- https://github.com/cloudmercato/awesome-benchmark
- https://www.spec.org/
