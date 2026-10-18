# Set

 : Boolean Algebra (Boolean%20Algebra%2029a6a469a6714ad89edc85c8ffbe2d57.md), σ-algebra (%CF%83-algebra%2015fc0f5171ec80f392e8ffbf11d4cf84.md), Configuration (Configuration%201d6c0f5171ec80c79c32ebd7ed9a1a24.md), Catalan Number (Catalan%20Number%201d6c0f5171ec80a68b9bd8773d4da78b.md), Discrete Structure (Discrete%20Structure%201d6c0f5171ec8003b425f870f463a807.md), Combinatorics (Combinatorics%20231c0f5171ec8005bd62f206032ece34.md), Enumeration (Counting) (Enumeration%20(Counting)%20256c0f5171ec80ec80dfdcb8bc82d1e6.md), Measure (Measure%20273c0f5171ec80ae812dc3c73aad95dc.md), Vitali Set (Vitali%20Set%20273c0f5171ec80b89ebbf64e1c55fa26.md), Order (Order%2027ac0f5171ec80faabcbdc8078658589.md)

> **Set theory** is a branch of mathematical logic that studies sets, which are collections of objects, and forms the foundation for most of modern mathematics.
> 

> **Set Theory** (singular) refers to the general field of study, encompassing all approaches and frameworks related to sets.
> 

## Formulation

### Set

> Collections of distinct objects considered as a whole,  $\{1, 2, 3\}, \{a, b, c\}, \mathbb{N}$ (set of natural numbers).
> 

> **Subset**: \( A \subseteq B \) if every element of \( A \) is in \( B \).
> 

> **Power Set**: \( \mathcal{P}(A) = \) set of all subsets of \( A \).
> 

> **Cardinality**: The "size" of a set (\( |A| \)).
> 

## Property

> **Countable Sets**: Sets with the same cardinality as \( \mathbb{N} \) (e.g., integers, rationals).
> 

> **Uncountable Sets**: Sets like \( \mathbb{R} \) (Cantor’s diagonal argument).
> 

> **Ordinals**: Extend \( \mathbb{N} \) to describe order types (e.g., \( 0, 1, 2, \dots, \omega, \omega+1 \)).
> 

> **Cardinals**: Represent sizes of sets (\( \aleph_0, \aleph_1, \dots \)).
> 

> Continuum Hypothesis (CH): \( 2^{\aleph_0} = \aleph_1 \) (no set has cardinality between \( \mathbb{N} \) and \( \mathbb{R} \)).
> 

> Partition: …
> 

> Countable Set: …
> 

> Uncountable Set: …
> 

> Empty Set: …
> 

> Set Algebra:
> 

> **Cartesian Product**: The set of all ordered pairs taken from two sets. If  $(A)$ and $(B)$ are two sets, the Cartesian product $(A \times B)$ is the set of all pairs $(a, b)$ where $(a \in A)$ and $(b \in B)$.
> 

> **Power Sets**: The set of all possible subsets of a set, including the empty set and the set itself.
> 

## Operator

> Here’s a structured table of **set functionals** (also called **set operations**), which are fundamental operations used in set theory. These operations allow us to manipulate and analyze sets, and they are widely used in mathematics, computer science, and logic.
> 

| **Operation Name** | **Symbol** | **Definition** | **Description** |
| --- | --- | --- | --- |
| **Union** | $A \cup B$ |  $A \cup B = \{ x \mid x \in A \text{ or } x \in B \}$ | The set of all elements that belong to  $A$ or  $B$ (or both). |
| **Intersection** | $A \cap B$ | $A \cap B = \{ x \mid x \in A \text{ and } x \in B \}$ | The set of all elements that belong to both  $A$ and $B$. |
| **Set Difference** | $A \setminus B$ | $A \setminus B = \{ x \mid x \in A \text{ and } x \notin B \}$ | The set of all elements that belong to  $A$ but not to  $B$. |
| **Symmetric Difference** | $A \Delta B$ | $A \Delta B = (A \setminus B) \cup (B \setminus A)$ | The set of all elements that belong to exactly one of  $A$ or  $B$. |
| **Complement** | $A^c$ or $\overline{A}$ | $A^c = \{ x \mid x \notin A \}$ (relative to a universal set $U$) | The set of all elements not in  $A$. |
| **Cartesian Product** | $A \times B$ | $A \times B = \{ (a, b) \mid a \in A, b \in B \}$ | The set of all ordered pairs where the first element is from  $A$ and the second is from  $B$. |
| **Power Set** | $\mathcal{P}(A)$ | $\mathcal{P}(A) = \{ X \mid X \subseteq A \}$ | The set of all subsets of $A$. |
| **Disjoint Union** | $A \sqcup B$ | $A \sqcup B = \{ (x, 0) \mid x \in A \} \cup \{ (y, 1) \mid y \in B \}$  | A union of $A$ and  $B$ where elements are tagged to indicate their origin. |

## Set Representation

> ….
> 

| **Type** | **Method** | **Description** | **Example** |
| --- | --- | --- | --- |
| **Symbolic** | **Roster (Tabular) Form** | List all elements of the set explicitly, enclosed in curly braces. | $A = \{1, 2, 3, 4\}$ |
|  | **Set-Builder Notation** | Define a set by specifying a property or condition that its elements satisfy. | $A = \{x \mid x \text{ is an even number}\}$ |
|  | **Interval Notation** | Represent subsets of real numbers using intervals. | $A = [1, 5)$ (includes 1, excludes 5) |
| **Descriptive** | **Descriptive Form** | Describe the set in words. | $A = \text{The set of all prime numbers}$ |
| **Visual** | **Venn Diagram** | Overlapping circles to represent sets and their relationships. | Two circles overlapping to show $A \cap B$. |
|  | **Euler Diagram** | Similar to Venn diagrams, but only shows relevant relationships. | A circle for  $A$ inside a circle for  $B$ to show $A \subseteq B$. |
|  | **Carroll Diagram** | A grid-based method for categorizing elements based on set membership. | A 2x2 grid showing $A \cap B$, $A \setminus B$, $B \setminus A$, and $(A \cup B)^c$. |
|  | **Tree Diagram** | A hierarchical structure to represent subsets or power sets. | A tree showing subsets of $\{1, 2\}$: $\emptyset, \{1\}, \{2\}, \{1, 2\}$. |
|  | **Lattice Diagram** | A diagram showing subset relationships in a partially ordered set. | A lattice for the power set of $\{1, 2\}$: $\{1, 2\}$ at the top, $\emptyset$ at the bottom. |
|  | **Graph (Directed/Undirected)** | Nodes represent sets, and edges represent relationships (e.g., subset, intersection). | A directed graph where $A \rightarrow B$ indicates $A \subseteq B$. |
|  | **Hypercube (n-Dimensional Cube)** | A cube or hypercube where each dimension represents a set, and vertices represent combinations of set memberships. | A 3D cube for three sets \( A, B, C \), with vertices representing $A \cap B \cap C$, etc. |
|  | **Matrix Diagram** | A matrix where rows represent elements and columns represent sets, with 1 indicating membership. | A matrix showing membership of elements$\{1, 2, 3\}$in sets  $A$ and  $B$. |
|  | **Coordinate Plane** | Represent sets as regions on a coordinate plane. | Shading the region $x \geq 0$ and $y \geq 0$  to represent a set. |
|  | **Hasse Diagram** | A diagram to represent partially ordered sets (e.g., power sets). | A Hasse diagram for the power set of $\{1, 2\}$. |
| **Computational** | **Characteristic Function** | Use a function to indicate membership of elements in a set. | $f_A(x) = 1$ if $x \in A$, else $0$. |
|  | **Bit Vector (Binary Representation)** | Represent a set as a sequence of bits, where each bit indicates membership. | $A = \{1, 3\}$ represented as  $1010$ (for universe $\{1, 2, 3, 4\}$. |
|  | **Matrix Representation** | Represent sets using matrices, where rows/columns indicate elements and membership. | A matrix where rows are elements and columns are sets, with 1 indicating membership. |
| **Recursive** | **Recursive Definition** | Define a set recursively by specifying base elements and rules for generating new elements. | $A = \{0\} \cup \{x + 2 \mid x \in A\}$  (set of even numbers). |
|  | **Recursive Enumeration** | Enumerate elements of a set recursively. | $A = \{2, 4, 6, 8, \dots\}$ (set of even numbers). |
| **Parametric** | **Parametric Representation** | Represent a set using parameters or variables. | $A = \{(x, y) \mid x = t, y = t^2, t \in \mathbb{R}\}$ (parabola). |
| **Logical** | **Logical Formula** | Represent a set using a logical expression. | $A = \{x \mid P(x)\}$, where $P(x)$ is a logical predicate. |

## References

- [Logic](https://app.notion.com/p/Logic-e04a5773f03c4db5ae23409d97d310b3?pvs=21)
- [Set Theory](https://app.notion.com/p/Set-Theory-7f150c9c26fe407fbc9f40f810600d3f?pvs=21)
- [Universe (mathematics)](https://en.wikipedia.org/wiki/Universe_(mathematics))
- https://en.wikipedia.org/wiki/Set_theory
- https://en.wikipedia.org/wiki/Field_of_sets
- https://en.wikipedia.org/wiki/Algebra_of_sets
- https://en.wikipedia.org/wiki/Set_(mathematics)
- https://en.wikipedia.org/wiki/Russell's_paradox
- https://en.wikipedia.org/wiki/Von_Neumann_universe
- [Representation Problem:  Set Data](https://app.notion.com/p/Representation-Problem-Set-Data-04afd18be1ec4edc964be2ce535f5860?pvs=21)
