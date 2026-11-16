---
tags: [note, computation, theory, complexity]
---

# P versus NP

> **P** is the class of decision problems a deterministic machine can decide in time polynomial in the length of the input. **NP** is the class of decision problems whose *yes* instances carry a certificate that a deterministic machine can check in polynomial time. Every problem in P is in NP — the certificate can simply be ignored — and whether the inclusion is strict is the open question.

> The question is one problem wearing a thousand faces. Cook, and independently Levin, showed that the satisfiability of propositional formulas is complete for NP: every problem in the class reduces to it in polynomial time. A polynomial algorithm for satisfiability would therefore be a polynomial algorithm for all of them, and a proof that none exists would separate the classes everywhere at once. Karp then showed twenty-one more problems are complete, in domains that share nothing with logic.

## The two classes

| Class | Machine definition | Witness definition |
| --- | --- | --- |
| **P** | decided by a deterministic Turing machine in $O(n^k)$ steps | no witness is needed: the machine decides without one |
| **NP** | decided by a nondeterministic Turing machine in $O(n^k)$ steps | $x \in L$ iff there is a $y$ with $\lvert y\rvert \le p(\lvert x\rvert)$ and a polynomial-time relation $R(x,y)$ |
| **coNP** | the complements of NP languages | every *no* instance has a polynomial certificate |
| **NP ∩ coNP** | both | a certificate for yes and one for no — the decision version of integer factoring sits here, and is not known to be complete for either |

The two definitions of NP agree by a simulation argument, not by definition: a nondeterministic machine's accepting path *is* a certificate, and a certificate is a path to check. The letter does not stand for "non-polynomial" — a misreading common enough to be worth denying — but for *nondeterministic polynomial time*, the machine that defines the class.

## Completeness

A problem is **NP-complete** when it is in NP and every problem in NP reduces to it in polynomial time. Two consequences follow immediately and both matter: a polynomial algorithm for any one complete problem gives one for the whole class, and a proof of intractability for any one gives it for the whole class. The class has a single hardest problem, repeated.

| Problem | Where it lives in the corpus | Why it is complete |
| --- | --- | --- |
| **Satisfiability (SAT / 3-SAT)** | — (no note yet) | the root: a machine's accepting computation is encoded as a formula whose satisfying assignment is the certificate |
| **Travelling salesman (decision)** | [Travelling Salesman Problem](../algorithm/traveling-salesman-problem.md) | Hamiltonian cycle, which reduces from 3-SAT |
| **Knapsack / subset sum (decision)** | [Knapsack Problem](../algorithm/knapsack-problem.md) | exact cover and partition constructions |
| **Graph colouring** | [Coloring](../algorithm/coloring.md) | 3-colourability reduces from 3-SAT; $k$-colourability from 3-colourability |
| **Bin packing** | [Bin Packing Problem](../algorithm/bin-packing-problem.md) | partition |
| **Job scheduling** | [Job Scheduling Problem](../algorithm/job-scheduling-problem.md) | partition and 3-partition, in the strong sense |

The notes above describe the optimisation problems; their decision versions — "is there a tour of length at most $k$?" — are the NP-complete ones. This is not a technicality: the optimisation problem is at least as hard, and the reduction runs on the decision version.

## What each answer would settle

| If P = NP | If P ≠ NP |
| --- | --- |
| The class collapses: every NP-complete problem has a polynomial algorithm, and finding a solution becomes no harder than checking one | Search is genuinely harder than verification |
| Public-key cryptography as practised — RSA, discrete logarithm, elliptic curves — falls, since its hardness assumptions are in NP | One-way functions may exist, but cryptography additionally needs *average-case* hardness over the distributions keys are drawn from; the worst-case separation supplies none of that |
| The polynomial hierarchy collapses to P, and with it most of the open separation questions in the shelf | NP-intermediate problems exist (Ladner): in NP, not in P, not complete — integer factoring is the standing candidate |
| Approximation, learning and combinatorial optimisation change character: exact answers become feasible where only heuristics were | The practical response is already in place: approximation ratios, parameterised algorithms, and average-case analysis, which is what [Computational Complexity Theory](computational-complexity-theory.md) exists to state precisely |

The gap between "P ≠ NP" and "cryptography is possible" is Impagliazzo's five worlds, and it is worth keeping the ladder in view:

| World | What holds | What it buys |
| --- | --- | --- |
| **Algorithmica** | P = NP | nothing is hard; cryptography ends |
| **Heuristica** | P ≠ NP, but hard problems are rare on the distributions met in practice | the worst case is hard, the typical case is not |
| **Pessiland** | hard problems are common, but no one-way functions | no cryptography, and no easy life either |
| **Minicrypt** | one-way functions exist | private-key cryptography, pseudorandomness |
| **Cryptomania** | public-key cryptography exists | the world RSA is sold in |

## The ladder

$$P \;\subseteq\; NP \cap coNP \;\subseteq\; PH \;\subseteq\; PSPACE \;\subseteq\; EXP$$

Every inclusion is believed strict and none is proved. P versus NP is the bottom rung, which is why it is the one asked first: the higher separations are not known to be easier, but they are known to be implied by it in one direction — if P = NP then the whole hierarchy collapses to P, and the rest of the ladder collapses with it. Non-relativising evidence for strictness at the top (the time hierarchy theorem) exists, but that theorem says nothing about P versus NP, because the hierarchy it gives is by polynomial degree and not by class.

## Why no proof exists yet

Not because nobody has tried, but because the obvious kinds of proof are now known not to work. A barrier is a statement about the *proof*, not about the answer, and any argument must evade all of them at once:

| Barrier | What it says | What it rules out |
| --- | --- | --- |
| **Relativization** (Baker, Gill & Solovay, 1975) | There are oracles $A$, $B$ with $P^A = NP^A$ and $P^B \ne NP^B$ | Any proof that survives the adjunction of an arbitrary oracle — which includes diagonalisation, the technique that settles the time hierarchy |
| **Natural proofs** (Razborov & Rudich, 1997) | A "natural" combinatorial property cannot prove superpolynomial circuit lower bounds unless one-way functions do not exist | A large family of circuit-lower-bound arguments, which is the route the separation is usually attempted by |
| **Algebrization** (Aaronson & Wigderson, 2009) | The relativization barrier survives algebraic oracle access — arithmetisation does not escape it | The proofs that use algebraic extensions of the diagonalisation idea |
| **Proof complexity** (Cook & Reckhow, 1979) | $NP \ne coNP$ would follow from superpolynomial lower bounds for every propositional proof system | A separation via proof length, since no such lower bound is known for any propositional system, including resolution |

Two further facts are worth stating because they are often misreported. The statement is **not known to be independent** of the standard axioms: what is known is that certain weak formal systems cannot prove it, which is a statement about those systems. And independence, were it proved, would settle nothing about the answer — a statement can be independent and true in the standard model.

## Why it is believed

The belief rests on evidence, and the evidence is inductive: a class of problems that has resisted every algorithmic idea for fifty years, and a completeness result that makes the failure of any one problem a failure of all. The pattern is not proof — mathematics has believed false things for longer — but it is the reason the question is treated as a fact to be proved rather than a coin to be flipped.

## References

- https://en.wikipedia.org/wiki/P_versus_NP_problem
- Aaronson, S., & Wigderson, A. (2009). Algebrization: A new barrier in complexity theory. *ACM Transactions on Computation Theory, 1*(1), 1–54. https://doi.org/10.1145/1490270.1490272
- Baker, T., Gill, J., & Solovay, R. (1975). Relativizations of the $P = ? NP$ question. *SIAM Journal on Computing, 4*(4), 431–442. https://doi.org/10.1137/0204037
- Cook, S. A. (1971). The complexity of theorem-proving procedures. In *Proceedings of the Third Annual ACM Symposium on Theory of Computing* (pp. 151–158). ACM. https://doi.org/10.1145/800157.805047
- Cook, S. A., & Reckhow, R. A. (1979). The relative efficiency of propositional proof systems. *The Journal of Symbolic Logic, 44*(1), 36–50. https://doi.org/10.2307/2273702
- Garey, M. R., & Johnson, D. S. (1979). *Computers and intractability: A guide to the theory of NP-completeness*. W. H. Freeman.
- Impagliazzo, R. (1995). A personal view of average-case complexity. In *Proceedings of the Tenth Annual IEEE Conference on Structure in Complexity Theory* (pp. 134–147). IEEE. https://doi.org/10.1109/SCT.1995.514853
- Karp, R. M. (1972). Reducibility among combinatorial problems. In R. E. Miller & J. W. Thatcher (Eds.), *Complexity of computer computations* (pp. 85–103). Plenum Press. https://doi.org/10.1007/978-1-4684-2001-2_9
- Ladner, R. E. (1975). On the structure of polynomial time reducibility. *Journal of the ACM, 22*(1), 155–171. https://doi.org/10.1145/321864.321877
- Levin, L. A. (1973). Universal sequential search problems. *Problems of Information Transmission, 9*(3), 265–266.
- Razborov, A. A., & Rudich, S. (1997). Natural proofs. *Journal of Computer and System Sciences, 55*(1), 24–35. https://doi.org/10.1006/jcss.1997.1494
- Sipser, M. (2013). *Introduction to the theory of computation* (3rd ed.). Cengage Learning. — the class definitions and the completeness proofs in full.
- [Computational Complexity Theory](computational-complexity-theory.md) — the taxonomy this question is asked about · [Turing Machine](turing-machine.md) — the machine the classes count steps of · [Algorithm](../algorithm.md) — the procedures whose cost is at stake
