---
tags: [domain]
---

# Representation Problem: Tensor


> **Domain Tensor**: Computational domain for representing multi-dimensional arrays, commonly used in deep learning and scientific computations.
> 

## Representations Systems

**Computational representations** for tensors in various contexts, from deep learning frameworks like PyTorch to more fundamental mathematical and physics-based applications, involve diverse techniques and methodologies:

1. **Cartesian Tensor Representations**: In learning molecular potentials, tensors can be represented as Cartesian complete tensor representations, specifically as 3x3 matrices for each atom. These representations are built from the composition of scalars, vectors encoded in skew-symmetric matrices, and symmetric traceless tensors. Such representations are crucial for ensuring that tensors behave appropriately under rotations and parity transformations, making them suitable for a wide range of applications, including the prediction of atomic or molecular properties【26†source】.
2. **Sparse Tensor Representations**: Techniques like "HighLight" and "Tailors and Swiftiles" have been developed to efficiently accelerate sparse tensors for AI models, particularly in high-performance computing applications. "HighLight" focuses on efficiently finding zero values within tensors to exploit sparsity, while "Tailors and Swiftiles" use an "overbooking" approach to increase tile size for data processing, allowing for more efficient data movement and processing on computer chips【27†source】.
3. **PyTorch Tensors**: PyTorch provides various functions for creating and manipulating tensors, such as `torch.zeros()`, `torch.ones()`, and `torch.randn()` for initializing tensors with zeros, ones, and random values, respectively. Additionally, tensors can be created from existing tensors through operations like cloning, reshaping, and concatenating. PyTorch also supports different data types for tensors, impacting computational accuracy and efficiency【28†source】.
4. **Array Representations in Physics and Mathematics**: Tensors can be represented as multi-dimensional arrays, commonly initialized using functions that create arrays filled with zeros or ones. Operations on these arrays, such as arithmetic operations and slicing, follow intuitive, element-wise rules. More complex operations like matrix multiplication can be performed using functions like `dot`, illustrating the versatility and power of array representations in computational applications【29†source】.

These computational representations for tensors highlight the flexibility and depth of tensor manipulation in various fields, from deep learning to theoretical physics, providing foundational tools for a broad range of scientific and engineering applications.