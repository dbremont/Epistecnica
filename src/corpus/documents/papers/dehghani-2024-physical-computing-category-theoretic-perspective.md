---
tags: [document, computation, category-theory, physics]
---

# Dehghani, N., & Caterina, G. (2024). Physical computing: a category theoretic perspective on physical computation and system compositionality. https://doi.org/10.1088/2632-072X/ad6051

```python
@article{dehghani2024physical,
  title = {Physical computing: a category theoretic perspective on physical computation and system compositionality},
  author = {Dehghani, Nima and Caterina, Gianluca},
  journal = {Journal of Physics: Complexity},
  volume = {5},
  number = {3},
  pages = {035005},
  year = {2024},
  doi = {10.1088/2632-072X/ad6051},
}
```

## Notes

The question is old and embarrassing: when does a physical system compute? Two answers fail in opposite directions. Putnam's simple mapping account is too generous — any system whose micro-states can be mapped onto a machine table is a computer, and since the mapping can nearly always be found, everything computes, which is pancomputationalism and the end of the question. A definition built on what a system *does* is too vague — "it processes information" applies to a rock falling as readily as to a processor. The paper's move is to keep the representational core of the best existing answer and give it the one thing it lacks: a formal constraint on the mapping.

That answer is Horsman, Stepney, and Kendon's Abstraction/Representation (AR) theory, which asks when a physical system's evolution matches the evolution of its abstract representation, and draws the compute cycle as a commuting diagram: a physical system `p` is represented as `m_p` by the modelling relation `R_T` of a theory `T`, the abstract dynamics `C_T` takes `m_p` to `m_p′`, the physical dynamics `H(p)` takes `p` to `p′`, and the diagram commutes. AR is the right shape — computation is a relation between a physical system and a representation, not a property of either alone — but it places no restriction on what the representation may be, so it risks the same permissiveness as the simple mapping account.

The formalism is category theory, and the construction is compact. **`PhysProc`** is the category of concrete physical processes: physical systems are the objects, a morphism `A → B` is a process transforming a system of type `A` into one of type `B`, processes take finite time, sequential composition is composition, and identity processes leave the system invariant. **`AbsProc`** is the category of abstract processes, with **`Comp`** as a pragmatic concrete choice: data types as objects, programs as morphisms, sequential composition as composition — plus a **null object** that serves as both initial and final, a placeholder for physical systems that have no abstract representation under a given `ℛ_T`. The null object is the detail that keeps the framework honest: it lets a system be an object of `PhysProc` while admitting that, under this theory, it computes nothing.

A physical computation is then defined as a **pair of functors** with the inverse conditions:

```text
ℛ_T  : PhysProc → AbsProc
ℛ̃_T  : AbsProc → PhysProc

ℛ_T ∘ ℛ̃_T = Id_AbsProc
ℛ̃_T ∘ ℛ_T = Id_PhysProc
```

Two consequences follow immediately. First, the "amount" of computation a system performs becomes the **size of the image** of `ℛ_T`: a system capable of universal computation yields a maximal image, and a system that computes nothing admits no such functor at all — the ascription is no longer a matter of taste but a question with an answer, relative to a stated theory. Second, the commuting diagram that AR drew informally is now a statement about functors, so the same machinery carries the relations between representations and between theories.

The second half of the paper is what the category buys. **Sequential composition** of processes is composition in the category. **Refinement and hierarchical composition** are reinterpreted as **natural transformations**: two representations that consistently perform the same computation must share structural properties, and the requirement is expressed as the existence of a natural transformation in the functor category from `PhysProc` to `AbsProc`. **Multiple realizability** — one abstraction, many physical substrates, the thesis Putnam introduced and Marr's tri-level picture assumes — becomes an **adjoint pair**: the strict inverse of `ℛ_T` is relaxed to a pair `(ℛ_T, ℛ̃_T)` that is adjoint, giving functional isomorphism where the paper's own examples would otherwise demand identity. **Nested composition** then allows a physical process to contain an abstract one and vice versa, which is what layered systems actually look like.

The discussion is where the framework is defended rather than applied. Representation and computation: the theory-relativity is explicit, because `ℛ_T` is indexed by the theory that supplies the representation. Computation and scale: the same physical system can carry different computations at different levels of description. Dynamics, information, and causality: the paper separates the computational reading from the informational one, and from the causal one. And the "Pandora's box of pancomputationalism" is addressed directly — the point of the inverse conditions is not to prove that rocks do not compute but to make the claim falsifiable, since a would-be computation that cannot exhibit the functor pair is not one under the stated theory. The closing argument borrows Deutsch's criterion: a good explanation is hard to vary, and a mapping account that can be adjusted to fit any observation explains nothing.

What the paper does not settle, and does not claim to: it licenses an ascription once a representation is chosen, but the choice of representation remains the modeller's act. Two physicists with different theories can disagree about whether a system computes, and the formalism will not adjudicate between them — it only makes each answer precise and vulnerable. Read that way, the contribution is a criterion of rigour rather than a discovery about which systems compute.

Provenance: the preprint is `arXiv:2210.00392`, first posted in October 2022 and revised through v4 on 31 December 2023; the journal version appeared in *Journal of Physics: Complexity* on 17 July 2024, open access under CC BY 4.0, which is the year cited here. The first author has also recorded a talk on the same question, listed below.

## References

- https://doi.org/10.1088/2632-072X/ad6051
- https://iopscience.iop.org/article/10.1088/2632-072X/ad6051
- [arXiv:2210.00392](https://arxiv.org/abs/2210.00392) — preprint, v4 dated 31 December 2023
- [Dehghani, N. — "What is 'Physical Computation'? Computational closure and System Compositionality"](https://www.youtube.com/watch?v=iXiZRvFW-6U) (talk, YouTube) — the first author on the paper's question; the talk's phrase "computational closure" is its own framing, not a term the paper uses
- [Theory of Computation](/view.html?p=notes/technica/computation/theory.md) — the field whose definitional question this paper addresses
- [Category](/view.html?p=notes/epistemica/mathematical/structure/category.md) — the formal language the argument is built in
- [(Hardware) Physical Substrate](/view.html?p=notes/technica/computation/platform/hardware-physical-substrate.md) — the instantiation side, read technically
- [Quantum Computation](/view.html?p=notes/technica/computation/quantum-computation.md) — the development that motivates redefining physical computing
- [Computer Science](/view.html?p=notes/epistemica/epistemic/discipline/computer-science.md) — the discipline that owns the question
