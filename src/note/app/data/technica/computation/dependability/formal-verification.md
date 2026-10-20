# Formal Verification

> Studying program correctness is essential to ensure that software behaves as intended, preventing costly, dangerous, or catastrophic failures in critical systems across various domains.
> 

> Given a formal specification, how can we verify that a system meets its formal requirements?
> 

Guiding questions:

- How to think about the **technical domain (framework)** of **Formal Verification**? How to make a technical **element map** and decompositio
- How is the overlap with automated - verification?
- Technical Problem  Space:
    - How to verify **Enterprise Information Systems (EIS)**?
    - …
- Which are the branches of formal verification?
    - Model Checking
    - ATP (Automated Theorem Prover)
    - …

| **Model** | **Description** | **Application Areas** |
| --- | --- | --- |
| **Hoare Logic** | Uses preconditions, postconditions, and loop invariants to reason about the correctness of programs. | Sequential programs |
| **Model Checking** | An automated technique that explores the state space of a program to verify it against a specification. | Concurrent and finite state systems |
| **Type Systems** | Uses data type information in programs to enforce correctness properties, such as no type errors during execution. | General programming, functional languages |
| **Symbolic Execution** | Analyzes programs by following paths of execution symbolically rather than with actual inputs, to check paths for errors and generate test cases. | Software testing and analysis |
| **Abstract Interpretation** | A static analysis technique that over-approximates the behaviors of a program to prove properties like absence of certain kinds of errors. | Static code analysis |
| **Temporal Logic** | A formalism for describing sequences of actions or events; used in model checking to specify and verify properties of reactive systems. | Reactive and concurrent systems |
| **Deductive Verification** | Uses formal methods to prove the correctness of algorithms, typically involving theorem proving. | Algorithms and critical software components |
| **Bisimulation** | A method for comparing the behavioral equivalence of two systems, often used to check the correctness of process algebra and concurrent systems. | Concurrent systems |
| **Petri Nets** | A mathematical modeling tool suitable for describing and studying systems that are characterized by concurrent, asynchronous, distributed, parallel actions. | Workflow and process management |

## References

- [Coq](note.html?n=technica/computation/language-system/conceptual-model-language-system/coq.md)
- [Hoare logic](https://en.wikipedia.org/wiki/Hoare_logic)
- [Verification](note.html?n=technica/computation/dependability/verification.md)
- [Formal System](https://app.notion.com/p/Formal-System-41d02881d0544314b0e7ad3e6ada608a?pvs=21)
- https://www.sqlite.org/testing.html
- https://en.wikipedia.org/wiki/Formal_verification
- https://cmu-fantastic-bugs.github.io/
- [*A Survey of Automated Techniques for Formal Software Verification*](http://www.kroening.com/publications/view-publications-dkw2008.html), by D'Silva et al., *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, v. 27(7), pp. 1165-1178, 2008
- (Automated Theorem Prover) Robinson, John Alan. "A machine-oriented logic based on the resolution principle." *Journal of the ACM (JACM)* 12.1 (1965): 23-41.
- (Model Checking) Emerson, E. Allen, and Edmund M. Clarke. "Using branching time temporal logic to synthesize synchronization skeletons." *Science of Computer programming* 2.3 (1982): 241-266.
- https://www.youtube.com/watch?v=BGg-gxhsV4E&list=PLre5AT9JnKShFK9l9HYzkZugkJSsXioFs
- Davis, Martin, George Logemann, and Donald Loveland. "A machine program for theorem-proving." *Communications of the ACM* 5.7 (1962): 394-397.
- https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/
- https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/