---
tags: [representation]
---

# Text Document Representation


**Set-theoretic models** represent documents as sets of words or phrases. Similarities are usually derived from set-theoretic operations on those sets. Common models are: 

- Standard Boolean model
- Extended Boolean model
- Fuzzy retrieval

**Algebraic models** represent documents and queries as vectors, matrices, or tuples. The similarity of the query vector and document vector is represented as a scalar value: 

- Vector space model
- Generalized vector space model
- (Enhanced) Topic-based Vector Space Model
- Extended Boolean model
- Latent semantic indexing, a.k.a. latent semantic analysis.

**Probabilistic models** treat the process of document retrieval as a probabilistic inference. Similarities are computed as probabilities that a document is relevant for a given query. Probabilistic theorems like the Bayes’ theorem are often used in these models.

- Binary Independence Model
- Probabilistic relevance model on which is based the okapi (BM25) relevance function
- Uncertain inference
- Language models
- Divergence-from-randomness model
- Latent Dirichlet allocation