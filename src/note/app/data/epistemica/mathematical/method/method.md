# Mathematical Method

> A **mathematical method** is a generalized routine a mathematical activity runs — the reproducible order of acts by which a claim is derived, a solution is approximated, or a system is reduced to one that can already be solved.

## Formulation

### What is this epistemic instance?

> The method scope of the mathematical domain: the routines by which mathematics is done, gathered as one catalogue. Each member is a routine, not a result — the result belongs to the `construction` scope, and the rule it operates on belongs to the representational system that carries it.

### What epistemic element type does this epistemic instance belong to?

> An `Aggregate` over `Epistemic Method`s. A method prescribes acts but never contains them: the acts belong to the activity that performs them, and the prescription is recorded on the act's node as metadata, never as a further link. The schema is owned by the canonical
> [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

### Is the type of this `epistemic element instance` ambiguous?

> No: a method is the reproducible order of acts, which is what separates it from the rule it applies (`Transformation Rule`, a constituent of a representational system) and from the sitting that runs it (`Epistemic Activity`). Multiplying is a rule; *Shift-And-Add Multiplication* is a method; a column-sums session is an activity.

### What is the recursive instance decomposition of this epistemic instance?

> The members below are the routines the mathematics corpus has written down. Each is a method of the domain; the grouping says which family of problems it reduces.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Mathematical Method | The catalogue of mathematical routines. |
| `Aggregate` → Mathematical Method → Solution Approximation | Grouping: routines that replace an unsolvable problem with a solvable one. |
| `Aggregate` → Mathematical Method → Solution Approximation → Perturbation Method | Expands a small parameter into an asymptotic series and solves term by term. |
| `Aggregate` → Mathematical Method → Solution Approximation → Asymptotic Analysis | Characterizes a solution's behaviour in a limit instead of solving it exactly. |
| `Aggregate` → Mathematical Method → Solution Approximation → Variational Method | Selects the admissible function that makes a functional stationary. |
| `Aggregate` → Mathematical Method → Solution Approximation → Iterative Method | Approaches the solution by repeated correction from an initial guess. |
| `Aggregate` → Mathematical Method → Solution Approximation → Linearization | Replaces a nonlinear problem by its first-order behaviour near a point. |
| `Aggregate` → Mathematical Method → Solution Approximation → Discretization | Replaces a continuum problem by a finite one. |
| `Aggregate` → Mathematical Method → Dimensional Reduction | Grouping: routines that cut away structure the answer cannot depend on. |
| `Aggregate` → Mathematical Method → Dimensional Reduction → Dimensional Analysis | Derives admissible relations from the units a quantity carries. |
| `Aggregate` → Mathematical Method → Combinatorial Correspondence | Grouping: routines that transport a result across representations. |
| `Aggregate` → Mathematical Method → Combinatorial Correspondence → Bijective Method | Proves a counting identity by exhibiting a bijection rather than counting both sides. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- Polynomial-system elimination and other solving routines currently sit in the [equation scope](../equation/equation.md).
