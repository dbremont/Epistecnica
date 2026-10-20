# Multidimensional Data Visualization

> In this note, we will explore the art of visualizing high-dimensional data—that is, data with more than three dimensions.
> 

Guiding Questions:

- What techniques exist for visualizing high-dimensional data?
- How to evaluate a visualization?
- What are the trade-offs and limitations of each technique?
- Why is it important to visualize high-dimensional data in the first place?

## Formulation

> How to think about Multidimensional Data Visualization?
> 

> Why is it important to visualize high-dimensional data in the first place?
> 

## Technique Space

> What techniques exist for visualizing high-dimensional data?
> 

> What are the trade-offs and limitations of each technique?
> 

| Technique | Description | Critical Review |
| --- | --- | --- |
| **Scatterplot Matrix (Pairplot)** | Grid of 2D scatterplots showing pairwise feature relationships. | Simple and interpretable for small dimensions (<10), but cluttered for high dimensions. |
| **Principal Component Analysis (PCA)** | Linear projection onto top principal components capturing most variance. | Captures global variance, but may miss non-linear patterns or local clusters. |
| **t-SNE (t-Distributed Stochastic Neighbor Embedding)** | Non-linear embedding emphasizing local neighborhood relationships. | Good for cluster detection, but distorts global structure and is sensitive to parameters. |
| **UMAP (Uniform Manifold Approximation and Projection)** | Non-linear embedding preserving local and some global structure. | Faster than t-SNE; preserves topology better, but parameter tuning affects results. |
| **Parallel Coordinates** | Each feature is a vertical axis; points are polylines crossing axes. | Shows correlations, but clutter grows with dataset size. |
| **Radial / Star Plots** | Axes radiate from a center; points plotted along axes. | Intuitive for comparing individual points; not scalable. |
| **HyperSlice / Projection Views** | Multiple 2D slices through subsets of dimensions. | Detailed local inspection, useful for functions or loss landscapes; complex to navigate. |
| **Glyphs / Chernoff Faces** | Map features to symbol properties (shape, size, orientation). | Good for small datasets; quickly confusing for large datasets. |
| **Self-Organizing Maps (SOMs)** | Maps high-dimensional data onto a 2D lattice preserving topology. | Useful for discovering clusters; interpretation may be tricky. |
| **Contour Plots / Level Sets** | Plots curves where a function (f(x_1,...,x_n)=c) is constant, usually 2–3 variables. | Clear for visualizing function topology; limited to low dimensions (2–3). |
| **Surface Plots (3D plots)** | 3D representation of a function (z=f(x,y)) with color/height encoding. | Very intuitive for 2-variable functions; cannot scale beyond 3 variables. |
| **Gradient / Vector Field Plots** | Visualize gradient vectors, slope directions, or flow in 2–3 variables. | Shows local behavior of functions; hard to generalize beyond 3D. |
| **Slicing / Cross-Sections** | Fix some variables and visualize remaining 2–3 dimensions. | Extends visualization to higher dimensions; requires multiple slices and interpretation effort. |
| **Level Hypersurfaces (Implicit Plots)** | Plots (f(x_1,...,x_n)=c) in higher dimensions via projections or slices. | Conceptually generalizes contours; hard to render or interpret in >3D directly. |

## Evaluation

> How to evaluate a visualization?
> 

| Criteria | Description |
| --- | --- |
| **Interpretability** | How easily a human can understand patterns, clusters, correlations, or anomalies in the visualization. |
| **Faithfulness / Accuracy** | How well the visualization preserves the true relationships, distances, or structures present in the original high-dimensional data. |
| **Scalability** | How well the visualization handles increasing numbers of dimensions or data points without becoming cluttered or misleading. |
| **Comparability** | Whether multiple subsets, groups, or models can be meaningfully compared using the visualization. |
| **Clarity of Patterns** | The extent to which the visualization highlights meaningful patterns, trends, or structures rather than noise. |
| **Dimensional Coverage** | How much of the original feature space is represented; whether important variables or combinations are visible. |
| **Flexibility / Adaptability** | Whether the technique can accommodate different data types (categorical, continuous) or transformations. |
| **Computational Efficiency** | The resources (time/memory) required to generate the visualization, particularly important for very high-dimensional datasets. |
| **Robustness** | Sensitivity of the visualization to hyperparameters (e.g., t-SNE perplexity) or outliers in the data. |
| **Insight Generation** | The ability of the visualization to support actionable insights, hypothesis formation, or model diagnostics. |

## Case Study

| Data Set | Description | Visualization Technique |
| --- | --- | --- |
| **MNIST** | Handwritten digits (28×28 pixels, 784-dimensional vectors) | t-SNE, UMAP, PCA for embedding; HyperSlice for weight-space visualization in neural networks |
| **Iris Dataset** | 4 features, 150 samples (sepal/petal length & width) | Scatterplot Matrix, Parallel Coordinates, Radial / Star Plots |
| **Neural Network Weight Space** | Thousands of parameters in trained networks | PCA, HyperSlice, Loss Landscape Visualization, Gradient / Vector Field Plots |
| **Gene Expression** | Thousands of genes per sample, often >100 samples | PCA, UMAP, Parallel Coordinates, SOMs |
| **Housing Dataset (Boston / Kaggle)** | Multivariate regression dataset with ~13 features | Scatterplot Matrix, Parallel Coordinates, PCA for dimensionality reduction |
| **Climate / Environmental Data** | Multi-sensor data: temperature, humidity, CO₂, etc., over time | Parallel Coordinates, Surface Plots (3 variables), Contour / Level Plots, Slicing for higher dimensions |
| **Customer Behavior / Marketing** | High-dimensional behavioral features: clicks, purchases, demographics | PCA, t-SNE, UMAP, Parallel Coordinates, Radial Plots |
| **Physics / Computational Simulations** | High-dimensional parameter sweeps in simulations | HyperSlice / Projection Views, Contour Plots, Surface Plots for selected slices, Level Hypersurfaces |

## References

- [Multidimensional Data Visualization](https://www.projects.science.uu.nl/ics-vig/uploads/DataVis/7.%20High-dimensional-vis.pdf)
- Li, Hao, et al. "Visualizing the loss landscape of neural nets." Advances in neural information processing systems 31 (2018).
- [Visualizing High-Dimensional Spaces](https://sethna.lassp.cornell.edu/Teaching/BasicTraining/Sloppy/Quinn_Visualizing_High-Dimensional_Spaces.pdf)
- https://en.wikipedia.org/wiki/Parameter_space
- [Manifold](https://app.notion.com/p/Manifold-0a4e49f73dc6401b986c5ea752d80e82?pvs=21)
- [**Embedding**](https://app.notion.com/p/Embedding-f47ac9d5aa264a5e90408da8292d9671?pvs=21)