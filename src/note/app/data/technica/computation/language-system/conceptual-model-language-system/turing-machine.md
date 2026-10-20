---
tags: [model-of-computation]
---

# Turing Machine

- [Imperative Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/imperative-model-of-computation.md), [Lambda Calculus](note.html?n=technica/computation/language-system/conceptual-model-language-system/lambda-calculus.md)

> A **Turing machine** is a simple, abstract machine used to model computation. It has a tape divided into cells that can hold symbols, a head that reads and writes symbols on the tape, and a set of rules that tell it how to change states, write symbols, and move the head. It starts with some input on the tape and runs step-by-step until it reaches a special “halt” state, indicating whether the input is accepted or rejected. Despite its simplicity, it can simulate any algorithm.
> 

## Introduction

> A **Turing machine** is an abstract computational device that manipulates symbols on an infinite tape according to a fixed set of rules.
> 

> At the start, the input string is written on the tape with all other cells blank, and the tape head is positioned at the beginning of the input. The machine proceeds step-by-step, consulting the transition function, updating its state and the tape, and moving the tape head accordingly.
> 

> The computation halts when the machine reaches either the accepting or rejecting state. If the machine halts in the accepting state, the input is accepted; if it halts in the rejecting state, the input is rejected. If the machine never halts, **the input is considered not decided**.
> 

> This simple model is powerful enough to simulate any algorithmic process and forms the foundation of computability theory.
> 

It consists of the following components:

- A finite set of **states**, which represent the machine's internal configurations during computation.
- An **infinite tape** divided into discrete cells, each capable of holding one symbol from a finite set called the **tape alphabet**. Among these symbols, a special blank symbol denotes an empty cell.
- A **tape head** that can read and write symbols on the tape and move one cell to the left or right at each step.
- A **transition function** that, given the **current state** and the **symbol currently under the tape** head, determines:
    - The next **state the machine** will enter,
    - The symbol to write in the current cell (possibly the same as the one read),
    - The direction to move the tape head (left or right).
- A distinguished **start state** where computation begins.
- Two distinguished **halting states**: one indicating acceptance and the other rejection of the input.

## Formulation

> A **Turing Machine (TM)** is a fundamental abstract computational model defined as a 7-tuple $M = (Q, \Gamma, \Sigma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$, where:
> 
- $Q$ is a finite set of **states**,
- $\Gamma$ is a finite **tape alphabet** (including a *blank symbol*  $b \in \Gamma$,
- $\Sigma \subseteq \Gamma \setminus \{b\}$ is the **input alphabet**,
- $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$ is the **transition function**,
- $q_0 \in Q$ is the **initial state**,
- $q_{\text{accept}} \in Q$ is the **accepting state**,
- $q_{\text{reject}} \in Q$is the **rejecting state** $q_{\text{accept}} \neq q_{\text{reject}}$.

### Transition Relation

- The **one-step transition relation** $\vdash_M$ on configurations is defined by:

$(q, T, h) \vdash_M (q', T', h') \quad \text{iff} \quad \delta(q, T(h)) = (q', a', d),$

where

$T'(i) = \begin{cases}
a', & \text{if } i = h \\
T(i), & \text{otherwise}
\end{cases}
\quad \text{and} \quad
h' = \begin{cases}
h-1, & \text{if } d = L \\
h+1, & \text{if } d = R
\end{cases}$

### Configuration

- A **configuration** of $M$ is a triple $(q, T, h)$ where:
    - $q \in Q$ is the current state.
    - $T: \mathbb{Z} \to \Gamma$ is the tape content function mapping each tape cell index to a symbol.
    - $h \in \mathbb{Z}$ is the current tape head position.

### Operational Description

- The machine has an infinite tape divided into discrete cells indexed by integers (often $\mathbb{Z}$ or $\mathbb{N}$ with one-sided infinite tape), each cell containing a symbol from $\Gamma$.
- At any computation step, the machine is in a current state $q \in Q$, and the tape head scans one cell containing symbol $a \in \Gamma$.
- The transition function $\delta(q,a) = (q', a', d)$ specifies that:
    - The machine writes symbol $a' \in \Gamma$ into the scanned cell (possibly the same as $a$).
    - The machine moves the tape head one cell in direction $d \in \{L, R\}$.
    - The machine updates its internal state to $q' \in Q$.
- Computation begins with the tape initialized so that the input string $w \in \Sigma^*$ occupies the first ∣w∣|w| cells, the rest filled with blanks $\sqcup$, the head at the leftmost cell of the input, and the machine in the start state $q_0$.
- The machine **halts** if it enters either $q_{\text{accept}}$ or $q_{\text{reject}}$.
- The machine **accepts** an input if it halts in $q_{\text{accept}}$; it **rejects** if it halts in $q_{\text{reject}}$.

## **Variants**

- **Non-deterministic TM**: $\delta$ maps to *sets* of possible transitions (equivalent in power to deterministic TMs).
- **Multi-tape TM**: Multiple tapes (speedup but not computational power).
- **Universal TM**: Simulates other TMs given their descriptions (foundation for programmable computers).

## Case Study

### String Reversal

> 

## QA

### What do we mean by the ‘Current State’?

> The current state is the machine’s internal memory of "where it is" in the computation. It acts like a pointer into the machine’s program, telling it what transition rule to apply based on the symbol being read.
> 

It's analogous to:

- The **program counter** in a CPU,
- The **current line** in a flowchart,
- Or the **active branch** in a decision tree.

## References

- https://en.wikipedia.org/wiki/Turing_machine
- https://plato.stanford.edu/entries/turing-machine/
- Turing Machine Simulators
    - [http://turingmachine.vassar.edu/](http://turingmachine.vassar.edu/)
    - https://turingmachinesimulator.com/
    - https://math.hws.edu/eck/js/turing-machine/TM.html
    - https://morphett.info/turing/turing.html