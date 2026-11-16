---
tags: [note, mathematics, analytical, functional-analysis]
qa:
  - "Why is there no function with the properties the Dirac delta is asked to have?"
  - "Why does δ(ax) equal δ(x) divided by the absolute value of a?"
---

# Dirac Delta

> The **Dirac delta** is the evaluation functional at a point: $\langle \delta, \varphi\rangle = \varphi(0)$ for every test function $\varphi$. It is a Radon measure — unit mass at the origin — and therefore a distribution; it is not a function, and the phrase *delta function* is a historical name that the theory kept while removing its referent.

> The construct exists because physics needed an object with contradictory demands: zero everywhere except one point, and integral one. No function satisfies both, since a function vanishing almost everywhere integrates to zero. The delta is what those demands become when the point is replaced by a probe: the demand that the object return $\varphi(0)$ for every probe is consistent, and it defines a measure, which is why the delta is the standard example of the gap between functions and distributions.

> Its importance is out of proportion to its complexity. The delta is the unit impulse whose response is a Green's function, the point charge whose field is Coulomb's, the eigenstate of position in quantum mechanics, and the identity of convolution. Every one of those uses is a use of the pairing, and none of them needs a pointwise value.

## Formulation

### What is this epistemic instance?

> The delta is defined by its action. For $\varphi \in C_c^\infty(\mathbb{R}^n)$,
>
> $$\langle \delta, \varphi\rangle = \varphi(0), \qquad \langle \delta_a, \varphi\rangle = \varphi(a).$$
>
> Its support is $\{0\}$, its order is zero, and it is positive: $\langle \delta,\varphi\rangle \ge 0$ whenever $\varphi \ge 0$. Being a positive distribution of order zero, it is a Radon measure — the **Dirac measure** $\delta_0$, which assigns mass one to every set containing the origin and zero to every set that does not.

> The derived objects are equally exact. The distributional derivative is $\langle \delta', \varphi\rangle = -\varphi'(0)$, a distribution that no measure represents, since measures assign mass to sets and $\delta'$ assigns none. The Heaviside distribution $H$ — the step read as a regular distribution — satisfies $H' = \delta$, which is the cleanest statement of what the derivative of a step means. Convolution with the delta is the identity, $\delta * \psi = \psi$, so the delta is the unit of the convolution algebra; and translation is convolution with a shifted delta, $\tau_a T = \delta_a * T$.

> The transform is the constant: with the normalisation $\mathcal{F}\varphi(\xi) = (2\pi)^{-n/2}\int e^{-i\xi\cdot x}\varphi(x)\,dx$, one has $\mathcal{F}\delta = (2\pi)^{-n/2}$, and dually $\mathcal{F}1 = (2\pi)^{n/2}\delta$. The pair is the sharpest illustration of why the tempered distributions are the natural home of the transform: neither side is a function.

> The scaling rule is where the notation earns its keep: $\delta(a x) = \lvert a\rvert^{-n}\delta(x)$ in $n$ dimensions, forced by the change of variables in the pairing and not by any pointwise computation. It is also the rule that carries the physical dimension: a density concentrated on a point has units inverse to the volume it is squeezed into, and the delta inherits them through the Jacobian.

> What the delta is *not* is a limit of functions in any pointwise sense. A **delta sequence** $\rho_\varepsilon$ — a mollifier family — converges to $\delta$ in $\mathcal{D}'$, meaning that $\langle \rho_\varepsilon,\varphi\rangle \to \varphi(0)$ for every probe; no individual member is the delta, and no pointwise limit exists. The distinction matters whenever an approximation is used as if it were the object.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the delta scheme: the evaluation functional, the normalisation and scaling conventions, the rules that produce its derivatives and transforms, and the readings under which it is an impulse, a point charge, or a unit mass.

> `readable as` an **`Epistemic Tool`** when attention falls on it operationally: the unit impulse of linear response theory, the object convolved with a signal to read off a response. `readable as` an **`Epistemic Construction`** when attention falls on it as the worked instance that motivated Schwartz's theory. `readable as` an **`Epistemic Act`** is *refused*: the delta is a functional, and the acts that use it — integration against a probe, convolution — are acts performed with it.

### Is the type of this `epistemic element instance` ambiguous?

> Yes — the ambiguity is the whole history of the object, and it must be resolved before anything is computed.

> **Delta as function.** Refused, and the refusal is a theorem: no function vanishes almost everywhere and has integral one. The pointwise notation $\delta(x)$ is a shorthand for the pairing written as an integral, useful because it makes the algebra of impulses look like the algebra of densities, and misleading exactly when a reader takes $\delta(0)$ to be a value.

> **Delta as measure.** Accepted: $\delta_0$ is a Radon measure, positive, of total mass one, supported at a point. This reading is the primary one for probabilistic and physical uses, where the delta is a distribution of a unit mass. It is also the reading under which the delta is a *probability distribution* — a degenerate one — which is a different element from the mathematical distribution it also is.

> **Delta as distribution.** Accepted and more general: the evaluation functional is a distribution of order zero, and its derivatives $\delta^{(\alpha)}$ are distributions that are not measures. Everything the delta does in analysis is done in this reading, and the measure reading is recovered as the special case where positivity holds.

> **Delta vs delta sequence.** A sequence of mollifiers converging to $\delta$ is not the delta, and treating a member as if it were is the standard error of the applied literature. The convergence is weak-*, in the dual; no individual term is the limit.

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the delta scheme — into the notation that carries it, the conventions and rules constituting it, the readings it licenses, the kinds that realise it, and the predicates it carries. The general theory of distributions is linked, never grown; the impossibility of multiplying deltas belongs to its own construction note.

> **Stopping rule.** A row is terminal when it names a notation element, a convention, a rule, a reading, a kind, or a predicate.

> **Identity.** Instance Tree Path holds instances only; every path is unique and no type segment terminates a branch.

> **Typing.** The root type is `Epistemic Representation`, declared once; notation under `Representational System`, conventions and rules under `Constitutive Substrate`, kinds and predicates by `Instance` and `Has Property`.

> **Reading.** The tree is read as **representation**: one functional's machinery, not the physical impulses it is used to model.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta | The evaluation functional at a point: unit mass at the origin, and the standard example of an object that is not a function. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` | Grouping: the sign system carrying the functional. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Representation Element` | Grouping: combinable constituents of the notation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Point of Concentration | The point $a$ at which the probe is evaluated: the only datum the functional carries. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Unit Mass | The normalisation: total weight one, written as $\int \delta = 1$ in the integral shorthand. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Representation Element` (→ Instance) Integral Shorthand | $\int \delta(x)\varphi(x)\,dx$ as a rendering of $\langle\delta,\varphi\rangle$: convenient, and the source of the pointwise misreading. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` | Grouping: the conventions and rules constituting the scheme. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: what the functional is founded on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Evaluation Functional | $\langle\delta,\varphi\rangle = \varphi(0)$: the definition, and the reason the delta is not a function. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Point Support Foundation | The support is a single point, so the functional is localised without being pointwise. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: stabilized choices the notation rests on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Normalisation Convention | Unit total mass, fixed by the probe's value at the point and by nothing else. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Dimensional Convention | The $\lvert a\rvert^{-n}$ of the scaling rule: a density concentrated on a point carries units inverse to volume. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Integral Notation Convention | Writing the pairing as an integral against $\delta(x)$, kept because it makes algebraic manipulation uniform — and never read pointwise. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` | Grouping: licences producing derived objects. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Translation Rule | $\langle\delta_a,\varphi\rangle = \varphi(a)$: shifting the concentration point shifts the probe's argument. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Scaling Rule | $\delta(ax) = \lvert a\rvert^{-n}\delta(x)$: the Jacobian of the change of variables, forced by the pairing. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Differentiation Rule | $\langle\delta^{(\alpha)},\varphi\rangle = (-1)^{\lvert\alpha\rvert}\partial^\alpha\varphi(0)$: the derivatives exist and are not measures. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Convolution Identity Rule | $\delta * \psi = \psi$ and $\delta_a * T = \tau_a T$: the delta as the unit of the convolution algebra. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Fourier Transform Rule | $\mathcal{F}\delta = (2\pi)^{-n/2}$ and $\mathcal{F}1 = (2\pi)^{n/2}\delta$: the pair that shows the transform leaving the class of functions in both directions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` | Grouping: rules of well-formed use. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Delta Sequence Rule | A mollifier family $\rho_\varepsilon$ converges to $\delta$ weakly: the only legitimate sense in which the delta is a limit. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Pairing Formation Rule | $\delta$ appears only inside a pairing; "$\delta(x)$" alone is notation without a statement. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` | Grouping: assignments of meaning to the functional. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Impulse Reading | A unit impulse: all the effect at an instant, none elsewhere — the reading behind Green's functions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Point Charge Reading | A charge or mass concentrated at a point: the reading behind the Coulomb and Newtonian potentials of a point source. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Degenerate Law Reading | A probability law putting all mass on one outcome: the measure reading at total mass one. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has) `Representational System` (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Identity Reading | The unit of convolution: the object that leaves a signal unchanged. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Instance) Dirac Measure | The delta as a Radon measure of unit mass at a point — the reading under which it is also a probability distribution. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Instance) Derivative of the Delta | $\delta'$: a distribution of order one that no measure represents — the standard witness that distributions exceed measures. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Instance) Delta Sequence | A mollifier family converging weakly to the delta: an approximation scheme, never the object. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has Property) `Property` | Grouping: predicates the functional carries. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has Property) `Property` (→ Instance) Point Support | The support is a single point — localisation without a pointwise value. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has Property) `Property` (→ Instance) Order Zero | The evaluation functional needs no derivatives of the probe: the least singular of the non-regular distributions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has Property) `Property` (→ Instance) Positivity | Non-negative probes return non-negative values — the property that identifies the delta as a measure. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Instance) Dirac Delta (→ Has Property) `Property` (→ Instance) Homogeneity | The scaling rule as a property: the delta is homogeneous of degree $-n$, which is what the $\lvert a\rvert^{-n}$ records. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdict.** The construct is determinate in the theory and undetermined in its name. As a functional it is the simplest possible: evaluation at a point, order zero, support a point, no parameter beyond the point itself. As a *name* it is a relic — "delta function" survives from the period when the object was used before it was defined, and the notation $\delta(x)$ still invites the reading the theory forbids. The definition itself has no such gap: every computation with a delta is a computation with a pairing, and every apparent pointwise manipulation is justified by a change of variables or a transposition.

| Criterion | Verdict | Diagnostic Focus |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from a function (no function vanishes a.e. with unit integral), from a measure ($\delta'$ is not one), from a delta sequence (the limit, not a term), and from the general distribution (a specific order-zero element); the differentia — evaluation at a point — is stated outright. |
| Definitional Clarity | Moderate | The definition is exact, but the received notation is not: $\delta(x)$ and $\int\delta(x)\varphi(x)\,dx$ are shorthands whose pointwise reading is false, and the note has to keep saying so. The clarity is in the definition, not in the name. |
| Conceptual Determinacy | Strong | Boundary rule: $\langle T,\varphi\rangle = \varphi(0)$ for all probes decides every case. A candidate is the delta iff it is that functional; anything agreeing only on a subclass is another object, and a delta sequence is not the delta at any term. |
| Internal Consistency | Strong | The scaling, convolution, and transform rules all follow from the one definition by transposition; the dimensional convention is the Jacobian of the same rule, so no separate stipulation is smuggled in. |
| Representational Adequacy | Strong | Notation, conventions, rules, readings, kinds, and predicates occupy separate branches; the measure reading and the functional reading are kept as kinds of one instance rather than as rival definitions. |
| Purpose Adequacy | Strong | The purpose — an exact object with the effect of an impulse — is met, and the cost (no pointwise value, no product with itself) is stated rather than hidden behind the notation. |

## QA

### Why is there no function with the properties the Dirac delta is asked to have?

> Because the two demands contradict integration. A function that is zero everywhere except at one point is zero almost everywhere, and a function that is zero almost everywhere has integral zero with respect to Lebesgue measure. The demand that its integral be one therefore cannot be met by any function — not by a narrow spike, not by a limit of narrow spikes, since the pointwise limit of the spikes is zero almost everywhere and the integrals do not follow it.

> What survives is the pairing. Replace "the value at the point" by "the value of the probe at the point" and the contradiction disappears: $\varphi \mapsto \varphi(0)$ is a perfectly good linear functional, continuous for the test-function topology, and it is the delta. The measure reading gives the same object from the other side — a measure concentrated on a point assigns mass one to every set containing it — and that is why the delta is both a measure and a distribution while being no function at all.

### Why does δ(ax) equal δ(x) divided by the absolute value of a?

> Because the pairing must be preserved under the change of variables the notation performs. Writing the action as an integral against a probe, the substitution $y = ax$ moves the factor $\lvert a\rvert^{-1}$ from the differential onto the delta; requiring $\int \delta(ax)\varphi(x)\,dx = \lvert a\rvert^{-1}\varphi(0)$ for every probe fixes the identity. In $n$ dimensions each coordinate contributes, so the factor is $\lvert \det A\rvert^{-1}$ for a linear map $A$ — the Jacobian of the transformation, not a separate rule.

> The same computation explains the dimensional content of the notation. A density concentrated at a point must carry units inverse to the volume it is confined to, so a delta in one dimension has units of inverse length, in three dimensions inverse volume; the scaling rule is the statement of that fact, and it is the reason a delta cannot appear in a physical equation with dimensions left implicit.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Distribution](/view.html?p=notes/epistemica/mathematical/mapping/distribution/distribution.md) · [Test Function](/view.html?p=notes/epistemica/mathematical/mapping/distribution/test-function.md) · [Tempered Distribution](/view.html?p=notes/epistemica/mathematical/mapping/distribution/tempered-distribution.md) · [Schwartz's Impossibility of Multiplication](/view.html?p=notes/epistemica/epistemic/construction/mathematical/schwartz-impossibility-of-multiplication.md)
- [Heaviside Function](/view.html?p=notes/epistemica/mathematical/mapping/heaviside-function.md) · [Generalized Function](/view.html?p=notes/epistemica/mathematical/mapping/generalized-function.md) · [Convolution Operator](/view.html?p=notes/epistemica/mathematical/mapping/convolution-operator.md) · [Measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) · [Lebesgue Integral](/view.html?p=notes/epistemica/mathematical/mapping/lebesgue-integral.md)
- [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function)
- [Dirac measure](https://en.wikipedia.org/wiki/Dirac_measure)
- Dirac, P. A. M. (1930). *The principles of quantum mechanics*. Oxford University Press.
- Heaviside, O. (1893–1919). *Electromagnetic theory* (Vols. I–III). The Electrician Printing and Publishing Company.
- Schwartz, L. (1950–1951). *Théorie des distributions* (Vols. I–II). Hermann.
- Lighthill, M. J. (1958). *Introduction to Fourier analysis and generalised functions*. Cambridge University Press.
- Gelfand, I. M., & Shilov, G. E. (1964). *Generalized functions: Vol. 1. Properties and operations*. Academic Press.
- Kanwal, R. P. (2004). *Generalized functions: Theory and technique* (3rd ed.). Birkhäuser.
