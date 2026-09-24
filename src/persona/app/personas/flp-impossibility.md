---
type: paper
tags: [consensus, distributed-systems]
---

# Impossibility of Distributed Consensus with One Faulty Process (FLP)

> Michael J. Fischer, Nancy A. Lynch, and Michael S. Paterson, 1985. The paper that bounds what agreement can achieve: in a fully asynchronous system, no deterministic algorithm guarantees consensus with even one faulty process.

## Formulation

### What does the paper prove?

> That every deterministic consensus protocol has at least one non-deciding execution when one process may fail by stopping. Asynchrony makes it impossible to distinguish a crashed process from a slow one, so the protocol can be delayed forever.

### Why does it matter?

> It draws the boundary every later protocol designs against: Paxos, Raft, and PBFT all escape through the exits FLP leaves open — randomization, partial synchrony, or failure detectors.

## References

- [Impossibility of Distributed Consensus with One Faulty Process (PDF)](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf)
