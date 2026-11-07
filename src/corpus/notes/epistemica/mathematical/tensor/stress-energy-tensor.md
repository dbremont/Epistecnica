---
tags: [note, mathematics, analytical, type, physical]
---

# Stress-Energy Tensor

> The **stress-energy tensor** $T_{\mu\nu}$ packages the energy density, momentum density, energy flux and stress of matter and fields into one symmetric two-tensor: the source term of gravity.

## Formulation

> **What it is.** The relativistic generalization of density, pressure and shear. Its $00$ component is energy density, $0i$ momentum density, and $ij$ the stress — so one object carries everything that curves spacetime.
>
> **Type.** A `Concept`; a [tensor field](tensor-field.md) on spacetime.
>
> **Boundary.** It is not the [Cauchy stress tensor](stress-tensor.md): that one is purely spatial and lives in continuum mechanics. The relativistic tensor includes energy and momentum flux, and reduces to the Cauchy stress only in a non-relativistic limit.

## Key results

- **Conservation.** $\nabla^\mu T_{\mu\nu} = 0$ — local conservation of energy and momentum, and the compatibility condition with the [Einstein tensor](einstein-tensor.md).
- **Perfect fluid.** $T_{\mu\nu} = (\rho + p)u_\mu u_\nu + p\,g_{\mu\nu}$ — the form behind cosmology and the Friedmann equations.
- **Trace and equation of state.** $T = -\rho + 3p$; radiation has $T = 0$, dust has $T = -\rho$ — the trace is the equation-of-state summary.
- **Energy conditions.** Weak, strong, dominant and null conditions are inequalities on $T$; the singularity theorems are stated in their terms.
- **Electromagnetic contribution.** $T_{\mu\nu} = \frac{1}{\mu_0}(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta})$ — the field's own stress-energy, from the [electromagnetic tensor](electromagnetic-tensor.md).

## References

- https://en.wikipedia.org/wiki/Stress%E2%80%93energy_tensor
- [Einstein Tensor](einstein-tensor.md) · [Electromagnetic Tensor](electromagnetic-tensor.md) · [Stress Tensor](stress-tensor.md) · [Metric Tensor](metric-tensor.md)
