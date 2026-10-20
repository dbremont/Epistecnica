---
tags: [technique]
---

# Succinct Data Structure


> How to represent data with the minimum about of information?
> 

> **Succinct data structures** are designed to represent large amounts of data in a space-efficient manner efficiently.
> 

Several techniques can be used to create such structures, including:

- **Bit-level compression** uses variable-length encoding to represent data in fewer bits than its original size. For example, Huffman coding or arithmetic coding can be used to compress data at the bit level.
- **Wavelet trees**: This structure allows the representation of a sequence of elements by storing the wavelet transform of the sequence, which represents the sequence in terms of its frequency components.
- **Bloom filters**: This probabilistic data structure tests whether an element is a set member. It encodes the set using a bit array and a set of hash functions.
- **Compact tries**: This tree-like structure stores a set of strings, compressing them to minimize memory usage.
- **Elias-Fano encoding**: This technique encodes monotonic sequences of integers in a compressed form. It uses a combination of delta encoding and variable-length encoding to represent the integers in fewer bits.

## References

- [Succinct data structure](https://en.wikipedia.org/wiki/Succinct_data_structure)