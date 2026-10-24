# JAX


> **JAX** is a high-performance numerical computing library developed by Google, and **JAX-ML** refers to a collection of machine learning (ML) tools, libraries, and frameworks built on top of JAX.
> 

### **JAX**

- **Type**: Numerical computing library.
- **Purpose**: Designed for high-performance numerical and scientific computing, with a focus on machine learning research.
- **Key Features**:
    - **Automatic Differentiation**: Supports forward and reverse-mode autodiff, making it ideal for gradient-based optimization (e.g., training neural networks).
    - **Just-In-Time (JIT) Compilation**: Uses XLA (Accelerated Linear Algebra) to compile Python functions into optimized machine code for CPUs, GPUs, and TPUs.
    - **Vectorization**: Provides `vmap` for automatic vectorization, enabling efficient batch processing.
    - **Parallelization**: Offers `pmap` for parallelizing computations across multiple devices (e.g., multi-GPU or TPU pods).
    - **NumPy-like API**: Familiar syntax for users of NumPy, making it easy to adopt.
    - **Hardware Acceleration**: Optimized for GPUs and TPUs, with seamless integration into Google’s hardware ecosystem.

### **JAX-ML**

- **Type**: Ecosystem of machine learning libraries and tools built on JAX.
- **Purpose**: Provides tools and frameworks for building and training ML models using JAX’s capabilities.
- **Key Components**:
    - **Flax**: A neural network library for JAX, designed for flexibility and scalability.
    - **Haiku**: A simpler neural network library by DeepMind, built on JAX.
    - **Optax**: A library for gradient-based optimization (e.g., optimizers like Adam, SGD).
    - **Chex**: A library for testing and debugging JAX code.
    - **RLax**: A library for reinforcement learning algorithms.
    - **Jraph**: A library for graph neural networks (GNNs) built on JAX.
    

### **System Type**

- **JAX**: A **numerical computing framework** with a focus on high-performance machine learning and scientific computing.
- **JAX-ML**: An **ecosystem of ML tools and libraries** built on JAX, designed to simplify the development of machine learning models and algorithms.

## References

- https://github.com/jax-ml/jax
- https://news.ycombinator.com/item?id=37698740
