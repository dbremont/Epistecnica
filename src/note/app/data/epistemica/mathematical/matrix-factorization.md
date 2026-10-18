---
tags: [inference, linear-algebra]
---

# Matrix Factorization

 : Matrix (Matrix%20171c0f5171ec80c58898c4e26151fbb8.md)

> 

## Collaborative Filtering

> Collaborative filtering assumes that users with similar preferences for specific items are likely to have similar preferences for other items. This can be represented mathematically as a user-item rating matrix, where each row represents a user, each column represents an item, and each entry in the matrix represents a rating the user gives. However, this matrix is typically very sparse because most users have only rated a small subset of items.
> 

> Matrix factorization is a technique that can be used to decompose the user-item rating matrix into two lower-dimensional matrices, one representing users and the other representing items. Doing so can help reduce the sparsity of the matrix and uncover hidden relationships between users and items. Specifically, it seeks to find latent factors representing the items' underlying features and the users' preferences.
> 

> Once the matrix has been factorized, the resulting lower-dimensional matrices can be used to predict ratings for items that a user has not yet rated based on the user’s preferences for the latent factors and the item’s characteristics in those factors. This allows the system to recommend items to users that they are likely to be interested in, even if they have not explicitly rated those items in the past.
> 

## References

- https://en.wikipedia.org/wiki/Matrix_decomposition
- https://en.wikipedia.org/wiki/Matrix_factorization_(recommender_systems)
- https://arxiv.org/abs/2203.11026
