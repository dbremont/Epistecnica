---
tags: [document, paper, machine-learning, cellular-automata, emergence, computation]
---

# Emergent Models: Intelligence from Tiny Substrates (2026). *arXiv*:2608.14019. https://arxiv.org/abs/2608.14019

## Notes

> The paper proposes **Emergent Models** (EMs): a learning paradigm built on *simple but open-ended substrates* — the paper's own example is the **cellular automaton** — in which modelling is not the learning of a closed-form input–output map but the **emergence, inside a simple dynamical system, of computational behaviours that solve an external task**.

**The architecture, as the abstract states it:**

| Element | Description |
| --- | --- |
| **Substrate** | A simple local rule (a cellular automaton being the canonical case) iterated over a latent space |
| **Adaptive iteration** | The number of steps is not fixed — the system runs until its behaviour solves the task |
| **Interface** | A link between the latent state and external input/output signals, so the dynamics can be trained against a task |
| **Training** | **Evolutionary search** rather than gradient descent — the rule is the genotype, the behaviour is the phenotype |

> The claim is a hypothesis rather than a result at the time of writing: that some instances of this framework reach behaviour that generalises, which would make the substrate — not the network — the unit of learning. Read against the corpus's machine-learning notes, the interest is the **training signal**: evolutionary search needs only a fitness, so it can train systems that are not differentiable, and the CA is the cleanest such system.

> Read against [Cellular Automata](/view.html?p=notes/epistemica/mathematical/change/cellular-automata.md), the paper is the computational claim that note already makes — a CA with a suitable rule is a computer — turned into a learning paradigm: the rule is fixed, the behaviour is what is selected. It is also the strongest contemporary answer to the objection that CA are models *of* computation but not *for* it.

## References

- [Emergent Models — arXiv](https://arxiv.org/abs/2608.14019)
- [Cellular Automata](/view.html?p=notes/epistemica/mathematical/change/cellular-automata.md) — the substrate, and the Turing-completeness argument
- [Adaptive Systems](/view.html?p=notes/epistemica/adaptative/adaptative.md) — the learning frame
- [Evolutionary Computation](/view.html?p=notes/epistemica/optimization/evolutionary-computation.md) — the training method
