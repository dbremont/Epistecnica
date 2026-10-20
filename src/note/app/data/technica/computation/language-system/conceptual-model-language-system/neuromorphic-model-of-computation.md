---
tags: [model-of-computation]
---

# Neuromorphic Model of Computation


> 

## 🧠 **Key Principles of Neuromorphic Computing**

> Neuromorphic systems aim to mimic biological nervous systems. Core principles include:
> 

| **Principle** | **Description** |
| --- | --- |
| **Event-Driven** | Computation happens when signals (spikes) are received, not on a fixed clock. |
| **Spiking Neural Networks (SNNs)** | Information is processed using spikes (discrete events) rather than continuous values. |
| **Local Memory & Computation** | Each "neuron" processes and stores locally, unlike von Neumann architecture. |
| **Parallelism** | Many neurons and synapses operate simultaneously. |
| **Low Power** | Energy-efficient due to sparsity and locality. |

## Computation

> 

| **Concept** | **Example** |
| --- | --- |
| **Representation** | Encode values as spike rates or spike timings. |
| **Computation** | Spikes are processed through a network → output spikes represent the result. |
| **Learning** | The system adapts weights (synapses) based on spike patterns. |

## References

- https://en.wikipedia.org/wiki/Neuromorphic_computing
- https://github.com/nengo/nengo
- https://uci-carl.github.io/CARLsim3/
- https://www.fz-juelich.de/en/ias/jsc/about-us/structure/simulation-and-data-labs/sdl-neuroscience/teams/testteams/large-scale-simulation-and-neuromorphic-systems