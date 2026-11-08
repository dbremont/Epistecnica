---
tags: [note, mathematics]
order: 0
---

# Mathematical Method

> A **mathematical method** is a generalized routine a mathematical activity runs — the reproducible order of acts by which a claim is derived, a solution is approximated, or a system is reduced to one that can already be solved.

## Formulation

### What is this epistemic instance?

> The method scope of the mathematical domain: the routines by which mathematics is done, gathered as one catalogue and filed by what the routine *does to the problem*. A result belongs to the [construction scope](../construction/construction.md); the rule a method operates on belongs to the representational system that carries it, catalogued in [transformation.md](../transformation.md).

### What epistemic element type does this epistemic instance belong to?

> An `Aggregate` over `Epistemic Method`s. A method prescribes acts but never contains them: the acts belong to the activity that performs them, and the prescription is recorded on the act's node as metadata, never as a further link. The schema is owned by the canonical
> [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

### Is the type of this `epistemic element instance` ambiguous?

> Three boundaries are worth stating. Against a **rule**: multiplying is a transformation rule, *Shift-And-Add Multiplication* is a method, and a column-sums session is an activity. Against a **construction**: a theorem is the artifact, the proof routine is the method that produced it. Against a **principle**: a principle guides inquiry without prescribing an order of acts — [pigeonhole](/view.html?p=notes/epistemica/epistemic/guidance/principle/pigeonhole-principle.md) and [inclusion–exclusion](proof/inclusion-exclusion.md) sit on that line, and both are filed here as routines because each is a sequence of counting acts, not a norm of judgment.

### What are the families of this `epistemic element instance`?

> The axis is **what the routine does to the problem**. Five families; a method that does two things sits in the family that names its principal move.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Mathematical Method | The catalogue of mathematical routines. |
| `Aggregate` → Mathematical Method → Proof Routine | Grouping: routines that establish truth without computing the object. |
| `Aggregate` → Mathematical Method → Proof Routine → [Induction](proof/induction.md) | Base case plus successor step; weak, strong, structural and transfinite forms. |
| `Aggregate` → Mathematical Method → Proof Routine → [Diagonalization](proof/diagonalization.md) | Encode the enumeration, alter the diagonal, conclude impossibility. |
| `Aggregate` → Mathematical Method → Proof Routine → [Contradiction](proof/contradiction.md) | Assume the negation, derive an impossibility; classical, not constructive. |
| `Aggregate` → Mathematical Method → Proof Routine → [Extremal Principle](proof/extremal-principle.md) | Take the extreme object; maximality or minimality supplies the contradiction. |
| `Aggregate` → Mathematical Method → Proof Routine → [Descent](proof/descent.md) | Any counterexample yields a smaller one; no infinite descending chain exists. |
| `Aggregate` → Mathematical Method → Proof Routine → [Invariant Method](proof/invariant-method.md) | A quantity every operation preserves, or one that strictly decreases. |
| `Aggregate` → Mathematical Method → Proof Routine → [Double Counting](proof/double-counting.md) | Count one set two ways; the identity follows. |
| `Aggregate` → Mathematical Method → Proof Routine → [Inclusion–Exclusion](proof/inclusion-exclusion.md) | Alternating correction of an over-counted union. |
| `Aggregate` → Mathematical Method → Proof Routine → [Bijective Method](proof/bijective-method.md) | Exhibit a bijection rather than count both sides. |
| `Aggregate` → Mathematical Method → Proof Routine → [Probabilistic Method](proof/probabilistic-method.md) | Positive probability of a good object proves existence. |
| `Aggregate` → Mathematical Method → Reduction Routine | Grouping: routines that rewrite the problem into one already solved. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Change of Variables](reduction/change-of-variables.md) | Move to coordinates adapted to the problem, solve, transport back. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Separation of Variables](reduction/separation-of-variables.md) | A product ansatz splits one PDE into ordinary equations. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Symmetry Reduction](reduction/symmetry-reduction.md) | Descend along group orbits to a quotient problem. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Linearization](reduction/linearization.md) | Replace the problem by its first-order behaviour at a point. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Dimensional Analysis](reduction/dimensional-analysis.md) | Derive admissible relations from the units quantities carry. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Decomposition](reduction/decomposition.md) | Rewrite the object as simpler, reconstructible components. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Compactness Argument](reduction/compactness-argument.md) | Extract a convergent subsequence and pass to the limit. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Variational Method](reduction/variational-method.md) | Turn a solution into a stationary point of a functional. |
| `Aggregate` → Mathematical Method → Reduction Routine → [Contraction Mapping](reduction/contraction-mapping.md) | Iterate a contraction on a complete space to its fixed point. |
| `Aggregate` → Mathematical Method → Approximation Routine | Grouping: routines that accept error for tractability. |
| `Aggregate` → Mathematical Method → Approximation Routine → [Asymptotic Analysis](approximation/asymptotic-analysis.md) | Characterize behaviour in a limit instead of solving exactly. |
| `Aggregate` → Mathematical Method → Approximation Routine → [Perturbation Method](approximation/perturbation-method.md) | Expand in a small parameter, order by order. |
| `Aggregate` → Mathematical Method → Approximation Routine → [Stationary Phase](approximation/stationary-phase.md) | Localize an oscillatory integral to its critical points. |
| `Aggregate` → Mathematical Method → Approximation Routine → [Discretization](approximation/discretization.md) | Replace a continuum problem by a finite one. |
| `Aggregate` → Mathematical Method → Approximation Routine → [Iterative Method](approximation/iterative-method.md) | Approach the solution by repeated correction. |
| `Aggregate` → Mathematical Method → Transform Routine | Grouping: routines that move the problem to a representation where it is trivial. |
| `Aggregate` → Mathematical Method → Transform Routine → [Generating Function](transform/generating-function.md) | Encode a sequence as coefficients, compute by algebra. |
| `Aggregate` → Mathematical Method → Transform Routine → [Green's Function Method](transform/green-s-function.md) | Solve for a point source; superpose for any source. |
| `Aggregate` → Mathematical Method → Certificate Routine | Grouping: routines that bound without solving. |
| `Aggregate` → Mathematical Method → Certificate Routine → [Convex Duality](certify/convex-duality.md) | Pair the problem with its dual to obtain bounds and optimality certificates. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- Domain methods that belong to their own scopes: [Newton–Raphson](/view.html?p=notes/epistemica/singular/newton-raphson-method.md), [Monte Carlo](../../observational/computational/monte-carlo-toolbox.md), [MCMC](../../observational/computational/mcmc-markov-chain-monte-carlo.md), [dynamic programming](../../optimization/dynamic-programming.md), [Lagrange multipliers](../../optimization/lagrange-multiplier.md).
