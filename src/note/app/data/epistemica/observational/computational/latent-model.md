---
tags: [learning-system]
---

# Latent Model


> 

## 🔍 **What does “latent” mean?**

In the context of statistics, machine learning, and dynamical systems, **latent** means **not directly observable**. A *latent variable* or *latent state* is something we *infer* from the data but cannot measure or observe directly.

Examples:

- In psychology, intelligence or anxiety is latent—you can't measure them directly, but you can estimate them from test results or behavior.
- In topic modeling, the topics are latent, inferred from the frequency and co-occurrence of words.
- In physics-based models or robotics, true positions or forces might be latent if sensors are limited or noisy.

## 🔮 **What does it mean to “predict a latent state”?**

It means to estimate or forecast the value of an unobserved variable based on:

- **Observed variables** (data you *can* measure),
- **A model** that describes the relationship between latent and observed variables.

This often appears in **state-space models** (e.g., Kalman filters, HMMs, or RNNs), where:

- The **latent state** evolves over time (e.g., position, velocity).
- You receive **noisy observations** (e.g., GPS signals, sensor readings).
- You use those observations to estimate or predict the current or future **true (latent) state**.

## 🧩 **If the state is hidden, is its structure also unknown?**

Not necessarily.

There are **two separate notions** here:

1. **Unobserved value** (latent): You can't see the *current value* of the state directly.
2. **Unknown structure**: You don’t know how many variables make up the state, what equations describe it, or what distributions they follow.

You might know the **structure** of the latent state, but not its **value**:

- For example, in a Kalman filter, you might know the state is a vector `[position, velocity]`, and how it evolves (the motion model), even if you can’t measure it directly.

## References

- https://en.wikipedia.org/wiki/Latent_and_observable_variables
