---
tags: [problem]
---

# Search


## References

- https://en.wikipedia.org/wiki/Search_problem

## Search Space

> A **Search Space** is the set of **elements** plus a given **structure**. The structure(organization of the elements) can be a sorted set, a tree, a graph, an index, etc.
> 

Features:

In computer science, search spaces exhibit various features that influence the complexity, structure, and properties of the search problem. Here are some standard features of search spaces:

- **Size**: The size of a search space refers to the number of possible configurations or states within the space. Larger search spaces typically require more extensive search algorithms and can lead to increased computational complexity.
- **Dimensionality**: Dimensionality refers to the number of variables or dimensions that define the search space. Higher-dimensional search spaces often present challenges in terms of exploration and optimization due to the increased complexity and size of the space.
- **Connectivity**: Connectivity relates to the relationships and connections between different states or elements within the search space. It determines the possible transitions or paths that can be taken during the search process.
- **Constraints**: Constraints represent the limitations or conditions that restrict the valid configurations or transitions within the search space. Constraints can significantly impact the search algorithm design and the feasibility of finding solutions.
- **Symmetry**: Symmetry in a search space refers to the presence of equivalent or indistinguishable states. Exploiting symmetry can reduce redundancy in the search process and improve search efficiency.
- **Objective Function**: If the search problem involves optimization, an objective function is used to evaluate the quality or fitness of a particular state. The nature and complexity of the objective function influence the optimization strategy and the search space exploration.
- **Granularity**: Granularity refers to the level of detail or resolution at which the search space is defined. Fine-grained search spaces involve more precise and detailed configurations, while coarse-grained spaces provide a broader exploration scope.
- **Hierarchical Structure**: Some search spaces exhibit hierarchical or nested structures, where states can be organized in levels or layers. Hierarchical search spaces often require specialized search algorithms that consider the hierarchical relationships.
- **Search Landscape**: The search landscape refers to the distribution and arrangement of states or solutions within the search space. It can exhibit characteristics such as plateaus, cliffs, valleys, or multiple peaks, which impact the behavior and performance of search algorithms.
- **Domain-Specific Properties**: Search spaces in specific problem domains may have unique characteristics, such as spatial relationships in geometric search, dependencies in constraint satisfaction problems, or grammar rules in language processing. Understanding these domain-specific properties is essential for designing effective search strategies.
- **Metadata Augmentation**: The items in a Search Space can be augmented with data to facilitate searching.

## Search Method

> **Search methods** encompass a variety of algorithms and techniques used to efficiently locate and retrieve relevant information from a dataset or system based on specified criteria or patterns.
> 

**Traverse the Structure**:

- **Linear Search**: Also known as sequential search, this method checks each element in a list or array until the desired item is found or the end of the list is reached. Linear search has a time complexity of O(n), where n is the number of elements in the data structure.
- **Binary Search**: This search algorithm applies to sorted arrays or lists. It repeatedly divides the search space in half, comparing the target value with the middle element and discarding the half in which the target cannot be present. Binary search has a time complexity of O(log n), making it more efficient than linear search for large data sets.
- **Tree-based Search**: Various tree structures, such as binary search trees (BSTs), balanced search trees (e.g., AVL trees, red-black trees), and B-trees, facilitate efficient searching. These structures impose a hierarchical organization on the data, enabling logarithmic time complexity for searching operations.
- **Graph Search**: Graph search algorithms, such as depth-first search (DFS) and breadth-first search (BFS), traverse and search for elements in graph structures. These algorithms are employed in various applications, including pathfinding, network analysis, and graph traversal.

**Heuristic**:

- **Heuristic Search**: Heuristic search algorithms, such as A* (A-star) and Dijkstra’s algorithm, utilize heuristics or estimated cost functions to guide the search towards the goal. These algorithms are often used in pathfinding and optimization problems.
- **Metaheuristic Search**: Metaheuristic algorithms, such as genetic algorithms, simulated annealing, and particle swarm optimization, provide powerful search techniques for solving complex optimization problems where an exact solution is complicated.