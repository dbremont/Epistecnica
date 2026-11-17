---
tags: [note, nature, epistemica, construction]
qa:
 - Is the irreversibility of the equation derived or inserted? Molecular chaos buys the arrow of time with an assumption about correlations, and the assumption is not a consequence of mechanics.
 - Which is the real content of the H-theorem — a statement about a gas, or a statement about the closure that was chosen to describe it?
 - The Chapman–Enskog expansion recovers Navier–Stokes at first order, so where does the hydrodynamic description stop being a limit of this equation and start being an independent model?
 - Is the Boltzmann equation a reduction of mechanics or an independent law? It does not follow from the N-particle dynamics without truncation, and it cannot be derived from thermodynamics at all.
 - Which of the equation's failures are its own and which belong to the closure — dense fluids, plasmas, quantum gases, long-time tails?
 - Boltzmann's name now sits on an equation, a constant, an equilibrium distribution and a machine. Which of these is the element this note is about?
---

# Boltzmann Equation

> A **construction about a natural target**: a dilute gas — many particles whose individual trajectories are beyond tracking — is observer-independent reality, and the Boltzmann equation is the law built to describe it: the evolution equation for the one-particle distribution $f(\mathbf{r}, \mathbf{v}, t)$, closed by a collision term that assumes the particles entering a collision are uncorrelated. The note is filed under `nature/` for navigability; its typing follows the epistemic grammar, and its natural target is cited, never decomposed here. Worked per [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md); the gas itself belongs to [Philosophia Naturalis et Operis](/view.html?p=notes/philosophia-naturalis-et-operis.md).

> Note: the equation is a **closure**, not a reduction. It does not follow from the mechanics of $N$ particles — it follows from that mechanics *plus* the assumption that pairs of particles about to collide are statistically independent, and that assumption is the whole difficulty: it is what makes the equation solvable, what makes it irreversible, and what its critics have attacked since 1876.

> It is one member of a hierarchy, and the note is easier to read beside its relatives: the [Liouville equation](/view.html?p=notes/nature/result/liouville-equation.md) is the exact equation it truncates, the [Vlasov equation](/view.html?p=notes/nature/result/vlasov-equation.md) is what remains when the collision term is deleted, and the [Jeans equations](/view.html?p=notes/nature/result/jeans-equations.md) are its velocity moments in the collisionless case. The shelf master, [Equation](/view.html?p=notes/nature/result/equation.md), states why the form travels and the closure does not.

## Formulation

### What is this epistemic instance?

**The Boltzmann equation**: the transport equation for the single-particle distribution function of a dilute gas,

\[
\frac{\partial f}{\partial t}
\;+\; \mathbf{v}\cdot\nabla_{\mathbf{r}} f
\;+\; \frac{\mathbf{F}}{m}\cdot\nabla_{\mathbf{v}} f
\;=\; \left(\frac{\partial f}{\partial t}\right)_{\mathrm{coll}}
\;=\; Q(f,f),
\]

where $f(\mathbf{r},\mathbf{v},t)\,d^{3}r\,d^{3}v$ is the expected number of particles in the phase-space volume $d^3r\,d^3v$ about $(\mathbf{r},\mathbf{v})$ at time $t$, and the collision integral

\[
Q(f,f) = \int \Big[ f(\mathbf{v}') f(\mathbf{v}_1') - f(\mathbf{v}) f(\mathbf{v}_1) \Big]\,
\lvert \mathbf{v} - \mathbf{v}_1 \rvert\, \sigma(\Omega)\, d\Omega\, d^{3}v_1
\]

is bilinear in $f$: the gain term counts collisions into the velocity pair, the loss term collisions out of it, and $\sigma$ is the differential cross-section of the molecular interaction.

What is **in**: the distribution function as the unknown; the streaming operator, split into free flight and the action of an external force; the collision integral with its cross-section; the **molecular-chaos** assumption that lets the two-particle distribution be written as a product of one-particle ones and so closes the equation on $f$ alone; the **H-functional** $H = \int f \ln f\, d^{3}v$ and its monotone decrease; the **Maxwell–Boltzmann distribution** as the unique equilibrium the H-theorem singles out; the **Chapman–Enskog expansion** that carries the equation to the hydrodynamic limit; the transport coefficients — viscosity, thermal conductivity, diffusion — that the expansion produces; and the conservation laws that follow by taking moments of the collision integral rather than being added to it.

What is **out**: the gas itself, which is the natural target — a segment of reality that would carry the same particles and collisions unobserved; [kinetic theory](/view.html?p=notes/epistemica/singular/kinetic-theory.md) as a `Theory`, which owns the distribution-function ontology and the probabilistic interpretation of $f$; [entropy](/view.html?p=notes/nature/property/entropy.md) and [thermodynamics](/view.html?p=notes/nature/thermodynamics.md), which are concept and theory notes on the thermodynamic side, cited rather than restated; the [lattice-Boltzmann method](/view.html?p=notes/epistemica/singular/lattice-boltzmann-method-lbm.md), which is a technical practice that *discretizes* this equation on a lattice and solves it; the numerical solvers; and the other elements that share the name — the [Boltzmann constant](/view.html?p=notes/nature/boltzmann-constant.md), a conversion factor between temperature and energy; the [Stefan–Boltzmann constant](/view.html?p=notes/nature/stefan-boltzmann-constant.md), which belongs to radiation; and the [Boltzmann machine](/view.html?p=notes/technica/cybernetics/architecture/boltzmann-machine.md), a technical architecture named after the equilibrium distribution. No row below carries two types.

### What epistemic element type does this epistemic instance belong to?

**`Epistemic Construction`**, kind **`Model`** — a construction enabling prediction or explanation of the segment. It is a *result*: a law of evolution obtained by truncating the hierarchy of $N$-particle distributions, not a report of an observation and not the theory that carries it. It is **not** a `Description`: its content is an assertion about the future distribution of an unobserved gas, not a structured affirmation of what was seen. It is **not** a `Theory`: it posits no constructs of its own beyond the distribution function that kinetic theory supplies, and it carries no interpretation of probability — that argument belongs to the theory. Its standing is `Validated` inside the dilute-gas regime, where its transport coefficients agree with measurement and where its hydrodynamic limit reproduces the known equations of fluid motion, and it is silent outside it: dense fluids, plasmas, degenerate gases and asymptotically long times each lie beyond the assumptions that close it.

### Is the type of this `epistemic element instance` ambiguous?

**Yes, in three ways, and each is resolved rather than merged.**

First, the name covers three different elements: the **equation** (the law, documented here), the **phenomenon** — the irreversible approach to equilibrium and the transport it produces, which is a behaviour of a many-particle system and belongs to the naturalis reading, not to this note — and the **equilibrium solution**, the Maxwell–Boltzmann distribution, which is a part of this construction and a concept in its own right. Only the equation is the root.

Second, the same mathematical object sits on the technical side. The [lattice-Boltzmann method](/view.html?p=notes/epistemica/singular/lattice-boltzmann-method-lbm.md) and [its counterparts](/view.html?p=notes/epistemica/singular/lattice-boltzmann-method.md) are *practices*: they discretize velocity space onto a lattice and integrate the equation as a simulation scheme. They are typed by the technica grammar, they cite this equation, and none of them is it. The same holds for direct-simulation Monte Carlo, which samples the collision integral instead of solving it.

Third, the name has detached from the element altogether. **Boltzmann** now qualifies a constant, a distribution, a radiation law, a machine-learning architecture and a transport equation, and the corpus holds notes for four of them. They are not variants of one thing: the [constant](/view.html?p=notes/nature/boltzmann-constant.md) is a unit conversion, the [Stefan–Boltzmann constant](/view.html?p=notes/nature/stefan-boltzmann-constant.md) belongs to radiative transfer, the equilibrium distribution is a solution, and the [machine](/view.html?p=notes/technica/cybernetics/architecture/boltzmann-machine.md) is a technical object. Type, not the surname, tells them apart.

The attribution needs the same care. **Maxwell** (1867) wrote the transport equation first, for the special interaction he could integrate — inverse-fifth-power "Maxwell molecules". **Boltzmann** (1872) generalised it to arbitrary interaction potentials and added the H-theorem that gives the equation its direction. The note attributes both.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: one law, decomposed to the models it is assembled from, the concepts it turns on, the segment it represents, the standards that license its closure, the checks that test it, the constraints that bound it and the notation it is written in — not to the gas's own structure, which belongs to the natural target and is typed there.
>
> Identity: every Instance Tree Path is a valid prefix of the tree, each non-root row extends an existing path by exactly one labelled link, grouping types are `` `code` ``, instances are Title Case, and no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` Boltzmann Equation | The evolution law for the one-particle distribution of a dilute gas: free flight plus external force on the left, a bilinear collision integral on the right. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` | Grouping: the constituent models the law is assembled from. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Distribution Function | $f(\mathbf{r},\mathbf{v},t)$: the expected phase-space density of particles, the single unknown the equation evolves. Everything thermodynamic is a moment of it. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Streaming Operator | $\partial_t + \mathbf{v}\cdot\nabla_{\mathbf r} + (\mathbf{F}/m)\cdot\nabla_{\mathbf v}$: transport in space by the particles' own velocity and transport in velocity by an external force. It is the only part that carries time-reversal symmetry. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Collision Integral | $Q(f,f)$: the gain and loss of particles at a velocity through binary collisions, weighted by the differential cross-section. Bilinear in $f$, which is what makes the equation nonlinear. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Molecular Chaos Closure | The assumption — Boltzmann's *Stosszahlansatz* — that pre-collision particles are uncorrelated, so the two-particle distribution factors into $f f_1$. It is what closes the equation, and it is the only place the arrow of time enters. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` H-Theorem | $H = \int f \ln f\, d^{3}v$ decreases monotonically under the collision integral and is stationary only at equilibrium. Entropy production is its sign; the theorem is a consequence of the closure, not of mechanics. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Maxwell–Boltzmann Equilibrium | The unique distribution for which the collision integral vanishes: $f \propto \exp(-m\lvert\mathbf{v}\rvert^{2}/2kT)$. The fixed point the H-theorem selects, and the bridge from the kinetic description to the thermodynamic one. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Chapman–Enskog Expansion | The asymptotic solution in powers of the Knudsen number: zeroth order returns the Euler equations, first order the [Navier–Stokes equations](/view.html?p=notes/epistemica/singular/navierstokes-equations.md) with the transport coefficients as integrals over the cross-section. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Transport Coefficients | Viscosity, thermal conductivity and diffusion, computed from the same cross-section rather than measured independently — which is what makes them predictions and not parameters. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Model` `(→ Instance)` Moment Closure | Grad's expansion of $f$ about a local Maxwellian in Hermite polynomials: the alternative to Chapman–Enskog when the departure from equilibrium is large, and the source of extended thermodynamics. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Concept` | Grouping: the discriminators the law turns on. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Concept` `(→ Instance)` Mean Free Path | The distance a particle travels between collisions. Together with the body's scale it fixes the small parameter of the whole construction. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Concept` `(→ Instance)` Knudsen Number | The ratio of mean free path to macroscopic length. Small: the expansion converges and hydrodynamics follows. Large: the expansion fails and the distribution must be solved directly. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Concept` `(→ Instance)` Differential Cross-Section | The scattering law of the molecular interaction. It is the construction's only empirical input: every material property of the gas enters here. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Concept` `(→ Instance)` Local Equilibrium | A Maxwellian whose parameters vary slowly in space and time — the state the expansion departs from, and the sense in which a gas out of global equilibrium is still locally described by thermodynamics. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Part)` `Concept` `(→ Instance)` Entropy Production | The rate at which $H$ decreases. Non-negative by the collision integral's symmetry, zero only at equilibrium, and the microscopic counterpart of the [entropy](/view.html?p=notes/nature/property/entropy.md) account. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Represents)` `Segment of Reality` `(→ Instance)` Dilute Gas | The natural target: a system of many particles, dilute enough that binary encounters dominate and small enough that the Knudsen number is the scale that matters. Read also as [Gas](/view.html?p=notes/nature/matter/state/gas.md) the state of matter and [Kinetic Theory of Gases](/view.html?p=notes/epistemica/singular/kinetic-theory.md) the account it belongs to. Cited, not decomposed here. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Governed By)` `Epistemic Standard` | Grouping: the conditions the law must satisfy to be stated at all. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Diluteness | Collisions are overwhelmingly binary: the gas is rarefied enough that three-body encounters are negligible, and the collision integral is written for a pair. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Molecular Chaos | Pre-collision independence, assumed rather than derived. Adopted because the alternative — tracking correlations — is the $N$-particle problem the equation exists to avoid. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Classical Statistics | Dilute also means non-degenerate: the occupation of a quantum state is small, so the classical collision term is licensed and the Uehling–Uhlenbeck and Bose–Einstein forms are not yet needed. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Short-Range Interaction | Cross-sections that decay fast enough for the collision integral to converge. For Coulomb interaction the integral diverges and a different collision term is required. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Governed By)` `Epistemic Standard` `(→ Instance)` Separation of Scales | Collisions are instantaneous on the scale of the mean free time, and the mean free path is short on the scale of the flow: the two-scale separation that makes a local equilibrium meaningful. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Evaluated By)` `Validation` | Grouping: the checks that discharge doubt about the law. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Transport-Coefficient Measurement | Viscosity and thermal conductivity measured as functions of temperature agree with the values the collision integral predicts from the molecular interaction — the sharpest test, because the numbers are not fitted. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Hydrodynamic Limit Check | The first-order Chapman–Enskog expansion reproduces the [Navier–Stokes equations](/view.html?p=notes/epistemica/singular/navierstokes-equations.md), and the second-order corrections account for the departures observed at moderate Knudsen number. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Direct Simulation and Molecular Dynamics | Direct-simulation Monte Carlo and particle-based molecular dynamics sample the same gas without the closure; agreement in rarefied and shock regimes is evidence that the closure, not the physics, was the approximation. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Evaluated By)` `Validation` `(→ Instance)` Rarefied-Gas Experiments | Sound absorption, shock structure and Couette flow at low pressure, where Navier–Stokes fails and the kinetic description still holds. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` | Grouping: the limits the law carries inside itself. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Reversibility Objection | Loschmidt: the mechanics the equation starts from is time-reversal symmetric, so a monotone H cannot follow from it. The arrow enters through molecular chaos — an assumption about initial correlations, not a consequence of dynamics. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Recurrence Objection | Zermelo, from Poincaré's recurrence theorem: a finite mechanical system returns arbitrarily close to its initial state, so $H$ cannot decrease forever. The monotonicity is statistical — overwhelmingly probable, not certain. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Long-Time Tails | The transport coefficients are not constants: velocity correlations decay algebraically, and the Chapman–Enskog expansion fails at asymptotically long times. Hydrodynamics is a limit in the Knudsen number, not in time. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Dense-Fluid Breakdown | Past diluteness the binary-collision picture misses multi-particle encounters and excluded volume; Enskog's modification and mode-coupling theory patch the description, and neither restores the original derivation. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Long-Range Interaction Breakdown | For plasmas the Coulomb cross-section makes the collision integral diverge at small angles; the Landau and Fokker–Planck collision terms replace it, and [plasma](/view.html?p=notes/nature/matter/state/plasma.md) transport is governed by those. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Epistemic Constraint` `(→ Instance)` Quantum-Statistics Limit | At degeneracy the classical collision term is wrong: the Uehling–Uhlenbeck form for fermions and the Bose–Einstein form for bosons replace it, and with them the equilibrium distribution. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `(→ Instance)` Relativistic Limit | The streaming and collision terms are Galilean: near $c$ they are replaced by the Marle and Israel–Stewart formulations, and the equilibrium the collision integral selects changes with them. |
| `Model` `(→ Instance)` Boltzmann Equation `(→ Has)` `Representational System` `(→ Instance)` Integro-Differential Phase-Space Notation | The sign system the law is written in: a partial differential equation in $(\mathbf{r},\mathbf{v},t)$ whose right-hand side is an integral operator over velocity — a kinetic equation, neither a pure differential law nor a pure integral one. |

### What is a critical conceptual evaluation of this epistemic instance?

The concept under evaluation is **the Boltzmann equation**, precised as *the closed evolution equation for the one-particle distribution of a dilute gas, with binary collisions whose pre-collision partners are assumed independent*. Its verdicts: conceptually identified against the theory that supplies its ontology and against the techniques that solve it, defined precisely enough to compute transport coefficients from a cross-section, internally consistent — conservation laws and the H-theorem are consequences of the collision integral's symmetries rather than added postulates — determinate only inside the dilute regime, representationally adequate exactly there and empty elsewhere, and adequate for its purpose while being the wrong thing to ask for a fundamental description. The one gap that is not a domain boundary is the arrow of time: irreversibility is *inserted* by molecular chaos, and the equation's success is evidence that the inserted assumption is right about gases, not that it follows from mechanics.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Strong | Separated from kinetic theory, which owns the distribution function and the probabilistic reading; from the lattice-Boltzmann and Monte-Carlo practices that solve it; from the natural phenomenon of irreversible transport; and from the four other elements that carry Boltzmann's name. |
| Definitional Clarity | Strong | The streaming operator, the collision integral, the cross-section, the closure assumption and the two small parameters are all stated. What is left to convention — the cross-section model, the sign convention of $H$ — is named as a choice rather than absorbed. |
| Conceptual Determinacy | Conditional | Inside the dilute regime the equation fixes the distribution and nothing else must be supplied; outside it the closure is not determined by the physics, and the several extensions (Enskog, Landau, Uehling–Uhlenbeck, Israel–Stewart) are different closures rather than corrections to one. The concept knows where it governs; it cannot extend itself. |
| Internal Consistency | Strong | Collision invariants — mass, momentum, energy — vanish under $Q$, so the conservation laws follow rather than being assumed; the H-theorem follows from the same symmetry; the equilibrium that nulls $Q$ is exactly the Maxwellian the H-functional minimises. The parts cohere. |
| Representational Adequacy | High inside the dilute regime, empty outside it | Viscosity, conductivity and sound absorption are predicted from the molecular interaction to within measurement error, and the hydrodynamic limit is recovered as an expansion. Nothing in the equation represents a plasma's grazing collisions, a dense fluid's multi-particle encounters, or a degenerate gas, so it does not misrepresent them — it has no content there. |
| Purpose Adequacy | Adequate for dilute-gas transport, inadequate as a foundation | For "how does this rarefied gas evolve, and what are its transport coefficients", it is the right construction and no alternative improves on it. For "where does irreversibility come from", it answers by assumption, and treating the assumption as an explanation is the mistake the criterion is meant to surface. |

## References

- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) — the evaluation criteria applied above
- [Philosophia Artium Epistemicarum et Operis](/view.html?p=notes/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Naturalis et Operis](/view.html?p=notes/philosophia-naturalis-et-operis.md)
- [Boltzmann equation — Wikipedia](https://en.wikipedia.org/wiki/Boltzmann_equation)
- Maxwell, J. C. (1867). On the dynamical theory of gases. *Philosophical Transactions of the Royal Society of London*, 157, 49–88. — the transport equation, written for the interaction Maxwell could integrate
- Boltzmann, L. (1872). Weitere Studien über das Wärmegleichgewicht unter Gasteilchen. *Sitzungsberichte der kaiserlichen Akademie der Wissenschaften in Wien*, 66, 275–370. — the equation for arbitrary potentials, and the H-theorem
- Chapman, S., & Cowling, T. G. (1970). *The mathematical theory of non-uniform gases* (3rd ed.). Cambridge University Press. — the Chapman–Enskog expansion and the transport coefficients
- Cercignani, C. (1988). *The Boltzmann equation and its applications*. Springer. — the mathematical treatment, and the objections of Loschmidt and Zermelo
- [Kinetic Theory](/view.html?p=notes/epistemica/singular/kinetic-theory.md) — the theory that supplies the distribution function and its interpretation
- [Kinetic Theory](/view.html?p=notes/epistemica/singular/kinetic-theory.md) · [Kinetic Theory of Gases](/view.html?p=notes/epistemica/singular/kinetic-theory.md) — the natural-side accounts of the same target
- [Gas](/view.html?p=notes/nature/matter/state/gas.md) — the state of matter the equation represents
- [Plasma](/view.html?p=notes/nature/matter/state/plasma.md) — the target the collision integral does not reach
- [Entropy](/view.html?p=notes/nature/property/entropy.md) · [Thermodynamics](/view.html?p=notes/nature/thermodynamics.md) — the thermodynamic reading of the H-functional
- [Navier–Stokes Equations](/view.html?p=notes/epistemica/singular/navierstokes-equations.md) — the first-order hydrodynamic limit
- [Lattice-Boltzmann Method](/view.html?p=notes/epistemica/singular/lattice-boltzmann-method-lbm.md) · [Lattice-Boltzmann Method](/view.html?p=notes/epistemica/singular/lattice-boltzmann-method.md) — the practice that discretizes and solves it
- [Boltzmann Constant](/view.html?p=notes/nature/boltzmann-constant.md) · [Stefan–Boltzmann Constant](/view.html?p=notes/nature/stefan-boltzmann-constant.md) · [Boltzmann Machine](/view.html?p=notes/technica/cybernetics/architecture/boltzmann-machine.md) — the other elements that carry the name

## Provenance

- Notion export: `Gas 1bac0f5171ec803d8072e7bf9b5c96ff.md` — the placeholder this note replaces
