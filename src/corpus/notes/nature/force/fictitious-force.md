---
tags: [note, nature, force, physics, property]
---

# Fictitious Force

> A **fictitious force** — also called an inertial force or pseudo-force — is the term that appears in Newton's second law when it is written in a non-inertial frame: the frame's own acceleration, moved to the other side of the equation and given the dimensions of a force.

> The term names no interaction. No body exerts it, it has no agent, no reaction partner and no field; it appears because the frame accelerates, and it vanishes when the same motion is described from an inertial frame. What makes it worth a note is that it is not merely a bookkeeping trick: locally, a fictitious force and a gravitational field are indistinguishable, and that indistinguishability is where general relativity starts.

## Formulation

### What natural element type does this natural instance belong to?

`Interaction-Derived Quantity` at meso level of organization (Ontic; Qualitative), specialized from `Property` — a quantity carried by a state of motion rather than by a body.

**Boundary.** Every other note on the [force shelf](/view.html?p=notes/nature/force/forces.md) describes a quantity derived from an *interaction between bodies*. This one is derived from the relation between a body and a **frame**: the acceleration of the observer's coordinate system. That is why the type still holds — it is a derived quantity of a joint state — while the reading as an interaction does not. It is also not a [fundamental force](/view.html?p=notes/nature/force/fundamental-forces.md): the four interactions have agents and fields, and this has neither. And it is not a violation of Newtonian mechanics: the law holds in the inertial frame, and the fictitious force is the correction that lets the same law be written in a frame that accelerates.

### What is this natural instance?

> A passenger thrown forward when the bus brakes; the outward push felt in a car taking a curve; the paraboloid surface of water in a rotating bucket; the deflection of a pendulum or an artillery shell by the Earth's rotation.

Each is the same situation: an observer in an accelerating frame, insisting on writing $\mathbf{F} = m\mathbf{a}$ with $\mathbf{a}$ measured in that frame. The correction is proportional to the mass of the body, which is why it is felt as weight and why it can be transformed away by changing the frame.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the quantity itself, decomposed to its kinds, the properties it carries, the frames in which it appears and the bounds on it — not the dynamics of the frames, which belong to mechanics, and not the equivalence principle as a theory, which is a construction about gravity.
>
> Identity: every Instance Tree Path is the full path from `Ontic Element`, each non-root row extends an existing path by exactly one labelled link, type segments are backticked, instances are Title Case, every leaf resolves to an instance, and no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force | Meso. The frame-acceleration term written as a force. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Kind)` Translational Fictitious Force | Meso. The uniform term $-m\mathbf{a}_0$ of a linearly accelerating frame: the bus, the lift, the launch. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Kind)` Centrifugal Force | Meso. The outward term $-m\,\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r})$ of a rotating frame — the one that makes the water surface a paraboloid. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Kind)` Coriolis Force | Meso. The term $-2m\,\boldsymbol{\omega}\times\mathbf{v}$ that appears only when the body moves in the rotating frame: the deflection of a pendulum, a shell or a cyclone. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Kind)` Euler Force | Meso. The term $-m\,\dot{\boldsymbol{\omega}}\times\mathbf{r}$ that appears only when the rotation itself changes rate. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Attribute)` `Property` | Grouping. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Attribute)` `Property` `(→ Instance)` Mass Proportionality | Micro. The term is proportional to the body's mass, so it accelerates every body in the frame equally — the property that makes it indistinguishable from gravity. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Attribute)` `Property` `(→ Instance)` Frame Dependence | Meso. It exists only relative to the chosen frame; in an inertial frame the same motion needs no term at all. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Situation)` `Environment` | Grouping. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Situation)` `Environment` `(→ Instance)` Non-Inertial Frame | Meso. The accelerating or rotating frame — the situation in which the term is needed and outside of which it is not defined. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Bound)` `Natural Constraint` | Grouping. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Bound)` `Natural Constraint` `(→ Instance)` Vanishing in Inertial Frames | Micro. The bound that defines it: change to an inertial frame and the term is gone, with no change in the motion described. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Fictitious Force `(→ Bound)` `Natural Constraint` `(→ Instance)` Local Indistinguishability from Gravity | Meso. Because it is proportional to mass, no local experiment distinguishes it from a gravitational field — the equivalence principle's premise. |

**Limitation checklist** — **Scale** (the term is meaningful at the scale of the frame: a rotating laboratory, a planet, a galaxy); **Partial Observability** (the frame's acceleration is inferred from the apparent forces, not measured independently); **Many-Body coupling** (in a rotating frame every body carries the same terms, so the corrections are collective rather than per-object); **Non-Repeatability** (the frame's own motion is part of the experiment and rarely reproducible in detail).

**Secondary readings** (kept as prose, never merged into the tree): readable as **technique** — the centrifuge, which uses a fictitious force as its working principle; readable as **epistemic** — the term as a coordinate artefact, and its disappearance under a change of frame as the argument that forces are not absolute; readable as **production** — rotating machinery whose design must carry the centrifugal term.

## The two readings of the term

| Reading | What it says | What it costs |
| --- | --- | --- |
| **Bookkeeping** | The term is an artefact of a bad frame; the inertial description is the true one, and the fictitious force is a correction to be removed | Makes the term sound dispensable — yet it is the term that makes the calculation possible in the frame where the problem is posed |
| **Equivalence** | Locally, the term and gravity are the same thing; the inertial frame is a local notion, not a global one | Takes the term seriously: what looks fictitious in one frame is indistinguishable from a field in another, and this is the route to general relativity |

## References

- https://en.wikipedia.org/wiki/Fictitious_force
- Lanczos, C. (1970). *The variational principles of mechanics* (4th ed.). University of Toronto Press. — the classical treatment of inertial forces and the rotating frame.
- Taylor, J. R. (2005). *Classical mechanics*. University Science Books. — the derivations of the centrifugal, Coriolis and Euler terms.
- [Forces](/view.html?p=notes/nature/force/forces.md) — the shelf this note belongs to · [Fundamental Forces](/view.html?p=notes/nature/force/fundamental-forces.md) — the interactions it is *not* · [Force](/view.html?p=notes/nature/property/force.md) — the quantity it imitates
- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md)
