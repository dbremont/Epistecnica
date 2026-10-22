---
tags: [axiom, discrete]
---

# Pigeonhole Principle

 : Combinatorics (Combinatorics%20231c0f5171ec8005bd62f206032ece34.md), Function (Function%20049537a4fd564eaaac4bae443839b0c0.md)

> A **combinatorial counting principle**, equivalent to a simple fact about finite sets and functions.
> 

> If $N$ objects are placed into $k$ boxes and $N > k$, then at least one box contains at least two objects.
> 

> AKA: There is no **bijective assignment**; only assignments that map at **least two elements** of the domain to the same element of the codomain are possible.
> 

> Note: The key in applying the Pigeonhole Principle is to learn to recognize problems in terms of assignments or mappings. This does not necessarily require thinking about the assignment directly; often it is done through transformations, logical reformulations, or other indirect approaches that eventually produce a form amenable to the principle.
> 

![image.png](../assets/note/epistemica/mathematical/pigeonhole-principle/image.png)

## Formalism

> Note: In this formalism, I approached the problem via collisions, though the standard method uses the concept of bijective functions.
> 
- Let $h: X \to Y$ be a hash function, mapping a large set of inputs $X$ (pigeons) into a smaller set of outputs $Y$ (buckets/pigeonholes).
- Let $|X| = N$ and $|Y| = k$.
- A **collision** occurs when **two distinct inputs map to the same hash value**: $x_1 \neq x_2 \in X, \quad h(x_1) = h(x_2)$
- **Pigeonhole Principle Applied**  If $N > k$, then **at least one collision must exist**. Formally:

$\exists x_1 \neq x_2 \in X : h(x_1) = h(x_2)$

- This is exactly the pigeonhole principle in the context of hashing: more items than hash outputs guarantees a collision.

## Mental Representation

> Is the question asking for **at least one collision**, or **minimum guaranteed collisions**?
> 

> What are the “pigeons”?
> 

> What are the “holes”?
> 

## Contradiction Proof

> See more in [Proof](https://app.notion.com/p/Proof-110c0f5171ec8074a9aeda9277860dea?pvs=21).
> 

The PHP is inherently about **counting and inevitability**. Proof by contradiction is effective because:

- PHP often involves statements like: "something must happen."
- By assuming "it does NOT happen," you get an **impossible counting scenario**, i.e., a contradiction.

## Use

| **Domain** | **Problem Type** | **Explanation** | **Example** |
| --- | --- | --- | --- |
| **Combinatorics** | Prove existence of repetition | Show that some element must repeat when objects exceed containers | Among 13 people, at least 2 share the same birth month |
| **Number Theory** | Remainders / modulo problems | Map integers to modular classes (boxes) to guarantee collisions | Pick 6 integers → at least 2 have the same remainder mod 5 |
| **Graph Theory** | Degree argument | Show that some vertex has certain properties | In a graph with nn vertices, some vertex has degree ≥ average degree |
| **Probability** | Birthday problem | Show inevitability of repeated events | 23 people → >50% chance two share a birthday |
| **Computer Science** | Hash collisions | More keys than buckets guarantees collisions | 10 keys hashed to 3 buckets → at least 1 bucket has ≥4 keys |
| **Spatial reasoning** | Packing / Covering | Place points in regions → some region contains ≥1 point | 5 points in a square divided into 4 smaller squares → one square has ≥2 points |
| **Algorithm Analysis** | Load balancing | Estimate worst-case distribution in arrays / hash tables | Distribute 101 tasks to 10 servers → one server has ≥11 tasks |

## Case Study

### There is an element in the sequence 7, 77, 77, 777, 7777, …,  that is divisible by 2003.

### During the last 1000 years, the reader had an ancestor A such that there was a person P who was an ancestor of both the father and the mother of A.

## References

- https://en.wikipedia.org/wiki/Pigeonhole_principle
- [**Division**](division.md)
