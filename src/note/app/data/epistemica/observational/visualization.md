# Visualization


> In this note, we construct an index of data visualization techniques; for more detail, see:  ([Data Visualization](https://app.notion.com/p/Data-Visualization-29cc0f5171ec80fdbe89cd26c26feaac?pvs=21)).
> 

## How to think deeply about data visualization?

- Data visualization is the design of perceptual encodings that transform a captured representation of reality into a cognitively efficient medium for exploring and validating an affirmation space.
- **Data visualization** is the alchemy of transforming ontological residues into epistemic cartographies through calibrated semiotic encodings that leverage the bandwidth of human perception. It is a meta-representational practice—simultaneously capturing traces of reality and constructing cognitive scaffolds that compress high-dimensional state spaces into cognitively accessible forms—thereby turning the **hermeneutic circle** of inquiry into a navigable topology for the validation and falsification of propositions.

## How to visualize a list of numbers?

| Category | Technique | Description | Information Preserved | Lossiness | Scalability | Interpretability | Primary Use Case |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Distribution | Histogram | Binned frequency representation | Approx. distribution shape | Medium (binning) | High | High | General distribution inspection |
| Distribution | KDE | Smoothed density estimate | Continuous distribution shape | Medium (smoothing bias) | Medium–High | Medium | Detect modality, smooth structure |
| Distribution | Frequency Polygon | Line over bin midpoints | Approx. distribution shape | Medium | High | Medium | Compare distributions |
| Summary Statistics | Box Plot | Median, quartiles, outliers | 5-number summary + outliers | High | Very High | Very High | Robust comparison, outlier detection |
| Summary Statistics | Violin Plot | Box plot + density | Summary + distribution shape | Medium | Medium | Medium | Distribution + summary combined |
| Summary Statistics | Strip Plot | Raw data points (jittered) | Full data | Low | Low–Medium | High (small N) | Small datasets, exact values |
| Sequence / Order-Based | Line Plot | Connected ordered values | Value + order | Low | High | High | Trends, temporal structure |
| Sequence / Order-Based | Scatter (Index vs Value) | Points vs index | Value + order | Low | High | High | Non-interpolated sequence view |
| Sequence / Order-Based | Run Chart | Line plot with emphasis on shifts | Value + order + shifts | Low | High | High | Process monitoring |
| Discrete | Bar Chart | Values as bars | Exact values | Low | Low–Medium | Very High | Small categorical/numeric sets |
| Discrete | Dot Plot | Points instead of bars | Exact values | Low | Medium | Very High | Compact discrete visualization |
| Rank / Order Statistics | Sorted Value Plot | Sorted values plotted | Full data (ordered) | Low | High | High | Spread, monotonic structure |
| Rank / Order Statistics | ECDF | Cumulative distribution | Full distribution (no binning) | Low | Very High | Medium | Probabilistic queries |
| Density & Compact Encoding | Rug Plot | Marks each observation | Full data (minimal encoding) | Low | Low | Low–Medium | Supplementary density info |
| Density & Compact Encoding | 1D Heatmap | Density via color bins | Approx. density | Medium | Very High | Medium | Large-scale density overview |
| Comparative | Overlayed Histograms | Multiple histograms together | Relative distributions | Medium | Medium | Medium | Compare distributions |
| Comparative | Faceted Plots | Separate panels | Full per-group structure | Low–Medium | High | High | Multi-group comparison |

## References

- [Data Visualization](https://app.notion.com/p/Data-Visualization-29cc0f5171ec80fdbe89cd26c26feaac?pvs=21)
- https://datavizcatalogue.com/search/distribution.html
https://seaborn.pydata.org/tutorial/distributions.html
