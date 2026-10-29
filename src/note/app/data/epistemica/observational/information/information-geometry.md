---
tags: [probability]
---

# Information Geometry

 : Shannon Information Theory (Shannon%20Information%20Theory%20a22d92f3a8b845698e10e8039544dad3.md), Information (Information%2017ac0f5171ec813d813ff6055c98fe7d.md), Fisher Information (Fisher%20Information%204cefa509a9c94f7b912cfbdc477adbec.md)

> **Information geometry** is a field at the intersection of **differential geometry, probability theory, and statistics**. It studies the geometric structures that arise naturally when you treat **families of probability distributions** as *manifolds*.
> 

> What is a **family of probability distribution**? Take a distribution Let Sat N {}
> 

Information geometry provides the "shape" of the space of probability distributions. It tells us:

- How distributions relate to each other.
- How to move optimally through the space (e.g., when learning or estimating).
- How information (in Fisher’s sense) constrains inference and learning.

## **Family of Probability Distribution**

A  family of distributions is a set of probability distributions $\mathcal{P} = \{ p(x;\theta) \mid \theta \in \Theta \}$,

where:

- $x$ is the random variable (observed data),
- $\theta$ is the parameter (unknown, varies in parameter space $\Theta$).
- Each **point** in $\Theta$ corresponds to one distribution in the family.

Case:

- Bernoulli Family:  $p(x;\theta) = \theta^x (1-\theta)^{1-x}, \quad \theta \in (0,1)$
- Normal Family**:** $p(x;\mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad \mu \in \mathbb{R}, \sigma > 0$

Manifold View

- The parameter space $\Theta$ can be seen as a **differentiable manifold**.
- Each distribution $p(x|\theta)$ is a point on this manifold.
- Tangent vectors at a point $\theta$ are given by derivatives of $\log p(x;\theta)$ w.r.t. parameters.

## Statistical Manifold

> 

## Use

- **Statistics**: Clarifies the geometry of maximum likelihood estimation, hypothesis testing, and sufficiency.
- **Machine Learning**: Natural gradient descent (Amari’s method) uses information geometry to optimize more efficiently by following the manifold’s structure instead of plain Euclidean space.
- **Physics**: Applied in statistical mechanics, thermodynamics, and quantum information.
- **Information Theory**: KL divergence and other divergences have geometric interpretations as distances on these manifolds.

## QA

- What Problems Do the Tools Solve?
- How does problems related to core statitical - proabilty thoery?
- What are the tools used?

## References

- https://en.wikipedia.org/wiki/Information_geometry
- [‣](https://app.notion.com/p/275598edb79080db98e5cc50af744331?pvs=21)
- [Distribution](distribution-2.md)
- https://differentialgeometri.wordpress.com/2022/07/07/information-geometry-and-optimal-transport/
- https://www.youtube.com/playlist?list=PLvVaDdaHGtpesn2DHUo6ete-1pPhT1xzj
- https://www.youtube.com/playlist?list=PLHZhjPByiV3L94AeJ9FcK1yrnRDOt3Vit
- Khan, Gabriel, and Jun Zhang. "When optimal transport meets information geometry." Information Geometry 5.1 (2022): 47-78.
- https://en.wikipedia.org/wiki/Statistical_manifold
- https://www.reddit.com/r/math/comments/1htom49/information_geometry/
- https://mathoverflow.net/questions/215984/research-situation-in-the-field-of-information-geometry
- https://mathoverflow.net/questions/480903/examples-of-problems-in-statistics-accessible-only-using-information-geometry
- https://mathoverflow.net/questions/344452/introduction-to-information-geometry-and-or-geometric-control-theory
- https://www.robots.ox.ac.uk/~lsgs/posts/2019-09-27-info-geom.html
