---
tags: [discrete]
---

# Enumeration (Counting)

 : Combinatorics (Combinatorics%20231c0f5171ec8005bd62f206032ece34.md), Set (Set%20176c0f5171ec800f8b41f66b6d8cc5b3.md), Bijective Method (Bijective%20Method%20258c0f5171ec805191e3ea620c687525.md)

> This note explores **Enumerative Combinatorics** (often framed as *Enumeration Techniques: Enumeration Problem → Counting*).
> 

> **Enumerative combinatorics** is the branch of combinatorics concerned with *counting the number of discrete structures that satisfy given conditions*. Rather than just “doing arithmetic,” it develops systematic techniques to translate problems into precise counts, formulas, generating functions, or asymptotic estimates.
> 

## Meta

> Evaluation Framework.
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

### 🧠 Mental Representation

> How should we think about **Enumeration**?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Formulation

> What is the object? Which method applies? Do I want exact counts, asymptotics, or structure-preserving correspondences?
> 

> Enumeration Techniques: Enumeration Problem → Counting.
> 

**Enumerative Combinatorics:**

- **Objects to count** (sets, partitions, graphs, paths, etc.)
- **Techniques** (formulas, recurrences, generating functions, bijections, symmetries, asymptotics)
- **Frameworks** (combinatorial species, labeled/unlabeled, exact/asymptotic)

## Object

> Given some class of discrete objects, how many objects of size $n$ exist that satisfy certain properties?
> 

| **Problem Type** | **Description** | **Underlying Structure** |
| --- | --- | --- |
| **Permutations** | Number of ways to order nn objects; may involve restrictions (e.g., derangements, pattern avoidance). | Arrangements of elements of a finite set; structure is a *sequence with no repetition*. |
| **Combinations (Subsets)** | Number of ways to choose kk objects from nn, possibly with conditions (e.g., with/without repetition). | Subsets of a finite set; structure is *unordered selection*. |
| **Partitions of Sets** | Ways to divide a set into disjoint subsets (e.g., Bell numbers, Stirling numbers). | Set partition lattice; structure is a *collection of blocks*. |
| **Partitions of Integers** | Ways to express an integer as a sum of positive integers, ignoring order. | Integer partitions; structure is *multisets of integers* summing to $n$. |
| **Compositions of Integers** | Ordered decompositions of an integer into positive parts. | Sequences of integers summing to n. |
| **Graphs** | Count of unlabeled/labeled graphs with nn vertices (e.g., connected, planar, bipartite). | Graph structures (vertices, edges); adjacency relations. |
| **Trees** | Number of labeled/unlabeled rooted or unrooted trees; e.g., Cayley’s formula for labeled trees. | Acyclic connected graphs; hierarchical structure. |
| **Matchings** | Number of ways to pair up elements (e.g., perfect matchings in graphs). | Edge sets with no overlaps; pairings in sets/graphs. |
| **Words (Strings)** | Number of words of length nn over an alphabet, often with constraints (e.g., no consecutive letters). | Sequences over a finite alphabet. |
| **Pattern Avoidance (in words/permutations)** | Count of sequences avoiding specific subpatterns (e.g., permutations avoiding 132). | Constraint-satisfying sequences; subword pattern restrictions. |
| **Lattice Paths** | Paths on a grid (e.g., Dyck paths, Motzkin paths, Catalan structures). | Step sequences constrained by rules (up/down, right/left). |
| **Tilings** | Number of ways to tile a region with given tiles (e.g., domino tilings, polyomino tilings). | Coverings of a region by pieces; geometric combinatorics. |
| **Polyominoes** | Count of distinct shapes formed by joining squares edge-to-edge (fixed/free). | Planar connected sets of cells; geometric shapes. |
| **Colorings** | Number of colorings of graphs/objects under constraints (e.g., proper graph coloring). | Assignments of labels/colors to elements; symmetries. |
| **Polya Counting (Necklaces, Bracelets)** | Count of distinct arrangements under symmetry (rotation/reflection). | Orbits of group actions on sequences/sets. |
| **Plane Partitions** | 2D generalizations of integer partitions, arrays of integers decreasing along rows/columns. | Arrays of integers with order constraints. |
| **Young Tableaux** | Number of ways to fill a Young diagram with integers satisfying rules. | Ferrers diagrams with filling rules; representation theory links. |
| **Latin Squares** | n×nn \times n arrays filled with nn symbols, each appearing once per row/column. | Constraint-satisfying arrays; combinatorial designs. |
| **Designs (e.g., block designs, Steiner systems)** | Number of ways to construct incidence structures with balance properties. | Incidence matrices with symmetry and balance. |
| **Permuted Structures** | E.g., derangements (permutations with no fixed points), involutions (self-inverse permutations). | Special classes of permutations. |

## **Technique**

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| Basic Counting Principles | Addition Principle | If outcomes are mutually exclusive, sum their counts. |
|  | Multiplication Principle | If outcomes are independent steps, multiply their counts. |
|  | Inclusion-Exclusion Principle | Adjust for overcounting when sets overlap. |
| Recursive Techniques | Recurrence Relations | Express counts in terms of smaller cases. |
|  | Divide-and-Conquer Strategies | Break problems into simpler subproblems. |
|  | Generating Recurrence Formulas | Derive formulas based on the recursive structure of objects. |
| Generating Functions | Ordinary Generating Functions (OGFs) | Encode sequences algebraically; useful for unlabelled objects. |
|  | Exponential Generating Functions (EGFs) | Encode labelled structures; exponential weights for indexing. |
|  | Operations on Generating Functions | Translate combinatorial constructions into algebraic operations (sum, product, etc.). |
| Bijective Methods | Bijection Construction | Prove two sets have equal cardinality via explicit one-to-one mapping. |
| Symmetry-Based Techniques | Burnside’s Lemma | Average fixed points under group actions to count distinct configurations. |
|  | Pólya Enumeration Theorem | Generalizes Burnside’s Lemma using cycle index to count up to symmetry. |

### **Addition Principle (Sum Rule)**

> The **Addition Principle** states that if a task can be done in one of several mutually exclusive ways, the total number of ways to do it is the **sum** of the ways.
> 

### Multiplication Principle (Product Rule)

> The **Multiplication Principle** states that if a task is performed in sequence, and each step has a certain number of independent choices, the total number of ways to perform the task is the **product** of the number of choices at each step.
> 

### Inclusion-Exclusion Principle

> The **Inclusion-Exclusion Principle** is a counting technique used to find the size of the union of overlapping sets. It corrects for overcounting elements that belong to multiple sets.
> 

### Formula

| **Concept** | **Formula** | **Notes** |
| --- | --- | --- |
| **Factorial** | $n! = n \cdot (n-1) \cdot \dots \cdot 2 \cdot 1$ | Number of ways to arrange $n$ distinct items in order. |
| **Permutation (all items)** | $P(n) = n!$ | Arrangements of all $n$ items. |
| **Permutation (r items)** | $P(n,r)=\dfrac{n!}{(n-r)!}$ | Ordered arrangements of $r$ items from $n$. |
| **Permutation with repetition** | $n^{r}$ | Ordered arrangements of $r$ items from $n$ when repetition is allowed. |
| **Combination (r from n)** | $C(n,r)=\dbinom{n}{r}=\dfrac{n!}{r!(n-r)!}$ | Unordered selection of $r$ items from $n$. |
| **Combination with repetition** | $C(n+r-1,r)=\dbinom{n+r-1}{r}$ | Unordered selection of $r$ items from $n$ with repetition allowed. |
| **Multinomial coefficient** | $\dfrac{n!}{k_{1}!k_{2}!\dots k_{m}!}$ | Ways to divide $n$ items into groups of sizes $k_{1},k_{2},\dots,k_{m}$ ($\sum k_{i}=n$). |
| **Binomial theorem** | $(x+y)^{n}=\displaystyle\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k}$ | Expands powers of a sum using combinations. |
| **Pascal's rule** | $\dbinom{n}{r}=\dbinom{n-1}{r-1}+\dbinom{n-1}{r}$ | Recurrence relation for binomial coefficients. |
| **Stirling numbers of the second kind** | $S(n,k)$ | Number of ways to partition $n$ items into $k$ non-empty, unlabeled subsets. |
| **Bell numbers** | $B_{n}=\displaystyle\sum_{k=1}^{n}S(n,k)$ | Total number of partitions of $n$ elements. |
| **Derangements (subfactorial)** | $!n = n!\displaystyle\sum_{k=0}^{n}\frac{(-1)^{k}}{k!}$ | Number of permutations of $n$ items with no fixed points. |

## Pitfall

| **Pitfall** | **Description** | **Example** | **How to Fix** |
| --- | --- | --- | --- |
| **Double counting** | Counting the same element more than once | Counting students who play soccer (30) or basketball (20) as 50, ignoring overlap of 10 | Use **Inclusion-Exclusion Principle**: 30 + 20 − 10 = 40 |
| **Under-counting / missing cases** | Failing to consider all possibilities | Counting 3-digit numbers with increasing digits but ignoring repeated digits (if allowed) | Systematically classify cases or list possibilities |
| **Order confusion** | Confusing when order matters (permutations) vs doesn’t (combinations) | Counting arrangements of letters “ABC” as 3 instead of 6 | Clarify whether **order matters** and use correct formula |
| **Assuming independence incorrectly** | Treating events as independent when they are not | Rolling two dice with a constraint on sum, treating dice as independent | Use **conditional counting** or account for dependencies |
| **Miscounting identical objects** | Failing to account for indistinguishable objects | Arranging letters in “AAB”: total permutations = 6, but two A’s are identical → 3 | Divide by factorial of repeated elements: 3! / 2! = 3 |
| **Confusing “at least” vs “exactly”** | Counting “at least” events as “exactly” events | Number of ways to roll at least one 6 with 2 dice = 11, not 2 | Use **complementary counting** or carefully handle inequalities |
| **Ignoring constraints** | Forgetting problem-specific restrictions | Seating 5 people with 2 who cannot sit together | Apply **case analysis**, **inclusion-exclusion**, or **gap method** |
| **Overcomplicating formulas** | Using complex formulas unnecessarily | Using permutations with repetition instead of counting directly | Consider **simpler combinatorial reasoning** and small examples |

## Counting  Sequence

> Which are the useful sequences used in **counting problems**?
> 

> See more in [Catalan Number](catalan-number.md), [**Stirling Number**](stirling-number.md), …
> 

| **Sequence** | **What it Counts?** |
| --- | --- |
| **Catalan numbers** | Dyck paths, binary trees, polygon triangulations, etc. |
| **Bell numbers** | Set partitions of an nn-element set. |
| **Stirling numbers (1st & 2nd kind)** | Permutations by cycle structure; partitions into blocks. |
| **Fibonacci numbers** | Tilings with 1s and 2s, binary strings avoiding consecutive 1s. |
| **Binomial coefficients** | Subsets, lattice paths, Pascal’s triangle. |
| **Eulerian numbers** | Permutations classified by number of descents. |
| **Motzkin numbers** | Paths with steps up, down, horizontal. |

## Guide

- [ ]  Translate problems into structures:  Don’t think “just count.” Instead, ask: *What is the structure of the set I’m counting?*
- [ ]  Exploit Symmetry and Structure: Counting often involves recognizing when two seemingly different objects are actually equivalent under some transformation.
- [ ]  Build Generating Functions: Enumerative combinatorics often converts counting into algebra.
- [ ]  Recursive Decomposition: Many combinatorial objects can be broken down recursively.
- [ ]  Be comfortable switching between **combinatorial, algebraic, and analytic views**.
- [ ]  Remember that many hard problems are really about *encoding* and *transforming* objects in clever ways.

## Relation

> Which are the relation with other fields of mathematics or science?
> 

| **Field** | **Relation to Enumeration** | **Instance(s)** |
| --- | --- | --- |
| **Algebra** | Enumeration often uses algebraic structures (groups, rings, symmetric functions). Algebraic methods encode and manipulate combinatorial objects. | Polya’s enumeration theorem (group actions), representation theory & Young tableaux, symmetric function theory in counting partitions. |
| **Number Theory** | Integer partitions and modular forms connect combinatorics and number theory. Many counting functions are arithmetic in nature. | Partition function p(n)p(n), Ramanujan congruences, q-series and generating functions. |
| **Probability & Statistics** | Counting underlies probability spaces. Enumerative methods are used to compute probabilities, expected values, and distributions. | Binomial and multinomial coefficients, random graphs, occupancy problems. |
| **Analysis** | Asymptotic enumeration uses analytic tools (generating functions, complex analysis, saddle-point methods). | Singularity analysis of generating functions, Stirling’s approximation. |
| **Geometry** | Many counting problems are geometric in disguise (polyominoes, lattice point enumeration, polytopes). | Ehrhart polynomials (counting lattice points in polytopes), tilings, Catalan objects as planar embeddings. |
| **Topology** | Enumeration of topological structures, or using topology to compute counts. | Counting maps on surfaces, Euler characteristic as alternating sum of counts, configuration spaces. |
| **Representation Theory** | Certain enumeration problems are solved using characters and irreducible representations. | Counting standard Young tableaux, hook-length formula, Schur functions. |
| **Computer Science (Theoretical)** | Enumeration provides foundations for algorithms, complexity, and discrete structures in CS. | Counting automata states, complexity of counting (#P problems), combinatorial enumeration in algorithm analysis. |
| **Physics (Statistical Mechanics, Quantum)** | Enumeration is used to count states, configurations, and paths. | Partition functions in physics ↔ generating functions, lattice models, Feynman diagrams. |
| **Biology & Chemistry** | Combinatorial enumeration helps count molecular structures, DNA sequences, chemical isomers. | Counting RNA secondary structures, graph enumeration of molecules. |
| **Operations Research / Optimization** | Counting underlies feasible solution enumeration, network flows, scheduling. | Enumeration of matchings in bipartite graphs, integer programming via generating functions. |
| **Logic & Formal Languages** | Enumeration of words, languages, and grammars. | Counting words of given length in a formal language, combinatorics on words. |

## ❓ QA

> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- 
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- https://en.wikipedia.org/wiki/Enumerative_combinatorics
- https://oeis.org/
- https://en.wikipedia.org/wiki/Combinatorics
- https://en.wikipedia.org/wiki/Enumeration
- [Inclusion-Exclusion Principle](inclusion-exclusion-principle.md)
