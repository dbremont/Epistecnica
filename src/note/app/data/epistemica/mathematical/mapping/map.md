---
order: 0
---

# Map

> A **map** is a rule that assigns to every element of a domain exactly one element of a codomain. Mathematics names the same assignment *function*, *functional*, *operator*, *transformation*, or *morphism* depending on what the assignment is being used to emphasise — the value, the scalar result, the space it acts on, the state it changes, or the structure it preserves.

## Formulation

### What is this epistemic instance?

> The catalogue of the kinds of assignment mathematics uses: what a map is, the words that name it, and the boundary at which a map generalises into a relation. The notes of the [mapping scope](function.md) are the functions these maps define; the licences that rewrite expressions with them live in the [transformation-rule catalogue](../transformation.md).

### What epistemic element type does this epistemic instance belong to?

> A **`Concept`** — an `Epistemic Construction`: a constructed discriminator of an aspect of the mathematical target. The same assignment is *readable as* a `Transformation Rule` only where it is used to rewrite a well-formed expression (`a × b ↦ c`); the concept and the rule are two elements, not one, and the kind tree below covers the concept. The schema is owned by the canonical
> [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

### Is the type of this `epistemic element instance` ambiguous?

> Yes, and the ambiguity is lexical before it is epistemic. The same set-theoretic object — a single-valued, total assignment — is called a **function** when the value matters, a **functional** when that value is a scalar, an **operator** when the elements being assigned are themselves functions or vectors and the space is the object of study, a **transformation** when the space maps to itself, and a **morphism** when the point is that a structure survives the trip. No new type is needed for the change of name; what changes is the emphasis, and the note records it rather than splitting the concept.

> One boundary is genuine and is kept in the tree: a **relation** is the many-valued case. It assigns to each element of the domain a *set* of codomain elements, so it relaxes single-valuedness and totality while remaining a map of the same shape. A relation is therefore a kind of map, not its negation — and an ordinary map is exactly the single-valued, total relation.

### What are the kinds of this `epistemic element instance`?

> A **kind tree** (the guide's second instrument): it states the kinds the type admits and stops at types. It is not an instance decomposition, and the two are never mixed in one table.

| Kind Path | Domain → Codomain | What the name emphasises |
| --- | --- | --- |
| `Concept` (→ Kind) Map | any → any | the assignment itself |
| Map (→ Kind) Function | set → set | the value assigned |
| Map (→ Kind) Functional | function space → scalar field | the assigned value is a scalar |
| Map (→ Kind) Operator | function space → function space | the space is the object; the map acts on it |
| Map (→ Kind) Transformation | space → the same space | the state of the space changes |
| Map (→ Kind) Morphism | structure → structure | a structure survives the assignment |
| Morphism (→ Kind) Homomorphism | algebra → algebra | operations are preserved |
| Morphism (→ Kind) Isomorphism | algebra → algebra | a homomorphism with an inverse |
| Morphism (→ Kind) Endomorphism | object → itself | a morphism whose domain is its codomain |
| Morphism (→ Kind) Automorphism | object → itself | an endomorphism that is an isomorphism |
| Function (→ Kind) Linear Map | vector space → vector space | addition and scaling are preserved |
| Function (→ Kind) Multilinear Map | product of spaces → space | linear in each slot separately |
| Function (→ Kind) Embedding | space → space | injective and structure-preserving |
| Function (→ Kind) Isometry | metric space → metric space | distance is preserved |
| Function (→ Kind) Projection | space → subspace | idempotent: applying it twice changes nothing |
| Map (→ Kind) Functor | category → category | objects *and* morphisms are assigned |
| Map (→ Kind) Relation | any → power set of any | many-valued: a set of values per element |

## Naming rules

| Situation | The word to use | The word to avoid |
| --- | --- | --- |
| The value the map produces is the subject | **function** | "operator" (hides that the output is a value) |
| Domain is a space of functions, codomain the scalars | **functional** | "function" (true but loses the scalar codomain) |
| The elements being mapped are themselves functions or vectors, and the space is studied | **operator** | "function" (true but loses that the object is the space) |
| Domain and codomain are the same space, and the point is what changes | **transformation** | "operator" unless the space is linear |
| The point is that algebraic or topological structure is preserved | **morphism** (and its homomorphism/isomorphism kinds) | "function" (true but loses the preserved structure) |
| The domain element can have several images | **relation** | "map" or "function" (both assert single-valuedness) |

> The trap the table guards against: writing "operator" for every map, or "function" for a functional. Both are true statements about the same object and both lose the distinction the name was carrying.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) — the `Concept` construction kind and the §Kind Trees rule
- [Function](function.md) · [Functional](functional.md) · [Operator](operator.md) · [Linear Map](../algebra/linear/linear-map.md) · [Multilinear Map](../algebra/linear/multilinear-map.md)
- [Transformation Rule](../transformation.md) — the rewrite licence, a different element from the map
