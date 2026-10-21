---
tags: [linear-algebra, space]
---

# Linear Space

 : Norm (Norm%20170c0f5171ec8070b6c5f594eeab1e7b.md), Linear Combination (Linear%20Combination%201bbc0f5171ec80d6a2dee212799dd4e3.md), Sobolev Space (Sobolev%20Space%201ffc0f5171ec80728368cfbe793ecde3.md), Matrix (Matrix%20171c0f5171ec80c58898c4e26151fbb8.md), Linear  Algebra (Linear%20Algebra%20d4ca395ec6c545c1bf2387d2fbdc732f.md), Inner Product Space (Inner%20Product%20Space%20ccdaf9b41b20443cb416c7b1bd5e4ef7.md), Multilinear Map (Multilinear%20Map%208989cd621d7a407d9137711e88aac9d1.md), Inner Product (Inner%20Product%20171c0f5171ec80439aa0fc448d33b98a.md)

> A **vector space** is a **mathematical structure** consisting of a set of vectors that satisfy certain properties, including closure under addition and scalar multiplication.
> 

> Note: A linear space illustrates the fluidity of mathematical structures, as it is simultaneously a space (in the geometric sense) and a structure (in the algebraic sense).
> 

> Notes intent.
> 

> **Short definition** of the topic.
> 

## Meta

> Evaluation Framework.
> 

> **The understanding of a concept is proportional** to the time invested in deep reflection, deliberate practice, and repeated engagement with its nuances. If a Concept has been learned soft of by osmosis - then is not well understood.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | … |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | … |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | What is the deepest essence? |
| **Evidentia (Evidence) 📊** | What proofs, data, or logical arguments support it? How can its claims or performance be verified? |
| **Telos (Intent) 🎯** | What is it for? Toward what end is it directed? What tools does it offer, if any? What outcomes does it aim to achieve? |
| **Gnosis (Understanding) 🧠** | How to grow a **mental represented** (compress, fluid,  hierarchical (depth, abstraction), meta-awareness, flexibility, minimal sensitivity, well-connected) that capture this topic both its declarative aspects and procedural aspects?  How can we develop an **explicit representation & organization** of this topic that supports the growth of a strong **mental representation**? What **previous structure**  must be in place in order to make the growth of the new representation feasible? |
| **Epignosis (Application) 🛠️** | How is this knowledge applied in practice? What advanced skills or insights emerge from mastery? What real-world problems does it solve? |
| **Relatio (Connections) 🔗** | How does this topic relate to other subjects or fields? What are the interdisciplinary connections? |
| **Idoneitas (Suitability) 📐** | How effectively does it achieve its purpose? What metrics prove its value? |
| **Limites (Limits) ⛔** | What are its boundaries? What constraints define its operation? |
| **Contextus (Context) 🌍** | What is the historical, cultural, or situational context in which this study occurs? |
| **Dynamis (Evolution) 🌱** | How might it transform? What emerging influences could redefine it? |
| **Critica (Critique) 🔍** | What are the common criticisms or challenges associated with this topic? How have these been addressed or debated? |
| **Verbum Usus (Language Use) 🗣️** | How is the word/concept used in language and discourse? What are the typical semantic, pragmatic, and stylistic patterns surrounding its use? How do people’s usage contexts, connotations, and variations influence understanding? What shifts or trends in language use reflect its evolving meaning or social significance? |

### 📚Terminology

- A **vector space** is a structured set where linear combinations make sense.
- **Subspaces** are smaller vector spaces inside larger ones.
- **Basis & dimension** define the "coordinate system" of the space.
- **Linear transformations** generalize matrix-vector multiplication.
- **Inner products** introduce geometry (lengths, angles).
- Linear Independence
- Linear Dependence

### 🧠 Mental Representation

> How should we think about x?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

QA:

- What does "linearity" really mean in the context of vector spaces, and is there such a thing as a "nonlinear space" with similar structure?
- …

> Kernel (Null Space): …
> 

> Eigenspaces: …
> 

> Image (Range): …
> 

## Formulation

A **vector space** $V$ over a field $\mathbb{F}$ is an algebraic structure consisting of a set $V$ equipped with two operations:

1. **Vector addition**: a binary operation $+: V \times V \to V$,
2. **Scalar multiplication**: a binary operation $\cdot : \mathbb{F} \times V \to V$,

such that the following axioms are satisfied for all $u, v, w \in V$ and $\alpha, \beta \in \mathbb{F}$:

1. **Additive closure**: $u + v \in V$
2. **Additive associativity**: $(u + v) + w = u + (v + w)$
3. **Additive identity**: There exists $0 \in V$ such that $v + 0 = v$
4. **Additive inverse**: For each $v \in V$, there exists $-v \in V$ such that $v + (-v) = 0$
5. **Commutativity of addition**: $u + v = v + u$
6. **Multiplicative closure**: $\alpha \cdot v \in V$
7. **Distributivity of scalar sums over vectors**: $(\alpha + \beta) \cdot v = \alpha \cdot v + \beta \cdot v$
8. **Distributivity of scalar multiplication over vector sums**: $\alpha \cdot (u + v) = \alpha \cdot u + \alpha \cdot v$
9. **Associativity of scalar multiplication**: $\alpha \cdot (\beta \cdot v) = (\alpha \beta) \cdot v$
10. **Multiplicative identity of scalars**: $1 \cdot v = v$

## Structure

> A vector space can have several kinds of **sub-structures**, each corresponding to a subset of elements with inherited operations that satisfy certain axioms. F
> 

| **Sub-Structure** | **Definition** | Case |
| --- | --- | --- |
| **Zero Subspace** | The trivial subspace containing only the zero vector. | $\{0\} \subseteq \mathbb{R}^3$ |
| **One-Dimensional (Line)** | Subspace spanned by a single nonzero vector. | x-axis in $\mathbb{R}^3$ |
| **Subspace** | Any subset closed under addition and scalar multiplication. | xy-plane in $\mathbb{R}^3$ |
| **Linear Span (Generated Subspace)** | Smallest subspace containing a set of vectors. | $\text{span}\{(1,0,0),(0,1,0)\}$ |
| **Direct Sum (Complementary Subspaces)** | $V = U \oplus W$, every $v \in V$ has unique decomposition $v = u + w$. | x-axis $\oplus$ y-axis in $\mathbb{R}^2$ |
| **Quotient Space** | Cosets of a subspace $W$ in $V$, denoted $V/W$. | $\mathbb{R}^3 / \text{xy-plane} \cong \mathbb{R}$ |
| **Affine Subspace (Linear Manifold)** | Translation of a subspace by a fixed vector. | Line in $\mathbb{R}^2$ not through origin |
| **Hyperplane** | Subspace of codimension 1. | Plane through origin in $\mathbb{R}^3$ |

### **Subspace**

> A **subspace** $W$ of a vector space  $V$ is a subset that is itself a vector space under the same operations.
> 

**Conditions for a Subspace**:

1. $\mathbf{0} \in W$.
2. Closed under addition: $\mathbf{u}, \mathbf{v} \in W \implies \mathbf{u} + \mathbf{v} \in W$.
3. Closed under scalar multiplication: $\alpha \in \mathbb{F}, \mathbf{v} \in W \implies \alpha \mathbf{v} \in W$.

Cases:

- …

### **Quotient Space**

> 

## Map

> Which are the functions - operator define in term of vector spaces?
> 

| **Category** | **Map** | **Description** |
| --- | --- | --- |
| **Linear Maps** | Linear Map (Homomorphism) | $T: V \to W$, preserves addition and scalar multiplication: $T(\alpha u + \beta v) = \alpha T(u) + \beta T(v)$ |
|  | Endomorphism | Linear map from a vector space to itself: $T: V \to V$ |
|  | Automorphism | Invertible endomorphism ($T: V \to V$ bijective and linear) |
|  | Inclusion Map | Embeds a subspace $W \subseteq V$ into $V$: $i: W \hookrightarrow V$ |
|  | Projection Map | Projects vectors onto a subspace $W \subseteq V$: $P: V \to W$, $P^2 = P$ |
|  | Quotient Map | Maps $v \in V$ to the coset $v + W$ in $V/W$ |
| **Functional** | Linear Functional | $\phi: V \to \mathbb{F}$, linear map into the field |
|  | Evaluation Functional | $\text{ev}_v(\phi) = \phi(v)$, evaluates functionals at $v$ |
|  | Dual Space Map | Operator on $$V^.$*$ induced by a linear map $T: V \to W$: $T^*: W^* \to V^*$ |
| **Multilinear** | Bilinear Map | $B: V \times W \to U$, linear in each argument separately |
|  | Multilinear Map | $f: V_1 \times \cdots \times V_k \to U$, linear in each argument |
|  | Tensor Product Operator | Encodes all bilinear maps: $V \otimes W \to U$ |
|  | Inner Product | $\langle u, v \rangle: V \times V \to \mathbb{F}$, symmetric, linear in first argument, positive-definite |
| **Inner Product** | Norm Operator | $|v| = \sqrt{\langle v, v \rangle}$, defines length |
|  | Orthogonal Projection | Projects onto subspaces orthogonally: $P^2 = P$, $P = P^*$ |
|  | Adjoint Operator | $T^*$ such that $\langle T(u), v \rangle = \langle u, T^(v) \rangle$* |
| **Function Space Operator** | Differential Operator | $D f = f'$, linear map on a function vector space |
|  | Integral Operator | $(Tf)(x) = \int K(x,y) f(y) dy$, linear transformation on function space |
|  | Shift Operator | $(Sf)(n) = f(n+1)$ on sequences or discrete function spaces |
|  | Multiplication Operator | $(Mf)(x) = g(x) f(x)$, multiplies function by a fixed function $g(x)$\ |

## **Characteristic Equation**

> See [https://en.wikipedia.org/wiki/Characteristic_polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial)
> 
- [https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)

## Representation Power

> **Vector spaces** directly **represent physical systems**, such as forces, velocities, and electric fields. In this case, vectors represent the magnitude and direction of the physical quantity, allowing for a more precise description of the system.
> 

| **System Type** | **Description** | **Representation in Vector Spaces** |
| --- | --- | --- |
| **Physical Systems** | Systems involving forces, velocities, electric and magnetic fields, etc. | Vectors represent the magnitude and direction of physical quantities, enabling precise modeling of physical phenomena (e.g., force, velocity). |
| **Abstract Systems** | Mathematical objects or data structures. | Vectors represent features or characteristics of the system, such as coefficients of polynomials or function values at different points. |
| **Geometric Systems** | Points, lines, and planes in Euclidean space. | Vectors represent displacements and directions in space, allowing representation of geometric shapes and movements in $\mathbb{R}^n$ space. |
| **Mathematical Objects** | Systems involving polynomials, matrices, or functions. | Vectors represent coefficients of polynomials, entries of matrices, or values of functions at different points in their domain. |
| **Data Structures** | Digital data, such as images, audio signals, or text documents. | Vectors represent features or characteristics of data, such as pixel values in images, frequencies in audio, or word frequencies in text. |

## Taxonomy

> A comprehensive list of Vector Spaces.
> 

| **Category** | **Space** | **Description** |
| --- | --- | --- |
| **Finite-Dimensional Vector Space** | $\mathbb{R}^n, \mathbb{C}^n$ | Vector spaces with a finite basis; dimension = number of basis vectors. |
|  | Polynomial space $P_n$ | Polynomials of degree ≤ n; dim = n+1. |
|  | Matrix space $M_{m \times n}(\mathbb{R})$ | All $m \times n$ matrices over $\mathbb{R}$; dim = m·n. |
| **Infinite-Dimensional Vector Space** | Sequence space $\ell^p$ | Sequences $(x_n)$ with (\sum |
|  | Function space $C([a,b])$ | Continuous functions on [a,b]. |
|  | Sobolev space $W^{k,p}([a,b])$ | Functions with weak derivatives up to order k in $L^p$. |
|  | Schwartz space $\mathcal{S}(\mathbb{R}^n)$ | Smooth functions rapidly decaying at infinity. |
| **Normed Vector Space** | $L^p([a,b])$ |  |
| **Metric Vector Space** |  |  |
| **Inner Product Space** | $\mathbb{R}^n, \mathbb{C}^n$ with dot product | Spaces where angles and lengths can be defined via $\langle x, y\rangle$. |
| **Pre-Hilbert Space** | $C([a,b])$ with inner product $\int_a^b f g dx$ | Inner product defined but not necessarily complete. |
| **Hilbert Space** | $L^2([a,b])$, $\ell^2$ | Complete inner product spaces; important in quantum mechanics and Fourier analysis. |
| **Banach Space** | $L^p([a,b]), C([a,b])$ | Complete normed vector spaces; includes Hilbert spaces as special cases. |
| **Topological Vector Space** | Fréchet space, LF-space | Vector spaces with a topology making vector addition and scalar multiplication continuous. |
| **Functional Space** | Space of linear operators $L(V,W)$ | All linear maps from V to W; may have additional structure like norm or topology. |
| **Dual Space** | $V^* = \text{Hom}(V, \mathbb{F})$ | Space of linear functionals mapping vectors to scalars. |

## **Linear Independence & Basis**

- **Linear Independence**: Vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k$ are **linearly independent** if the only solution to $\alpha_1 \mathbf{v}_1 + \dots + \alpha_k \mathbf{v}_k = \mathbf{0}$ is $\alpha_1 = \dots = \alpha_k = 0$.
- **Basis**: A **basis** of  $V$ is a linearly independent set $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ that **spans**  $V$ (every $\mathbf{v} \in V$) can be written as a linear combination of basis vectors).
- **Dimension**: The number of vectors in a basis is the **dimension** of  $V$, denoted $\dim(V)$.

## **Linear Transformations**

A **linear transformation** $T: V \to W$ between two vector spaces satisfies:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$.
2. $T(\alpha \mathbf{v}) = \alpha T(\mathbf{v})$.

## Basis

> A basis of a vector space is a set of vector; that are ..,  in which every vector in the space is a linear combinator of some vector of the basis.
> 

> Note: We can say that the basis is a coordinate? Why?  Remember that the concept of a coordinate is complex - and has many uses.
> 

- **Coordinates** are the numbers (scalars) you use to express a vector **in a particular basis**.
- Example: If v=2e1+3e2+5e3\mathbf{v} = 2\mathbf{e}_1 + 3\mathbf{e}_2 + 5\mathbf{e}_3v=2e1+3e2+5e3, then the coordinates of v\mathbf{v}v in the basis {ei}\{\mathbf{e}_i\}{ei} are (2,3,5)(2,3,5)(2,3,5).

- **Basis** → a set of “directions” or reference vectors.
- **Coordinates** → the representation of a vector **relative to that basis**.

## Dot Product

> For vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$, the **inner product** is usually defined as the **dot product**: $\langle \mathbf{u}, \mathbf{v} \rangle = u_1 v_1 + u_2 v_2 + \dots + u_n v_n = \sum_{i=1}^n u_i v_i$
> 

Properties of an **inner product**:

1. **Symmetry:** $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$
2. **Linearity in the first argument:** $\langle a\mathbf{u} + b\mathbf{w}, \mathbf{v} \rangle = a \langle \mathbf{u}, \mathbf{v} \rangle + b \langle \mathbf{w}, \mathbf{v} \rangle$
3. **Positive-definiteness:** $\langle \mathbf{u}, \mathbf{u} \rangle \ge 0$, with equality only if $\mathbf{u} = 0$

Relation:

- Geometric Meaning -  Length (Norm) - Angle Between Vectors - Orthogonality.
- Complex Vector
- Function Inner Product

## Relation

> Which are the ideas related with vector spaces?
> 

Idea; Relation

| **Idea** | **Relation to Vector Spaces** |
| --- | --- |
| **Linear Independence** | Defines whether a set of vectors can form a basis; fundamental to dimension. |
| **Basis / Dimension** | Basis vectors span the vector space; dimension = number of vectors in a basis. |
| **Subspace** | Any subset closed under addition and scalar multiplication; a vector space itself. |
| **Span** | Set of all linear combinations of a set of vectors; generates a subspace. |
| **Linear Transformation** | Maps between vector spaces preserving addition and scalar multiplication. |
| **Kernel / Null Space** | Set of vectors mapped to zero under a linear transformation; a subspace. |
| **Image / Range** | Set of all outputs of a linear transformation; a subspace. |
| **Inner Product** | Defines angles and lengths; allows geometric notions in vector spaces. |
| **Norm** | Assigns length to vectors; induces metric and topology. |
| **Metric** | Defines distance between vectors; allows analysis in vector spaces. |
| **Dual Space** | Space of all linear functionals; provides functional viewpoint. |
| **Orthogonality** | Relation defined via inner product; important in decomposition and projections. |
| **Projection** | Linear operator mapping vectors onto a subspace; used in approximations. |
| **Eigenvectors / Eigenvalues** | Vectors scaled under linear transformations; key in diagonalization. |
| **Direct Sum** | Combines subspaces into a larger vector space; each vector uniquely decomposable. |
| **Quotient Space** | Space of equivalence classes modulo a subspace; constructs new vector spaces. |
| **Tensor Product** | Combines vector spaces to form a higher-dimensional space; important in multilinear algebra. |
| **Functional Space** | Vector space whose elements are functions; often infinite-dimensional. |
| **Topology** | Structure allowing convergence and continuity in vector spaces. |
| **Completeness** | Property of Banach or Hilbert spaces; all Cauchy sequences converge. |
| **Algebraic Structures** | Some vector spaces are equipped with multiplication (e.g., algebras). |

## Limit

> **Vector spaces** are a powerful mathematical tool widely used in various fields of mathematics and physics.
> 

| **Drawback** | **Description** |
| --- | --- |
| **Limited Applicability** | Vector spaces may not be suitable for non-linear systems, where relationships between variables are not linear. |
| **Inability to Handle Complex Structures** | Vector spaces struggle with complex structures like manifolds or topological spaces, requiring more advanced frameworks (e.g., differential geometry). |
| **Difficulty Handling Infinite-Dimensional Spaces** | Techniques used in finite-dimensional spaces may not generalize to infinite-dimensional settings, which are critical in some applications. |
| **Dependence on the Choice of Basis** | Computations often depend on the choice of basis vectors, and selecting the right basis for a problem can be difficult. |
| **Difficulty in Visualization** | High-dimensional vector spaces are hard to visualize, making it difficult to intuitively understand their properties and structure. |
| **High Dimensionality** | Large vector spaces lead to computational and visualization challenges, especially with high-dimensional data. |
| **Linearity Assumption** | Vector spaces are built on the assumption of linearity, which limits their use in inherently nonlinear real-world problems. |
| **Lack of Semantic Meaning** | Vectors can represent abstract concepts (e.g., words, images), but they lack inherent semantic meaning, making interpretation difficult. |
| **Data Sparsity** | Sparse data, such as text or image data, can be challenging to represent and analyze in vector spaces without specialized techniques. |
| **Limited Expressive Power** | Vector spaces cannot represent all mathematical objects, particularly infinite-dimensional objects such as certain functions or distributions. |
| **Computational Complexity** | Operations like finding eigenvalues and eigenvectors can be computationally expensive, especially for large systems, making them difficult to compute. |

## **Case**

- **Euclidean Space $\mathbb{R}^n$**: Vectors of real numbers with component-wise addition and scalar multiplication.
- **Function Spaces**: The set of all real-valued functions $f: \mathbb{R} \to \mathbb{R}$ forms a vector space under pointwise addition and scalar multiplication.
- **Polynomial Spaces $P_n$**: The set of all polynomials of degree $\leq n$ with real coefficients.
- **Matrix Spaces $M_{m \times n}$**: The set of all $m \times n$ matrices with real entries under matrix addition and scalar multiplication.

## ❓ QA

> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- 
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [Plato’s Dialectic Method](https://app.notion.com/p/Plato-s-Dialectic-Method-268c0f5171ec805cbb91d16158ae579e?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- https://en.wikipedia.org/wiki/Vector_space
- https://en.wikipedia.org/wiki/Linear_subspace
- [Intuitive and convincing argument that functions are vectors](https://math.stackexchange.com/questions/902133/intuitive-and-convincing-argument-that-functions-are-vectors)
- https://mathworld.wolfram.com/InnerProduct.html
