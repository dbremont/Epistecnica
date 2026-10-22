# Recommender System


> Search and filter.
> 

## List of Recommender Systems Methods

> Here’s a table summarizing different methods used in recommender systems:
> 

| **Method** | **Description** | **Examples/Applications** |
| --- | --- | --- |
| **Collaborative Filtering** | Recommends items by analyzing past interactions (e.g., ratings, clicks) between users and items. | Netflix movie recommendations, Amazon product suggestions. |
| **Content-Based Filtering** | Recommends items based on similarity between item features and user profiles or past interactions. | Spotify suggests songs based on a user’s listening history and news article recommendations. |
| **Hybrid Methods** | Combines collaborative filtering and content-based filtering to improve recommendation accuracy and address their limitations. | YouTube video recommendations and e-commerce sites combine user behavior and item features. |
| **Matrix Factorization** | Decomposes the user-item interaction matrix into lower-dimensional matrices to capture latent factors for recommendations. | Netflix uses Singular Value Decomposition (SVD) in its recommendation algorithm. |
| **Deep Learning-Based Methods** | Uses neural networks to model complex patterns in user-item interactions, often leveraging embeddings and multi-modal data. | Personalized content on platforms like Instagram, Pinterest, or Netflix. |
| **Association Rule Learning** | Identifies associations or correlations between items in large datasets used for market basket analysis. | Amazon’s "Customers who bought this also bought" feature. |
| **Knowledge-Based Recommenders** | Uses domain-specific knowledge about users and items to make recommendations, often involving explicit user preferences. | Travel or real estate websites recommend options based on user input criteria. |
| **Context-Aware Recommenders** | Incorporates contextual information (e.g., time, location, device) into the recommendation process. | Mobile app recommendations based on location and time-sensitive offers on e-commerce sites. |
| **Graph-Based Methods** | Models users and items as nodes in a graph, with edges representing interactions, to capture complex relationships. | Social media friend suggestions, LinkedIn’s "People You May Know". |
| **Bandit-Based Approaches** | Uses exploration-exploitation strategies to recommend items while optimizing for user satisfaction over time. | News article recommendations where new content is frequently introduced. |
| **Latent Factor Models** | Identifies hidden (latent) factors that explain user preferences and item characteristics, often used in collaborative filtering. | Movie or music recommendation systems. |
| **Sequential/Session-Based Models** | Models user behavior as a sequence of interactions, often using RNNs or transformers for session-based recommendations. | Spotify’s playlist continuation, e-commerce browsing history-based recommendations. |
| **Social-Based Recommenders** | Leverages social network data and user connections to provide personalized recommendations. | Facebook’s content suggestions are based on friends’ interactions. |

## **References**

- [Recommender System](https://en.wikipedia.org/wiki/Recommender_system)
- [Information Filtering System](https://en.wikipedia.org/wiki/Information_filtering_system)
- [Twitter’s Recommendation Algorithm (blog.twitter.co](https://news.ycombinator.com/item?id=35391433)
- [Monolith: Real Time Recommendation System With Collisionless Embedding Table](https://arxiv.org/pdf/2209.07663.pdf)
- [Real-Time Personalisation of Search Results with Auto Trader’s Customer Data Platform](https://engineering.autotrader.co.uk/2022/11/23/real-time-personalisation-of-search-results-with-auto-traders-customer-data-platform.html)
- Hanani, U., Shapira, B., Shoval, P. (2001) Information filtering: Overview of issues, research and systems. User Modeling and User-Adapted Interaction, 11, pp. 203–259.
- Smith, Brent, and Greg Linden. "Two decades of recommender systems at Amazon. com." *Ieee internet computing* 21.3 (2017): 12-18.
- https://github.com/bytedance/monolith
- https://github.com/twitter/the-algorithm
