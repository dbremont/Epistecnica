---
tags: [domain]
---

# Representation Problem: Sequence (Data)


> **Domain: Sequence representations** is a representation system that allows us to represent a sequence of elements and their associated operations.
> 

## Representations System

- **Arrays** are contiguous blocks of memory that store elements of the same type in a linear order. Elements can be accessed using an index, and arrays offer constant-time access to elements.
- **Linked Lists**: Linked lists contain nodes containing the data and a reference (or pointer) to the next node in the sequence. Linked lists provide dynamic memory allocation but have slower access times than arrays.
- **Strings**: Strings are sequences of characters and are widely used for text representation in programming. Strings can be represented as arrays of characters or as more sophisticated data structures, like rope data structures, for efficient manipulation of long strings.
- **Tuples**: Tuples are fixed-size sequences that can store elements of different types. They are often used to represent a collection of related values.
- **Queues**: Queues are data structures that follow the First-In-First-Out (FIFO) principle, where elements are inserted at the back and removed from the front.
- **Stacks**: Stacks follow the Last-In-First-Out (LIFO) principle, where elements are inserted and removed from the same end, known as the top.
- **Deques (Double-Ended Queues)**: Deques are data structures that allow the insertion and deletion of elements from both ends, offering more flexibility than stacks and queues.
- **Compressed Sequence Representations**: In some cases, especially when dealing with repetitive or large datasets, compressed sequence representations can save memory and improve processing efficiency.
- **Distributed Queues**: Distributed queues allow multiple distributed nodes to exchange messages or tasks efficiently, enabling load balancing and task distribution in real-time scenarios.
- **Vector**: A "Vector" data structure is a resizable array-like container that can dynamically store elements, allowing for efficient random access, insertion, and deletion of elements at its end.
- Infinite Sequence

## Reference

- [In defense of linked lists](http://antirez.com/news/138)
- Perlis, Alan J., and Charles Thornton. “Symbol manipulation by threaded lists.” Communications of the ACM 3.4 (1960): 195-204.

[Skip List](note.html?n=technica/computation/data-system/data-system-conceptual-model/skip-list.md)

[**Linked Lists**](note.html?n=technica/computation/representation/conceptual-model-computational-representation/representation-problem-sequence-data/linked-lists.md)