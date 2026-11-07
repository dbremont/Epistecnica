---
tags: [note, mathematics, analytical, type, physical]
---

# Stress Tensor

> The **Cauchy stress tensor** $\sigma_{ij}$ gives the force per unit area transmitted across any surface in a material: the traction on a surface with normal $n$ is $t_i = \sigma_{ij}n_j$.

## Formulation

> **What it is.** The complete state of internal force in a continuous body, packaged so that every cutting plane's traction is a contraction away. Symmetric in the absence of body couples, and the object constitutive laws are written in.
>
> **Type.** A `Concept`; a [tensor field](tensor-field.md) on a material body.
>
> **Boundary.** It is the spatial, non-relativistic relative of the [stress-energy tensor](stress-energy-tensor.md), and the two must not be conflated: Cauchy stress has no energy or momentum-flux components.

## Key results

- **Cauchy's theorem.** Traction is linear in the normal, so a tensor exists; this is the reason stress is a tensor at all rather than a vector field.
- **Equilibrium.** $\nabla\cdot\sigma + \mathbf{b} = 0$ — the momentum balance in statics.
- **Principal stresses.** Eigenvalues of $\sigma$ are the normal stresses on planes with no shear; the eigenvectors are the principal directions (see [eigenvalue](../structure/linear/eigenvalue.md)).
- **Invariants.** $\operatorname{tr}\sigma$, $\tfrac12[(\operatorname{tr}\sigma)^2 - \operatorname{tr}\sigma^2]$ and $\det\sigma$ are frame-independent — the basis of yield criteria such as von Mises.
- **Constitutive laws.** Linear elasticity writes $\sigma = \mathbb{C}:\varepsilon$ with a fourth-rank stiffness tensor; fluids write $\sigma = -pI + 2\mu\dot\varepsilon$ for a Newtonian fluid.

## References

- https://en.wikipedia.org/wiki/Cauchy_stress_tensor
- [Strain tensor](stress-tensor.md) · [Stress-Energy Tensor](stress-energy-tensor.md) · [Continuum Mechanics](note.html?p=notes/epistemica/singular/continuum-mechanic-framework.md) · [Eigenvalue](../structure/linear/eigenvalue.md)
