---
tags: [ec]
---

# Evolutionary Computation


> **Evolutionary Computation** =  Representation + Evolutionary Optimization Algorithms.
> 

> **Evolutionary computation frameworks** are computational systems that simulate natural evolutionary processes, such as selection, mutation, and recombination, to optimize solutions to complex problems.
> 

> **Genetic programming (GP)** is a technique for evolving computer programs to solve problems. In GP, a population of computer programs has evolved over many generations, using techniques inspired by natural selection and genetics.
> 

> **GP** has been used to model various systems, including financial markets, climate, ecology, robotics, and more. The advantage of GP is that it can automatically evolve models to fit data and discover novel solutions that may be difficult for humans to find.
> 

> 

## Index

|  | **Description** | **Key Techniques** | **Common Applications** |
| --- | --- | --- | --- |
| **Genetic Algorithms (GA)** | Simulates natural selection using selection, crossover, and mutation to evolve solutions. | Selection, Crossover, Mutation, Elitism | Optimization, Scheduling, Machine Learning |
| **Genetic Programming (GP)** | Evolves programs or mathematical expressions as trees to solve problems. | Tree-based Crossover, Mutation | Symbolic Regression, Automated Code Generation |
| **Evolution Strategies (ES)** | Focuses on self-adaptive mutation and selection, often using real-valued representations. | Self-Adaptive Mutation, Recombination, Selection | Industrial Design, Continuous Optimization |
| **Evolutionary Programming (EP)** | Similar to ES but emphasizes mutation over recombination and is often used for evolving finite state machines. | Mutation, Selection | Control Systems, Robotics |
| **Differential Evolution (DE)** | A population-based algorithm for continuous optimization that uses vector differences for mutation. | Mutation via Differential Changes, Crossover, Selection | Engineering Design, Function Optimization |
| **Swarm Intelligence (SI)** | Inspired by the collective behavior of social animals, like ants and birds, to solve optimization problems. | Particle Swarm Optimization (PSO), Ant Colony Optimization (ACO), Bee Algorithm | Pathfinding, Data Clustering, Network Routing |
| **Artificial Immune Systems (AIS)** | Models the adaptive immune system to recognize patterns and optimize solutions. | Clonal Selection, Negative Selection, Immune Network Theory | Anomaly Detection, Security, Bioinformatics |

| **Genetic Operator** | **Description** | **Purpose** |
| --- | --- | --- |
| **Selection** | Chooses individuals for reproduction based on fitness. Methods include Roulette Wheel, Tournament, and Rank Selection. | Ensures survival of the fittest. |
| **Crossover (Recombination)** | Combines genetic material from two parents to create offspring. Types include Single-Point, Multi-Point, and Uniform Crossover. | Introduces diversity and combines good traits. |
| **Mutation** | Randomly alters genes in an individual. Methods include Bit Flip, Swap, and Gaussian Mutation. | Maintains genetic diversity and prevents premature convergence. |
| **Elitism** | Directly carries the best individuals from one generation to the next without modification. | Preserves high-fitness solutions. |
| **Inversion** | Reverses the order of a gene sequence within a chromosome. | Helps maintain useful gene clusters. |
| **Duplication** | Duplicates part of a chromosome. | Enhances beneficial traits. |
| **Deletion** | Removes part of a chromosome. | Reduces redundant or harmful traits. |
| **Repair** | Corrects infeasible or invalid solutions. | Ensures solutions remain valid. |
| **Reinsertion** | Chooses which offspring replace the current population. | Controls population dynamics. |

## Co-Evolutionary Algorithms

> 

## Representation

> 

| **Representation Technique** | **Description** | **Applications** |
| --- | --- | --- |
| **Binary Representation** | Solutions are encoded as strings of binary digits (0s and 1s). Each bit or group can represent a decision variable or a problem parameter. | Simple optimization problems, combinatorial problems, bit-string optimization. |
| **Real-Valued Representation** | Solutions are encoded as strings of real numbers. Each actual number represents a continuous variable or parameter in the problem space. | Function optimization, parameter tuning, continuous domains. |
| **Permutation Representation** | Solutions are encoded as sequences of integers or objects where the order matters. Each permutation represents a specific arrangement of elements. | Traveling Salesman Problems (TSP), scheduling problems, and ordering problems. |
| **Tree-Based Representation** | Solutions are encoded as tree structures, with nodes representing functions or operations and leaves representing variables or constants. | Genetic Programming (GP), symbolic regression, expression evolution. |
| **Graph-Based Representation** | Solutions are represented as graphs or networks; nodes represent entities; edges represent relationships or connections between them. | Network optimization, circuit design, route planning. |
| **Floating-Point Representation** | Solutions are encoded as strings of floating-point numbers, similar to real-valued representation, but with higher precision for complex problem spaces. | High-precision optimization problems, continuous optimization. |
| **Hybrid Representation** | Solutions are encoded using a combination of different representations (e.g., combining binary and real-valued representations). | Complex, multi-modal problems requiring diverse encoding. |
| **Matrix Representation** | Solutions are encoded as matrices where elements represent variables, constraints, or interactions between components. | Machine learning, neural network design, multi-dimensional optimization. |
| … | … | … |

## Evolution

> 

| **Evolution Algorithm** | **Description** |
| --- | --- |
| **Standard Genetic Programming (GP)** | Evolves programs using standard genetic operations such as selection, crossover, and mutation. |
| **Strongly Typed Genetic Programming (STGP)** | Enforces type constraints in GP, ensuring that the evolved programs adhere to specific type requirements. |
| **Koza-style GP** | A classic GP approach where programs are represented as tree structures and evolved using crossover and mutation. |
| **Linear Genetic Programming (LGP)** | Evolves linear sequences of instructions instead of tree structures, focusing on instruction sequences. |
| **Cartesian Genetic Programming (CGP)** | Represents programs as 2D grids (or n-dimensional grids) of nodes and evolves them through mutation. |
| **Grammatical Evolution (GE)** | Uses a grammar-based approach to evolve programs, ensuring syntactically correct programs are generated. |
| **Probabilistic Incremental Program Evolution (PIPE)** | A probabilistic model-building GP technique that evolves a population by sampling from probabilistic models. |
| **Genetic Programming with Automatically Defined Functions (ADF)** | Incorporates subroutine evolution, allowing reusable sub-programs to evolve within the main program. |
| **Multi-Objective Genetic Programming (MOGP)** | Evolves programs to optimize multiple objectives simultaneously, rather than a single objective. |
| **Hierarchical Genetic Programming (HGP)** | Evolves programs with hierarchical structures, allowing sub-programs to be evolved independently. |
| **Age-Fitness Pareto Optimization (AFPO)** | A GP technique that uses age and fitness as criteria to maintain diversity and prevent premature convergence. |
| **Gene Expression Programming (GEP)** | Similar to GP but uses linear chromosomes that are expressed as expression trees, combining features of GA and GP. |
| **Parallel Genetic Programming (PGP)** | Evolves programs using parallel processing techniques to enhance computational efficiency. |

## On Designing Fitness Function

> 

## Training

> 

### **Initialization**

> 

### Evolution

> 

### Termination

> 

## References

- [Genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm)
- https://en.wikipedia.org/wiki/Genetic_programming
- https://en.wikipedia.org/wiki/Memetic_algorithm
- https://github.com/arsbremontix/algorithms/blob/main/src/Genetic_Programming_Synthetizing_Boolean_Functions.ipynb
- [Metaheuristic](https://en.wikipedia.org/wiki/Metaheuristic)
- [Neuroevolution](https://en.wikipedia.org/wiki/Neuroevolution)
- [Search Problem](https://en.wikipedia.org/wiki/Search_problem)
- [Risto Miikkulainen](https://scholar.google.com/citations?user=2SmbjHAAAAAJ&hl=en)
- [Evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm)
- [Evolutionary Computation](https://en.wikipedia.org/wiki/Evolutionary_computation)
- [Mathematical Optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Evolutionary Computation](http://bactra.org/notebooks/evol-comp.html)
- [Introduction to Evolutionary Computation](https://faculty.kashanu.ac.ir/file/download/course/1570381415-session-2.0.pdf)
- [Neuroevolution: A different kind of deep learning](https://www.oreilly.com/radar/neuroevolution-a-different-kind-of-deep-learning/)
- [DEAP: Distributed Evolutionary Algorithms in Python](https://deap.readthedocs.io/en/master/)
- http://bactra.org/notebooks/evol-comp.html
- Koza, J. R. (1995). Survey of genetic algorithms and genetic programming. 589–594.
- Michalewicz, Z., Fogel, D. B. (2013). How to solve it: modern heuristics. Springer Science Business Media.
- Schmidhuber, J. (1987). Evolutionary Principles in Self-Referential Learning. On Learning now to Learn: The Meta-Meta-Meta…-Hook.
- Info-Evo: Using Information Geometry to Guide Evolutionary Program Learning https://arxiv.org/pdf/2103.04747.pdf
