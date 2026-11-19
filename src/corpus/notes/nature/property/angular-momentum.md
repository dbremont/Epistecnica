---
tags: [note, nature, property, interaction-derived-quantity, physics, mechanics]
qa:
 - Is angular momentum a property of a body, or of a body *and* an origin — and if the second, what exactly does the joint state consist of?
 - If spin carries angular momentum without anything rotating, is the word naming one quantity or two?
---

# Angular Momentum

> **Angular momentum** is the quantity of motion taken at a distance from an axis: $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ for a body about an origin, and the sum of such terms for a system. Euler's name for it — *moment of momentum* — is the more honest one, because it says what the quantity is made of: a linear momentum and a lever arm.

> It is the quantity that **rotational symmetry conserves**, and that is the whole of its standing. Where the forces on a system are central — the planets, an electron in a Coulomb field, a body under gravity — the torque vanishes and $\mathbf{L}$ does not change; Kepler's second law, that a planet sweeps equal areas in equal times, is that statement in its oldest form.

## Formulation

### What natural element type does this natural instance belong to?

`Interaction-Derived Quantity` at **meso** level of organization (Ontic; Qualitative), specialized from `Property` — a quantity carried by a body's configuration *and* its motion together, not by the body alone.

**Boundary.** The shelf master already files it here: `Ontic Element (→ Kind) Property (→ Kind) Interaction-Derived Quantity (→ Instance) Angular Momentum`, "the rotational analogue of momentum, defined over a body's configuration and its motion" ([Property](/view.html?p=notes/nature/property/property.md)). Three neighbours it is not:

- not [momentum](/view.html?p=notes/nature/property/momentum.md), which is a single body's mass in motion and needs no origin — $\mathbf{p}$ is intrinsic to the motion, $\mathbf{L}$ is not;
- not [spin](/view.html?p=notes/nature/property/spin.md), which is an *intrinsic* property of a particle and belongs to the intrinsic kind: a spin carries angular momentum, but nothing rotates and no lever arm exists;
- not a `Constraint`. That $\mathbf{L}$ is conserved under central forces is a constraint on the dynamics, and it is filed as a bound on this property, never as the property.

### What is this natural instance?

> A planet about the Sun, sweeping equal areas in equal times. A rifle bullet through a rifled barrel, carrying $\mathbf{L}$ along its axis and staying pointed. A gyroscope refusing to fall. An electron in an atom, whose orbital angular momentum takes only the values $\hbar\sqrt{l(l+1)}$.

The classical object is straightforward to state and awkward to compute with, for three reasons that belong to the note rather than to its arithmetic.

**It needs an origin.** Change the point about which it is taken and $\mathbf{L}$ changes: about a new origin $O'$ at $\mathbf{R}$ from $O$, $\mathbf{L}' = \mathbf{L} + \mathbf{R}\times\mathbf{P}$. This is why the quantity is *interaction-derived* in the guide's sense — the joint state is the body's motion together with the axis it is referred to — and why a statement that angular momentum is conserved is meaningless until the point is named.

**It is a vector whose direction is not the direction of rotation.** For a rigid body $\mathbf{L} = I\boldsymbol{\omega}$, where $I$ is the [inertia tensor](/view.html?p=notes/epistemica/mathematical/tensor/moment-of-inertia-tensor.md), not a scalar; so $\mathbf{L}$ is in general *not* parallel to $\boldsymbol{\omega}$. The angular velocity and the angular momentum precess about each other, which is the whole phenomenon of a free body wobbling and the reason a spinning top slowly turns rather than simply staying put. The kinetic energy of the rotation is $\tfrac12\,\boldsymbol{\omega}\cdot\mathbf{L}$.

**Its conservation is a symmetry, not a coincidence.** The equation of motion is $\dot{\mathbf{L}} = \boldsymbol{\tau}$, so $\mathbf{L}$ is constant exactly when the total torque vanishes — under central forces, always. Read the other way round, rotational invariance of the dynamics *implies* a conserved angular momentum, which is Noether's theorem applied to the rotation group; see [Conservation Law](/view.html?p=notes/epistemica/meta/guidance/principle/conservation-law.md) and [Symmetry](/view.html?p=notes/nature/result/principle/symmetry.md).

In quantum mechanics the same quantity survives with a changed arithmetic. The components no longer commute,
$[L_i,L_j]=i\hbar\,\varepsilon_{ijk}L_k$, so a state cannot have a sharp $\mathbf{L}$: only $L^2=\hbar^2 l(l+1)$ and one component $L_z=m\hbar$ are simultaneously definite. The classical vector becomes an operator whose magnitude is graded in units of $\hbar$, and its classical limit is the vector above — which is why the two readings must be kept as two levels of the same instance rather than as two instances.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the quantity itself, decomposed to its kinds, the properties it carries and the bounds imposed on it — not the dynamics of the bodies that carry it, which belong to [rigid-body mechanics](/view.html?p=notes/epistemica/singular/rigid-body-mechanics.md), and not the symmetry principle in general, which is a construction about laws.
>
> Identity: every Instance Tree Path is the full path from `Ontic Element`, each non-root row extends an existing path by exactly one labelled link, type segments are backticked, instances are Title Case, every leaf resolves to an instance, and no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum | Meso. The moment of momentum about an origin: the joint quantity of a body's configuration and its motion. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Kind)` Orbital Angular Momentum | Meso. The part carried by motion about the origin, $\mathbf{L}=\mathbf{r}\times\mathbf{p}$ summed over the system's constituents. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Kind)` Spin Angular Momentum | Micro. The intrinsic part, carried with no rotation behind it and no lever arm — the quantum property at [Spin](/view.html?p=notes/nature/property/spin.md). |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Kind)` Total Angular Momentum | Meso. $\mathbf{J}=\mathbf{L}+\mathbf{S}$: the quantity that is conserved when spin and orbit exchange, as in spin–orbit coupling. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Attribute)` `Property` | Grouping. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Attribute)` `Property` `(→ Instance)` Axis Dependence | Meso. Defined only relative to an origin, and shifted by $\mathbf{R}\times\mathbf{P}$ when the origin moves — the property that makes the quantity interaction-derived. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Attribute)` `Property` `(→ Instance)` Magnitude | Meso. $L = r\,p_\perp$; for a rigid body $L = I\omega$ with $I$ a tensor, so $\mathbf{L}$ and $\boldsymbol{\omega}$ need not be parallel. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Attribute)` `Property` `(→ Instance)` Handedness | Meso. A pseudovector: unchanged by rotation, reversed by reflection, which is why parity is a meaningful test on it. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Bound)` `Constraint` | Grouping. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Conservation of Angular Momentum | Macro. Rotational symmetry bounds the dynamics: $\dot{\mathbf{L}}=\boldsymbol{\tau}$, so $\mathbf{L}$ is constant under central forces — Kepler's second law, and Noether's theorem on the rotation group. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Angular Momentum `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Quantization of Angular Momentum | Micro. At the quantum level the bound is stronger than conservation: $L^2=\hbar^2l(l+1)$, $L_z=m\hbar$, and the non-commuting components forbid a sharp vector. |

**Limitation checklist.** This instance exhibits **Scale** — the classical vector and the $\hbar$-graded spectrum are the same name at two levels, and a statement true at one is not automatically true at the other; **Uncertainty** — the components cannot be simultaneously definite, so the vector is not an observable in the quantum reading; **Measurement Disturbance** — angular momentum is read by acting on the body (a torque applied, a photon scattered), and the reading changes the quantity it measures; **Many-Body coupling** — a composite carries the sum of its parts' angular momenta plus the angular momentum of their relative motion, so the quantity of the whole is not the sum of the quantities of the members.

## QA

### Is angular momentum a property of a body, or of a body and an origin?

> Of a body *and* an origin — and the note is filed under the interaction-derived kind for exactly that reason. The definition $\mathbf{L}=\mathbf{r}\times\mathbf{p}$ names two things: the body's momentum, and the vector from the chosen point to the body. Move the point and the quantity changes by $\mathbf{R}\times\mathbf{P}$, so angular momentum is not a feature the body carries in the way mass or charge is. What makes it a single property rather than a relation is that, once the origin is fixed, it is a definite function of the body's state and it is conserved; the joint-state requirement is a condition on the definition, not a sign that the quantity is vague.

### If spin carries angular momentum without anything rotating, is the word naming one quantity or two?

> One quantity, two ways of being carried. Angular momentum is defined by what it *does*: it is the generator of rotations, the quantity conserved under rotational symmetry, and entering the commutation relations $[J_i,J_j]=i\hbar\varepsilon_{ijk}J_k$ of the rotation group. Orbital angular momentum realizes it by motion in space, with a lever arm and a classical limit; spin realizes it by an internal degree of freedom with no lever arm and no classical limit. Both are, in the precise sense, the same representation-theoretic object — the generators of $\mathrm{SO}(3)$ or its cover $\mathrm{SU}(2)$ — which is why they add: $\mathbf{J}=\mathbf{L}+\mathbf{S}$, and why a photon's circular polarization is angular momentum too. The classical picture of something rotating is the *realization*, not the definition.

## References

- Kepler, J. (1609). *Astronomia nova*. Voegelin. — the equal-area law, which is the conservation of angular momentum stated as a fact about orbits
- Newton, I. (1687). *Philosophiæ naturalis principia mathematica*. Streater. — the laws from which the quantity and its conservation follow
- Euler, L. (1765). *Theoria motus corporum solidorum seu rigidorum*. Röse. — the rigid body, the moment of inertia tensor, and the name *moment of momentum*
- Bohr, N. (1913). On the constitution of atoms and molecules. *Philosophical Magazine*, 26(151), 1–25. — the angular momentum of the electron quantized in units of $\hbar$
- Noether, E. (1918). Invariante Variationsprobleme. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 1918, 235–257. — rotational invariance implies a conserved angular momentum
- Uhlenbeck, G. E., & Goudsmit, S. (1925). Spinning electrons and the structure of spectra. *Nature*, 117(2938), 264–265. — spin: angular momentum with no rotation behind it
- Dirac, P. A. M. (1930). *The principles of quantum mechanics*. Clarendon Press. — the commutation relations, and angular momentum as the generator of rotations
- Landau, L. D., & Lifshitz, E. M. (1976). *Mechanics* (3rd ed.). Pergamon Press. — angular momentum, its conservation and the rigid body
- Goldstein, H. (1980). *Classical mechanics* (2nd ed.). Addison-Wesley. — the classical treatment, Euler angles and the inertia tensor
- [Angular momentum](https://en.wikipedia.org/wiki/Angular_momentum)
- [Property](/view.html?p=notes/nature/property/property.md) — the shelf this belongs to, and the intrinsic / interaction-derived split
- [Momentum](/view.html?p=notes/nature/property/momentum.md) · [Spin](/view.html?p=notes/nature/property/spin.md) · [Inertia](/view.html?p=notes/nature/property/inertia.md) · [Photon Momentum](/view.html?p=notes/nature/photon-momentum.md) · [Electromagnetic Momentum](/view.html?p=notes/nature/electromagnetic-momentum.md)
- [Rigid-Body Mechanics](/view.html?p=notes/epistemica/singular/rigid-body-mechanics.md) · [Moment of Inertia Tensor](/view.html?p=notes/epistemica/mathematical/tensor/moment-of-inertia-tensor.md) · [Conservation Law](/view.html?p=notes/epistemica/meta/guidance/principle/conservation-law.md) · [Symmetry](/view.html?p=notes/nature/result/principle/symmetry.md)
