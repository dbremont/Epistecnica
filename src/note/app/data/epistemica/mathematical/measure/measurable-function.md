---
tags: [measure-theory, function]
---

# Measurable Function

> A **measurable function** is a map between measurable spaces such that the preimage of every measurable set is measurable. It is the structure-preserving map of measure theory, and the object over which the [Lebesgue integral](../mapping/lebesgue-integral.md) is defined.

## Formulation

> **What it is.** The right notion of "function" when the codomain carries a $\sigma$-algebra: continuity preserves open sets, measurability preserves measurable ones. Without it, integration cannot be defined on a general space.
>
> **Type.** A `Concept` — a `Morphism` of measurable spaces, in the [category](../structure/category.md) of measurable spaces and measurable maps.
>
> **Boundary.** Measurability is weaker than continuity and stronger than nothing: every continuous function is Borel measurable, and every measurable function is the pointwise limit of simple ones. The hierarchy is what lets approximation arguments work.

## Key results

- **Approximation.** Every non-negative measurable function is a monotone limit of simple (finite-valued, measurable) functions — the construction that defines the integral.
- **Closure.** Sums, products, limits and compositions of measurable functions are measurable; the class is stable under everything an analyst needs.
- **Pushforward.** A measurable map transports a measure to its codomain, which is exactly how a [random variable](../../observational/probability/random-variable.md) induces a distribution.
- **Lusin.** A measurable function is continuous off a set of arbitrarily small measure — measurability is "continuity almost everywhere" in disguise.

## References

- https://en.wikipedia.org/wiki/Measurable_function
- [Measure](measure.md) · [Lebesgue Integral](../mapping/lebesgue-integral.md) · [Generalized Function](../mapping/generalized-function.md) · [Category](../structure/category.md)
