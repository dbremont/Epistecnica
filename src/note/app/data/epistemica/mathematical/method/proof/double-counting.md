---
tags: [method, technique, discrete, mathematics]
---

# Double Counting

> **Double counting** proves an identity by counting one set in two ways: the same number is computed along two different decompositions, and the equality of the two totals is the identity.

## Formulation

> **What it is.** The combinatorial proof routine. Rather than manipulating sums, one exhibits a set whose size has two natural descriptions — by rows and by columns, by elements and by incidence — and equates them.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** The two counts must be of *the same* set; a double count that accidentally counts two different sets proves nothing. The method gives identities, not bounds — for bounds one needs [double counting with inequalities](inclusion-exclusion.md) or the [probabilistic method](probabilistic-method.md).

## Key results

- **Handshakes.** $\sum_v \deg(v) = 2|E|$: count edge-endpoints by vertex and by edge. Every graph theorem about degree sums is this argument.
- **Binomial identities.** $\sum_k \binom{n}{k} = 2^n$ by counting subsets by size and by choice; Vandermonde's identity by counting pairs of committees.
- **Cauchy–Schwarz, combinatorial form.** Counting pairs $(i,j)$ two ways yields the inequality — the same argument as the analytic proof, without the algebra.
- **Incidence counting.** Double counting incidences between points and lines proves Szemerédi–Trotter-type bounds and the Sylvester–Gallai theorem.
- **Averages.** Counting the sum of a quantity two ways and dividing gives the existence of an element at least average — the bridge to the [extremal principle](extremal-principle.md).

## References

- https://en.wikipedia.org/wiki/Double_counting_(fallacy)
- https://en.wikipedia.org/wiki/Combinatorial_proof
- [Combinatorics](../../discrete/combinatorics.md) · [Bijective Method](bijective-method.md) · [Inclusion–Exclusion](inclusion-exclusion.md) · [Probabilistic Method](probabilistic-method.md)
