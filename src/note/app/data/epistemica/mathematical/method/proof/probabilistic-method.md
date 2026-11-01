---
tags: [method, technique, probability]
---

# Probabilistic Method

> The **probabilistic method** proves the existence of an object by showing that a randomly chosen object has the required property with positive probability.

## Formulation

> **What it is.** A routine that trades construction for expectation: instead of exhibiting an object, one puts a probability distribution on a family and shows the probability of a counterexample is less than one. Non-constructive, but often the only way — and the expectation bound usually suggests a derandomization.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** It proves existence, never uniqueness, and says nothing about how to find the object unless a derandomization step is added. It is not a substitute for a construction when one is available.

## Key results

- **First moment.** If the expected number of bad events is below one, a good object exists.
- **Lovász local lemma.** Even with many bad events, if each is rare and depends on few others, a good object still exists — the method's most powerful form.
- **Ramsey bounds.** $R(k,k) > 2^{k/2}$ comes from a single expectation computation, and remains the best elementary lower bound.
- **Expander existence.** Random regular graphs are expanders with high probability — the existence proof that started the theory.
- **Derandomization.** The conditional expectation method turns many probabilistic proofs into polynomial-time algorithms.

## References

- https://en.wikipedia.org/wiki/Probabilistic_method
- [Combinatorics](../../discrete/combinatorics.md) · [Expectation](../../../observational/probability/expected-value.md) · [Concentration Inequality](../../construction/chebyshev-s-inequality.md) · [Generating Function](../transform/generating-function.md)
