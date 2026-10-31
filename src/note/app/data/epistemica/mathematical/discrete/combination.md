---
tags: [discrete, operator]
---

# Combination

 : Binomial Coefficient (Binomial%20Coefficient%201d6c0f5171ec80809b7ff2ad6af7bfa2.md), Combinatorics (Combinatorics%20231c0f5171ec8005bd62f206032ece34.md)

> A **combination** is a selection of items from a larger set **where the order does not matter**.
> 

## Formalism

> If you have a set of $n$ distinct items, and you want to select $k$ of them, a **combination** counts **all possible groups of $k$ items** without regard to the sequence in which they are chosen.
> 

The number of combinations is given by: $C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$

Where:

- $n!$ (n factorial) is the product of all positive integers up to $n$.
- $k!$ is the factorial of $k$.

## Reduction

> Which problems can be reduced to a **combination computation problem**?
> 

| Problem Type | Typical Question | How It Maps to $\binom{n}{k}$ |
| --- | --- | --- |
| **Subset  (Selection)** | Pick $k$ items from $n$ | Direct: choose $k$ elements from $n$ |
| **Committee (Group Formation)** | Form a group of size $k$ from $n$ candidates | Equivalent to selection |
| **Binary (Two-option Choices)** | Count sequences with exactly $k$ successes | Pick positions for successes among $n$ trials |
| **Population (Survival Models)** | Choose which elements survive or split | Similar to binary choices |
| **Partitioning (Grouping)** | Divide a set into fixed-size groups | Pick members of first group; remaining are automatic |
| **Path (Lattice Counting)** | Count sequences of moves (e.g., right/up) | Pick positions for one type of move |
| **Polynomial Expansion (Coefficients)** | Find coefficient of a term in $(x+y)^n$ | Number of ways to pick $k$ $x$-terms |
| **Complement (Symmetry)** | Count subsets of size $k$ via complement | Use $\binom{n}{k} = \binom{n}{n-k}$ to simplify |
| **Multiset (Stars and Bars)** | Distribute identical items into bins | Can reduce to $\binom{n+k-1}{k}$ |

## References

- https://en.wikipedia.org/wiki/Combination
