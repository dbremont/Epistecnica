---
tags: [method, technique, discrete]
---

# Inclusion–Exclusion

> **Inclusion–exclusion** computes the size of a union by alternately adding and subtracting intersections: $|A_1 \cup \cdots \cup A_n| = \sum |A_i| - \sum |A_i \cap A_j| + \cdots$.

## Formulation

> **What it is.** The exact counting routine for overlapping sets. Each element counted $k$ times contributes $\sum_{j=1}^{k}(-1)^{j+1}\binom{k}{j} = 1$, so over- and under-counting cancel and every element counts once.
>
> **Type.** An `Epistemic Method` — a counting routine, not a principle of inquiry. It answers "how many" by correcting the naive sum rather than by finding a bijection.
>
> **Boundary.** It requires the intersection structure to be computable: the formula is exact but useless when the higher intersections are as hard as the original set. Its complement form, counting *derangements* or surjections, is usually where it earns its keep.

## Key results

- **Complement form.** $|A^c_1 \cap \cdots \cap A^c_n| = |S| - \sum|A_i| + \sum|A_i\cap A_j| - \cdots$ — the form used for "none of these properties".
- **Derangements.** $!n = n!\sum_{k=0}^{n}(-1)^k/k!$, the classical application: permutations with no fixed point.
- **Surjections.** The number of onto maps from an $n$-set to a $k$-set is $\sum_j (-1)^j \binom{k}{j}(k-j)^n$.
- **Bonferroni inequalities.** Truncating the alternating sum gives bounds — the probabilistic reading of the same identity.
- **Sieve methods.** In number theory the same inclusion–exclusion over primes is the sieve, and the parity problem is its fundamental obstruction.

## References

- https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
- [Combinatorics](../../discrete/combinatorics.md) · [Double Counting](double-counting.md) · [Binomial Coefficient](../../discrete/binomial-coefficient.md) · [Generating Function](../transform/generating-function.md)
