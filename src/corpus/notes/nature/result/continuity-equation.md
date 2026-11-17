---
tags: [note, nature, epistemica, construction]
qa:
 - The equation says the quantity is conserved. Where in it is the claim that the quantity exists?
 - What does it add beyond "what enters minus what leaves equals what accumulates"? Is it a law or a bookkeeping convention?
 - Charge conservation, mass conservation and probability conservation have the same form. Are they the same statement or three?
 - The flux must be supplied by a constitutive law before anything can be computed. Is the equation therefore empty without a second model — and does that make it a schema rather than a model?
 - At a shock the derivatives do not exist. Is the differential form wrong there, or is the integral form the real equation?
 - The corpus already has a note called "continuity" in the mathematical corpus. Is that the same word doing a different job?
---

# Continuity Equation

> The **continuity equation** is the local statement of conservation: the rate at which a quantity accumulates in a region equals the flux through its boundary, so in differential form $\partial_{t}\rho + \nabla\cdot\mathbf{j} = 0$. It is the most widely reused equation in the corpus and the least informative on its own — mass in a fluid, charge in a conductor, probability in quantum mechanics, species in a reaction, vehicles on a road. Read per [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md).

> Its epistemic character is unusual among the equations on this shelf: **it is exact, universally applicable, and nearly empty.** Nothing follows from it until the flux is written as a function of the state, and that second statement — the constitutive law — is where the physics, and the failures, live. It is therefore the clearest case of an equation that is a *schema*: a form waiting for a closure that it does not contain.

## Formulation

### What is this epistemic instance?

**The continuity equation** for a conserved density $\rho$ with flux $\mathbf{j}$:

\[
\frac{\partial \rho}{\partial t} + \nabla\cdot\mathbf{j} = 0
\qquad\left(\text{or}\qquad
\frac{\partial \rho}{\partial t} + \nabla\cdot\mathbf{j} = \sigma
\right)
\]

with the source term $\sigma$ where the quantity is not conserved, and with the four canonical readings

\[
\partial_{t}\rho + \nabla\cdot(\rho\mathbf{u}) = 0
\ \ \text{(mass)},\qquad
\partial_{t}\rho_{q} + \nabla\cdot\mathbf{J} = 0
\ \ \text{(charge)},
\]

\[
\partial_{t}P + \nabla\cdot\mathbf{j}_{\psi} = 0
\ \ \text{(probability)},\qquad
\partial_{t}c_{i} + \nabla\cdot\mathbf{N}_{i} = R_{i}
\ \ \text{(species)}.
\]

What is **in**: the conserved density; the flux; the divergence that binds them; the integral form, which survives where the differential form does not; the source term that generalises it to a balance law; the constitutive relations that close it — Fourier, Fick, Darcy, Ohm, the probability current, the Euler and Navier–Stokes momentum fluxes; and the jump conditions at discontinuities.

What is **out**: the physics that makes the quantity conserved — Noether's theorem, the gauge symmetry behind charge conservation, the particle number behind mass conservation; the constitutive relations themselves, which are separate models; the momentum and energy balances, which are different equations with a similar form; and the topological notion of continuity, which is an unrelated homonym.

### What epistemic element type does this epistemic instance belong to?

**`Epistemic Construction`**, kind **`Model`** — a construction enabling prediction or explanation of the segment. It is a *result*, and it is the thinnest one on the shelf: an identity about a conserved quantity, true of any system that has one. It is **not** a `Theory`: it posits no constructs and asserts no mechanism. It is **not** a conservation *law* in the same sense as the conservation of energy, which is a claim about nature: the continuity equation is a claim about **bookkeeping**, and the conservation itself is the premise it takes for granted.

Its standing is `Validated` wherever a conserved quantity exists, which is everywhere in continuum physics — and it is `Empty` as a predictor, because it determines the evolution of $\rho$ only once $\mathbf{j}$ is given.

### Is the type of this `epistemic element instance` ambiguous?

**Yes, in three ways.**

First, the four readings are different physical quantities and the same form. What differs is the closure: mass flow needs a velocity field or a pressure gradient, charge flow needs Ohm's law or a plasma response, probability flow needs the wave function, species flow needs a reaction network. The equation is one; the models built on it are four.

Second, the **differential form and the integral form are not interchangeable in practice**. The differential form presupposes differentiability, which fails at shocks, interfaces and moving boundaries; the integral form is the real statement and survives there, which is why shock-capturing schemes discretise it and why the Rankine–Hugoniot conditions are derived from it. An equation whose two forms have different domains of validity is a fact about the element, not a technicality.

Third, the word is a **homonym inside this corpus**: `mathematical/change/continuity.md` is about the continuity of a function — a topological property — and has nothing to do with this equation. The name attaches to a shared Latin root, not to a shared content, and the corpus keeps them apart by typing.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: one model, decomposed to the parts it is assembled from, the concepts it turns on, the segments it represents, the standards that license it, the checks that test it, the constraints that bound it and the notation it is written in — not to the fluids, fields and populations it represents, which are typed where they live.
>
> Identity: every Instance Tree Path is a valid prefix of the tree, each non-root row extends an existing path by exactly one labelled link, grouping types are `` `code` ``, instances are Title Case, and no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` Continuity Equation | The local statement of conservation: accumulation equals negative divergence of flux, for any quantity that is conserved. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` | Grouping: the constituent models the law is assembled from. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Conserved Density | $\rho$: the quantity per unit volume. It is the equation's only unknown, and the equation's premise is that it exists as a field. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Flux | $\mathbf{j}$: the quantity crossing unit area per unit time. The term that must be closed by another model before the equation can be solved. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Divergence Balance | $\nabla\cdot\mathbf{j}$: what leaves a point. The whole content of the equation is the identity between this and the local rate of change. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Source Term | $\sigma$: creation or destruction of the quantity by a process outside the flux — a reaction, a radioactive decay, a current injected into a node. The generalised balance law. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Integral Form | $\frac{d}{dt}\int_{V}\rho\,dV = -\oint_{\partial V}\mathbf{j}\cdot d\mathbf{S}$: the statement that survives at discontinuities, and the one the finite-volume discretisation implements. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Constitutive Closure | The relation that writes the flux as a function of the state — Fourier's law, Fick's law, Darcy's law, Ohm's law, the Schrödinger current. The step that turns this equation into a model of something. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Model` `(→ Instance)` Jump Conditions | The Rankine–Hugoniot relations: what the integral form supplies across a shock, where the differential form has no meaning. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Concept` | Grouping: the discriminators the law turns on. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Concept` `(→ Instance)` Conservation Premise | The assumption that the quantity is neither created nor destroyed within the region. Everything the equation says is conditional on it, and it is a premise rather than a result. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Concept` `(→ Instance)` Control Volume | The region over which the balance is stated. The equation is local, but its justification is always an accounting over a volume. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Concept` `(→ Instance)` Flux–Gradient Relation | The empirical law linking flux to gradient. It is where a material property enters, and where the equation acquires its physical content. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Concept` `(→ Instance)` Weak Solution | The generalised solution admitted where derivatives do not exist. It is what makes the equation applicable to the phenomena, which are not smooth. |
| `Model` `(→ Instance)` Continuity Equation `(→ Part)` `Concept` `(→ Instance)` Homonymy | The same word naming a topological property of a function. The discriminator that keeps this note apart from the mathematical one. |
| `Model` `(→ Instance)` Continuity Equation `(→ Represents)` `Segment of Reality` | Grouping: the readings, one per quantity, all of the same form. |
| `Segment of Reality` `(→ Instance)` Fluid Mass | $\partial_{t}\rho + \nabla\cdot(\rho\mathbf{u}) = 0$: the mass balance of a moving fluid, the reading Euler wrote and every hydrodynamic model inherits. |
| `Segment of Reality` `(→ Instance)` Electric Charge | $\partial_{t}\rho_{q} + \nabla\cdot\mathbf{J} = 0$: the charge balance that Maxwell's displacement current was introduced to preserve. |
| `Segment of Reality` `(→ Instance)` Quantum Probability | $\partial_{t}\lvert\psi\rvert^{2} + \nabla\cdot\mathbf{j}_{\psi} = 0$: the conservation of probability, exact for any solution of the Schrödinger equation. |
| `Segment of Reality` `(→ Instance)` Chemical Species | $\partial_{t}c_{i} + \nabla\cdot\mathbf{N}_{i} = R_{i}$: a species balance with reaction sources — the form every reactor and transport-reaction model is written in. |
| `Segment of Reality` `(→ Instance)` Traffic and Queues | $\partial_{t}\rho + \partial_{x}(\rho u(\rho)) = 0$: vehicles or items conserved along a one-dimensional path, the reading in which the flux is a function of density alone. |
| `Model` `(→ Instance)` Continuity Equation `(→ Governed By)` `Epistemic Standard` | Grouping: the conditions the law must satisfy to be stated at all. |
| `Model` `(→ Instance)` Continuity Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Existence of a Conserved Quantity | There is a quantity with a density and a flux. Without it the equation has no subject and reduces to an identity in zero. |
| `Model` `(→ Instance)` Continuity Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Differentiability | For the differential form, the fields must be smooth enough for the divergence to exist. The integral form relaxes this and is the primary statement. |
| `Model` `(→ Instance)` Continuity Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Local Equilibrium | The flux responds to the local state rather than to history, which is what makes a constitutive relation possible at all. |
| `Model` `(→ Instance)` Continuity Equation `(→ Evaluated By)` `Validation` | Grouping: the checks that discharge doubt about the law. |
| `Model` `(→ Instance)` Continuity Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Control-Volume Mass Balance | What enters a vessel minus what leaves equals what accumulates, over every time scale tested. The measurement is an accounting, and the equation is the accounting's differential form. |
| `Model` `(→ Instance)` Continuity Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Charge Conservation Test | Current into a node equals current out, at every frequency and in every circuit — the reading in which the equation is exact and independently measurable. |
| `Model` `(→ Instance)` Continuity Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Probability Normalisation | The norm of a quantum state is preserved by its evolution, which is this equation written for $\lvert\psi\rvert^{2}$. |
| `Model` `(→ Instance)` Continuity Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Conservative Numerical Scheme | A discretisation that conserves the total to machine precision reproduces the analytic balance where a non-conservative one drifts. |
| `Model` `(→ Instance)` Continuity Equation `(→ Has)` `Epistemic Constraint` | Grouping: the limits the law carries inside itself. |
| `Model` `(→ Instance)` Continuity Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Predictive Emptiness | The equation does not determine $\rho$ until the flux is closed. It constrains a model; it is not one, and reading it as one produces the illusion of a law that explains nothing. |
| `Model` `(→ Instance)` Continuity Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Discontinuity Failure | Where the field jumps, the differential form is undefined and only the integral form with its jump conditions applies. Shocks are the standing case. |
| `Model` `(→ Instance)` Continuity Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Non-Local Flux Breakdown | Where the flux depends on the state elsewhere — non-Fickian diffusion, memory effects, anomalous transport — a local closure is false and the equation must be replaced by an integro-differential form. |
| `Model` `(→ Instance)` Continuity Equation `(→ Has)` `(→ Instance)` Conservation-Regime Dependence | Where the quantity is created or destroyed, the source term carries the physics and the equation says nothing about it — the form is preserved and the content is entirely in $\sigma$. |
| `Model` `(→ Instance)` Continuity Equation `(→ Has)` `Representational System` `(→ Instance)` Divergence-Form Notation | $\partial_{t}\rho + \nabla\cdot\mathbf{j} = 0$: a single first-order conservation law, written in the divergence form that numerical schemes and weak formulations both read directly. |

### What is a critical conceptual evaluation of this epistemic instance?

The concept under evaluation is **the continuity equation**, precised as *the local differential statement that a conserved density changes only by the divergence of its flux*. Its verdicts: conceptually identified against the conservation laws that justify it and against the constitutive models that complete it, defined precisely enough to be integrated, internally consistent — the integral and differential forms agree wherever both exist — fully determinate as an identity and indeterminate as a predictor, representationally adequate to the balance and empty about the transport, and adequate for its purpose as the skeleton every transport model is built on while being worthless if read as a complete law. The gap is the one the note exists to name: **the conservation is the premise and the closure is the physics, and the equation shows neither as such.**

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Strong | Held apart from the conservation law that grounds it, from the constitutive relation that closes it, from the momentum and energy balances that share its form, and from the topological homonym `continuity` in the mathematical corpus. |
| Definitional Clarity | Strong | Density, flux, divergence, source, integral form and jump conditions are all stated, and the boundary between the equation and its closure is drawn explicitly rather than assumed. |
| Conceptual Determinacy | Complete as an identity, empty as a model | Given $\rho$ and $\mathbf{j}$, the equation is either satisfied or violated; given only $\rho$, it constrains $\mathbf{j}$ and nothing else. Determinacy arrives with the constitutive law, never with the equation. |
| Internal Consistency | Strong | The differential and integral forms are the same statement under the divergence theorem; the jump conditions are its weak form; the source term generalises without changing the structure. |
| Representational Adequacy | Exact for the balance, silent about the transport | Every conservation check ever performed is an instance of it. No transport process is represented by it, so no transport can be misrepresented — the adequacy is entirely inherited from the closure. |
| Purpose Adequacy | Adequate as a schema, inadequate as a law | For "what balance must any transport model satisfy", it is the right element and no alternative exists. For "how does this quantity move", it answers by deferring, and treating the deferral as an explanation is the error it invites. |

## References

- [Philosophia Conceptuum et Operis](/view.html?p=notes/philosophia-conceptuum-et-operis.md) — the evaluation criteria applied above
- [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Naturalis et Operis](/view.html?p=notes/philosophia-naturalis-et-operis.md)
- [Continuity equation — Wikipedia](https://en.wikipedia.org/wiki/Continuity_equation)
- Euler, L. (1757). Principes généraux du mouvement des fluides. *Mémoires de l'Académie Royale des Sciences et Belles-Lettres de Berlin*, 11, 274–315. — the mass balance, written for fluids
- Batchelor, G. K. (1967). *An introduction to fluid dynamics*. Cambridge University Press. — the control-volume derivation and its role in the equations of motion
- Landau, L. D., & Lifshitz, E. M. (1987). *Fluid mechanics* (2nd ed.). Pergamon. — the integral form, and the conditions under which the differential form fails
- Jackson, J. D. (1999). *Classical electrodynamics* (3rd ed.). Wiley. — the charge reading, and the displacement current that preserves it
- Truesdell, C., & Toupin, R. (1960). The classical field theories. In S. Flügge (Ed.), *Handbuch der Physik* (Vol. III/1). Springer. — the general balance law, of which every reading is a case
- [Equation](/view.html?p=notes/nature/result/equation.md) — the shelf master: the bookkeeping mode of transfer
- [Poisson Equation](/view.html?p=notes/nature/result/poisson-equation.md) — the definitional mode, where the form defines its own field
- [Vlasov Equation](/view.html?p=notes/nature/result/vlasov-equation.md) · [Boltzmann Equation](/view.html?p=notes/nature/result/boltzmann-equation.md) — transport equations whose left-hand side is this balance and whose content is the closure
- [Jeans Equations](/view.html?p=notes/nature/result/jeans-equations.md) — the zeroth moment, which is this equation for a collisionless system
