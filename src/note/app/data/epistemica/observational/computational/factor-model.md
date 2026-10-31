---
tags: [fixed-structure-parametric-model, technique]
---

# Factor Model


> **Factor Analysis:** A technique for reducing the dimensionality of data by identifying underlying factors that explain correlations among observed variables.
> 

## List of Methods

> 

| **Method** | **Description** | **Common Use** |
| --- | --- | --- |
| **Principal Component Analysis (PCA)** | PCA reduces the dimensionality of data by creating uncorrelated variables (principal components) that explain the most variance in the data. | Used for data reduction, pattern recognition, feature extraction, noise removal. |
| **Exploratory Factor Analysis (EFA)** | EFA seeks to uncover the underlying factors or latent variables that explain correlations among observed variables, often used when the relationships among variables are not predefined. | Identifying latent variables in social sciences, psychology, and marketing. |
| **Confirmatory Factor Analysis (CFA)** | CFA tests predefined hypotheses about the relationships between observed variables and latent factors. It's used to confirm the validity of a factor model. | Validating theoretical models, especially in structural equation modeling (SEM). |
| **Factor Rotation (Varimax, Promax, etc.)** | Factor rotation, applied after extraction, helps in making factor patterns more interpretable. Varimax is orthogonal, while Promax is oblique, allowing for correlated factors. | Improving factor interpretability in EFA by simplifying the factor structure. |
| **Maximum Likelihood Factor Analysis (MLFA)** | A method for estimating the parameters of a factor model by maximizing the likelihood function, assuming the data follow a multivariate normal distribution. | Estimating models when data are normally distributed, especially in structural equation modeling (SEM). |
| **Bayesian Factor Analysis** | Bayesian Factor Analysis incorporates prior beliefs and probabilistic models to estimate the factors and their loadings, offering a flexible and interpretable framework for analyzing complex data. | Used when prior information is available or when a probabilistic approach is required for model inference. |
| **Principal Axis Factoring (PAF)** | PAF is used to extract common factors that explain shared variance among observed variables, emphasizing the common variance while ignoring unique variance. | Often used in social sciences when dealing with correlated data or when shared variance is more important. |
| **Dynamic Factor Models (DFMs)** | DFMs extend traditional factor analysis by modeling dynamic relationships between factors and observed variables over time, typically used for analyzing time-series data. | Time-series data analysis, modeling economic and financial systems with latent factors driving changes over time. |
| **Factor-Augmented Vector Autoregressions (FAVARs)** | FAVARs combine factor analysis with vector autoregressions (VARs), incorporating latent factors as additional variables in a VAR model to improve forecasting and understanding of economic relationships. This approach captures information across multiple time series with common latent dynamics. | Economic forecasting, especially in situations with large datasets where latent variables affect multiple economic indicators. |
| **Sparse Factor Models** | These models are designed to select only the most important factors by imposing sparsity constraints on factor loadings. This approach is useful when you have many potential factors, but only a few have significant impacts. | Feature selection and dimensionality reduction, particularly in high-dimensional settings (e.g., finance, genomics). |
| **Non-Negative Matrix Factorization (NMF)** | NMF factorizes a matrix into two non-negative matrices, which can be useful for data where negative values do not make sense, such as in image processing, document classification, or market basket analysis. | Data extraction from non-negative data, such as in image or document clustering. |

## References

- [Factor analysis](https://en.wikipedia.org/wiki/Factor_analysis)
- [g, a Statistical Myth](http://bactra.org/weblog/523.html)
