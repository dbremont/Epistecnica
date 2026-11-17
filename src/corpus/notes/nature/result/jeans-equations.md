---
tags: [note, nature, epistemica, construction]
qa:
 - Four equations, ten unknowns. Is the Jeans system a model or the first four lines of an argument that never closes?
 - The mass inferred from stellar motions depends on the anisotropy assumed. How much of the dark-matter result is measurement and how much is the closure?
 - The same moment-taking gives Euler from Boltzmann. Why does that derivation count as a reduction and this one as an inference?
 - Jeans wrote these for star-streaming in 1915. Are they the equations of a galaxy, or the equations of any collisionless system whose tracers we can see?
 - If the second moment is unobservable along the line of sight, what exactly is being measured when a dispersion is reported?
---

# Jeans Equations

> The **Jeans equations** are the velocity moments of the collisionless kinetic equation: the continuity equation and the momentum equation for a stellar system, obtained by integrating the [Vlasov equation](/view.html?p=notes/nature/result/vlasov-equation.md) over velocity. They are the stellar-dynamics counterpart of the Euler equations, produced by exactly the same moment-taking — and they differ from Euler in one decisive respect: **the pressure is a tensor nobody can measure, and the system does not close.** Read per [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md).

> That is the whole epistemic content. The equations are exact consequences of the kinetic description; the *inference* from them to a mass distribution is not, because it requires an anisotropy that the data do not supply and the equations do not determine. Jeans modelling is therefore a family of models indexed by an assumption, and the reported mass is a function of that assumption as much as of the observation.

## Formulation

### What is this epistemic instance?

**The Jeans equations** for a collisionless system with distribution $f(\mathbf{x},\mathbf{v},t)$, density $\rho = m\!\int f\,d^{3}v$ and mean velocity $\bar{v}_{i} = \langle v_{i}\rangle$:

\[
\frac{\partial \rho}{\partial t} + \frac{\partial}{\partial x_{i}}\left(\rho\,\bar{v}_{i}\right) = 0,
\]

\[
\frac{\partial}{\partial t}\left(\rho\,\bar{v}_{j}\right)
+ \frac{\partial}{\partial x_{i}}\left(\rho\,\bar{v}_{i}\bar{v}_{j}\right)
= -\rho\,\frac{\partial \Phi}{\partial x_{j}}
- \frac{\partial}{\partial x_{i}}\left(\rho\,\sigma^{2}_{ij}\right),
\qquad
\sigma^{2}_{ij} = \langle v_{i}v_{j}\rangle - \bar{v}_{i}\bar{v}_{j},
\]

with the potential $\Phi$ from the [Poisson equation](/view.html?p=notes/nature/result/poisson-equation.md) and, in the steady spherical case that is actually used,

\[
\frac{d}{dr}\left(\rho\,\sigma_{r}^{2}\right)
+ \frac{2}{r}\,\rho\left(\sigma_{r}^{2} - \sigma_{t}^{2}\right)
= -\rho\,\frac{G\,M(r)}{r^{2}}.
\]

What is **in**: the density and the mean-velocity field; the velocity-dispersion tensor as the pressure analogue; the potential as the source of the force; the steady-state and symmetry assumptions that reduce the system to something solvable; the anisotropy parameter that parametrises the closure; and the mass profile as the quantity inferred.

What is **out**: the distribution function itself, which is the kinetic object the moments are taken from and which the moments do not determine; the higher moments, which the next equation in the hierarchy would need; the **virial theorem**, which is a scalar consequence rather than a member of the system; and the N-body and Schwarzschild practices that solve the inference numerically.

### What epistemic element type does this epistemic instance belong to?

**`Epistemic Construction`**, kind **`Model`** — a construction enabling prediction or explanation of the segment. It is a *result*, and specifically an **inference scheme**: a set of exact equations plus a parametrised closure, used to convert a projected observable into a mass. It is **not** a `Theory`: it carries no constructs beyond the distribution function and its moments. It is **not** a closed model in the sense Euler is: the closure is supplied by the analyst, not by the physics.

Its standing is `Conditionally valid`: the equations are exact, the inference is only as good as the anisotropy assumption, and the corpus's own record shows both — mass profiles that agree with independent tracers, and mass profiles that moved by factors when the assumption changed.

### Is the type of this `epistemic element instance` ambiguous?

**Yes, and the ambiguity is the point.**

First, the name covers **the equations** and **the modelling technique**. The equations are four exact moment identities. "Jeans modelling" is the practice of solving them under an assumed anisotropy to recover $M(r)$ — a technique, typed on the technical side, that cites these equations. The note is about the former; the practice is cited.

Second, the equations are **the same moment-taking that produces Euler from Boltzmann**. In a collisional fluid the second moment closes because collisions restore local isotropy and the stress is a function of the thermodynamic state; in a collisionless system nothing restores it, so the ten unknowns (density, three mean velocities, six dispersions) outnumber the four equations and the hierarchy does not terminate. That is not a defect of the derivation — it is the difference between a fluid and a collisionless system, expressed in the only place it can be expressed.

Third, the **inference is underdetermined in a way that has produced a physical discovery and a methodological scandal at once**: the mass that the equations require to hold a cluster together exceeds the luminous mass, which is the historical route to dark matter; and the same equations, with a different anisotropy, return a different mass. The equations did not discover dark matter — the *assumption that the system is in a steady state with modest anisotropy* did, and the assumption has been defended ever since by independent evidence.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: one model, decomposed to the parts it is assembled from, the concepts it turns on, the segment it represents, the standards that license it, the checks that test it, the constraints that bound it and the notation it is written in — not to the galaxy's own structure, which belongs to the natural target and is typed there.
>
> Identity: every Instance Tree Path is a valid prefix of the tree, each non-root row extends an existing path by exactly one labelled link, grouping types are `` `code` ``, instances are Title Case, and no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` Jeans Equations | The velocity moments of the collisionless kinetic equation: continuity plus momentum, with a stress tensor that is not determined by them. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` | Grouping: the constituent models the law is assembled from. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` `(→ Instance)` Continuity Moment | The zeroth moment: density and mean velocity satisfy the conservation of mass. It is identical in form to the [continuity equation](/view.html?p=notes/nature/result/continuity-equation.md) of a fluid. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` `(→ Instance)` Momentum Moment | The first moment: the mean velocity is accelerated by the potential and decelerated by the divergence of the dispersion tensor. The pressure gradient's collisionless replacement. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` `(→ Instance)` Velocity-Dispersion Tensor | $\sigma^{2}_{ij}$: the second moment minus the mean's outer product. The pressure analogue, and the object that cannot be measured along the line of sight. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` `(→ Instance)` Anisotropy Parameter | $\beta = 1 - \sigma_{t}^{2}/\sigma_{r}^{2}$: the single number that stands in for the missing closure. Every mass inferred from these equations is a function of it. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` `(→ Instance)` Spherical Steady Reduction | The one-dimensional form actually used: steady state, spherical symmetry, no rotation. It is an assumption about the target, and it is what makes the system solvable at all. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Model` `(→ Instance)` Mass Inversion | $M(r)$ obtained from the dispersion profile and the deprojected density. The output of the modelling, and the reason the equations are used. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `(→ Instance)` Higher-Moment Hierarchy | The next equation, for the third moment, which would be needed to close the second. It is never written in practice, and its absence is the closure problem stated formally. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Concept` | Grouping: the discriminators the law turns on. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Concept` `(→ Instance)` Moment Closure | The requirement that the $n$-th moment equation be closed by an assumption about the $(n+1)$-th. In a fluid, thermodynamics closes it; here nothing does. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Concept` `(→ Instance)` Velocity Anisotropy | The radial-to-tangential dispersion ratio. It is a property of the system, unobservable from a projected line-of-sight dispersion, and it is the free parameter of the inference. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Concept` `(→ Instance)` Line-of-Sight Projection | The observable dispersion is an integral of the intrinsic tensor along the line of sight, weighted by surface brightness. What is measured is not any component of $\sigma^{2}_{ij}$ but a convolution of them. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Concept` `(→ Instance)` Tracer Population | The stars or globular clusters whose motions are measured. The equations describe them; the mass they respond to includes everything else, which is what makes the inference a mass measurement rather than a kinematic description. |
| `Model` `(→ Instance)` Jeans Equations `(→ Part)` `Concept` `(→ Instance)` Mass-to-Light Ratio | The ratio the inference delivers. Its excess over the stellar value is the observational statement of missing mass, and it is exactly as uncertain as the anisotropy. |
| `Model` `(→ Instance)` Jeans Equations `(→ Represents)` `Segment of Reality` | Grouping: the target the law represents. |
| `Segment of Reality` `(→ Instance)` Stellar System | A gravitationally bound system of stars in a steady state: the natural target, the same one the [Vlasov equation](/view.html?p=notes/nature/result/vlasov-equation.md) represents, read here through its lowest moments. Cited, not decomposed here. |
| `Model` `(→ Instance)` Jeans Equations `(→ Governed By)` `Epistemic Standard` | Grouping: the conditions the law must satisfy to be stated at all. |
| `Model` `(→ Instance)` Jeans Equations `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Collisionlessness | The same standard as the kinetic equation: the relaxation time far exceeds the age of the system. Remove it and the fluid closure becomes available and the Euler equations apply instead. |
| `Model` `(→ Instance)` Jeans Equations `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Steady State | The system is in equilibrium over the observation time. Remove it and the time-dependent moments are needed, which no observation supplies. |
| `Model` `(→ Instance)` Jeans Equations `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Symmetry Assumption | Spherical, axisymmetric or triaxial, chosen to match the target. The assumption is what decides how many of the moment equations are independent. |
| `Model` `(→ Instance)` Jeans Equations `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Assumed Anisotropy | A functional form for $\beta(r)$, adopted rather than measured. It is not a property of the equations, and it is the standard the inference actually depends on. |
| `Model` `(→ Instance)` Jeans Equations `(→ Evaluated By)` `Validation` | Grouping: the checks that discharge doubt about the inference. |
| `Model` `(→ Instance)` Jeans Equations `(→ Evaluated By)` `Validation` `(→ Instance)` Independent Tracer Agreement | Masses inferred from different tracers — stars, globular clusters, planetary nebulae, X-ray gas — agree where the assumptions are independently justified. |
| `Model` `(→ Instance)` Jeans Equations `(→ Evaluated By)` `Validation` `(→ Instance)` Stellar-Dynamical versus Lensing Mass | Lensing measures mass without assuming anisotropy. Agreement with the Jeans inference is the strongest available check, and disagreement is how the assumption is caught. |
| `Model` `(→ Instance)` Jeans Equations `(→ Evaluated By)` `Validation` `(→ Instance)` N-Body and Schwarzschild Modelling | Direct integration of the collisionless system, and orbit-superposition modelling, reproduce the same dispersion profiles without the Jeans closure — evidence about the closure rather than the equations. |
| `Model` `(→ Instance)` Jeans Equations `(→ Has)` `Epistemic Constraint` | Grouping: the limits the law carries inside itself. |
| `Model` `(→ Instance)` Jeans Equations `(→ Has)` `Epistemic Constraint` `(→ Instance)` Closure Indeterminacy | Four equations, ten unknowns. The system does not close, and no observation supplies the missing six components; the closure is a choice, and the mass is a function of it. |
| `Model` `(→ Instance)` Jeans Equations `(→ Has)` `Epistemic Constraint` `(→ Instance)` Projection Degeneracy | Only line-of-sight integrated quantities are observable, so a mass–anisotropy degeneracy is structural rather than incidental: different pairs give the same data. |
| `Model` `(→ Instance)` Jeans Equations `(→ Has)` `Epistemic Constraint` `(→ Instance)` Steady-State Assumption | The equations describe equilibrium. A system observed mid-merger, or with a live bar or spiral, violates the premise, and the inferred mass is not the mass of anything. |
| `Model` `(→ Instance)` Jeans Equations `(→ Has)` `Epistemic Constraint` `(→ Instance)` Tracer–Mass Separation | The equations constrain the tracers' kinematics, not the potential directly. Converting one into the other assumes the tracers sample the potential and that no unseen component moves differently. |
| `Model` `(→ Instance)` Jeans Equations `(→ Has)` `Representational System` `(→ Instance)` Moment-Equation Notation | A system of first-order partial differential equations in the moments, written in the same notation as fluid dynamics and therefore inviting the fluid reading that the collisionless case does not license. |

### What is a critical conceptual evaluation of this epistemic instance?

The concept under evaluation is **the Jeans equations**, precised as *the exact velocity moments of the collisionless kinetic equation, used under an assumed anisotropy to infer a mass distribution*. Its verdicts: conceptually identified against the kinetic equation they descend from and against the Euler equations they resemble, defined precisely enough to state the closure problem explicitly, internally consistent as moment identities, indeterminate as an inference — the mass is a function of a free function — representationally adequate to the kinematics of the tracers and not to the mass, and adequate for its purpose only when an independent check pins the anisotropy. The gap is the classic one: **the equations are exact and the inference is not, and the notation does not distinguish them.**

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Strong | Held apart from the [Vlasov equation](/view.html?p=notes/nature/result/vlasov-equation.md) (the kinetic object), from the Euler equations (the collisional closure of the same moment-taking), from the virial theorem (a scalar consequence), and from Jeans modelling (the practice that solves them). |
| Definitional Clarity | Strong | The moments, the dispersion tensor, the anisotropy parameter, the spherical reduction and the inversion step are all stated. The closure is named as an assumption rather than presented as a derived term. |
| Conceptual Determinacy | Weak as an inference, complete as identities | The moment equations determine the divergence of the stress from the density and the potential, and nothing more. The mass is determined only once $\beta(r)$ is fixed, and $\beta$ is not determined by anything the equations contain. |
| Internal Consistency | Strong | The moments are exact consequences of the kinetic equation; the hierarchy's failure to close is a property of the system, not an error in the derivation. Nothing in the system contradicts another row. |
| Representational Adequacy | High for kinematics, conditional for mass | Projected dispersions are reproduced to measurement accuracy for a given anisotropy. The mass is represented only up to the degeneracy, and the degeneracy is not visible in the notation. |
| Purpose Adequacy | Adequate when cross-checked, misleading when not | For "what mass is required to hold this system with this anisotropy", it is the right tool and the only tractable one. For "what is the mass", it answers a question the equations cannot pose, and the answer's uncertainty is methodological rather than statistical. |

## References

- [Philosophia Conceptuum et Operis](/view.html?p=notes/philosophia-conceptuum-et-operis.md) — the evaluation criteria applied above
- [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Naturalis et Operis](/view.html?p=notes/philosophia-naturalis-et-operis.md)
- [Jeans equations — Wikipedia](https://en.wikipedia.org/wiki/Jeans_equations)
- Jeans, J. H. (1915). On the theory of star-streaming and the structure of the universe. *Monthly Notices of the Royal Astronomical Society*, 76(2), 70–84. — the moment equations, written for star-streaming
- Binney, J., & Tremaine, S. (2008). *Galactic dynamics* (2nd ed.). Princeton University Press. — the moment hierarchy, the closure problem and the anisotropy degeneracy
- Mo, H., van den Bosch, F. C., & White, S. D. M. (2010). *Galaxy formation and evolution*. Cambridge University Press. — the mass-inference practice and its systematics
- Zwicky, F. (1933). Die Rotverschiebung von extragalaktischen Nebeln. *Helvetica Physica Acta*, 6, 110–127. — the first mass discrepancy, obtained from the virial theorem rather than from these equations
- Ferrarese, L., & Merritt, D. (2000). A fundamental relation between supermassive black holes and their host galaxies. *The Astrophysical Journal*, 539(1), L9–L12. — the dispersion-based scaling relation these equations underwrite
- [Equation](/view.html?p=notes/nature/result/equation.md) — the shelf master: the moment mode of transfer
- [Vlasov Equation](/view.html?p=notes/nature/result/vlasov-equation.md) — the kinetic equation whose moments these are
- [Boltzmann Equation](/view.html?p=notes/nature/result/boltzmann-equation.md) — the same moment-taking, with a closure that terminates
- [Continuity Equation](/view.html?p=notes/nature/result/continuity-equation.md) — the zeroth moment, shared with every fluid
- [Poisson Equation](/view.html?p=notes/nature/result/poisson-equation.md) — the field equation that supplies the force
