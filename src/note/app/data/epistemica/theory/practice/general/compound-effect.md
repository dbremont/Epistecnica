# Compound Effect

Related: [Multiplicative Effect](note.html?n=epistemica/theory/practice/general/multiplicative-effect.md), [Non Linear System](note.html?n=epistemica/theory/ontology/non-linear-system.md)

> What are the sources of nonlinearity in the system?
> 

> Compounding effects emerge when the accumulation of minor causes, seemingly insignificant in isolation, precipitates transformations of disproportionate magnitude over time. The whole becomes not a sum, but a new order born from the silent insistence of repetition.
> 

> The **Compound Effect** describes a dynamical process in which incremental, consistent inputs $x(t)$ into a system produce a cumulative nonlinear output $y(t)$, often exhibiting an *exponential-like* growth or significant divergence over time due to continuous feedback and accumulation.
> 

Mathematically:

- Let $x(t)$ be the magnitude of small, consistent actions at time $t$.
- The system accumulates these actions over discrete time steps $\Delta t$, where each step includes a function $f(x(t))$ that maps the input to a measurable effect.
- The cumulative output y(t)y(t) evolves according to a difference equation:

$y(t+\Delta t) = y(t) + f(x(t)) + \epsilon(t)$

where:

- $\epsilon(t)$ accounts for noise, errors, or environmental perturbations.
- $f(x)$ is often sublinear at the input scale but becomes superlinear in cumulative effect due to repeated application (e.g., reinforcement, habit loops, or compounding rewards).

Under idealized conditions (minimal ϵ\epsilon), and when f(x)f(x) includes multiplicative or feedback components (e.g.,  $f(x) = r \cdot y(t) + c \cdot x(t)$ with $r > 0$), the system transitions from **linear growth** to **exponential growth** described by:

$y(t) \sim e^{rt}$ thus illustrating the profound effect small, consistent inputs have over a long horizon.

From the viewpoint of **dynamical systems**, the Compound Effect can be interpreted as a **positive feedback loop** within an **autonomous system** where:

- **Stability** depends on the magnitude and direction of inputs x(t)x(t).
- **Trajectory divergence** increases with consistent bias in the input direction.
- **Nonlinearity** emerges from feedback amplification.

## References

- https://en.wikipedia.org/wiki/Compound_interest
- …
