---
tags: [search]
---

# Similarity Search


> **Similarity search** is a technique for finding items or data points in a dataset that are similar to a given query item or data point. The goal of similarity search is to identify items that are “close” to the query item in some sense, and the definition of “close” depends on the application.
> 

## Similarity Metrics

> In **similarity search**, each item in the dataset is typically represented as a vector in a **high-dimensional space**, where each dimension corresponds to a feature or attribute of the item. The similarity between two items is then defined in terms of the distance between their corresponding **vectors** in this space. Common **distance metrics** used for similarity search include **Euclidean distance**, **cosine similarity**, and **Jaccard similarity**.
> 

## Uses

1. **Information Retrieval**: In information retrieval, similarity search is used to find documents similar to a given query document. Search engines use this to find relevant documents based on the user’s search query.
2. **Image Retrieval**: In image retrieval, similarity search is used to find images that are similar to a given query image. This is used in applications such as reverse image search, where the user can upload an image and find similar images.
3. **Music Recommendation**: In music recommendation, similarity search is used to find songs that are similar to a given query song. This is used in music streaming services to recommend songs to users based on their listening history.
4. **Drug Discovery**: In drug discovery, similarity search is used to find molecules that are similar to a given query molecule. This is used to discover new drugs by identifying molecules that have similar chemical properties to known drugs.
5. **Fraud Detection**: In fraud detection, similarity search is used to find patterns of behavior that are similar to known fraudulent behavior. This is used to identify fraudulent transactions and prevent financial loss.

## References

- Gionis, Aristides, Piotr Indyk, and Rajeev Motwani. “Similarity search in high dimensions via hashing.” VLDB. Vol. 99. No. 6. 1999.
- Halevy, Alon, et al. “Similarity search for web services.” Proceedings of the 30th VLDB Conference. 2004.
- “Locality-Sensitive Hashing Scheme Based on p-Stable Distributions” by Moses Charikar (2002)
- Andoni, Alexandr, et al. “Beyond locality-sensitive hashing.” Proceedings of the twenty-fifth annual ACM-SIAM symposium on Discrete algorithms. Society for Industrial and Applied Mathematics, 2014.
- [Similarity Search](https://en.wikipedia.org/wiki/Similarity_search)
- [Faiss: The Missing Manual](https://www.pinecone.io/learn/faiss/)
- [Locality-Sensitive Hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)
- [faiss](https://github.com/facebookresearch/faiss)
- [Bisection method](https://www.wikiwand.com/en/Bisection_method)
- [Prune and search](https://www.wikiwand.com/en/Prune_and_search)
- [Feasible region](https://www.wikiwand.com/en/Feasible_region)
- [Text Search with Tries (2021) (chidiwilliams.com)](https://news.ycombinator.com/item?id=35028370)
- [eBay’s Blazingly Fast Billion-Scale Vector Similarity Engine](https://tech.ebayinc.com/engineering/ebays-blazingly-fast-billion-scale-vector-similarity-engine/)
