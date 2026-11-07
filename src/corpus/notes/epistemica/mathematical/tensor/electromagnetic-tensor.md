---
tags: [note, mathematics, analytical, type, physical]
---

# Electromagnetic Tensor

> The **electromagnetic tensor** $F_{\mu\nu}$ is the antisymmetric two-tensor whose components are the electric and magnetic fields: one object, two fields, and a transformation law that mixes them under a change of frame.

## Formulation

> **What it is.** The field strength of the electromagnetic [connection](../geometry/connection.md). Its $0i$ entries are the electric field and its $ij$ entries the magnetic field; what one observer calls electric, a moving observer sees partly as magnetic.
>
> **Type.** A `Concept`; an antisymmetric [tensor field](tensor-field.md) — equivalently, a differential two-form.
>
> **Boundary.** It is not the potential: $F = dA$ locally, and the potential is defined only up to a gauge transformation. The tensor is the gauge-invariant content, which is why the physics is stated in it.

## Key results

- **Components.** $F_{0i} = E_i/c$ and $F_{ij} = -\epsilon_{ijk}B_k$; antisymmetry encodes the absence of magnetic monopoles.
- **Maxwell's equations.** $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ and $\partial_{[\mu}F_{\nu\rho]} = 0$ — the four equations become two.
- **Lorentz invariants.** $F_{\mu\nu}F^{\mu\nu} = 2(B^2 - E^2/c^2)$ and $F_{\mu\nu}\tilde F^{\mu\nu} \propto \mathbf{E}\cdot\mathbf{B}$ — the two scalars that no frame can change.
- **Gauge field.** $F = dA$ with $A \mapsto A + d\lambda$: the archetype of a gauge field strength, and the model every other gauge theory copies.
- **Stress-energy.** Its quadratic combination is the electromagnetic [stress-energy tensor](stress-energy-tensor.md).

## References

- https://en.wikipedia.org/wiki/Electromagnetic_tensor
- [Differential Form](../differential-form.md) · [Connection](../geometry/connection.md) · [Stress-Energy Tensor](stress-energy-tensor.md) · [Electromagnetism](note.html?p=notes/epistemica/singular/electromagnetism.md)
