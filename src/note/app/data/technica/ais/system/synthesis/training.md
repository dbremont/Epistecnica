---
tags: [technique, training]
---

# Training

 : Transformer System: Training (Transformer%20System%20Training%2031fc0f5171ec80f1b717c78ede39a9db.md)

> In this note, we will build a **conceptual schema** related to the **training and synthesis of computational systems**.
> 

Guiding Questions:

- How should we think about the **training (synthesis) of a synthesized computational system**?
- Which techniques are used to train such systems?
- How to frame teaching? Which are the teaching strategies? Masking, etc.
- Which tasks are **incidental to training** (e.g., monitoring, debugging, evaluation)?
- Which principles guide the training process?
- What are the common **pitfalls and failure modes** encountered during training?
- How to scale the training?

## Monitoring

**Guiding Questions:**

- How to visualize and monitor the training? (A Model of the Model) → The Dynamics of the Training,  Performance Visualization, Time, Loss,  current parameters,  etc.

Training Visualization:

- Plot loss vs epoch
- Plot weight evolution

Performance Visualization:

- Plot predicted vs actual outputs
- Confusion matrix (2×2 for binary)

Experiment Tracking:

- Log initialization, learning rate, activation, optimizer type

## References

- https://github.com/dbremont/mlsys-lab/tree/main/protonn
