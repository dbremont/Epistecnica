---
tags: [verification]
---

# Verification


> 

| **Proof Technique** | **Description** |
| --- | --- |
| **Induction** | A mathematical technique used to prove correctness by showing: <br>1. **Base Case**: The algorithm works for the smallest input. <br>2. **Inductive Step**: If it works for an input of size \(n\), it works for \(n+1\). |
| **Loop Invariants** | Used to prove correctness of iterative algorithms. A loop invariant is a condition that holds true before and after each iteration of the loop. Proving the invariant ensures the algorithm works as intended. |
| **Greedy Choice Property** | Used to prove the correctness of greedy algorithms. It involves showing that making a locally optimal choice at each step leads to a globally optimal solution. |
| **Optimal Substructure** | Used in dynamic programming and greedy algorithms. It involves proving that an optimal solution to the problem can be constructed from optimal solutions to its subproblems. |
| **Contradiction** | Assumes the algorithm is incorrect and derives a contradiction. This proves the algorithm must be correct. |
| **Exchange Argument** | Used in greedy algorithms. It involves showing that swapping or exchanging elements in a solution cannot improve the result, proving the solution is optimal. |
| **Amortized Analysis** | Used to analyze the average time complexity of operations over a sequence of steps. Common methods include the **aggregate method**, **accounting method**, and **potential method**. |
| **Recurrence Relations** | Used to analyze the time complexity of recursive algorithms. The recurrence relation is solved using techniques like the **Master Theorem** or **substitution method**. |
| **Probabilistic Analysis** | Used to analyze randomized algorithms. It involves calculating the expected behavior of the algorithm over all possible random choices. |
| **Duality** | Used in optimization problems (e.g., linear programming). It involves proving the correctness of an algorithm by showing a relationship between the primal and dual problems. |
| **Invariant Maintenance** | Used to prove correctness by showing that a specific property (invariant) is maintained throughout the execution of the algorithm. |
| **Witness Proofs** | Used to verify the correctness of an algorithm by providing a "witness" (e.g., a certificate or solution) that can be checked efficiently. |
| **Reduction** | Used to prove correctness by reducing the problem to another problem with a known solution. If the reduction is correct, the algorithm is correct. |
| **Case Analysis** | Used to prove correctness by considering all possible cases or scenarios that the algorithm might encounter and showing it works in each case. |
| **Potential Function Method** | Used in amortized analysis. A potential function is defined to measure the "potential energy" of a data structure, and changes in potential are used to analyze the cost of operations. |
| **Dimensionality Argument** | Used to prove correctness by analyzing the problem in terms of its dimensions (e.g., space, time, or input size) and showing the algorithm behaves as expected within those dimensions. |
| **Monotonicity Argument** | Used to prove correctness by showing that a specific property (e.g., a value or condition) monotonically increases or decreases, ensuring progress toward the solution. |
| **Lower and Upper Bounds** | Used to prove optimality by showing that the algorithm achieves a solution that is both a lower bound (best possible) and an upper bound (worst possible) for the problem. |

## References

- [Formal System](https://app.notion.com/p/Formal-System-41d02881d0544314b0e7ad3e6ada608a?pvs=21)