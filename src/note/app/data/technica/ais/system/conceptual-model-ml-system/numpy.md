---
tags: [library, tool]
---

# Numpy


> **NumPy** is a foundational Python library for scientific computing, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these data structures.
> 

> 

## Data Model

NumPy's data model revolves primarily around the `ndarray` object, which stands for "n-dimensional array". This object is a powerful data structure for efficient computation and manipulation of large datasets, underpinned by the following key attributes and concepts:

1. **Homogeneous Data**: All elements in an `ndarray` are of the same data type, typically numeric (integers or floats), but can also include more complex types.
2. **Fixed Size**: An `ndarray`'s size is fixed upon creation, meaning the number of elements it contains cannot change. However, its shape (the dimensionality and size along each dimension) can be modified, as long as the total number of elements remains constant.
3. **N-Dimensional**: While arrays can be one-dimensional (like a list), NumPy's real power lies in multi-dimensional arrays, facilitating operations on vectors, matrices, and tensors.
4. **Contiguous Memory Allocation**: NumPy arrays are stored in contiguous blocks of memory, ensuring efficient access and manipulation of array elements, which is crucial for performance in large-scale computations.
5. **Vectorization**: NumPy enables vectorized operations, allowing mathematical operations to be performed on entire arrays without the need for explicit loops, leading to concise code and improved performance.
6. **Broadcasting**: This powerful mechanism allows NumPy to work with arrays of different shapes during arithmetic operations, intelligently 'broadcasting' smaller arrays across the larger ones.
7. **Data Type Objects (`dtype`)**: Each `ndarray` has an associated data type (`dtype`), describing the kind of elements contained within the array, including their size and byte order.
8. **Indexing and Slicing**: NumPy offers a rich set of indexing and slicing techniques, enabling the selection and manipulation of complex subsets of an array's data.
9. **Memory Views and Copies**: Operations on NumPy arrays can return either views (which are references to the original data, allowing for efficient data manipulation without copying) or copies (separate instances of data).
10. **Universal Functions (`ufunc`)**: These are functions that operate element-wise on arrays, enabling fast computation and are a cornerstone of NumPy's efficiency.

NumPy's data model, built around the `ndarray`, is designed to handle large data sets with high performance and ease of use in mathematical computations, forming the backbone of the Python scientific computing stack.

## N-Array Functions

> NumPy provides a wide array of functions to create and manipulate N-dimensional arrays (`ndarray`).
> 

Here is a list of some commonly used NumPy functions related to N-dimensional arrays:

**Array Creation Functions**

- **`numpy.array()`**: Create an array from a regular Python list or tuple.
- **`numpy.zeros()`**: Return a new array of given shape and type, filled with zeros.
- **`numpy.ones()`**: Return a new array of given shape and type, filled with ones.
- **`numpy.empty()`**: Return a new array of given shape and type, without initializing entries.
- **`numpy.arange()`**: Return evenly spaced values within a given interval.
- **`numpy.linspace()`**: Return evenly spaced numbers over a specified interval.
- **`numpy.eye()`**: Create a 2-D array with ones on the diagonal and zeros elsewhere (identity matrix).
- **`numpy.identity()`**: Return the identity array, a square array with ones on the main diagonal.
- **`numpy.full()`**: Return a new array of given shape and type, filled with a specified value.
- **`numpy.random.rand()`**: Return an array of the given shape filled with random values.

**Array Manipulation Functions**

- **`numpy.reshape()`**: Gives a new shape to an array without changing its data.
- **`numpy.ravel()`**: Return a contiguous flattened array.
- **`numpy.transpose()`**: Permute the dimensions of an array.
- **`numpy.concatenate()`**: Join a sequence of arrays along an existing axis.
- **`numpy.split()`**: Split an array into multiple sub-arrays.
- **`numpy.hstack()`**: Stack arrays in sequence horizontally (column-wise).
- **`numpy.vstack()`**: Stack arrays in sequence vertically (row-wise).

**Mathematical Functions**

- **`numpy.add()`**: Add arguments element-wise.
- **`numpy.subtract()`**: Subtract arguments element-wise.
- **`numpy.multiply()`**: Multiply arguments element-wise.
- **`numpy.divide()`**: Divide arguments element-wise.
- **`numpy.sqrt()`**: Return the non-negative square-root of an array, element-wise.
- **`numpy.exp()`**: Calculate the exponential of all elements in the input array.
- **`numpy.log()`**: Natural logarithm, element-wise.
- **`numpy.dot()`**: Dot product of two arrays.

### **Statistical Functions**

- **`numpy.mean()`**: Compute the arithmetic mean along the specified axis.
- **`numpy.median()`**: Compute the median along the specified axis.
- **`numpy.std()`**: Compute the standard deviation along the specified axis.
- **`numpy.var()`**: Compute the variance along the specified axis.
- **`numpy.min()`**: Return the minimum of an array or minimum along an axis.
- **`numpy.max()`**: Return the maximum of an array or maximum along an axis.

### **Linear Algebra Functions**

- **`numpy.linalg.inv()`**: Compute the (multiplicative) inverse of a matrix.
- **`numpy.linalg.det()`**: Compute the determinant of an array.
- **`numpy.linalg.eig()`**: Compute the eigenvalues and right eigenvectors of a square array.

These functions represent just a portion of what NumPy offers, but they are among the most commonly used in various scientific computing tasks.

## References

- [Numpy](https://numpy.org/)
- [A Visual Intro to NumPy and Data Representation](https://news.ycombinator.com/item?id=20282985) ([jalammar.github.io](http://jalammar.github.io/))
- [Python's Matrix Multiplication Operator](https://alysivji.github.io/python-matrix-multiplication-operator.html)
- Harris, Charles R., et al. "Array programming with NumPy." *Nature* 585.7825 (2020): 357-362.
- …
