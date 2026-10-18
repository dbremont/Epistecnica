---
tags: [fixed-structure-parametric-model, graph-data, process-representation, technique]
---

# Exponential Random Graph Model (ERGM)


> Models network structure by representing the probability of edges based on node attributes.
> 

> **Exponential Random Graph Models (ERGMs)** explicitly model the **data-generating process (DGP)** of networks (graphs) by mathematically representing how local structural features (e.g., edges, triangles, degree distributions) probabilistically give rise to observed network data.
> 

> **Note:** This is a hypothetical statistical data generation simulation model, not necessarily representative of the underlying mechanisms. It’s simply an effective model.
> 

> 

## Index

QA:

- How ERGMs Represent the Data-Generating Process? **** [**How ERGMs Represent the Data-Generating Process?**](exponential-random-graph-model-ergm.md)

## Breviarium

An **ERGM** says:

- *"Suppose* the observed network $G$ is drawn randomly *from a distribution* where the probability of a graph depends on certain structural features (edges, triangles, etc.) via an exponential-family form."
- It **hypothesizes** that the network was generated from a stochastic process driven by these features, weighted by parameters $\theta$.
- It **does not claim** that the real-world process *literally* followed this model, unless the model is a perfect fit.

ERGMs define a **probability distribution over all possible graphs** with a fixed number of nodes, where the likelihood of observing a specific graph $G$ depends on:

- **Sufficient statistics** $s_i(G)$: User-specified features of the graph (e.g., number of edges, triangles, or homophily patterns).
- **Parameters** $\theta_i$: Weights that quantify how strongly each feature influences the graph's formation.

The probability of $G$ is: 

$P(G | \theta) = \frac{1}{\kappa(\theta)} \exp \left( \sum_{i} \theta_i s_i(G) \right)$,

where $\kappa(\theta)$ is a normalizing constant ensuring probabilities sum to 1.

## Formal Specification

The probability of a graph $G$ (or $Y = G$) is modeled as:

$P(Y = G) = \frac{1}{\kappa(\theta)} \exp\left( \theta^T s(G) \right)$

where:

- $\theta \in \mathbb{R}^d$ is the **parameter vector**,
- $s(G) \in \mathbb{R}^d$ is the **vector of sufficient statistics** (features of the graph),
- $\kappa(\theta)$ is the **normalizing constant** ensuring the probabilities sum to 1:
    - $\kappa(\theta) = \sum_{G'} \exp\left( \theta^T s(G') \right)$  over all possible graphs $G'$ on the given node set.
    - Hard to compute directly because it requires summing over *all* possible graphs.
    - In practice, estimation uses **MCMC** techniques to sidestep explicit calculation.

### **Parameter Vector**

> Each statistic gets a weight:
> 
- A *positive* $\theta_i$ encourages the corresponding feature to appear more.
- A *negative* $\theta_i$ discourages it.

### **Sufficient Statistics s(G)**

> These encode *features* of the graph you think are important. Examples include:
> 
- **Edges**: total number of edges.
- **Triangles**: number of triangles (captures clustering).
- **k-stars**: a node connected to $k$ other nodes.
- **Degree distribution** features.
- **Homophily** terms (nodes with similar attributes connecting).
- **Geometrically Weighted Degree (GWD)** or **Geometrically Weighted Edgewise Shared Partners (GWESP)** (for modeling more complex degree patterns and clustering).

## Limits

> ..
> 

**Limitations in Modeling DGP**

- **Assumption-Driven**: Requires *a priori* choice of $s_i(G)$. Misspecified statistics lead to poor DGP representation.
- **Degeneracy**: Some parameter values generate unrealistic graphs (e.g., near-empty or near-complete networks).
- **Intractability**: Calculating $\kappa(\theta)$ requires MCMC sampling for large graphs.

**When to Use ERGMs?**

- **Hypothesis Testing**: Test if specific features (e.g., triangles) drive network formation.
- **Policy Simulation**: Simulate how banning certain ties (e.g., smoking influences) affects the network.
- **Comparative Analysis**: Compare generative rules across cultures/organizations.
    
    

## Case Study

> …..
> 

## QA

### **How ERGMs Represent the Data-Generating Process?**

**Local Mechanisms → Global Structure**

ERGMs assume that the observed network emerges from **local stochastic processes** governed by the selected statistics. For example:

- **Edges $\theta_1$**: Baseline propensity for ties to form.
- **Triangles $\theta_2$**: Tendency for transitive closure ("friends of friends become friends").
- **Degree distribution $\theta_3$**: Controls whether nodes have similar/hub-like degrees.

**Interpretation of Parameters**

- **Positive $\theta_i$**: The corresponding feature $s_i(G)$ appears more often than expected by chance.
- **Negative $\theta_i$**: The feature is suppressed in the network.

**Analogous to Regression**

- Like logistic regression predicts binary outcomes, ERGMs predict tie existence based on network features.
- Example: If $\theta_2 > 0$, networks with many triangles are more likely, implying **triadic closure** is a generative mechanism.

## References

- Lusher, D., Koskinen, J., & Robins, G. (2013). *Exponential Random Graph Models for Social Networks*.
- Snijders, T. A. B. (2002). *Markov Chain Monte Carlo Estimation of Exponential Random Graph Models*.
