---
tags: [note, probability, stochastic-process]
---

# Markov Process

Related: [Stochastic Process](stochastic-process.md), [Markov Model](markov-model.md), [CTMC](ctmc-continuous-time-markov-chain.md), [Random Walk](random-walk-drunkard-s-walk.md), [Poisson Process](poisson-process.md), [Brownian Motion](brownian-motion.md), [Stationary Process](stationary-process.md).

> A **Markov process** is a stochastic process that satisfies the Markov property: given the present state, the future is conditionally independent of the past. The class is exactly the processes the property admits — nothing else is assumed, and everything a Markov process allows follows from that one condition.

> The structural consequence is that a Markov process is fixed by two objects: the **initial law** of $X_0$ and the **transition law** that moves a state to the next. Given those, the distribution of every trajectory is determined, and the whole analysis of the class is the analysis of the transition law.

## The property

> The condition that defines the class: given the present state, the future is conditionally independent of the past.

$$ \mathbb{P}(X_{n+1} \in A \mid X_n, X_{n-1}, \dots, X_0) = \mathbb{P}(X_{n+1} \in A \mid X_n) $$

Three readings say the same thing. The **past and the future are conditionally independent given the present**; the present state is a **sufficient statistic** for what happens next; the process **forgets the path but not the state** — everything the history carries that bears on the future has already been packed into the current value.

| It does say | It does not say |
| --- | --- |
| The future depends on the past only through the present | That successive values are independent — they are, in general, dependent through the state |
| The transition law and the initial law determine every finite-dimensional distribution | That the transition law is time-homogeneous; that is a separate assumption, and a Markov process with a time-dependent kernel is still Markov |
| The state can be any object — a number, a vector, the position of a whole system | That the process is stationary, ergodic or reversible; each is a further condition |
| Holding times in continuous time are exponential *once* the rates are constant | That every Markov process has exponential holding times — a time-inhomogeneous chain does not |

The last row is the one most often confused: memorylessness of the *waiting time* follows only after time-homogeneity is added. The property itself is about the state, not about the clock.

**Higher order and generalisations.** If the future depends on the last $k$ values, the process is not first-order Markov in its original state — but it becomes so once the state is enlarged to the $k$-tuple, which is why the property is a statement about the *choice of state* as much as about the process: a poor state definition makes a memoryless process look like it has memory. The **strong Markov property** applies the same conditional independence at a stopping time instead of a fixed index; it does not follow from the plain property in full generality, and it is what makes the transition law usable at random times. The **local Markov property** is the same condition on a graph — a value is independent of the rest given its neighbours — and its operational form is the **Markov blanket**, the smallest set that screens a variable off from all the others.

## The transition law

In discrete time the transition law is a matrix or kernel,

$$ P_{ij} = \mathbb{P}(X_{n+1} = j \mid X_n = i), \qquad \mathbb{P}(X_n = j) = (P^n)_{ij} \text{ from } X_0 = i, $$

and in continuous time it is a family of kernels indexed by the elapsed time,

$$ P_t(x, A) = \mathbb{P}(X_{s+t} \in A \mid X_s = x). $$

The family composes — this is **Chapman–Kolmogorov**, and it is the statement that a Markov process may be cut at any intermediate time without changing the law of its endpoints:

$$ P_{t+s}(x, A) = \int P_s(y, A) \, P_t(x, dy). $$

The object $P_t$ is a **Markov kernel** — a stochastic kernel carrying a state to a probability law on the next state — and its action on observables,

$$ P_t f(x) = \int f(y) \, P_t(x, dy), $$

is the **Markov operator** of the process, with the dual action on laws giving the forward propagation of the distribution.

Three further conditions are usually imposed on top of the property, and each changes the class:

- **time-homogeneity** — $P_t$ does not depend on the starting time $s$, which is what makes the family a semigroup;
- **stationarity** — the law of $X_t$ does not change with $t$, a property of a *distribution*, not of the transitions;
- **regularity** — right-continuous paths with left limits, which is what lets the generator below exist.

## Classification

The class is indexed by two choices, the time set and the state space; the familiar named processes are its cells.

| | **Discrete state space** | **General state space** |
| --- | --- | --- |
| **Discrete time** | [Markov chain](ctmc-continuous-time-markov-chain.md) — random walk, Ehrenfest urn, Galton–Watson, PageRank | Markov chain on a general state space, driven by a transition kernel; iterated random maps |
| **Continuous time** | Markov jump process — CTMC, [Poisson process](poisson-process.md), birth–death and queueing processes | Diffusion — [Brownian motion](brownian-motion.md), Ornstein–Uhlenbeck, Itô diffusions; more generally Lévy-type processes |

The vertical axis decides whether the generator is a matrix (a rate matrix $Q$) or a differential operator; the horizontal axis decides whether the state is counted or measured.

## The generator

For a time-homogeneous process with sufficiently regular paths, the transition semigroup has an infinitesimal description,

$$ L f(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}[f(X_t) \mid X_0 = x] - f(x)}{t}, $$

and the **Kolmogorov forward equation** $\partial_t P_t = P_t L$ (equivalently the Fokker–Planck equation when $L$ is a diffusion operator) propagates the law, while the **backward equation** $\partial_t P_t = L P_t$ propagates the function. For a jump process with rate matrix $Q$, $L f(i) = \sum_j q_{ij}(f(j) - f(i))$ and $P_t = e^{tQ}$.

The generator is where the classification above becomes concrete: a diffusion has a second-order operator, a jump process a bounded rate kernel, and a discrete chain a matrix.

## Examples

- **Random walk** — the canonical discrete-time chain: increments independent, state the position, and the Markov property holds by construction.
- **Poisson process** — the canonical continuous-time counting process: independent exponential increments, so the future depends on the past only through the current count.
- **Birth–death and queueing processes** — a CTMC on the non-negative integers with transitions only to neighbours; the state is the queue length, and that is all the model needs.
- **Brownian motion** — the canonical diffusion; independent Gaussian increments make it Markov, and its generator is $\tfrac{1}{2}\Delta$.
- **Ornstein–Uhlenbeck** — a diffusion with a restoring drift, Markov with a Gaussian transition kernel.

## What the property alone does not give

Nothing about long-run behaviour follows from being Markov. A chain may be transient, null-recurrent or positive-recurrent; periodic or aperiodic; reducible or irreducible; reversible or not. Ergodicity, stationary distributions and mixing are conditions *on the transition law*, established by separate arguments — and the same is true of the strong Markov property, which requires regularity at stopping times rather than the plain conditional independence.

## References

- Doob, J. L. (1953). *Stochastic processes*. Wiley.
- Ethier, S. N., & Kurtz, T. G. (1986). *Markov processes: Characterization and convergence*. Wiley. https://doi.org/10.1002/9780470316658
- Kemeny, J. G., & Snell, J. L. (1960). *Finite Markov chains*. Van Nostrand.
- Markov, A. A. (1906/1971). Extension of the limit theorems of probability theory to a sum of variables connected in a chain. In R. A. Howard (Ed.), *Dynamic probabilistic systems: Vol. 1. Markov models* (pp. 552–577). Wiley.
- Meyn, S. P., & Tweedie, R. L. (2009). *Markov chains and stochastic stability* (2nd ed.). Cambridge University Press.
- Norris, J. R. (1998). *Markov chains*. Cambridge University Press.
- Seneta, E. (1996). Markov and the birth of chain dependence theory. *International Statistical Review*, 64(3), 255–263. https://doi.org/10.2307/1403785
