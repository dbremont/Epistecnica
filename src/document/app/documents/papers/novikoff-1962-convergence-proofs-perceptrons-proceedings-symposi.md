---
tags: [paper]
---

# Novikoff, A. B. J. (1962). On Convergence Proofs on Perceptrons. Proceedings of the Symposium on the Mathematical Theory of Automata, 12, 615–622.


## Notes

---

> A short proof in given of the convergence (in a finite number of steps) of an algorithm for adjusting weights in a single-threshold device.
> 

QA:

- …
- How to prove a convergence claim?
- How to proof that a sequence converges to a **fixed point**?

> The theorem states that there exists a vector $y$ such that for every vector $v_i$ in the set, the inner product $(v_i, y)$  is greater than a positive constant $\theta$.   In mathematical terms:  $(v_i, y) > \theta > 0 \quad \text{for all } i = 1, \ldots, N$.
> 

> **Interpretation**: This condition implies that all the vectors $v_i$ have a positive projection onto the vector $y$, and this projection is bounded below by  $\theta$. Geometrically, this means that all the vectors $v_i$ lie within a certain "half-space" defined by the vector  $y$, and they are not too "close" to being orthogonal to $y$.
> 

## Inner Product

> …
> 

For two vectors  $\mathbf{u} = (u_1, u_2, \dots, u_n)$ and  $\mathbf{v} = (v_1, v_2, \dots, v_n)$ in $\mathbb{R}^n$, the **inner product** is defined as:

- $\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = u_1 v_1 + u_2 v_2 + \dots + u_n v_n$
- $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta$; where $\|\mathbf{u}\|$and $\|\mathbf{v}\|$ are the magnitudes (lengths) of the vectors.

## Theorem

Let $v_1, \ldots, v_N$ be a set of vectors in a finite-dimensional Euclidean space. Suppose there exists a vector $y$ such that for each vector $v_i$ in the set, the inner product $(v_i, y)$  is greater than a positive constant $\theta$. That is,

$(v_i, y) > \theta > 0 \quad \text{for all } i = 1, \ldots, N.$

Consider an infinite sequence $v_{i_1}, v_{i_2}, v_{i_3}, \ldots$ , where each $v_{i_k}$ is one of the vectors $v_1, \ldots, v_N$, and each vector $v_1, \ldots, v_N$  appears infinitely often in the sequence.

Define a sequence of vectors $v_0, v_1, \ldots, v_n, \ldots$ recursively as follows:

- Start with an arbitrary vector $v_0$.
- For each $n \geq 1$, define $v_n$  based on the inner product condition:

$v_n =
\begin{cases}
v_{n-1} & \text{if } (v_{i_n}, v_{n-1}) > \theta \\
v_{n-1} + v_{i_n} & \text{if } (v_{i_n}, v_{n-1}) \leq \theta
\end{cases}$

The theorem states that the sequence  $(v_n$) converges. Specifically, there exists an index $n$ such that for all subsequent indices, the vectors remain unchanged: $v_n = v_{n+1} = v_{n+2} = \ldots = v$.

## References

- https://en.wikipedia.org/wiki/Perceptron
- [https://apps.dtic.mil/sti/tr/pdf/AD0298258.pdf](https://apps.dtic.mil/sti/tr/pdf/AD0298258.pdf) [Paper]
- [https://intelligentmachinerycourse.com/wp-content/uploads/2018/09/block_perceptron_1962p.pdf](https://intelligentmachinerycourse.com/wp-content/uploads/2018/09/block_perceptron_1962p.pdf)
- https://en.wikipedia.org/wiki/Error_detection_and_correction
- https://en.wikipedia.org/wiki/Convergent_series
- https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality
- https://en.wikipedia.org/wiki/Dichotomy
- [https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs344+386-s2017/resources/classnote-1.pdf](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs344+386-s2017/resources/classnote-1.pdf)
- [http://www.cs.columbia.edu/~mcollins/courses/6998-2012/notes/perc.converge.pdf](http://www.cs.columbia.edu/~mcollins/courses/6998-2012/notes/perc.converge.pdf)
- 
- [Rosenblatt, F. (1958). *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*. *65*(6), 386–408. https://doi.org/10.1037/H0042519](Rosenblatt,%20F%20(1958)%20The%20Perceptron%20A%20Probabilisti%2010e598edb790810e94a3f30d738d983b.md)
- [Rosenblatt, F. (1961). *Principles of Neurodynamics: Perceptrons and the Theory of Brain Mechanisms*. Spartan Books.](Rosenblatt,%20F%20(1961)%20Principles%20of%20Neurodynamics%20P%2010e598edb7908122953de6e522a65e91.md)
- https://en.wikipedia.org/wiki/Convergent_series
- https://en.wikipedia.org/wiki/Invariant_(mathematics)
- https://en.wikipedia.org/wiki/Inner_product_space
- https://en.wikipedia.org/wiki/Norm_(mathematics)
