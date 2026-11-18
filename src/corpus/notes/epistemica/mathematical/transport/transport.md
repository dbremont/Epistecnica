---
tags: [note, mathematics, transport, transfer, optimization]
order: 0
---

# Transport

- What is meant by transport?
- Which kinds of problems can be modeled as transport problems?
- What is the essence of transport?

> **Transport** is the mathematical study of moving something from where it is to where it is wanted: a distribution, a mass, a flow, a probability, a signal or a quantity, carried from a source to a target under a cost, a capacity, or a conservation law.

> The word names one problem in several mathematical clothes. Move dirt from a pile into a hole at least cost: that is **optimal transport**, a measure-theoretic optimization problem. Ship a commodity from warehouses to markets through a network with capacities: that is a **flow problem**, a linear program on a graph. Carry a density along a velocity field while it is conserved: that is a **transport equation**, a PDE. Push a distribution through a channel and read what comes out: that is a **Markov kernel**, probability's version of the same move. Assign workers to jobs one apiece: that is the **assignment problem**, transport with indivisible units.

> What makes these one subject is not a shared theorem but a shared question: *what do we know that lets us model a transfer?* The answer has four parts in every case — a **source**, a **target**, a **carrier** that takes the source to the target, and a **cost or constraint** that ranks the carriers. Change any one of the four and the mathematics changes; keep the four in view and the branches become comparable.

## What is transferred

| Carried quantity | Source / target | Carrier | Constraint | Where it is studied |
| --- | --- | --- | --- | --- |
| Mass, earth, commodity | Two measures or two inventories | A map or a joint plan | Cost per unit moved | [Transportation Theory](/view.html?p=notes/epistemica/mathematical/transport/transportation-theory.md) |
| Flow through a network | Sources and sinks on a graph | An edge flow | Capacities, conservation at nodes | Network flows — [Flows in Networks](/view.html?p=notes/epistemica/singular/transportation-system.md) |
| Density or concentration | Initial and boundary data | A velocity field | Conservation law, continuity equation | Diffusion and continuity — [Diffusion](/view.html?p=notes/nature/diffusion.md) |
| Probability | Two distributions | A coupling or a kernel | Marginal consistency | [Probability](/view.html?p=notes/miscellanea/discipline/probability.md) |
| Information | An input alphabet | A channel | Capacity, noise | [Information](/view.html?p=notes/epistemica/observational/information/information.md) |
| Units, not mass | Workers, jobs, schools | A matching | One-to-one, preferences | [Combinatorial Optimization](/view.html?p=notes/epistemica/optimization/combinatorial-optimization.md) |

> The four slots are the diagnostic. A transfer problem that seems unfamiliar is usually one of these with the source, carrier or cost changed — indivisible units instead of a continuous mass, capacities instead of a per-unit cost, a velocity field instead of a plan, a kernel instead of a map.

## Which are the branches of transport?

| Branch | Object | What it asks | Canonical statement |
| --- | --- | --- | --- |
| **Optimal transport** | A coupling between two measures | Which carrier minimises the expected cost? | Monge's map, Kantorovich's plan |
| **Network flow** | A flow on a graph | Which flow satisfies the demands within the capacities? | Max-flow min-cut |
| **Transport equation** | A density and a velocity field | How does the density evolve under the flow? | Continuity equation |
| **Markov transport** | A stochastic kernel | Which kernel carries one distribution to another? | Chapman–Kolmogorov |
| **Assignment and matching** | A bijection between finite sets | Which matching is optimal or stable? | Hungarian algorithm, stable matching |
| **Information transport** | A channel | How much of the source survives the transfer? | Channel capacity |

> The branches meet in the middle. Optimal transport's dual is a pricing problem, which is why it is a linear program; its dynamic form (Benamou–Brenier) is a transport equation minimised over velocity fields; its discrete form is the assignment problem. The corpus keeps the theory in its own note and the neighbouring branches where they already live.

## QA

### Is transport the same as flow?

> No. A flow is a *carrier*: a velocity field, or a flow along the edges of a network. Transport is the *problem* of choosing a carrier that moves one distribution onto another. Every transport problem has flows as candidates; not every flow problem is a transport problem, because a flow need not be required to reproduce a target distribution.

### Why is optimal transport "optimal"?

> Because a cost is minimised over all admissible carriers. The adjective is doing real work: the *set* of carriers from μ to ν is the set of couplings with those marginals, and without a cost every one of them is equally a transport. The cost — distance, squared distance, a concave function of it — selects among them, and its convexity decides whether the optimum is a map (each source goes to one target) or a plan (a source may split).

### Is the assignment problem a transport problem?

> It is the discrete, indivisible case. If the mass cannot be split, the plan must be supported on a permutation, and the linear program becomes the assignment problem; if it can, the same linear program has a continuous relaxation whose solutions may split mass. This is why the transportation problem is the historical entry point to linear programming and the assignment problem is its combinatorial sibling.

### Why does the physical theory of transport not live here?

> [Diffusion](/view.html?p=notes/nature/diffusion.md) holds the equations that *describe* transport in matter — diffusion, advection, the continuity equation — because those are results about nature. This note and its directory hold the *mathematics of the transfer problem*: the carriers, the costs, the dualities. The two are linked, not merged.

## Related

- [Transportation Theory](/view.html?p=notes/epistemica/mathematical/transport/transportation-theory.md) — the Monge–Kantorovich theory and its literature
- [Transportation System](/view.html?p=notes/epistemica/singular/transportation-system.md) — the physical system, a different object with a similar name
- [Diffusion](/view.html?p=notes/nature/diffusion.md) — the equations that describe transport in matter
- [Combinatorial Optimization](/view.html?p=notes/epistemica/optimization/combinatorial-optimization.md) · [Calculus of Variations](/view.html?p=notes/epistemica/optimization/calculus-of-variations.md) — the two optimization families the theory sits between
- [Probability](/view.html?p=notes/miscellanea/discipline/probability.md) · [Measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) — the objects a coupling is built from
- [Information Geometry](/view.html?p=notes/epistemica/observational/information/information-geometry.md) — where optimal transport meets statistical inference
- [Leonid Vitaliyevich Kantorovich](/view.html?p=notes/social/collective/actor/private/persona/leonid-vitaliyevich-kantorovich.md) — the mathematician who made the problem a linear program

## References

- Ford, L. R., & Fulkerson, D. R. (1962). *Flows in networks*. Princeton University Press.
- Kantorovich, L. V. (1942). On the translocation of masses. *Doklady Akademii Nauk SSSR*, 37, 199–201.
- Monge, G. (1781). Mémoire sur la théorie des déblais et des remblais. *Histoire de l'Académie Royale des Sciences de Paris*, 666–704.
- Villani, C. (2009). *Optimal transport: Old and new*. Springer.
- [Transportation theory (mathematics)](https://en.wikipedia.org/wiki/Transportation_theory_(mathematics))
