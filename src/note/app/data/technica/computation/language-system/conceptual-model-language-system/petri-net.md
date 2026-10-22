---
tags: [model-of-computation]
---

# Petri Net


![petry.png](../assets/note/technica/computation/language-system/conceptual-model-language-system/petri-net/petry.png)

Petri nets are a graphical model of computation used to study systems that involve the interaction of multiple components. The basic building blocks of Petri nets can be described in terms of the building blocks of a general model of computation as follows:

- **Data representation**: In Petri nets, data is represented by tokens, which are depicted as small circles. These tokens can be used to describe resources, entities, or events in the system being modeled.
- **Operations or functions**: In Petri nets, the basic operation is the firing of a transition, which is represented as a rectangular shape with incoming and outgoing arcs. A transition can only fire if it has enough tokens on its input arcs and can produce tokens on its output arcs.
- **Control flow**: The control flow in Petri nets is determined by the state of the system, which is represented by the distribution of tokens among the places in the net. A transition can fire only if its input places have enough tokens and its output places have enough capacity to receive the produced tokens.
- **Memory or storage**: Petri nets do not have an explicit memory or storage component. The state of the system is represented by the distribution of tokens among the places, which can be viewed as a form of distributed storage.
- **Input/output**: In Petri nets, input and output are represented by places that receive or produce tokens, respectively. Input places represent the sources of data or events that trigger the system, while output places represent the results or effects of the system.

Overall, Petri nets provide a way to model complex systems with many interacting components and processes. They can be used to study the behavior of such systems and to analyze their properties, such as reachability, liveness, and deadlock-freeness. The graphical nature of Petri nets makes them easy to understand and visualize, which can aid in the design and optimization of real-world systems.

## References

[Petri Net](https://www.wikiwand.com/en/Petri_net)