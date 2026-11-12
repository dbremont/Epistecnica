---
tags: [note, structural-engineering, beam-theory, solid-mechanics]
---

# Euler–Bernoulli Beam Theory

> **Euler–Bernoulli beam theory** is the model that reduces a slender loaded member to its neutral axis: plane cross-sections stay plane and normal to that axis, so the deflection `w(x)` of the member obeys `EI d⁴w/dx⁴ = q(x)`, the internal bending moment is `M = −EI d²w/dx²`, and the bending stress at a fibre is `σ = −M·y / I`. It is the oldest and most used technique in structural mechanics — the load-to-deflection rule for almost every beam ever built.

## Formulation

### What technical element type does this technical instance belong to?

**Beam theory belongs to the `Technical Principle` technical element type — a general rule governing the construction or operation of technical systems.**

```text
Technical Element
└── Technical Principle
    └── Euler–Bernoulli Beam Theory
```

It is a **principle** and not a `Constitutive Technique`: a technique is a procedure embodied in an element, while this is a rule that *governs* the member — the equation a quantity must satisfy. It is applied *as* a constitutive technique inside the structural and geotechnical practices, and it is a `Technical Model` readable as `Technical Research` once the question becomes whether the assumptions hold.

Boundaries: **Timoshenko beam theory** is the rival reading that keeps shear deformation and rotary inertia, and is taken when the member is short or the shear stiffness low. **Plate and shell theory** extends the same plane-section reasoning to two dimensions. **Strength of materials** is the wider family this principle belongs to; **continuum mechanics** is the parent framework that derives it from three-dimensional equilibrium and compatibility.

### What is this technical instance?

> A floor joist, a bridge girder, a rail, a shelf, a cantilever sign — any member whose length is large compared with its depth and whose load is transverse to its axis. It answers three questions with one equation: what shape does it take under this load (`w(x)`), what bending moment acts at each section (`M(x)`), and what stress does that moment put in the fibres (`σ = −My/I`).

The model rests on four assumptions, each with its own failure: **plane sections remain plane and normal** (fails for deep members), **small deflection** (fails for large displacement, where the geometry stiffens or softens), **linear elastic material** (`σ = Eε`, fails past yield) and **no shear deformation** (fails for short spans). Its thickness parameter is `L/h ≳ 10`; below that the shear correction of Timoshenko theory matters.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one principle, decomposed to its assumptions, the quantities it relates, its parameters and its validity bound.
>
> Identity: paths begin at `Technical Element`; grouping types are `` `code` ``, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Principle` → Euler–Bernoulli Beam Theory | Plane sections and small deflection give `EI w⁗ = q` for a slender member. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Assumption` | Grouping: the conditions the principle rests on. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Assumption` → Plane Section Assumption | Cross-sections stay plane and normal to the neutral axis under bending. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Assumption` → Small Deflection Assumption | Displacements are small enough that the undeformed geometry stays the reference. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Assumption` → Linear Elastic Assumption | Stress follows strain linearly through the Young's modulus. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Assumption` → Negligible Shear Deformation | Deformation by shear is small against deformation by bending. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Parameter` | Grouping: the quantities the equation carries. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Parameter` → Flexural Rigidity | The product `EI` fixing how much curvature a moment produces. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Parameter` → Second Moment of Area | The section's resistance to bending about its neutral axis. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Parameter` → Distributed Load | The transverse load intensity `q(x)` along the span. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Parameter` → Deflection Curve | The transverse displacement `w(x)` the equation solves for. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Parameter` → Bending Moment Distribution | The internal moment `M(x)` carried by each section. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Task` | Grouping: the tasks the principle is applied through. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Task` → Integrate the Governing Equation | Solve `EI w⁗ = q` with the support's boundary conditions. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Task` → Check the Slenderness Bound | Confirm the span-to-depth ratio keeps the assumptions admissible. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Task` → Switch to Timoshenko Theory | Leave the model for the shear-corrected reading when the bound fails. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Bound` | Grouping: where the principle stops governing. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Bound` → Deep Member Bound | Members with depth comparable to span fall outside the plane-section assumption. |
| `Technical Principle` → Euler–Bernoulli Beam Theory → `Technical Bound` → Large Deflection Bound | Displacements large against the depth require a second-order analysis. |

### What is a critical conceptual evaluation of this `technical element instance`?

The concept under evaluation is **Euler–Bernoulli Beam Theory**, defined above as *the rule that a slender member's deflection obeys `EI w⁗ = q` under plane-section, small-deflection, linear-elastic and shear-free assumptions*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: distinct from the practice that uses it, from the rival Timoshenko reading and from the continuum framework that derives it. Definitional Clarity — **pass**: the equation, the four assumptions and the slenderness bound are stated operationally. Conceptual Determinacy — **qualified**: the principle is exact within its assumptions and silent outside them, so the boundary is set by a ratio (`L/h`) rather than by a crisp class of members; the bound is stated rather than hidden. Internal Consistency — **pass**: the assumptions, the equation and the bounds agree; the shear-free assumption is the one that fails first and is the one the bound names. Representational Adequacy — **qualified**: excellent for bending of slender members, blind to shear deformation, large displacement and local instability, each of which is a named bound rather than an omission. Purpose Adequacy — **pass**: it exists to convert load to deflection and moment, and every leaf serves that conversion.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Separated from the practice, from Timoshenko theory and from continuum mechanics; typed as principle, not technique. |
| Definitional Clarity | pass | Equation, assumptions and bounds stated operationally; no undefined term. |
| Conceptual Determinacy | qualified | Exact inside the assumptions, silent outside; the boundary is a slenderness ratio, stated as a bound not a class. |
| Internal Consistency | pass | Assumptions, equation and bounds agree; the shear-free assumption is the first to fail and the one the bound names. |
| Representational Adequacy | qualified | Blind to shear, large displacement and local instability — each recorded as a named bound. |
| Purpose Adequacy | pass | Every leaf serves the load → deflection and load → moment conversion the principle exists for. |

## References

- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) (evaluation criteria)
- [Structural Mechanics](/view.html?p=notes/technica/discipline/structural-mechanics.md) — the practice this principle governs the members of
- [Stability Analysis](/view.html?p=notes/technica/discipline/stability-analysis.md) — the technique that uses the member stiffness this principle defines
- [Structure](/view.html?p=notes/nature/physical-object/structure.md) — the natural reading of the body the member belongs to
- https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory
- Timoshenko, S. P. "History of Strength of Materials" (1953), ch. on Euler and Bernoulli.
- Gere, J. M., and Timoshenko, S. P. *Mechanics of Materials*. PWS.
