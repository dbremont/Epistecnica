# Computational Complexity Theory

> Computational complexity refers to the study of the resources (such as time and space / cost) required to solve a computational problem. It is a field of computer science that seeks to understand the limitations of algorithms and computing devices, and to develop algorithms that can solve problems efficiently.
> 

> The cost of algorithms can be informally defined as the resources an algorithm takes to solve a computational problem.
> 

![image.png](data/technica/computation/assets/computational-complexity-theory/image.png)

Approaches to measuring the cost of an algorithm: 

- Measure the number of seconds a program takes to complete using a stopwatch (either physical or in software). The cost of the algorithms using this approach will depend on the inputs and machine.
- Count the number of operations needed for inputs of a given size. The cost of algorithms using this approach is machine-independent but still depends on the information and doesn’t tell you how long the code takes to run.
- Derive an algebraic expression relating the number of operations to the `size of an input`, and this tells you how the algorithm scales but does not tell you how long the code takes to run.
- Derive an algebraic expression that relates the sum of `instructions' weight by cost` to the `size of an input.`

**Computational Resources**:

- Space,
- Time,
- Network Bandwidth,
- …

**Methods for Modelling the Cost**

We will model the cost of algorithms as an expression in terms of the `input(size)`.

Select a specific `Computation Path` or use amortized analysis, 

- Worst Path,
- Best Path,
- Average Path,
- Use amortize analysis

Once we have chosen a path, we can derive an expression for the algorithm's cost using a specific `Automata Cost Model`.

### Automata Cost Model

It’s a description of the cost of every operation the automata performs.

### Taxonomy of Algorithms Costs

Also known as Complexity classes

- O(1): Constant: Cost Independent from the input,
- O(n): Linear: The cost will grow linear with the input size,
- O(log n): Logarithmic: `O(log N)` means time goes up linearly while n increases exponentially. So if it takes 1 second to compute 10 elements, it will take 2 seconds to compute 100 elements, 3 seconds to compute 1000 elements, and so on,
- O(n log n): Linearithmic: Using an iteration-logarithmic operation,
- O(n ** 2): Quadratic: Using two iterations,
- O(n ** k): Polynomic: Using `n` iterations,
- O(2 ^ n): Exponential: Behavior is similar to the power set,
- O(n!): : Going for each permutation of n
- P,
- NP,
- EXPTIME

## Asymptotic Behavior of Algorithms

Since we want to simplify the cost model for the algorithm, we will produce several limiting expressions for the model and use those instead of the model for communication.

Tools for describing the limiting behavior:

- Big O - Upper bound
- Big Omega - Lower bound
- Big Tetha - Lower bound - Upper bound

## References

- [Algorithmic efficiency](https://en.wikipedia.org/wiki/Algorithmic_efficiency)
- [Complexity Classes](https://brilliant.org/wiki/complexity-classes/)
- [Asymptotic analysis](https://en.wikipedia.org/wiki/Asymptotic_analysis)
- [The Computer Language Benchmarks Game](https://en.wikipedia.org/wiki/The_Computer_Language_Benchmarks_Game)
- [Know Thy Complexities!](https://www.bigocheatsheet.com/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- Johnson, D. S. (2012). A brief history of NP-completeness, 1954–2012. 359–376.
- Kriegel, H.-P., Schubert, E., & Zimek, A. (2017). The (black) art of runtime evaluation: Are we comparing algorithms or implementations? 52, 341–378.
- Tarjan, R. E. (1985). Amortized computational complexity. 6(2), 306–318.
- Sipser, M. (1992). The history and status of the P versus NP question. 603–618.
- https://blog.computationalcomplexity.org/2009/05/foundations-of-complexity.html
- https://blog.computationalcomplexity.org/2009/05/foundations-of-complexity.html

[Asymptotic Analysis](https://app.notion.com/p/Asymptotic-Analysis-809eaa4cd1ed4d96b1e55b6f7a002145?pvs=21)