---
tags: [note, mathematics, transport, optimization, probability]
order: 1
---

# Transportation Theory

> **Transportation theory** — optimal transport, or the Monge–Kantorovich problem — asks for the cheapest way to turn one distribution of mass into another. Given a pile of dirt and a hole of the same volume, which way of moving the dirt minimises the total distance carried?

> The problem was posed by Gaspard Monge in 1781 as a question about earthworks: a *map* `T` sends each point of the source to a point of the target, and the cost `∫ c(x, T(x)) dμ(x)` is minimised over all maps that push `μ` onto `ν`. Monge's formulation can fail to have an answer — if `μ` is a point mass and `ν` is not, no map can spread it — so Leonid Kantorovich replaced the map by a *plan* in 1942: a joint distribution `γ` on the product space whose marginals are `μ` and `ν`. The plan always exists, the problem becomes a linear program, and its dual is a pricing problem.

> The theory's modern life begins when the cost is a distance. Then the minimal cost raised to the power `1/p` is a metric on probability measures — the **Wasserstein distance** — and the space of measures becomes a geometric object in its own right: Brenier's theorem makes the optimal map the gradient of a convex function, McCann shows that entropy is convex along optimal paths, and Otto reads the whole thing as a Riemannian manifold whose geodesics are the transports. That is why optimal transport now appears wherever a distance between *distributions* is needed: statistics, machine learning, economics, imaging, seismology.

## Formulation

### Monge's problem

> Let `μ` be a probability measure on `X` and `ν` one on `Y`, and let `c : X × Y → [0, ∞)` be the cost of moving a unit from `x` to `y`. Find a measurable map `T : X → Y` with `T#μ = ν` — the pushforward of `μ` by `T` is `ν` — minimising `∫ c(x, T(x)) dμ(x)`.

> The constraint is the difficulty. A map cannot split mass, so it exists only when `ν` is not "more spread out" than `μ` in a way the map cannot follow; for Dirac masses the obstruction is immediate.

### Kantorovich's relaxation

> Replace the map by a **coupling**: a probability measure `γ` on `X × Y` with first marginal `μ` and second marginal `ν`. Minimise `∫ c(x, y) dγ(x, y)` over the set `Γ(μ, ν)` of such couplings. The set is convex and compact under mild conditions, the objective is linear in `γ`, and the problem is therefore a linear program — with a dual.

> The discrete case makes the linear program explicit: if `μ = Σ_i a_i δ_{x_i}` and `ν = Σ_j b_j δ_{y_j}`, the unknown is a matrix `γ_ij` with row sums `a_i` and column sums `b_j`, minimising `Σ c_ij γ_ij`. This is the **transportation problem** of Hitchcock (1941) and Koopmans (1949), and it is the historical entry point to linear programming.

### Duality

> **Kantorovich duality** states that the minimum cost equals a maximum over prices: `inf_γ ∫ c dγ = sup_{φ} ∫ φ dμ + ∫ φ^c dν`, where `φ^c(y) = inf_x (c(x,y) − φ(x))` is the `c`-transform of `φ`. The economic reading is the shipper's problem: a carrier quotes a loading price `φ(x)` and an unloading price `ψ(y)` with `φ(x) + ψ(y) ≤ c(x,y)`; the best such schedule extracts the same total as shipping the mass yourself. The optimum is characterised by complementary slackness: an optimal plan is supported on the pairs where `φ(x) + ψ(y) = c(x,y)`.

> When `c(x,y) = ‖x − y‖`, the `c`-convex functions are exactly the 1-Lipschitz functions, and the dual becomes the Kantorovich–Rubinstein norm — the formula that makes the Wasserstein distance computable as a supremum over Lipschitz test functions.

### Brenier's theorem and the geometry

> For quadratic cost `c(x,y) = ‖x − y‖²` on `ℝⁿ`, **Brenier's theorem** (1991) states that if `μ` does not charge small sets, the optimal plan is induced by a map `T = ∇u` for a convex function `u` — the optimal map is the gradient of a potential, and it is unique. The result turns the transport problem into a Monge–Ampère equation and connects it to convex analysis, fluid mechanics and meteorology.

> **McCann (1995)** showed that the entropy functional is displacement-convex along optimal paths; **Otto (2001)** made the consequence explicit: the space of probability measures with the Wasserstein metric behaves like a Riemannian manifold, and diffusions are gradient flows on it. **Benamou–Brenier (2000)** gave the dynamic formulation — minimise kinetic energy over velocity fields satisfying the continuity equation — which is the bridge between the static plan and the PDE reading.

### Computation

> The discrete problem is a linear program, solvable by network simplex or by the auction algorithm; when the mass is indivisible it is the assignment problem, solved by the Hungarian algorithm. At scale, the LP is too slow, and the field changed when **Cuturi (2013)** added an entropic penalty: the regularised problem has a dual solved by **Sinkhorn–Knopp** iterations, which are matrix scalings, and therefore GPU-fast. Nearly all applied optimal transport today is Sinkhorn.

## Literature map

> Ordered by the question each cluster answers, not by date. The clusters overlap — Brenier's theorem is geometry *and* PDE, Sinkhorn is computation *and* statistics — and the arrows run both ways: the computational revival fed back into the theory.

| Cluster | The question it answers | Canonical works | What it established |
| --- | --- | --- | --- |
| **Origins and the linear program** | How do you move a commodity from sources to sinks at least cost? | Monge (1781); Tolstoi (1930); Hitchcock (1941); Kantorovich (1942); Koopmans (1949); Ford & Fulkerson (1962); Schrijver (2003) | The problem itself, its discrete form, and its identity as a linear program with a dual |
| **Measure-theoretic formulation** | What is the problem when the mass is a measure, not a shipment? | Kantorovich (1942); Sudakov (1979); Rachev & Rüschendorf (1998); Villani (2003, 2009); Ambrosio, Gigli & Savaré (2005); Santambrogio (2015) | Existence, duality and stability under weak convergence; the modern definition of the coupling |
| **Geometry and PDE** | What does the set of measures look like when distance is the cost? | Brenier (1991); Caffarelli (1992); McCann (1995); Otto (2001); Figalli & Glaudo (2021) | Optimal maps as gradients of convex potentials; displacement convexity; the Wasserstein space as a Riemannian manifold |
| **Computation** | How is the plan computed at scale? | Sinkhorn (1967); Benamou & Brenier (2000); Cuturi (2013); Peyré & Cuturi (2019) | Entropic regularisation and Sinkhorn iterations; the dynamic formulation; the software stack (POT) |
| **Economics and matching** | Who is assigned to whom, and at what price? | Koopmans (1949); Shapley & Shubik (1971); Becker (1973); Gretsky, Ostroy & Zame (1992); Galichon (2016) | The assignment game and its core; hedonic pricing; the non-atomic limit; transport as equilibrium |
| **Statistics and machine learning** | How do you compare, learn from, or generate distributions? | Arjovsky, Chintala & Bottou (2017); Genevay, Peyré & Cuturi (2019); Schiebinger et al. (2019) | Wasserstein GANs; Sinkhorn divergences as losses; trajectory inference in single-cell data |
| **Applications** | How does the abstract plan become a numerical answer in a domain? | Haker et al. (2004); Glimm & Oliker (2003); Engquist & Froese (2014) | Image registration and warping; reflector design; seismic inversion with the Wasserstein metric |

## QA

### Why is the plan formulation preferred to the map?

> Because it always exists. Kantorovich's relaxation is a convex problem whose feasible set is compact under weak conditions, so a minimiser exists without any assumption on `μ` beyond finite first moment. The map formulation is sharper when it holds — a map tells you where each point goes — but it needs hypotheses (no atoms, a strictly convex cost) that the plan does not.

### What does the cost function really decide?

> The geometry. Linear cost makes the distance a transportation metric with a strong dual; quadratic cost gives Brenier's gradient-of-a-convex-potential structure and a Monge–Ampère equation; a concave cost in the distance can concentrate the plan on long moves rather than spreading it. The books move example in the Wikipedia article is the smallest illustration: with `|x−y|`, "move everything one step" and "move one book `n` steps" cost the same; with `|x−y|²`, only the first is optimal.

### Is the Wasserstein distance a metric?

> Yes, for `p ≥ 1` and cost `d(x,y)^p`, the `p`-th root of the minimal cost is a metric on the measures with finite `p`-th moment — the `p`-Wasserstein distance `W_p`. It metrises weak convergence plus convergence of moments, which is why it is used where the total-variation distance is too strong and the Prokhorov metric too weak.

### Why is this filed in the mathematical corpus and not among the natural transport notes?

> Because it is mathematics about transfer, not a result about a natural system. [Diffusion](/view.html?p=notes/nature/diffusion.md) holds the equations a physical transport obeys; this note holds the problem of choosing a carrier and the theorems that characterise its optimum. The branch master, [Transport](/view.html?p=notes/epistemica/mathematical/transport/transport.md), frames the relation between the two.

## Related

- [Transport](/view.html?p=notes/epistemica/mathematical/transport/transport.md) — the branch this theory belongs to
- [Combinatorial Optimization](/view.html?p=notes/epistemica/optimization/combinatorial-optimization.md) — the discrete, indivisible case
- [Calculus of Variations](/view.html?p=notes/epistemica/optimization/calculus-of-variations.md) — the continuous optimization family the dynamic formulation belongs to
- [Probability](/view.html?p=notes/miscellanea/discipline/probability.md) · [Measure](/view.html?p=notes/epistemica/mathematical/measure/measure.md) — the objects coupled by a plan
- [Information Geometry](/view.html?p=notes/epistemica/observational/information/information-geometry.md) — where Wasserstein geometry meets statistical inference
- [Diffusion](/view.html?p=notes/nature/diffusion.md) — the physical equations of transport
- [Leonid Vitaliyevich Kantorovich](/view.html?p=notes/social/actor/private/persona/leonid-vitaliyevich-kantorovich.md) — the mathematician behind the relaxation

## References

- Ambrosio, L., Gigli, N., & Savaré, G. (2005). *Gradient flows in metric spaces and in the space of probability measures*. Birkhäuser.
- Arjovsky, M., Chintala, S., & Bottou, L. (2017). Wasserstein GAN. *arXiv preprint*, arXiv:1701.07875.
- Becker, G. S. (1973). A theory of marriage: Part I. *Journal of Political Economy*, 81(4), 813–846.
- Benamou, J.-D., & Brenier, Y. (2000). A computational fluid mechanics solution to the Monge–Kantorovich mass transfer problem. *Numerische Mathematik*, 84(3), 375–393.
- Brenier, Y. (1991). Polar factorization and monotone rearrangement of vector-valued functions. *Communications on Pure and Applied Mathematics*, 44(4), 375–417.
- Caffarelli, L. A. (1992). The regularity of mappings with a convex potential. *Journal of the American Mathematical Society*, 5(1), 99–104.
- Cuturi, M. (2013). Sinkhorn distances: Lightspeed computation of optimal transport. *Advances in Neural Information Processing Systems*, 26, 2292–2300.
- Engquist, B., & Froese, B. D. (2014). Application of the Wasserstein metric to seismic signals. *Communications in Mathematical Sciences*, 12(5), 979–988.
- Figalli, A., & Glaudo, F. (2021). *An invitation to optimal transport, Wasserstein distances, and gradient flows*. EMS Press.
- Ford, L. R., & Fulkerson, D. R. (1962). *Flows in networks*. Princeton University Press.
- Galichon, A. (2016). *Optimal transport methods in economics*. Princeton University Press.
- Genevay, A., Peyré, G., & Cuturi, M. (2019). Learning generative models with Sinkhorn divergences. *Proceedings of the 21st International Conference on Artificial Intelligence and Statistics*, 1608–1617.
- Glimm, T., & Oliker, V. (2003). Optical design of single reflector systems and the Monge–Kantorovich mass transfer problem. *Journal of Mathematical Sciences*, 117(3), 4096–4108.
- Gretsky, N. E., Ostroy, J. M., & Zame, W. R. (1992). The nonatomic assignment model. *Economic Theory*, 2(1), 103–127.
- Haker, S., Zhu, L., Tannenbaum, A., & Angenent, S. (2004). Optimal mass transport for registration and warping. *International Journal of Computer Vision*, 60(3), 225–240.
- Hitchcock, F. L. (1941). The distribution of a product from several sources to numerous localities. *Journal of Mathematics and Physics*, 20(2), 224–230.
- Kantorovich, L. V. (1942). On the translocation of masses. *Doklady Akademii Nauk SSSR*, 37, 199–201.
- Koopmans, T. C. (1949). Optimum utilization of the transportation system. *Econometrica*, 17(Supplement), 136–146.
- McCann, R. J. (1995). Existence and uniqueness of monotone measure-preserving maps. *Duke Mathematical Journal*, 80(2), 309–323.
- Monge, G. (1781). Mémoire sur la théorie des déblais et des remblais. *Histoire de l'Académie Royale des Sciences de Paris*, 666–704.
- Otto, F. (2001). The geometry of dissipative evolution equations: The porous medium equation. *Communications in Partial Differential Equations*, 26(1–2), 101–174.
- Peyré, G., & Cuturi, M. (2019). Computational optimal transport. *Foundations and Trends in Machine Learning*, 11(5–6), 355–607.
- Rachev, S. T., & Rüschendorf, L. (1998). *Mass transportation problems: Volume I: Theory*. Springer.
- Santambrogio, F. (2015). *Optimal transport for applied mathematicians*. Birkhäuser.
- Schiebinger, G., Shu, J., Tabaka, M., Cleary, B., Subramanian, V., Solomon, A., … Regev, A. (2019). Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming. *Cell*, 176(4), 928–943.
- Schrijver, A. (2003). *Combinatorial optimization: Polyhedra and efficiency*. Springer.
- Shapley, L. S., & Shubik, M. (1971). The assignment game I: The core. *International Journal of Game Theory*, 1(1), 111–130.
- Sinkhorn, R. (1967). Diagonal equivalence to matrices with prescribed row and column sums. *American Mathematical Monthly*, 74(4), 402–405.
- Sudakov, V. N. (1979). Geometric problems in the theory of infinite-dimensional probability distributions. *Proceedings of the Steklov Institute of Mathematics*, 141, 1–178.
- Villani, C. (2003). *Topics in optimal transportation*. American Mathematical Society.
- Villani, C. (2009). *Optimal transport: Old and new*. Springer.
- [Transportation theory (mathematics)](https://en.wikipedia.org/wiki/Transportation_theory_(mathematics))
