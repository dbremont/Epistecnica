---
tags: [principle]
---

# Coupling


Remember that coupling is connection/interaction with the intra-module.

- Temporal Coupling
- Sequential Coupling

Is temporal coupling sequential coupling? Temporal coupling is a type of coupling where the timing and order of the execution of operations or components in a system depend on one another. Temporal coupling can result in the sequential coupling, where the order of the operations or components is critical to the correct functioning of the system.

What type of coupling is when operations depend on the ordering? When operations depend on the ordering, it is often called “sequential coupling”. Sequential coupling occurs when one component or operation in a system must be performed in a specific order or sequence with another component or operation. This means that the components or operations are coupled in such a way that they cannot be performed independently of one another, but rather must be executed in a particular order.

Sequential coupling can result in the tight coupling, making the system more brittle and difficult to modify. Loose coupling, on the other hand, refers to a system where the components or operations can be performed independently, with less or no dependency on the order in which they are executed. Loose coupling can make a system more flexible and easier to modify.

However, temporal coupling can also occur in cases where the order of operations is not necessarily sequential but where the timing of the operations is still important. For example, if one component in a system needs to be executed within a certain time frame relative to another component, this would be an example of temporal coupling but not necessarily sequential coupling.

Therefore, while temporal coupling and sequential coupling are related, they are not the same thing. Temporal coupling is a more general term that encompasses any kind of coupling that depends on timing or order. In contrast, the sequential coupling is specifically concerned with a coupling that results from the requirement that operations be performed in a specific order.

See how an event system can help to produce temporal coupling between components.

## References

- [https://www.wikiwand.com/en/Sequential_coupling](https://www.wikiwand.com/en/Sequential_coupling)
- [https://blog.ploeh.dk/2011/05/24/DesignSmellTemporalCoupling/](https://blog.ploeh.dk/2011/05/24/DesignSmellTemporalCoupling/)