---
tags: [linear-algebra]
---

# LU Decomposition


**LU decomposition** is a common matrix factorization technique used in numerical linear algebra. It decomposes a square matrix A into the product of two matrices, `L` and `U`, where `L` is a lower triangular matrix and U is an upper triangular matrix.

The **LU decomposition** works as follows:

- Start with a square matrix `A` of size `n x n`.
- Use Gaussian elimination to reduce `A` to an upper triangular matrix `U`, while keeping track of the operations used to eliminate the entries.
- The resulting upper triangular matrix `U` is the “U” factor of the `LU` decomposition.
- The “L” factor of the `LU` decomposition is obtained by reversing the operations used to eliminate the entries in the original matrix `A`. Specifically, the lower triangular matrix `L` is constructed such that `L` times `A` equals `U`, where `L` is a product of elementary matrices corresponding to the elimination operations used in step 2.
- The product of L and U gives the LU decomposition of matrix A.
- Once the `LU` decomposition is computed, it can be used to solve systems of linear equations involving matrix `A` more efficiently than directly solving the original system of equations. This is because the `LU` decomposition provides a computationally efficient way to solve multiple linear systems involving the same matrix `A` and compute the inverse of A and the determinant of `A`.

## References

- [LU Decomposition](https://www.wikiwand.com/en/LU_decomposition)
