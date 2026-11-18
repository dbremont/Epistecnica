---
tags: [note, nature, physical-object, structural-engineering, ontology]
qa:
 - Is a column a kind of member or a state of one — is "column" its geometry, its action, or the failure mode it is designed to survive?
 - Buckling is a stability failure, not a strength failure; why does the same body carry both bounds, and which of them decides its size?
---

# Column

> A **column** is a [structural member](/view.html?p=notes/nature/body/member.md) carrying **compression along its axis**, and its characteristic failure is not crushing but **buckling**: at a critical load the straight configuration stops being stable, and the member bows sideways while its material is still far below its strength. The column is the body in which strength and stability are two different bounds on the same member.

## Formulation

### What natural element type does this natural instance belong to?

`Structural Member` at **meso** level of organization (Ontic; Constitutive) — a `Building Block` of a [structure](/view.html?p=notes/nature/body/structure.md), specialized to the axial-compression case.

It is **not** the [beam](/view.html?p=notes/nature/body/beam.md): both resist load with the same geometry, and the difference is the direction of the action. A beam bends under transverse load and is sized by its bending stress and deflection; a column is compressed along its axis and is sized by its **slenderness**, because a long compressed member fails by losing its shape rather than by exceeding its stress. It is **not** a `Bar`: a bar is the abstract axial member of a truss, assumed not to buckle.

### What is this natural instance?

> A post under a floor, a pillar in a portico, a strut in a roof, a stanchion, a bone under a compressive load, a drinking straw between two fingers when it suddenly folds.

The physics is one-dimensional and clean. A straight elastic strut of length $L$, second moment $I$ and modulus $E$, pinned at both ends, is stable up to the Euler load

$$P_{\mathrm{cr}}=\frac{\pi^{2}EI}{L^{2}},$$

and beyond that the straight form is no longer the equilibrium of least energy. The lesson of the formula is in the exponents: the capacity falls with the **square** of the length and rises only linearly with the stiffness of the section, so slenderness — not area — governs the design. Fixing the ends instead of pinning them multiplies the capacity by four, which is why the *effective length* rather than the physical length enters the calculation.

Three regimes follow, and they are the note's real content: a **short** column crushes, and strength governs; a **long** column buckles elastically, and the Euler load governs; an **intermediate** column does both at once, and every code has its own empirical interpolation because no closed theory covers the transition. The stability bound is also the reason imperfections matter more here than anywhere else in the shelf: a column with a small initial bow fails below the ideal load, so the ideal formula is an upper bound rather than a capacity.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the compressed member — its length regimes, the geometric quantities that decide its capacity and the bounds it must respect — not the assembly, not the design rules, and not the dynamical stability of the structure it supports.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column | Meso. The member in axial compression. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Kind)` Short Column | Meso. Fails by crushing: the material's strength is reached before the shape becomes unstable. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Kind)` Long Column | Meso. Fails by elastic buckling at the Euler load, far below the crushing strength. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Kind)` Intermediate Column | Meso. Yielding and buckling act together; no closed theory, so the regime is empirical. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Attribute)` `Property` `(→ Instance)` Slenderness | Meso. Effective length over radius of gyration: the one number that decides which regime applies. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Attribute)` `Property` `(→ Instance)` Effective Length | Meso. The physical length corrected for end restraint: pinning, fixing, and their mixtures. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Euler Load | Meso. The critical load at which the straight configuration loses stability. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Imperfection Sensitivity | Micro. An initial bow or load eccentricity lowers the capacity below the ideal critical load, so the formula is an upper bound. |

**Limitations.** *Nonlinearity* — the buckling problem is geometrically nonlinear even when the material is elastic, and the ideal formula is the linearised first eigenvalue. *Uncertainty* — capacity depends on imperfections that are not measured, which is why design codes carry large margins here. *Scale* — the same body read as a member and as a cross-section gives two different problems.

## References

- Euler, L. (1759). Sur la force des colonnes. *Mémoires de l'Académie des Sciences de Berlin*, 13, 252–282. — the critical load, derived from the elasticity of a bent strut
- Timoshenko, S. P. (1953). *History of strength of materials*. McGraw-Hill. — the long argument between the strength and stability readings of compression
- Gordon, J. E. (1978). *Structures: Or why things don't fall down*. Penguin. — why a long column fails at a load it could easily have carried in compression
- [Stability Analysis](/view.html?p=notes/miscellanea/discipline/stability-analysis.md) — the technique that decides whether the configuration holds
- [Member](/view.html?p=notes/nature/body/member.md) · [Beam](/view.html?p=notes/nature/body/beam.md) · [Cable](/view.html?p=notes/nature/body/cable.md) · [Structure](/view.html?p=notes/nature/body/structure.md)
