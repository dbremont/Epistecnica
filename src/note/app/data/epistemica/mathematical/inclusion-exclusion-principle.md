---
tags: [discrete, technique]
---

# Inclusion-Exclusion Principle


> PIE is a method to count the exact size of a union of overlapping sets by alternately adding and subtracting the sizes of their intersections.
> 

> Note: Strictly speaking, this is `not a principle` but a formula—that can be rigorously proved.
> 

## Formulation

> When counting or measuring the size/probability of a union of sets, **naively adding their sizes overcounts the elements in intersections**. PIE systematically corrects this by:
> 
1. **Including** the sizes of all single sets.
2. **Excluding** the sizes of all pairwise intersections (since they were counted twice).
3. **Including** the sizes of triple intersections (since they were excluded too many times).
4. Continuing with alternating subtraction and addition until all overlaps are corrected.

In general, for $n$  sets  $A_1, A_2, \dots, A_n$:

$\Bigl|\bigcup_{i=1}^{n} A_i\Bigr|
= \sum_{i} |A_i|
- \sum_{i<j} |A_i \cap A_j|
+ \sum_{i<j<k} |A_i \cap A_j \cap A_k|
- \dots
+ (-1)^{n+1} |A_1 \cap A_2 \cap \dots \cap A_n|$

In probability theory, the same formula holds by replacing set cardinalities with probabilities:

$P\!\left(\bigcup_{i=1}^{n} A_i\right)
= \sum_{i} P(A_i)
- \sum_{i<j} P(A_i \cap A_j)
+ \sum_{i<j<k} P(A_i \cap A_j \cap A_k)
- \dots
+ (-1)^{n+1} P(A_1 \cap \dots \cap A_n)$

## Proof

> See https://github.com/csiglab/responsum/blob/main/praxis/src/proof/pie.md
> 

## Use

| **Domain** | **Application** | Description |
| --- | --- | --- |
| **Combinatorics** | 🔢 Counting elements in unions | Corrects over-counts by alternately subtracting / adding intersections of increasing size. |
|  | 🎩 Derangements (hat-check problem) | Count permutations where no item stays in its original place by excluding all fixed-point sets. |
|  | ↔️ Surjections | Count onto functions $[k] \twoheadrightarrow [n]$ by subtracting non-onto ones via $\sum_{i=0}^{n}(-1)^i\binom{n}{i}(n-i)^k$. |
| **Probability** | 🎲 Probability of unions | Convert inclusion-exclusion on set sizes into probabilities: $P(\bigcup A_i)=\sum(-1)^{k+1}\sum P(A_{i_1}\cap\cdots\cap A_{i_k})$. |
|  | ⚙️ Reliability of systems | Compute chance that a network works by alternating inclusion/exclusion of cut- or path-sets failure events. |
| **Number Theory** | ϕ Euler’s totient function |  |
|  | 🔍 Sieves (Eratosthenes, Euler) | Count primes $≤ x$ or integers coprime to $n$ by alternating inclusion-exclusion over primes. |
| **Graph Theory** | 🎨 Chromatic polynomial |  |
|  | 🕸 Independent sets / coverings | Compute number of independent sets or vertex covers by alternating over subgraphs that violate the property. |
| **Computer Science** | 💡 Boolean SAT counting | Exact-model-counting (#SAT) algorithms add/subtract satisfying assignments of sub-formulas obtained by fixing variables. |
|  | 🔤 Strings with forbidden patterns | Count binary strings avoiding a set of substrings by including all strings then excluding those that contain any forbidden pattern, re-including overlaps, etc. |
| **Algorithms** | 🌀 Möbius inversion | Generalisation of inclusion-exclusion on posets; used to invert sums over divisors or subsets (e.g., GCD convolution, FFT-like transforms). |
| **Information Theory** | 📡 Entropy inequalities | Han’s inequality and Shearer’s lemma bound joint entropies via alternating sums of subset entropies, mirroring inclusion-exclusion structure. |

## QA

### Why is called the “inclusion–exclusion” Principle?

The principle is called “inclusion–exclusion” because:

- we **include** the sizes of individual sets,
- then **exclude** the sizes of their pairwise intersections (to avoid double counting),
- then **include** the triple intersections (since they were subtracted too many times),
- and so on, alternating signs.

## References

- http://artofproblemsolving.com/wiki/index.php/Principle_of_Inclusion-Exclusion
- https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
- https://brilliant.org/wiki/principle-of-inclusion-and-exclusion-pie/
- https://cp-algorithms.com/combinatorics/inclusion-exclusion.html
