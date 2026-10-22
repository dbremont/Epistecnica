# Algorithm

> A note that explores the **tree of knowledge called *algorithm*** (Algorithm: Problem → Solution Recipe) in the section of the **knowledge section called *Computation***. An algorithm can be thought of as a systematic procedure that defines the rules for state evolution, transforming an initial state into a desired outcome—whether it be a solution, an optimization, or a classification.
> 

![**Computation** is the **evolution** of states under a governing **dynamic law**.](../assets/note/technica/computation/algorithm/image.png)

**Computation** is the **evolution** of states under a governing **dynamic law**.

> **Note:** **Classical algorithms** solve **tractable problems**—problems that can be fully described and solved using discrete, finite procedures. Modern algorithms extend this toolkit to **intractable problems**—problems that cannot be fully captured by a discrete, finite description and often require approaches that include a **general-architectural representation of the solution** and a **method for adapting that architecture** to approximate or converge toward the solution, often using indirect or iterative techniques.
> 

> Note: In this note, we focus only on problems, techniques, and related concepts—not on the solutions, which can be found in (https://github.com/dbremont/algorithms).
> 

## Problem Space

> A **computational problem** is a **specification** {(*x*, *y*), …} by **intention** of a mapping between a set of inputs and outputs.
> 

> An **algorithm** is a finite set of well-defined instructions or rules designed to perform a specific task or solve a problem systematically.
> 

> **Search problems**: These problems involve finding a particular solution from a set of possible solutions. Examples include the depth-first search, breadth-first search, and A* algorithm.
> 

> **Decision problems**: These are yes-or-no questions that a computer program can answer. For example, given a graph, is there a path from node A to node B?
> 

> **Optimization problems**: These are problems where the goal is to find the best solution out of all possible solutions. For example, finding the shortest path in a graph.
> 

> **Enumeration problems**: These problems aim to generate a list of all possible solutions, such as all permutations of a set of numbers.
> 

> **Simulation problems** are problems in which the goal is to simulate a real-world system or process—for example, the behavior of a crowd in an emergency.
> 

## Technique Space

> The **design of algorithms** often relies on a set of heuristics or guidelines that help create efficient and effective solutions to computational problems. Below is a table of common algorithm design heuristics associated with specific algorithm types or problem-solving strategies.
> 

> The problem of algorithm design can be formulated as follows: given a problem $P$ and a solution space $S_P$, solving the problem involves traversing the potentially infinite space $S_P$,  the ways to navigate such space are **given by the methods of the domain,** but **abstract and general strategies (meta techniques) are cover here**.
> 

> See ROE in [Observational](https://app.notion.com/p/Observational-111c0f5171ec801195d6ef963907bf3b?pvs=21) and specially in [Computational Learning](https://app.notion.com/p/Computational-Learning-232c0f5171ec801b9dfacf000e0e1a7e?pvs=21).
> 

> External Memory Problems ….
> 

Data Structure → Augmentation, ,…

| **Category** | **Technique** | **Description** | **Case(s)** |
| --- | --- | --- | --- |
| **Divide & Conquer** | **Recursion** | Breaks a problem into smaller subproblems, solves them recursively, and combines results. | Merge Sort, Quick Sort, Binary Search |
|  | **Multidimensional Partitioning** | Splits multi-dimensional data recursively for faster search or processing. | KD-Trees, Quadtrees |
| **Dynamic Programming** | **Memoization** | Stores solutions to overlapping subproblems to avoid redundant computation. | Fibonacci, Longest Common Subsequence |
|  | **Tabulation** | Iteratively fills a table to solve subproblems in a bottom-up fashion. | Knapsack Problem, Matrix Chain Multiplication |
| **Greedy** | **Activity Selection** | Chooses local optimum at each step to build global solution. | Interval Scheduling, Huffman Coding |
|  | **Prim / Kruskal MST** | Builds minimum spanning tree using local greedy choices. | Network Design, Graph Connectivity |
| **Backtracking** | **Recursive Exploration** | Explores all possible configurations, abandoning paths that fail constraints. | N-Queens, Sudoku Solver |
|  | **Constraint Propagation** | Uses inference to reduce search space during backtracking. | CSPs in AI, Map Coloring |
| **Branch & Bound** | **Search with Pruning** | Uses upper/lower bounds to eliminate infeasible subproblems efficiently. | TSP, Integer Linear Programming |
| **Probabilistic** | **Random Sampling** | Approximates solutions using randomness for faster or scalable computation. | Monte Carlo Integration, QuickSort (random pivot) |
|  | **Monte Carlo** | Guarantees correctness (Las Vegas) or allows probabilistic error (Monte Carlo). | Primality Testing, Graph Connectivity |
| **Heuristic** | **Greedy Heuristics** | Uses rules of thumb to find good solutions when exact ones are expensive. | TSP Approximation, Job Scheduling |
|  | **Local Search** | Iteratively improves a solution by exploring neighborhood solutions. | Hill Climbing, Tabu Search |
|  | **Metaheuristics** | Higher-level frameworks guiding heuristics for general optimization problems. | Genetic Algorithms, Simulated Annealing, Ant Colony Optimization |
| Data Structure | Hadhing | Maps data to fixed-size values for fast access and lookup. | Hash Tables, Cuckoo Hashing |
|  | Priority | Maintains elements with ordering to support efficient retrieval of min/max. | Heaps, Priority Queues, Event Scheduling |
|  | Augmentation | Enhances base data structures with extra info to support advanced queries. | Order-Statistic Trees, Range Trees, Fenwick Trees |
|  | Persistence | Maintains historical versions of a data structure for time-travel queries. | Persistent Segment Trees, Immutable Maps |
|  | Lazy Propagation | Delays updates to reduce redundant computations. | Segment Trees with Range Updates |
|  | Succinct | Minimizes space while supporting efficient queries. | Wavelet Trees, Compressed Suffix Arrays, FM-Index |
|  | Cache-Oblivious Design | Structures designed to exploit memory hierarchy without tuning for cache size. | Cache-Oblivious B-Trees, Matrix Multiplication Layouts |
|  | Probabilistic Structure | Use randomness and controlled error for space/time efficiency. | Bloom Filters, Skip Lists, Count-Min Sketch |
|  | Concurrency | Data structures designed for lock-free or wait-free parallel access. | Lock-Free Queues, Concurrent Hash Maps |
| **Modern (Representation → Evolution (Optimization) → Evaluation Scheme) ROE** | **Solution Representation** | Encodes candidate solutions in a format suitable for optimization or learning. | Bitstrings, Neural Network Weights, Decision Trees, Generative Representaton, Differentiable Representation, … |
|  | **Problem Representation** | Encodes problem data into forms suitable for learning or computation. | Masking, Tokenization,  Embedding.  (Data Transformation), Noising, Image Flipping, Rotation,  Mixup,  … |
|  | **Training Scheme** | Strategies applied to train or adapt the solution representation | Noising, Masking, Self-Supervised Learning, Contrastive Learning |
|  | **Ensemble** | Combines multiple learning algorithms or models to improve generalization and robustness of predictions. | Random Forests, Gradient Boosting, Stacking, Bagging, … |
|  | **Regularization** | Techniques that prevent overfitting by adding penalty terms to the loss function or constraining model complexity. | L1/L2 Regularization, Dropout in Neural Networks, Early Stopping, … |
|  | **Optimization** | Evolves candidate solutions using search, gradient, or evolutionary strategies. | Gradient Descent, Genetic Algorithms, Particle Swarm Optimization, … |
|  | **Evaluation** | Measures solution quality or fitness according to a performance metric. | Accuracy, Loss Functions, Objective Functions in Optimization, … |
|  | **Hyper Parameter Optimization** | Optimizes parameters of the ROE process itself to improve performance and convergence. | Experience 😎. |
|  | **Sampling** | Techniques to draw representative or useful subsets from a distribution, dataset, or latent space. | Importance Sampling, Negative Sampling, Variational Sampling, Diffusion Sampling |
|  |  |  |  |

## Correctness

> How to prove that an algorithm solves a problem? How to prove iterative algorithms? How to prove recursive algorithms?
> 

> **Precision**: An algorithm must be precise and unambiguous in its instructions.
> 

> **Correctness**: An algorithm must produce the correct output for all valid inputs.
> 

> **Finiteness**: An algorithm must terminate after a finite number of steps.
> 

> Note: As we design, a proof will consist of general techniques and specific arguments about the methods used in the domain.
> 

> Proof Scheme:  $\forall x \in D,\, S\!\bigl(A(x)\bigr)$ , meaning for every input $x$ in domain $D$ the output $A(x)$of algorithm $A$  satisfies the specification $S$.
> 

### Technique

| Technique | Description | Use |
| --- | --- | --- |
| **Mathematical Induction** | Prove a base case, then show that if it holds for an arbitrary case nn, it holds for $n+1$. | Recursive algorithms, dynamic programming correctness |
| **Structural Induction** | Induction over structured data (trees, graphs) instead of integers. | Correctness of tree algorithms, recursive data structures |
| Loop Invariante | Identify a property that holds before and after each loop iteration. | Iterative algorithms like sorting, searching, and graph traversal |
| **Contradiction** | Assume the algorithm produces an incorrect result and derive a logical contradiction. | Proving correctness of conditional or recursive algorithms |
| **Contrapositive** | Prove correctness by showing “if output is incorrect, then input violates assumptions.” | Algorithms with conditional logic or decision rules |
| **Case Analysis** | Prove correctness by considering all possible cases or inputs. | Algorithms with multiple branches or conditions |
| **Recursive Decomposition** | Show correctness by proving each subproblem is solved correctly and combined properly. | Divide & Conquer algorithms like Merge Sort, Quick Sort |
| Reduction | Show that correctness of one algorithm can be inferred from another by an equivalent. | Proving equivalence of algorithms, transferring correctness from a known algorithm |
| Hardness Proof | Demonstrate that no efficient (or correct) algorithm exists for a problem under certain assumptions, often via reduction. | Proving impossibility results, NP-hardness, or correctness bounds of approximation algorithms |
| **Direct Proof** | Show correctness directly by reasoning through the steps of the algorithm from input to output. | Simple iterative or recursive algorithms where properties can be followed step by step |
| Recursive Reduction | Map an algorithm to an equivalent recursive implementation, then prove correctness recursively. | Divide & Conquer or recursively defined algorithms, recursive data structures |

### Case Study

| Algorithm | Description | Technique | Author(s) |
| --- | --- | --- | --- |
| QuickSort | Shows that QuickSort produces a sorted array for all inputs by reasoning from the algorithm’s steps. | Direct reasoning over partitioning and recursive calls | C.A.R. Hoare |
| MergeSort | Proves correctness by showing the base case of one-element arrays, then assuming correctness for arrays of size nn to prove size n+1n+1. | Mathematical induction on array size | Standard CS texts (CLRS) |
| Insertion Sort | Uses a property that the first kk elements are sorted at iteration kk, proving it holds through all iterations. | Loop invariant | CLRS |
| Binary Search | Assumes the algorithm fails to find the element despite it being in the array, then derives a contradiction. | Proof by contradiction | Standard CS references |
| Dijkstra’s Algorithm | Reduces correctness to the known correctness of greedy choice and optimal substructure in shortest-path computation. | Reduction to known properties | E.W. Dijkstra |

## Benchmark

> **Algorithms Performance Benchmark:** Evaluate and compare the performance of different algorithms solving the same problem in terms of **time complexity**, **space complexity**, and other relevant metrics.
> 

> **Algorithm Complexity** refers to a quantitative measure of the **resources an algorithm consumes** as a function of the input size. These resources are typically **time** (how long it takes to run) and **space** (how much memory it uses).
> 

> **Efficiency**: An algorithm should be designed to execute efficiently in terms of time and space complexity.
> 

### Design

- **Problem** – Clearly define the computational problem to be solved, including inputs and expected outputs.
- **Algorithms Set** – List all algorithms to be evaluated, including classical and optimized variants.
- **Input Set** – Prepare datasets of varied sizes, distributions, and edge cases for testing.
- **Metrics** – Measure execution time, memory usage, and other relevant performance indicators.
- **Control** – Ensure a consistent environment and repeat measurements to reduce variability.

### Checklist

- ✅ Define the problem unambiguously with clear input/output specifications.
- ✅ Include a diverse set of algorithms for comparison.
- ✅ Prepare multiple input datasets covering various sizes and distributions.
- ✅ Identify and track relevant performance metrics.
- ✅ Run benchmarks under controlled and consistent conditions.
- ✅ Repeat tests multiple times to account for variability.
- ✅ Visualize results to identify trends, trade-offs, and bottlenecks.

### Pitfalls

- ⚠️ Comparing algorithms on insufficient or biased datasets.
- ⚠️ Ignoring worst-case or edge-case scenarios.
- ⚠️ Failing to control the environment, leading to inconsistent measurements.
- ⚠️ Using inadequate metrics that do not capture memory, scalability, or stability.
- ⚠️ Drawing conclusions from a single run instead of averaging multiple runs.

## Performance

> See more in ….
> 

## Conceptual Model

Conceptual Model: Algorithm

## References

- [List of algorithms](https://www.wikiwand.com/en/List_of_algorithms)
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Core algorithms deployed](https://cstheory.stackexchange.com/questions/19759/core-algorithms-deployed/19773)
- [Towards a Definition of an Algorithm](https://arxiv.org/pdf/math/0602053.pdf)
- [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
- [A framework for the greedy algorithm](https://people.clas.ufl.edu/avince/files/Greedy.pdf)
- [From design patterns to category theory](https://blog.ploeh.dk/2017/10/04/from-design-patterns-to-category-theory/)
- https://en.wikipedia.org/wiki/Branch_and_bound
- https://github.com/dbremont/algorithms
- https://news.ycombinator.com/item?id=43155839
- [How to profile an algorithm?](https://app.notion.com/p/How-to-profile-an-algorithm-1bcc0f5171ec8064abecf4faf209cb4b?pvs=21)
- [**Induction**](https://app.notion.com/p/Induction-3f5aa91bbe094d6ca92d955b7fb6080b?pvs=21)
- [**Computational Complexity Theory**](note.html?n=technica/computation/computational-complexity-theory.md)
- [‣](https://app.notion.com/p/17bc0f5171ec80608b34de6922b560e4?pvs=21)
- [Modelado](https://app.notion.com/p/Modelado-a6727ea210124fb9a00ff6bb5bcf7cd5?pvs=21)
- https://www.ime.usp.br/~pf/algorithms/
- https://en.wikipedia.org/wiki/Computational_problem
- https://en.wikipedia.org/wiki/Isolation_forest
- https://bleuje.com/physarum-explanation/
- [Proof](https://app.notion.com/p/Proof-110c0f5171ec8074a9aeda9277860dea?pvs=21)
- https://en.wikipedia.org/wiki/Set_cover_problem
- https://www.cs.umd.edu/class/spring2025/cmsc451-0101/lectures.html
- [Representation](note.html?n=technica/computation/representation.md)
- https://en.wikipedia.org/wiki/External_memory_algorithm