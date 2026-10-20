---
tags: [programming-paradigm]
---

# Map/Reduce (MapReduce) Paradigm

- [Programming Paradigm](note.html?n=technica/computation/language-system/conceptual-model-language-system/programming-paradigm.md)

> The Map/Reduce Model of Computation is a programming paradigm for processing and analyzing large datasets in a parallel and distributed manner by dividing tasks into map and reduce operations.
> 

> MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.
> 

![](https://storage.googleapis.com/algodailyrandomassets/curriculum/systems-design/map-reduce/mapReduce.png)

**¿What computations does the model help us to encode?**

The model helps us encode computations that involve processing large-scale data through two primary operations: map, which performs filtering and sorting, and reduce, which performs aggregation and summarization.

**¿What is the abstract machine?**

The abstract machine in the Map/Reduce Model is a distributed computing framework that manages the parallel execution of map and reduce tasks across a cluster of machines.

**¿How to encode computations?**

Computations in the Map/Reduce Model are encoded by defining the map and reduce functions, which operate on key-value pairs, to process and transform the input data. The abstract machine then orchestrates the distribution of data and tasks, executing the map and reducing operations in parallel across multiple machines to achieve efficient data processing. This model is commonly used in big data processing and analytics frameworks like Apache Hadoop.

## References

- [MapReduce](https://en.wikipedia.org/wiki/MapReduce)
- [MapReduce - A Framework for Large-scale Parallel Processing](https://people.cs.rutgers.edu/~pxk/417/notes/mapreduce.html)