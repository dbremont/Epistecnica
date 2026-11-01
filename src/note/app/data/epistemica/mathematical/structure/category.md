---
tags: [structure, algebraic, framework]
---

# Category

> A **category** consists of a collection of objects, a collection of arrows between them, an associative composition of arrows, and an identity arrow at every object. Nothing else is assumed — which is what makes it the language in which mathematics compares its own structures.

## Formulation

> **What it is.** The minimal setting in which "structure-preserving map" makes sense: a set with structure is an object, its maps are arrows, and the rules of composition are the only axioms. Groups, vector spaces, topological spaces, posets and logics all become categories, so a theorem proved once about categories holds in all of them.
>
> **Type.** A `Concept` — an `Epistemic Construction`. The arrows between structures are [maps](../mapping/map.md) read as `Morphism`; the functor is the map between categories.
>
> **Boundary.** A category is not a set of sets: its objects need not be elements of anything, and the collection of objects is allowed to be a proper class. This is why category theory needs care about size, and why it is a *language* rather than a branch of set theory.

## Key kinds

| Kind | What it is | Why it matters |
| --- | --- | --- |
| **Functor** | An assignment of objects to objects and arrows to arrows preserving composition and identities | Transports a structure from one category to another; forgetful functors record what a structure forgets |
| **Natural Transformation** | A family of arrows, one per object, commuting with every arrow | The notion of "canonical map" made precise; a natural isomorphism is what "the same object in disguise" means |
| **Universal Property** | A characterization of an object by the arrows into or out of it | Defines free objects, products, quotients and tensor products without choosing a construction |
| **Adjunction** | A pair of functors with a natural bijection of hom-sets | The general form of "free construction is left adjoint to forgetting"; it generates monads |
| **Monad** | An endofunctor with unit and multiplication | The algebraic structure of a computation or an effect; the bridge to type theory and programming |
| **Monoidal Category** | A category with a tensor product and unit | The setting for [tensor](../tensor/tensor.md) products, quantum mechanics, and linear logic |

## Key results

- **Yoneda lemma.** An object is determined up to isomorphism by the arrows into it — the most quoted theorem in the subject, and the justification for "universal property" as a definition.
- **Limits and colimits.** Products, pullbacks, equalizers and their duals are one construction, so a theorem about limits is a theorem about all of them.
- **Free–forgetful adjunctions.** Groups, rings, modules and algebras are all free objects, hence all adjunctions.
- **Duality.** Every statement has a dual obtained by reversing arrows — the systematic source of half of mathematics (see [duality](duality.md)).

## Where it sits in this corpus

The corpus already *uses* category-theoretic language without naming it: [Map](../mapping/map.md) lists `Functor` as a kind of map, [homology](../topology/homology.md) is a functor from spaces to graded groups, and the [universal property](../construction/construction.md) of a construction is what the construction notes really state. This note is the vocabulary those claims need.

## References

- https://en.wikipedia.org/wiki/Category_theory
- [Map](../mapping/map.md) · [Duality](duality.md) · [Tensor](../tensor/tensor.md) · [Algebra](algebra/algebra.md) · [Homology](../topology/homology.md)
