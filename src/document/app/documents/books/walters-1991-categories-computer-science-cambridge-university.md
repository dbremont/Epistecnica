# Walters, R. F. C., & Walters, R. F. (1991). Categories and computer science. Cambridge University Press.


```python
@book{walters1991categories,
  title={Categories and computer science},
  author={Walters, Robert Frank Carslaw and Walters, Richard F},
  year={1991},
  publisher={Cambridge University Press}
}
```

## Notes

---

> Functions are used to model variation.
> 

> Category theory is the algebra of functions; the principal operation on functions is taken to be composition.
> 

> A Category is a collection of objects, with a collection of arrows between them. Take as examples (geometric object , transformations).
> 

> Category theory was invented by S. Eilenberg and S. Mac Lane in 1945 and arose out of their work in algebraic topology.
> 

> Note. This book contains many taken from examples; and computer science; a computer science background is not necesarry.
> 

> Note. The names set, and functions are just names; better used collection, and maps / relations, or morphisms for them.
> 

> Note. Thinking deeply about function composition; commutativty, ...; Which type of functions are needed in order to this property holds?
> 

QA:

- Which are the properties of morphism composition?
- How to re-formulation functions operatiosn like multiplication or addition to composition?
- What is the meaning of a category with only one object? Can That Object be a Set?
- How to model formal languages systems using category theory?
- What is the pragmatic of the co-product (sum), and product categories? Does this have any relations with the product and sum types?

## The Algebra of Functions

> A Category is an algebra of functions; and composition is its main operation. They are many categories in computer; that goes unnotice; like iteration; func(S_1, iterationControl) -> func(S_1, interactionControl) -> ... Stop.
> 

> A category is composed by a "set of sets"; and a set of morphirms(functions) that goes between them.
> 

> A Category with only one object is called a monoid.
> 

> An arrow is called isomorphic if it has an inverse.
> 

> Dual Category Of A: Its another category B; with the same object; but maps reverse.
> 

A common way to describe an algebraic structure is to used:

- some of the elements (which are called generators); and
- some equestions between values of the operations (called relations).

Some Categories:

- Vector (finite-dimensional vector spaces, linear maps),
- Groups (groups, group homomorphism)
- Metric Space (metric spaces, continous maps)
- Relation (sets, binary relations)
- Par ???: (Set, Partial Functions)

## Products and Sums

> Note: Product Here does not means multiplication; and sum does not mean addition. Sad and horrible terminology;
> 

> Product, Sum Properties: if there is an arrow (product, sum) that maps two objects in the category; to a third one.  "Multi Object Arrow".
> 

> Characterictif Function of a set.
> 

> Initial Objects: ...
> 

> Terminal Objects: ...
> 

## Distributed Categories

> Products represents computation on data, sum represents control flow; key abstractions for analyzing computations.
> 

> Distributed Law: ...
> 

## Data Types

## Categories of Functors

## More About Products

## Computational Category Theory

> ...
>
