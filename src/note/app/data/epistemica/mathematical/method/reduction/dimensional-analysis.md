---
tags: [method, technique, measurement, mathematics]
---

# Dimensional Analysis

> **Dimensional analysis** derives the admissible form of a physical relation from the units its quantities carry: a relation must be dimensionally homogeneous, and that constraint fixes the exponents.

## Formulation

> **What it is.** The routine that reduces a problem's parameter count before any equation is written. Represent each quantity by its dimensions (M, L, T, …), impose homogeneity, and solve for the exponents — the result is a relation up to an unknown function of dimensionless groups.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** It gives form, never the constant or the function of the dimensionless groups. It works when the list of relevant quantities is complete; a missing variable yields a wrong (but plausible-looking) law.

## Key results

- **Buckingham Pi.** A relation among $n$ quantities in $k$ independent dimensions depends on $n-k$ dimensionless groups — the counting theorem of the method.
- **The pendulum.** Period depends on length and gravity as $\sqrt{l/g}$ — derived with no dynamics.
- **Reynolds number.** Viscous flow is governed by $\rho v L/\mu$; every regime diagram is a dimensionless-group statement.
- **Scaling laws.** Combining dimensions with the assumption of a power law yields the exponents directly — the route to Kolmogorov's $5/3$, and to the scaling laws the corpus already uses.
- **Consistency check.** Every equation in physics is a candidate: a mismatch in units is a proof of error, and that check is the method's cheapest use.

## References

- https://en.wikipedia.org/wiki/Dimensional_analysis
- [System of Units](../../../measurement/system-of-units-of-measurement.md) · [Change of Variables](change-of-variables.md) · [Scale](../../scale.md) · [Asymptotic Analysis](../approximation/asymptotic-analysis.md)
