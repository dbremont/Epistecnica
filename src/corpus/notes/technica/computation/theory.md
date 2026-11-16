---
tags: [note, computation, theory]
---

# Theory of Computation

> The theory of computation asks what a procedure can do before asking how a machine does it: which strings a machine of a given structure accepts, which problems any machine can decide at all, and which it can decide within a budget. Its answers are limits and equivalences, and they hold for every machine that can be built rather than for the one in front of you.

> Its central result is an equivalence. The Turing machine, the lambda calculus, the recursive functions and every general-purpose computer define the same class of computable functions, which is why the theory speaks about computation and not about a particular device — and why a result proved about a tape machine is a result about every program.

## The three questions

| Pillar | Question | What fixes the answer | Notes |
| --- | --- | --- | --- |
| **Automata and formal languages** | what a machine of a given structure recognises | the machine's memory: none (finite automaton, regular languages), a stack (pushdown automaton, context-free languages), an unbounded tape (Turing machine, recursively enumerable languages) | [Turing Machine](theory/turing-machine.md) |
| **Computability** | what any machine can decide at all | the limits: the halting problem and its relatives, the Church–Turing thesis, the existence of universal machines | [Turing Machine](theory/turing-machine.md), [Lambda Calculus](theory/lambda-calculus.md) |
| **Complexity** | what a machine can decide within a budget | time and space classes, reductions and completeness — P, NP, PSPACE, EXPTIME | [Computational Complexity Theory](theory/computational-complexity-theory.md), [P versus NP](theory/p-versus-np.md) |

The three are one ladder read at three heights: the first asks *which* language a machine accepts, the second asks whether *any* machine accepts it, the third asks what it costs. Each answer is a theorem about a class, and the classes nest — every regular language is context-free, every context-free language is decidable, every decidable language is decidable in exponential time.

## What is on the shelf

| Note | What it carries |
| --- | --- |
| [Turing Machine](theory/turing-machine.md) | the minimal universal machine — tape, head, transition function, halting — and the model every other one is measured against |
| [Lambda Calculus](theory/lambda-calculus.md) | the other universal model: abstraction, application and substitution, the same computable functions in a notation with no machine in it |
| [Computational Complexity Theory](theory/computational-complexity-theory.md) | cost as a function of input size, the asymptotic notation, and the taxonomy of complexity classes |
| [P versus NP](theory/p-versus-np.md) | the open question the taxonomy turns on: whether verification is as hard as search |

## Boundary

- Against [Language System](language-system.md): that shelf is the realisation — parsers, compilers, runtimes, type systems, the languages people write and run. This shelf is the mathematics those rest on. A parser *is* a pushdown automaton, but it is filed there because it is built; a Turing machine is filed here because it is proved about.
- Against [Algorithm](algorithm.md): an algorithm is a procedure for a problem. This shelf says whether the problem is decidable at all and what any procedure for it must cost; the algorithm shelf says which procedure is used and how it is written.
- Against the mathematical shelves ([Mathematical Object](../../epistemica/mathematical/mathematical-object.md)): the objects of the theory — languages, machines, classes — are mathematical objects, but they are kept here because the questions asked of them are about computation, not about a branch of mathematics.
- Against [Complexity Science](../../epistemica/complexity/complexity-science.md): a different use of the same word. Complexity science studies systems whose behaviour is hard to predict; complexity *theory* measures the cost of deciding, and says nothing about emergence.

## References

- https://en.wikipedia.org/wiki/Theory_of_computation
- Sipser, M. (2013). *Introduction to the theory of computation* (3rd ed.). Cengage Learning. — the standard treatment of automata, computability and complexity in one ladder.
- Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, 42(1), 230–265. — the machine and the undecidability result in one paper.
- [Turing Machine](theory/turing-machine.md) · [Lambda Calculus](theory/lambda-calculus.md) · [Computational Complexity Theory](theory/computational-complexity-theory.md) · [P versus NP](theory/p-versus-np.md) — the shelf · [Language System](language-system.md) — the realisation it grounds · [Algorithm](algorithm.md) — the procedures it bounds
