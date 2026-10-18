# Change-making Problem

 : Knapsack Problem (Knapsack%20Problem%201bbc0f5171ec8004b740e71e3ff92812.md)

> The **change-making problem** addresses the question of finding the 
**minimum number of coins** (of certain denominations) that add up to a 
given amount of money.
> 

QA:

- How to think deeply about mental model / representation  it’s symbolic computational representation?
- …

Related Topics:

- Knapsack problem
- Linear Combination
- Frobenius Coin Problem

## Formulations

> Note:  Weed need to check the `<value, quantity>` in some problems settings, the quantity may be infinity.
> 

### **General Setup**

1. **Input**:
    - A set of items, each with an associated value.
    - A target value  $T$.
2. **Objective**: Find a linear combination of the items' values that equals $T$.
3. **Mathematical Formulation**: $\sum_{i=1}^n c_i \cdot x_i = T$
    - $c_i$: Value of the $i$-th item.
    - $x_i$: Non-negative integer or real coefficient (depending on the problem).

### Minimization Constraint

- **Objective**: Find the minimum number of coins that sum to  $T$.
- $\sum_{i=1}^n c_i \cdot x_i = T \quad \text{(minimize } \sum_{i=1}^n x_i \text{)}$

### **Unbounded Knapsack Problem**

- **Objective**: Maximize the total value of items without exceeding the capacity $W$.
- **Mathematical Formulation**: 
$\sum_{i=1}^n w_i \cdot x_i \leq W \quad \text{(maximize } \sum_{i=1}^n v_i \cdot x_i \text{)}$

## Matrix Representation

> The **"Change-Making Problem"** can be formulated in terms of **linear combinations**. Given a set of coin denominations, the goal is to represent a target amount as a weighted sum of these coins.
> 

Let:

- $C = [c_1, c_2, \dots, c_n]$ be the available coin denominations.
- $x = [x_1, x_2, \dots, x_n]$ be the number of each coin used.
- T be the target amount.

The equation can be written as:

$C \cdot x = T$

or explicitly as:

$T\begin{bmatrix} c_1 & c_2 & \dots & c_n \end{bmatrix}  
\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}  
= T$

### **Example: U.S. Coins (1, 5, 10, 25 cents)**

For a target of **30 cents** using U.S. coins $\{1,5,10,25\}$:

$\begin{bmatrix} 1 & 5 & 10 & 25 \end{bmatrix}  
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix}  
= 30$

Where $x_1, x_2, x_3, x_4$ are non-negative integers.

**Solution Set as a Matrix**

Each valid solution (combination of coins) is a column in the solution matrix:

$X =  
\begin{bmatrix}  
5 & 0 & 10 & 0 \\  
1 & 2 & 0  & 1 \\  
0 & 1 & 2  & 0 \\  
0 & 0 & 0  & 1  
\end{bmatrix}$

Where each column represents a valid combination (e.g., the first column represents **5 pennies, 1 nickel, and no dimes or quarters**).

## Computational Complexity Analysis

> 

## **Methods of Solving**

> 

| **Category** | **Method** | **Optimality** | **Time Complexity** | **Use Case** |
| --- | --- | --- | --- | --- |
| **Exact Methods** | Dynamic Programming | Optimal | $O(n \cdot T)$ | General-purpose, small to medium $T.$ |
|  | Integer Linear Programming (ILP) | Optimal | Exponential (worst case) | Small problems with exact solvers (e.g., Gurobi, CPLEX). |
|  | Recursive Approach | Optimal | Exponential (without memoization), $O(n \cdot T)$ (with memoization) | Small problems, educational purposes. |
|  | Branch and Bound | Optimal | Exponential (worst case) | Problems with constraints or pruning opportunities. |
|  | Backtracking | Optimal | Exponential | Small problems, exhaustive search. |
| **Approximate Methods** | Greedy Algorithm | Suboptimal | $O(n \log n)$ | Canonical coin systems (e.g., U.S. coins). |
|  | Heuristic Search | Near-optimal | Varies | Problems with domain-specific heuristics. |
|  |  **Probabilistic Convolution Tree** |  |  |  |
| **Metaheuristic Methods** | Genetic Algorithms (GA) | Near-optimal | Depends on parameters | Large-scale or complex problems. |
|  | Simulated Annealing (SA) | Near-optimal | Depends on parameters | Large-scale or complex problems. |
|  | Particle Swarm Optimization (PSO) | Near-optimal | Depends on parameters | Large-scale or complex problems. |
| **Mathematical Methods** | Generating Functions | Exact count | Depends on method | Counting solutions (not minimizing). |
|  | Number Theory | Optimal | Varies | Analyzing canonical coin systems or **Frobenius numbers**. |
|  |  |  |  |  |

## Dynamic Programming Method

> **What makes it dynamic programming?**  It’s dynamic programming because it builds solutions incrementally, reuses solutions to sub-problems, and optimizes based on past results.
> 

> 

## Proof

> 

## References

- https://en.wikipedia.org/wiki/Change-making_problem
- https://en.wikipedia.org/wiki/Coin_problem
- https://github.com/dbremont/algorithms
- [Matrix](../mathematical/matrix.md)
- 
- [Linear Combination](../mathematical/linear-combination.md)
- [Diophantine Equation](../mathematical/diophantine-equation.md)
- [Dynamic Programming](dynamic-programming.md)
- [**Computational Complexity Theory**](https://app.notion.com/p/Computational-Complexity-Theory-1afc20d36374431dad13a8ec4e8ab849?pvs=21)
- [How to profile an algorithm?](https://app.notion.com/p/How-to-profile-an-algorithm-1bcc0f5171ec8064abecf4faf209cb4b?pvs=21)
- [ ]  [‣](https://app.notion.com/p/1be598edb790808c89d3ca0868fe8825?pvs=21)
- [ ]  [‣](https://app.notion.com/p/1be598edb790807495d3e57443f68bf0?pvs=21)
