---
tags: [note, nature, physical-object, structural-engineering, ontology]
---

# Structure

> A **structure** is a physical body whose parts are arranged by a load path: the members, connections and supports are held in relation to one another so that imposed forces travel through them to the ground. It is a body of the *discrete* type — its parts can be counted and traced — and what makes it one structure rather than a heap of members is the path the load takes through it.

## Formulation

### What natural element type does this natural instance belong to?

`Natural Object` at meso level of organization (Ontic; Existential), specialized through `Substantive` — a fully specified material particular whose parts are held together by a load path.

It is the note for the **discrete body** type the [Physical Object](/view.html?p=notes/nature/physical-object/physical-object.md) classification states without a note. It is **readable as** a `Constitutive Technical Object` in the technica grammar — a component or sub-assembly constituting a larger technical object, e.g. the built structure inside a construction project — and that reading is recorded as prose, not as a second root.

It is **not** a `Natural System`: a system is the members plus their interactions taken as the object; the structure is the member — one particular — and its load path is an attribute, not a membership relation. It is **not** a `Property`: stiffness, strength and stability are carried by the structure, not identical with it. It is **not** a `Substance / Matter`: steel, concrete and timber are its building blocks' stuff.

### What is this natural instance?

> A bridge span, a frame, a roof truss, a retaining wall, a dam, a crane jib, a bone. Every one of them is a set of members in relation, and the relation is fixed by where the load enters and where it leaves. Two arrangements of the same steel are two different structures because the load takes two different paths — and one may be stable while the other is not.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one structural body, decomposed to its members, connections, supports and the load path that holds them together — not to the design practice, which is decomposed in `technica/discipline/structural-mechanics.md`.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row; grouping types are `` `code` ``, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Kind)` Structure | Body whose parts are held by a load path carrying imposed forces to the ground. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` | Grouping: the compositional units of the structure. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Member | A bar, beam, column, slab or shell carrying actions along its own span. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection | The joint transmitting member actions: weld, bolt, bearing or anchorage. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support | The restraint through which the structure delivers its load to the ground. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` | Grouping: the stuff each unit is made of. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Structural Steel | Hot-rolled section with measured yield strength and toughness. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Structural Concrete | Cementitious material with specified cube strength and reinforcement. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Structural Timber | Graded sawn or engineered wood with directional strength. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Attribute)` `Property` | Grouping: what the structure carries as a whole. |
| `Natural Object` `(→ Kind)` Structure `(→ Attribute)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path | The relation through which every imposed force reaches a support. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Attribute)` `Property` `(→ Kind)` Stiffness | Resistance of the assembly to deformation under load. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Attribute)` `Property` `(→ Kind)` Strength | Capacity of the weakest member or connection to carry its action. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Attribute)` `Property` `(→ Kind)` Redundancy | Number of independent load paths between a load and its support. Meso. |
| `Natural Object` `(→ Kind)` Structure `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` | Grouping: the bounds a structure must respect. |
| `Natural Object` `(→ Kind)` Structure `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Equilibrium | Every load path delivers its forces and moments to the supports. Micro. |
| `Natural Object` `(→ Kind)` Structure `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Compatibility | Connected members deform consistently at the joints that join them. Micro. |
| `Natural Object` `(→ Kind)` Structure `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Stability | The configuration must survive a perturbation without losing equilibrium. Meso. |

**Limitations.** *Complexity* and *Many-Body coupling* — the members interact through every connection, so the response is not a sum of member responses. *Scale* — a structure is a meso body, but the same arrangement read at the scale of the building it supports becomes a member. *Partial Observability* — only the instrumented members report their real actions.

## References

- [Physical Object](/view.html?p=notes/nature/physical-object/physical-object.md) — the family and the discrete-body criterion this note instantiates
- [Continuous Medium](/view.html?p=notes/nature/physical-object/continuous-medium.md) — the field-side reading a member can be taken in
- [Structural Mechanics](/view.html?p=notes/technica/discipline/structural-mechanics.md) — the practice that designs such a body
- [Euler–Bernoulli Beam Theory](/view.html?p=notes/technica/discipline/euler-bernoulli-beam-theory.md) — the rule its members obey
- [Stability Analysis](/view.html?p=notes/technica/discipline/stability-analysis.md) — the technique that decides whether it holds
- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md)
