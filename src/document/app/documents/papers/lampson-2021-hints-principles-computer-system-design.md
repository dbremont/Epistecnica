---
tags: [physical]
---

# Lampson, B. (2021). Hints and Principles for Computer System Design. https://arxiv.org/abs/2011.02455


```bash
@misc{lampson2021hintsprinciplescomputerdesign,
      title={Hints and Principles for Computer System Design}, 
      author={Butler Lampson},
      year={2021},
      eprint={2011.02455},
      archivePrefix={arXiv},
      primaryClass={cs.DC},
      url={https://arxiv.org/abs/2011.02455}, 
}
```

## Index

## Notes

---

> List of hints (goals and techniques) for design systems.
> 

> List of principles for achieving the design goals.
> 

> Characterization of the process of software design.
> 

> List of opposition to remember that systems design is an art.
> 

## Topics

- Computer System
- System Success Factors
- Types of Software Systems
- Hints
    - Goals
    - Techniques
    - Processes
- Principles
- Oppositions

> There are also some principles (about abstraction and modules) that almost always apply, and some oppositions that suggest different ways to look at things.
> 

> STEADY by AID with ART
> 
- **What?** **Goals** **STEADY** — Simple, Timely, Efficient, Adaptable, Dependable, Yummy
- **How?** **Techniques** by **AID** —Approximate, Incremental, Divide & Conquer
- **When**, who? **Process** with **ART** —Architecture, Automate, Review, Techniques, Test

## On Designing Computer Systems

Designing a computer system is very different from creating an algorithm: - The external interface (the requirements) is more complicated, fuzzy, and changeable. - The system has much more internal structure, and hence many internal interfaces. - The measure of success needs to be clarified.

## Hints

There are a lot of hints, but here are the most important ones:

- Keep it simple.
- Write a spec.
- Design with independent modules.
- Exploit the ABCs of efficiency.
- Treat state as both being and becoming.
- Use eventual consistency to keep data local.

## Principles

> The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise. —Edsger Dijkstra
> 
- Abstraction—Have a spec.
- Writing a spec—KISS: Keep It Simple, Stupid.
- Writing the code: Correctness—Get it right.
- Modules and interfaces—Keep it clean. Keep basic interfaces stable.
- Points of view: Metamodels

## Techniques

> Techniques are the ideas and tools that you use to build a system; knowing about them keeps you from reinventing the wheel.
> 

> AID (Approximate, Incremental, Divide & Conquer).
> 

Questions to evalute techniques: - What it is. - Why it’s good. - How it can go wrong (when to avoid it; things to watch out for) 

I **describe** most of the **techniques** in the context of a goal, telling you for each one:

- **Simple**: Abstraction, action, extensible, interface, predictable, spec.
- **Efficient**: Algorithm, batch, cache, concurrent, lazy, local, shard, stream, summarize, translate.
- **Adaptable**: Dynamic, index, indirect, scale, virtualize.
- **Dependable**: Atomic, consensus, eventual, redundant, replicate, retry.
- **Incremental**: Becoming, indirect, interface, recursive, tree.

## Process

**Process** with **ART** —Architecture, Automate, Review, Techniques, Test.

- **Architecture**: Design that gets done and documented so that everyone can learn it.
- **Automation**: Code analysis tools (very cheap for the errors they can catch) and build tools.
- **Review**: Design review—manual, but a much cheaper way to catch errors than testing.
- **Review**: Code review—manual, but still cheaper than testing.
- **Testing**: Unit and component tests; stress and performance tests; end-to-end scenarios

## Oppositions

| Goal | Opposition | Slogan |
| --- | --- | --- |
| Principles | Spec ↔ code | Have a spec. Get it right. Keep it clean. |
| Simple | Simple ↔ Rich | KISS: Keep It Simple, Stupid. Don’t generalize. |
| Timely | Precise ↔ approximate software | Get it right. Make it cool |
| Efficient | Time ↔ space | ABCs. Use theory. Latency vs. bandwidth. |
| **Adaptable | Fixed ↔ Evolving | The only constant is change. |
| Dependable | Generate ↔ Check | Trust but verify. |
| Yummy | Simple ↔ rich | KISS: Keep It Simple, Stupid. |
| Incremental | Being ↔ becoming | Take small steps. |
| Process | … | Build on a platform. Keep interfaces stable. |

## References

- Lampson, B. (2020). Hints and Principles for Computer System Design. [https://doi.org/10.48550/arxiv.2011.02455](https://doi.org/10.48550/arxiv.2011.02455)
