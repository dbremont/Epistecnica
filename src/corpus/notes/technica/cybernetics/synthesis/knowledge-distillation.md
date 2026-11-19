---
tags: [note, machine-learning, distillation, training]
---

# Knowledge Distillation

> Transferring what one model has learned into another. The classical case is **compression**: a large teacher, a smaller student, and the student trained to match the teacher's output distribution rather than only the hard labels — the soft targets carry the teacher's uncertainty and its similarity structure, which is the extra information that makes the small model better than one trained on labels alone.

## Two uses, not one

> The definition above is the textbook one, and it covers only half of what the technique now does. The other half inverts its purpose:

| Use | Direction | What is transferred | Why |
| --- | --- | --- |
| **Compression** | many parameters → fewer | the teacher's *function*, in a cheaper model | deploy the capability at lower cost |
| **Integration** | many specialists → one generalist | several teachers' *capabilities*, into one model | combine skills that were trained separately |

> In the second use the student is not smaller and the goal is not efficiency: a set of domain-specialised models — each pushed by reinforcement learning on its own task — are consolidated into a single model that should retain nearly all of each. The technique is the same; the economics are opposite.

## Why the on-policy detail matters

> A distillation loss is computed on **states**. The classical form trains the student on states drawn from the teacher's distribution (or from data), while at inference the student visits *its own* states — so its errors take it where it was never trained, and they compound. Training on the student's own rollouts, with the teacher scoring each state the student actually reached, removes that mismatch. It is the same correction imitation learning needed (DAgger), and it is the difference between a distilled model that matches its teacher in the lab and one that holds up when it runs.

## In the corpus

> The compression case is the ordinary one and needs no citation. The integration case is documented by [MOPD](/view.html?p=documents/papers/mopd-2026.md), which trains one RL teacher per domain, then distils all of them into a shared student on the student's own rollouts — and argues that this modular route beats mixing the rewards in a single RL run. The general lesson: distillation is a **transfer of a distribution**, so it can move capability in any direction the distributions allow, including sideways between peers.

## References

- [MOPD (2026) — Multi-Teacher On-Policy Distillation](/view.html?p=documents/papers/mopd-2026.md) — the integration use
- [Training](/view.html?p=notes/technica/cybernetics/synthesis/training.md) — the training shelf
- [Reinforcement Learning](/view.html?p=notes/epistemica/adaptative/reinforcement-learning-rl.md) — how the specialist teachers are made
