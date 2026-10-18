---
tags: [technique]
---

# Principal Component Analysis (PCA)

 : Multicollinearity (Multicollinearity%2013cc0f5171ec80f08d22e7750df85ca6.md), Dimensionality Reduction (Dimensionality%20Reduction%203d78f26791cb44ce9c50211dab243e97.md)

> **Principal Component Analysis (PCA):** A method for reducing the dimensionality of multivariate data while retaining the most essential information.
> 

> In **Principal Component Analysis (PCA)**, the **covariance matrix** reveals feature relationships, with **eigenvalues** indicating directions of maximum variance. PCA reduces dimensionality by retaining principal components with the largest eigenvalues, capturing key data patterns in fewer dimensions.
> 

> The term **"principal component" in PCA** can be misleading, especially for beginners, as these are synthetic or derived features, not the original ones.
> 

## References

- [Principal component analysis](https://www.nature.com/articles/s43586-022-00184-w)
- https://en.wikipedia.org/wiki/Principal_axis_theorem
- https://en.wikipedia.org/wiki/Principal_component_analysis
- https://dataknowsall.com/blog/pcavisualized.html
- https://math.stackexchange.com/questions/3869/what-is-the-intuitive-relationship-between-svd-and-pca
- https://stats.stackexchange.com/questions/134282/relationship-between-svd-and-pca-how-to-use-svd-to-perform-pca
- https://stats.stackexchange.com/questions/81395/relationship-between-ridge-regression-and-pca-regression
- https://news.ycombinator.com/item?id=30876293
- https://arxiv.org/abs/1610.09733
- https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
- https://en.wikipedia.org/wiki/Biplot
- http://danluu.com/linear-hammer/
- [Principal Component Analysis (PCA)](https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/resources/mit18_650f16_pca/)
- [Understanding and Using Principal Component Analysis (PCA)](https://web.stanford.edu/class/cs168/l/l7.pdf)
- [‣](https://app.notion.com/p/9850521bfef94a4faeea15fbf9e630d3?pvs=21)
- [Eigenvector](../mathematical/eigenvector.md)
- 
- [Covariance Matrix](../mathematical/covariance-matrix.md)
- [Singular Value Decomposition (SVD)](../mathematical/singular-value-decomposition-svd.md)
- https://github.com/GeostatsGuy/DataScienceInteractivePython/blob/main/Interactive_PCA_Eigen.ipynb

```python
@article{pearson1901liii,
  title={On lines and planes of closest fit to systems of points in space},
  author={Pearson, Karl},
  journal={The London, Edinburgh, and Dublin philosophical magazine and journal of science},
  volume={2},
  number={11},
  pages={559--572},
  year={1901},
  publisher={Taylor \& Francis}
}
```

```python
@article{hotelling1933analysis,
  title={Analysis of a complex of statistical variables into principal components.},
  author={Hotelling, Harold},
  journal={Journal of educational psychology},
  volume={24},
  number={6},
  pages={417},
  year={1933},
  publisher={Warwick \& York}
}
```

```python
@article{shlens2014tutorial,
  title={A tutorial on principal component analysis},
  author={Shlens, Jonathon},
  journal={arXiv},
  year={2014}
}
```

```python
@BOOK{Jolliffe2002-ug,
  title     = "Principal Component Analysis",
  author    = "Jolliffe, Ian T",
  publisher = "Springer",
  series    = "Springer Series in Statistics",
  edition   =  2,
  month     =  oct,
  year      =  2002,
  address   = "New York, NY",
  language  = "en"
}
```

[http://cda.psych.uiuc.edu/statistical_learning_course/Jolliffe I. Principal Component Analysis (2ed., Springer, 2002)(518s)_MVsa_.pdf](http://cda.psych.uiuc.edu/statistical_learning_course/Jolliffe%20I.%20Principal%20Component%20Analysis%20(2ed.,%20Springer,%202002)(518s)_MVsa_.pdf)
