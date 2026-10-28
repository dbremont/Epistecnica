---
tags: []
qa:
   - What does the phrase **model of meaning** mean?
   - Which are the models of meaning?
---

# Clark, S., Coecke, B., & Sadrzadeh, M. (2008). A compositional distributional model of meaning. Proceedings of the Second Quantum Interaction Symposium (QI-2008), 133–140.


```python
@inproceedings{clark2008compositional,
  title={A compositional distributional model of meaning},
  author={Clark, Stephen and Coecke, Bob and Sadrzadeh, Mehrnoosh},
  booktitle={Proceedings of the Second Quantum Interaction Symposium (QI-2008)},
  pages={133--140},
  year={2008},
  publisher={College Publications}
}
```

### Which are the epistemic and ontic elements contained in this document?

| Element Type | Element Tree Path | Description |
| --- | --- | --- |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Meaning | The content of a word or sentence; the paper's target phenomenon. |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Meaning `(→ Part)` `Phenomenon` `(→ Instance)` Word Meaning | The meaning of a lexical item, modelled as a vector. |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Meaning `(→ Part)` `Phenomenon` `(→ Instance)` Sentence Meaning | The meaning of a compound expression, computed from its constituents. |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Context | The words surrounding an occurrence; the observable basis of a word vector. |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Semantic Similarity | Closeness of meaning between words or sentences, measured by inner product. |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Grammaticality | Whether a string is well-typed under the grammatical type calculus. |
| Ontic | `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Truth Value | True or false of a sentence in the Boolean/Montague variant. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Symbolic Theory of Meaning | Meaning as symbolic, rule-governed composition (Dowty, Wall and Peters). |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Distributional Theory of Meaning | Meaning as co-occurrence statistics in a vector space (Schütze). |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Compositional Semantics | Sentence meaning determined by constituent meanings and combination rules. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Pregroup Semantics | Lambek's pregroup algebra as the grammar of grammatical types. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Categorical Quantum Semantics | Compact closed categories as the logic underlying vector-space composition. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Montague Semantics | Truth-conditional semantics recovered when scalars range over Booleans. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Theory` `(→ Instance)` Compositional Distributional Model | The paper's synthesis: distributional vectors plus pregroup composition. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` Vector Space Model of Meaning | Words as vectors whose basis vectors are context words. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` Meaning Space | A pair of a vector space and a grammatical type for a word or sentence. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` FVect × P Model | The product of finite-dimensional vector spaces and the pregroup. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Model` `(→ Instance)` FRel × P Model | The relational variant that recovers Montague semantics. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Finite-Dimensional Vector Space | Meaning space with a fixed basis and inner product. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Inner Product | The measure of similarity between vectors. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Tensor Product | The operation forming compound meaning spaces. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Linear Map | The morphism realising a type reduction on vectors. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Monoidal Category | The categorical structure with tensor and unit. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Compact Closed Category | The structure supplying adjoints and yanking equations. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Pregroup | A partially ordered monoid with left and right adjoints. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Partially Ordered Monoid | The algebraic base of a pregroup. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Posetal Category | A pregroup read as a category with at most one morphism per pair. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Pregroup Type | Basic types π, s, q, i, o and their adjoints. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Type Reduction | Cancellation of adjacent adjoint types to verify grammaticality. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Diagrammatic Calculus | Caps, cups and wire-yanking diagrams for reductions. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Semiring | The scalar structure generalising real-valued matrices. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Representation` `(→ Has)` `Representational System` `(→ Instance)` Category of Relations | FRel, the Boolean-semiring limit of FVect. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Pregroup Analysis | Assigning types to words and reducing a sentence to its main type. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Type-Reduction Lifting | Lifting pregroup reductions to morphisms on meaning spaces. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Corpus-Based Vector Estimation | Building word vectors from co-occurrence counts. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Inner-Product Comparison | Comparing sentence meanings in a single space. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Word Sense Discrimination | The Schütze procedure cited as the distributional method. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Thesaurus Construction | Curran's similarity-based thesaurus as an application. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Truth-Vector Computation | Computing sentence truth by Boolean or relational encoding. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Matrix Calculus | Matrices over a semiring as the computational form. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Construction` `(→ Kind)` `Dataset` `(→ Instance)` Text Corpus | The body of text supplying co-occurrence data. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Evaluation` `(→ Instance)` John Likes Mary Example | The worked truth-vector computation for a transitive sentence. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Evaluation` `(→ Instance)` Loves/Likes/Hates Example | The superposition example showing verb meaning propagating to sentence similarity. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Evaluation` `(→ Instance)` Sentence Similarity Test | Comparing arbitrary sentence meanings by inner product. |
| Epistemic | `Epistemic Element` `(→ Kind)` `Aggregate` `(→ Instance)` Meaning Inquiry `(→ Kind)` `Epistemic Operation` `(→ Kind)` `Organization` `(→ Kind)` `Method` `(→ Instance)` Curry–Howard Correspondence | Proposed isomorphism between compact closed categories and bicompact linear logic; future work. |

### Why do purely representational (embedding-based) approaches fail to fully capture meaning?

> In this paper, the proposed model of meaning is a purely representational one. By *purely representational*, we mean an approach that models meaning through mathematical representations, rather than through its use in action and interaction.

> Representational (embedding-based) approaches model meaning as vectors in a mathematical space, using contextual co-occurrence to represent words and compositional operations to derive sentence meanings. However, a representation of meaning is not necessarily a complete account of meaning itself.

> Meaning is also embedded in use, but a purely representational approach falls short of capturing this dimension. Attempting to imitate the use of language was one way in which LLMs became able to capture meaning, at least to a considerable extent.

## References

- [Paper](https://www.academia.edu/2654380/A_compositional_distributional_model_of_meaning?auto=download)
