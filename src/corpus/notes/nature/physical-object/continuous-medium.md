---
tags: [note, nature, physical-object, physics, system, unfinished]
---

# Continuous Medium (Body)

> A **continuous medium** is a body described as a matter field over a volume: at the resolution used, the material is taken as filling space without gaps, so its state is a field — density, stress, strain, velocity — defined at every point rather than a list of parts. The continuous body is a *modelling cut* on matter, not a kind of substance: the same water is a continuous medium for a flow calculation and discrete molecules for a kinetic one.

## Formulation

### What natural element type does this natural instance belong to?

`Natural Object` at meso level of organization (Ontic; Existential), specialized from `Substantive` — a fully specified material particular, individuated by its **deformation field** rather than by countable parts.

It is **readable as** a `Natural System` when the internal fields are taken to interact — a stress field in equilibrium is a bounded set of interacting components — but the body reading comes first: the medium is one particular, not a system of particulars. It is **not** a `Substance / Matter`: the substance is what the medium is made of, the medium is the particular filling a volume. It is **not** a `Property`: density and stress are its attributes, carried by it.

### What is this natural instance?

> A steel beam under load, water in a pipe, air in a room, the mantle below the crust, muscle tissue under tension. What unifies them is the description: at the scale of interest no individual molecule is tracked, so the body is represented by fields that satisfy the balance laws — mass, momentum, energy — plus a constitutive law relating stress to strain, strain rate, or history.

The alternative description is the *discrete body* of countable particles; the two are linked by the continuum limit (many particles per representative volume) and agree while that limit holds.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one continuous body, decomposed to its fields and their governing relations — not to its molecules, which belong to the particle and matter notes.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row; grouping types are `` `code` ``, instances are Title Case, and no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Kind)` Continuous Body | Body individuated by a deformation field over a volume. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Part)` `Building Block` | Grouping: what carries the description — the material points and the volume they fill. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Part)` `Building Block` `(→ Kind)` Material Point | Representative volume element: small enough to be local, large enough to carry averages. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Kind)` Constitutive Material | The substance the medium is made of, as fixed by its constitutive behaviour. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Attribute)` `Property` | Grouping: the fields the description carries at every point. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Attribute)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Stress Field | Joint state of neighbouring material points: the internal force transmitted across a surface. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Attribute)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Strain Field | Relative deformation of neighbouring material points. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Attribute)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Velocity Field | Rate of change of material-point position, one value per point. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Attribute)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Density Field | Mass per unit volume at each material point. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` | Grouping: the laws every continuous body must satisfy. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Mass Balance | Conservation of mass across every control volume. Micro. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Momentum Balance | Force equals rate of change of momentum at every material point. Micro. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Constitutive Law | The material's own rule relating stress to strain and its history. Meso. |
| `Natural Object` `(→ Kind)` Continuous Body `(→ Kind)` Fluid Body | Continuous body that cannot sustain static shear stress and therefore flows. Meso. |

## What Set of Concepts Allows Us to Describe and Analyze a Continuous Body?

| Concept | Description |
|---|---|
| **Continuous Body** | A physical body modeled as a continuous distribution of matter throughout a spatial region. |
| **Material Point** | An idealized point representing a specific portion of matter within a continuous body. |
| **Configuration** | The spatial arrangement of all material points of a body at a given instant. |
| **Material** | The substance constituting a body, characterized by its physical and mechanical properties. |
| **Force** | A mechanical interaction capable of changing the motion or deforming a body. |
| **Load** | An externally applied mechanical action on a body, including forces and moments. |
| **Body Force** | A force distributed throughout the volume of a body, such as gravity. |
| **Traction** | Force per unit area acting on a surface of a body. |
| **Stress** | A measure of the internal force distribution per unit area within a body, represented by a stress tensor. |
| **Displacement** | The change in position of a material point relative to a reference configuration. |
| **Deformation** | The change in the relative spatial arrangement of material points within a body. |
| **Strain** | A mathematical measure of local deformation, describing changes in length, angle, and volume. |
| **Equilibrium** | A mechanical condition in which the resultant forces and moments satisfy the equilibrium equations. |
| **Constitutive Relation** | A mathematical relationship describing how a material responds to mechanical actions, relating quantities such as stress and strain. |
| **Stiffness** | Resistance to deformation under applied mechanical actions. |
| **Strength** | Capacity of a material or body to withstand mechanical stresses without failure. |
| **Stability** | Capacity of a body or mechanical system to maintain an equilibrium configuration under perturbations. |
| **Boundary Conditions** | Conditions specifying prescribed displacements, forces, or other physical quantities at the boundaries of a body. |
| **Failure** | Loss of mechanical integrity or intended function due to excessive deformation, fracture, yielding, or instability. |

## References

- [Continuous Medium (Body)](https://en.wikipedia.org/wiki/Continuum_mechanics)
- [Physical Object](/view.html?p=notes/nature/physical-object/physical-object.md) — the family and its identity criteria
- [Fluid](/view.html?p=notes/nature/physical-object/fluid.md) — the flowing specialization
- [Matter](/view.html?p=notes/nature/matter/matter.md) — the stuff the medium is made of
- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md)
