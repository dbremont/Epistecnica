---
tags: [tool]
---

# Scikit-learn


> 

> Here’s a table summarizing the core modules in `scikit-learn`, a popular Python library for machine learning:
> 

| **Module** | **Description** | **Key Classes/Functions** | **Example Usage** |
| --- | --- | --- | --- |
| **`sklearn.datasets`** | Tools for generating and loading datasets. | `load_iris`, `load_boston`, `make_classification` | `sklearn.datasets.load_iris()` |
| **`sklearn.preprocessing`** | Functions for data preprocessing and feature extraction. | `StandardScaler`, `OneHotEncoder`, `PCA` | `sklearn.preprocessing.StandardScaler()` |
| **`sklearn.model_selection`** | Functions for splitting data, cross-validation, and hyperparameter tuning. | `train_test_split`, `GridSearchCV`, `KFold` | `sklearn.model_selection.train_test_split()` |
| **`sklearn.metrics`** | Metrics and scoring functions for evaluating models. | `accuracy_score`, `confusion_matrix`, `roc_auc_score` | `sklearn.metrics.accuracy_score()` |
| **`sklearn.linear_model`** | Linear models for regression and classification tasks. | `LinearRegression`, `LogisticRegression`, `Ridge` | `sklearn.linear_model.LinearRegression()` |
| **`sklearn.svm`** | Support Vector Machines for classification and regression. | `SVC`, `SVR`, `NuSVC` | `sklearn.svm.SVC()` |
| **`sklearn.tree`** | Decision tree-based models for classification and regression. | `DecisionTreeClassifier`, `DecisionTreeRegressor` | `sklearn.tree.DecisionTreeClassifier()` |
| **`sklearn.ensemble`** | Ensemble methods that combine multiple models to improve performance. | `RandomForestClassifier`, `GradientBoostingRegressor` | `sklearn.ensemble.RandomForestClassifier()` |
| **`sklearn.cluster`** | Clustering algorithms for unsupervised learning. | `KMeans`, `DBSCAN`, `AgglomerativeClustering` | `sklearn.cluster.KMeans()` |
| **`sklearn.decomposition`** | Dimensionality reduction techniques for feature extraction and compression. | `PCA`, `NMF`, `TruncatedSVD` | `sklearn.decomposition.PCA()` |
| **`sklearn.neighbors`** | Algorithms for nearest neighbors search and classification. | `KNeighborsClassifier`, `RadiusNeighborsRegressor` | `sklearn.neighbors.KNeighborsClassifier()` |
| **`sklearn.pipeline`** | Tools for building and using pipelines to streamline workflows. | `Pipeline`, `FeatureUnion` | `sklearn.pipeline.Pipeline()` |
| **`sklearn.compose`** | Tools for combining transformers and models, particularly in pipelines. | `ColumnTransformer`, `TransformedTargetRegressor` | `sklearn.compose.ColumnTransformer()` |
| **`sklearn.impute`** | Techniques for handling missing values in datasets. | `SimpleImputer`, `KNNImputer` | `sklearn.impute.SimpleImputer()` |
| … | … | .. | .. |

## References

- https://scikit-learn.org/
- https://scikit-learn.org/stable/user_guide.html
