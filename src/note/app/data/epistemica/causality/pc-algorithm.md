---
tags: [causal-discovery]
---

# PC Algorithm

Formula: 12

> aka. PC Algorithm (Peter-Clark Algorithm).
> 

> The **PC Algorithm** is a **constraint-based causal discovery method** used to learn the causal structure (a Directed Acyclic Graph, DAG) from observational data. It was developed by **Peter Spirtes and Clark Glymour** (hence “PC”) and is widely used in statistics, machine learning, and bioinformatics.
> 

## What does it do?

- It takes data and **infers the causal graph structure** by testing conditional independencies between variables.
- The output is a **causal skeleton** (undirected graph) plus orientation of edges where possible, resulting in a **partial ancestral graph** or a **completed partially directed acyclic graph (CPDAG)** representing the Markov equivalence class of DAGs compatible with the data.

## How does it work? (High-level steps)

1. **Start with a complete undirected graph** where every variable is connected to every other.
2. **Remove edges** between variables that are conditionally independent given some subset of other variables (using statistical independence tests).
3. **Orient edges** based on discovered independencies and specific rules to avoid cycles and preserve conditional independencies.
4. **Output** the resulting graph encoding possible causal relations consistent with the data.

## Assumption

- **Causal Markov Condition:** Each variable is independent of its non-effects given its direct causes.
- **Faithfulness/ Stability:** All and only the conditional independencies implied by the causal graph are present in the data.
- **No hidden confounders:** All common causes of measured variables are included in the dataset (causal sufficiency).
- **Data is i.i.d.**

## Use

- Inferring gene regulatory networks from gene expression data.
- Social sciences for uncovering causal relationships.
- Economics and epidemiology for causal structure learning.

## Limitation

- Sensitive to statistical errors in independence tests.
- Assumes no latent confounders (though extensions like FCI algorithm handle that).
- Computationally intensive for large numbers of variables.

## References

- Spirtes, P., Glymour, C., & Scheines, R. (2001). Causation, prediction, and search. MIT press.  [https://ics.uci.edu/~dechter/courses/ics-295cr/2021-22_Q2_Winter/reading/Causation_Prediction_and_Search.pdf](https://ics.uci.edu/~dechter/courses/ics-295cr/2021-22_Q2_Winter/reading/Causation_Prediction_and_Search.pdf)
- …
