---
tags: [abstract-framework]
---

# Statistical Function

 : Operator (Operator%2025dc0f5171ec80028e91f72271b1e913.md), (Statistic) Estimator ((Statistic)%20Estimator%2010fc0f5171ec8015accadab377f913a5.md)

> In this note we will develop a unified abstraction -  a statistical function a mapping between some data capturing (data set ,distribution,  model,  etc) to  a scalar, etc.
> 

> This node represents the entry point to the function (operator, functional, etc.) used across all frameworks to observe and represent systems.
> 

## Signature

> Signatures describe the type of mapping, emphasizing the domain (input) and codomain (output), without tying to a specific field. They can be **functional** (producing numbers, vectors, distributions, labels, or functions) or **operator** (producing transformations or evolving other entities).
> 

> **Note:** Do not take this terminology as fixed or authoritative; it is intended only to help us understand the structure of certain types of functions.
> 

| Name | **Signature** | Description | Instance(s) |
| --- | --- | --- | --- |
| Functional | **Set → Scalar** | Maps a set of elements to a single numeric value summarizing some property. | Mean, Variance, Entropy, Cardinality |
| Functional | **Set → Vector** | Maps a set of elements to a vector, capturing multiple aggregated properties. | Histogram counts, Feature vector |
| Functional | **Function → Basic Object** | Evaluates a property from a function, e.g., extracting summary measures. | $\int f(x)dx$, $\max f(x)$ |
| Functional | **Set → Tag (Label)** | Maps a set of elements to a qualitative label or category. | Cluster assignment (k-means), Classification label (spam/not spam) |
| Functional | **Set → Distribution** | Maps a set of elements to a full distribution or function describing variation across the set. | Empirical CDF, Kernel density estimate |
| Functional | **Function → Distribution** | Converts a function into a distribution-like representation. | Fourier power spectrum, Histogram of function values |
| Operator | **Set → Operator** | Produces an operator or transformation acting on the system or set. | Covariance operator, Transition matrix, Adjacency operator |
| Operator | **Operator → Operator** | Evolves or modifies an operator according to a rule or process. | Matrix exponentiation, Functional derivative, Commutator $[A,B]$ |
| Operator (Functional) | **Set → Function** | Maps a set of elements to a function capturing relationships, correlations, or behaviors. | Empirical CDF, Regression function, Correlation function |
| Operator | **Function → Function** | Evolves a function over a domain, e.g., transformation or propagation. | Differential operator, Convolution operator, Time-evolution semigroup |
| Plain Function | **Basic Object → Basic Object** | Maps numeric summaries to other summaries, e.g., aggregations, transformations, or feature mappings. | Scaling $x\mapsto ax+b$, Standardization $z=(x-\mu)/\sigma$, PCA projection |

## Statistical Function Space

> **Note:** The meaning of each function depends on the types of objects involved, so this taxonomy is necessarily limited. In most cases, the “objects” can be understood as random variables.
> 

> **Affirmation Space Encoding:** A statistical function maps an object representing data to another object. The resulting object typically provides a more compressed representation that captures some aspect of the affirmation space underlying the original data.
> 

> Note: This functions capture elements of the affirmation space related to the generator - they  are not generic statistical procedures - to **validate the inference**, etc.
> 

> Tag(s): Area of Used Role, Apply, Fundamental, etc.
> 

> Functional Signature: I →  R Types.
> 

> Variant(s):  Variations.
> 

> Random Variables - [Operator](random-variable.md).
> 

| Category | Function | Function Spec | Description | Affirmation Space Encoding | Variant(s) | Tags |
| --- | --- | --- | --- | --- | --- | --- |
| **Central Tendency & Moments** | Mean | $\mu = \frac{1}{n}\sum x_i$ | Central point of mass in the data distribution. | Affirmation of the expected value or central generative tendency. | Trimmed Mean; Winsorized Mean; Weighted Mean; Geometric Mean; Harmonic Mean; Root Mean Square | Fundamental, Descriptive, Central |
| **Central Tendency & Moments** | Median | $M = \tilde{x}$ | Middle value of sorted data. | Affirmation of the typical value robust to outliers. | None | Fundamental, Descriptive, Robust |
| **Central Tendency & Moments** | Mode | $\arg\max f(x)$ | Most frequent value in the dataset. | Affirmation of the maximum likelihood observation or peak generative state. | None | Fundamental, Descriptive, Nominal |
| **Central Tendency & Moments** | Skewness | $\gamma_1 = E[(X-\mu)^3]/\sigma^3$ | Measure of asymmetry around the mean. | Affirmation of directional tail weight or generative drift. | None | Moment, Shape, Distributional |
| **Central Tendency & Moments** | Kurtosis | $\gamma_2 = E[(X-\mu)^4]/\sigma^4 - 3$ | Measure of tailedness and peakedness. | Affirmation of extreme event propensity within the generator. | None | Moment, Shape, Distributional |
| **Dispersion & Variability** | Range | $R = \max(X) - \min(X)$ | Total spread between extreme values. | Affirmation of the absolute bounds of the generated space. | Minimum; Maximum | Fundamental, Descriptive, Bounds |
| **Dispersion & Variability** | Interquartile Range (IQR) | $IQR = Q_3 - Q_1$ | Spread of the middle 50% of data. | Affirmation of typical dispersion resistant to generative anomalies. | Semi-Interquartile Range | Robust, Descriptive, Spread |
| **Dispersion & Variability** | Variance | $\sigma^2 = \frac{1}{n}\sum(x_i - \mu)^2$ | Average squared deviation from the mean. | Affirmation of informational content, spread, and generative volatility. | Between-Groups Variance; Within-Groups Variance; Total Variance; Pooled Variance; Root Pooled Variance; Harmonic Variance; Semi-Variance; Downside Deviation | Fundamental, Inferential, Spread |
| **Dispersion & Variability** | Standard Deviation | $\sigma = \sqrt{\sigma^2}$ | Square root of variance. | Affirmation of typical distance from the generative center. | None | Fundamental, Descriptive, Spread |
| **Dispersion & Variability** | Coefficient of Variation | $CV = \sigma / \mu$ | Ratio of standard deviation to mean. | Affirmation of scale-independent relative risk or spread. | Coefficient of Dispersion | Relative, Scale-Invariant, Risk |
| **Dispersion & Variability** | Mean Absolute Deviation | $MAD = \frac{1}{n}\sum|x_i - \mu|$ | Average absolute distance from the mean. | Affirmation of expected absolute generative error. | None | Robust, Descriptive, Spread |
| **Dispersion & Variability** | Median Absolute Deviation | $MAD = \text{median}(|x_i - \text{median}(X)|)$ | Median absolute distance from the median. | Affirmation of robust typical deviation in noisy generators. | None | Robust, Descriptive, Outlier-Resistant |
| **Quantiles & Ranks** | Quantiles | $Q(p) = F^{-1}(p)$ | Value at a specific cumulative probability. | Affirmation of distributional thresholds and generative boundaries. | Quartiles; Quintiles; Deciles; Percentiles | Fundamental, Distributional, Thresholds |
| **Quantiles & Ranks** | Standard Score | $Z = (x - \mu) / \sigma$ | Distance from mean in standard deviation units. | Affirmation of relative standing within the generative distribution. | T-Score; Stanine Score; Normalized Score; Standard Score Deviation | Standardization, Comparative, Scaling |
| **Correlation & Association** | Pearson Correlation Coefficient | $\rho = \text{cov}(X,Y)/(\sigma_X \sigma_Y)$ | Linear dependence between two variables. | Affirmation of linear co-movement in the bivariate generative space. | Spearman Rank Correlation; Kendall Tau; Point-Biserial Correlation; Phi Coefficient; Partial Correlation; Semi-Partial Correlation; Assortativity Coefficient; Correlation of Asset Returns; Covariance of Asset Returns | Association, Linear, Bivariate |
| **Correlation & Association** | Cramér's V | $V = \sqrt{\chi^2 / (n \min(c-1, r-1))}$ | Association between two nominal variables. | Affirmation of categorical dependency strength. | Contingency Coefficient | Categorical, Association, Nominal |
| **Correlation & Association** | Eta Squared | $\eta^2 = SS_{between} / SS_{total}$ | Non-linear correlation ratio for categorical-continuous data. | Affirmation of categorical-continuous association magnitude. | None | Association, Categorical-Continuous |
| **Regression & Prediction** | Regression Coefficient (Slope) | $\beta = \text{cov}(X,Y)/\text{var}(X)$ | Change in Y per unit change in X. | Affirmation of systematic predictive relationship in the generator. | Fixed Effects Coefficient; Autoregressive Coefficients (AR); Moving Average Coefficients (MA); ARMA/ARIMA/Seasonal ARIMA Coefficients; Poisson/NegBin/Quasi-Poisson Regression Coefficient; Geographically Weighted Regression Coefficients | Predictive, Inferential, Linear |
| **Regression & Prediction** | Intercept | $\alpha = \mu_Y - \beta\mu_X$ | Expected value of Y when X is zero. | Affirmation of the baseline generative state. | None | Predictive, Baseline |
| **Regression & Prediction** | R-Squared (R²) | $R^2 = 1 - SS_{res}/SS_{tot}$ | Proportion of variance explained by the model. | Affirmation of model's explanatory power over the generator. | Adjusted R²; Bayesian R²; Geographically Weighted R² | Predictive, Model Fit, Explained Variance |
| **Regression & Prediction** | Best Linear Unbiased Estimator (BLUE) | $\hat{\beta} = (X^TX)^{-1}X^Ty$ | Gauss-Markov optimal linear estimator. | Affirmation of minimum variance linear parameter extraction. | BLUP (Best Linear Unbiased Predictor) | Inferential, Optimal Estimation, Linear |
| **Effect Size** | Effect Size (Cohen’s d) | $d = (\mu_1 - \mu_2) / \sigma_{pooled}$ | Standardized mean difference between groups. | Affirmation of practical magnitude of a generative separation. | Hedges’ g; Glass’ Δ; Cliff’s Delta; Pearson’s r for Effect Size; Cohen’s f; Partial Eta Squared; Omega Squared; Epsilon Squared | Inferential, Magnitude, Standardized |
| **ANOVA & Group Comparisons** | Mean Square Error | $MSE = SS_{within} / df_{within}$ | Variance within groups (unexplained). | Affirmation of unexplained noise or natural generative variance. | Mean Square Between; Mean Square Within | Inferential, ANOVA, Noise |
| **ANOVA & Group Comparisons** | Planned Contrasts Statistic | $\Psi = \sum c_i \mu_i$ | Specific weighted comparison between group means. | Affirmation of a hypothesized structural difference in the generator. | Orthogonal Contrasts Statistic | Inferential, ANOVA, Hypothesis-Driven |
| **Risk, Odds & Rates** | Odds Ratio | $OR = (a/b) / (c/d)$ | Ratio of odds of event in two groups. | Affirmation of relative exposure effect in a binary generator. | Odds Ratio Log-Transform | Epidemiological, Binary, Association |
| **Risk, Odds & Rates** | Relative Risk | $RR = [a/(a+b)] / [c/(c+d)]$ | Ratio of probabilities of event in two groups. | Affirmation of relative risk change due to generative condition. | Risk Ratio Log-Transform; Hazard Ratio; Subdistribution Hazard Ratio | Epidemiological, Binary, Risk |
| **Risk, Odds & Rates** | Risk Difference | $RD = P_1 - P_0$ | Absolute probability difference between groups. | Affirmation of absolute change in generative event frequency. | Attributable Risk; Population Attributable Risk (PAR); Population Attributable Fraction (PAF) | Epidemiological, Absolute Risk |
| **Risk, Odds & Rates** | Incidence Rate | $IR = \text{New Cases} / \text{Person-Time}$ | Rate of new events per unit time. | Affirmation of the temporal speed of the generative event process. | Prevalence; Attack Rate; Case Fatality Rate; Mortality Rate; Age-Standardized Mortality Rate; Standardized Mortality Ratio (SMR); Relative Survival; Standardized Incidence Ratio; Age-Adjusted Incidence Rate | Epidemiological, Frequency, Time-Based |
| **Survival & Event History** | Survival Function Estimate | $\hat{S}(t) = \prod_{t_i \le t} (1 - d_i/n_i)$ | Probability of surviving past time $t$. | Affirmation of persistence duration of the generative subject. | Median Survival Time; Restricted Mean Survival Time; Cumulative Incidence Function; Competing Risks Statistics | Survival, Time-to-Event, Probability |
| **Survival & Event History** | Hazard Function | $h(t) = f(t) / S(t)$ | Instantaneous failure rate at time $t$. | Affirmation of instantaneous event propensity of the generator. | Cumulative Hazard Function; Baseline Hazard Function | Survival, Time-to-Event, Instantaneous |
| **Survival & Event History** | Concordance Index (C-Index) | $C = P(\hat{h}(t_i) > \hat{h}(t_j) | T_i < T_j)$ | Ranking accuracy of predicted survival times. | Affirmation of predictive ordinal accuracy of the survival model. | None | Survival, Model Evaluation, Discrimination |
| **Survival & Event History** | Accelerated Failure Time Coefficient | $\ln(T) = \mu + \sigma W + \gamma^T Z$ | Log-time scaling factor. | Affirmation of time-compression or expansion effect of a covariate. | None | Survival, Parametric, Regression |
| **Distribution Parameters** | Continuous Distribution Shape Parameter | $\alpha$ (e.g., Weibull, Gamma, Log-Logistic) | Controls the form/shape of the probability density. | Affirmation of distributional tail behavior and peak focus. | Weibull Shape Parameter; Gamma Shape Parameter; Log-Logistic Shape Parameter | Parametric, Distributional, Shape |
| **Distribution Parameters** | Continuous Distribution Scale Parameter | $\beta$ (e.g., Weibull, Gamma, Log-Logistic) | Stretches or compresses the distribution. | Affirmation of distributional spread or width. | Weibull Scale Parameter; Gamma Scale Parameter; Log-Logistic Scale Parameter | Parametric, Distributional, Spread |
| **Distribution Parameters** | Exponential Rate Parameter | $\lambda$ | Rate of decay in exponential distribution. | Affirmation of memoryless event frequency. | None | Parametric, Distributional, Rate |
| **Distribution Parameters** | Beta Distribution Parameters | $\alpha, \beta$ (domain $[0,1]$) | Shape of bounded probability distributions. | Affirmation of structural boundaries of probability generators. | None | Parametric, Distributional, Bounded |
| **Distribution Parameters** | Lognormal Distribution Parameters | $\mu, \sigma$ (of $\ln(X)$) | Parameters of the log-normal probability density. | Affirmation of multiplicative generative process characteristics. | None | Parametric, Distributional, Logarithmic |
| **Reliability & Psychometrics** | Intraclass Correlation Coefficient (ICC) | $ICC = \sigma^2_{between} / (\sigma^2_{between} + \sigma^2_{within})$ | Measure of absolute agreement/consistency. | Affirmation of rater/object interchangeability in the generator. | Inter-Rater Reliability; Test-Retest Reliability; Coefficient of Stability; Coefficient of Equivalence; Agreement Coefficient | Psychometrics, Reliability, Agreement |
| **Reliability & Psychometrics** | Cohen’s Kappa | $\kappa = (p_o - p_e) / (1 - p_e)$ | Chance-corrected categorical agreement. | Affirmation of true categorical concordance beyond baseline. | Fleiss’ Kappa; Weighted Kappa; Gwet’s AC1 | Psychometrics, Reliability, Categorical |
| **Reliability & Psychometrics** | Composite Reliability | $CR = (\sum \lambda_i)^2 / [(\sum \lambda_i)^2 + \sum \theta_i]$ | Reliability of a latent construct scale. | Affirmation of internal consistency of a multi-item generator. | McDonald’s Omega; Split-Half Reliability; Spearman-Brown Prophecy Formula; Coefficient of Homogeneity | Psychometrics, Reliability, Scale |
| **Reliability & Psychometrics** | Item-Total Correlation | $r_{x_i, X_{-i}}$ | Correlation of an item with the summed rest. | Affirmation of individual item alignment with the latent generator. | Item-Rest Correlation; Average Inter-Item Correlation | Psychometrics, Reliability, Item Analysis |
| **Dimensionality & Factor** | Eigenvalues | $ | \Sigma - \lambda I | = 0$ | Variance explained by a principal component direction. | Affirmation of latent dimension significance in the data space. |
| **Dimensionality & Factor** | Principal Component Loadings | $l_{ij} = \sqrt{\lambda_j} e_{ij}$ | Correlation between variable and component. | Affirmation of variable contribution to latent space compression. | Eigenvectors; Factor Loadings; Unstandardized Factor Loadings | Dimensionality, Structure, Weighting |
| **Dimensionality & Factor** | Principal Component Scores | $S = XW$ | Projected data coordinates in component space. | Affirmation of the compressed representation state of observations. | None | Dimensionality, Transformation, Compression |
| **Dimensionality & Factor** | Communalities | $h_i^2 = \sum_{j=1}^m l_{ij}^2$ | Variance in variable explained by factors. | Affirmation of variable capture by the latent affirmation space. | Uniqueness (Factor Analysis) | Factor Analysis, Variance, Extraction |
| **Dimensionality & Factor** | Average Variance Extracted (AVE) | $AVE = \sum \lambda_i^2 / (\sum \lambda_i^2 + \sum \theta_i)$ | Convergent validity metric. | Affirmation of latent construct explanatory power. | None | Psychometrics, Validity, Latent |
| **Dimensionality & Factor** | Explained Variance Ratio | $\text{EVR} = \lambda_j / \sum \lambda_k$ | Proportion of total variance a component explains. | Affirmation of compression efficiency of the latent space. | None | Dimensionality, Information, Reduction |
| **Multivariate & Structural** | Canonical Correlation Coefficients | $\rho = \sqrt{\text{eig}(\Sigma_{XX}^{-1}\Sigma_{XY}\Sigma_{YY}^{-1}\Sigma_{YX})}$ | Max correlation between linear combos of two variable sets. | Affirmation of cross-space relationship magnitude. | None | Multivariate, Association, Latent |
| **Multivariate & Structural** | Discriminant Function Coefficients | $\max_w (w^T S_B w) / (w^T S_W w)$ | Weights maximizing group separation. | Affirmation of class-distinguishing features in the generator. | None | Multivariate, Classification, Separation |
| **Multivariate & Structural** | Structural Equation Path Coefficients | $\beta$ in $y = \alpha + \beta x + \zeta$ | Direct effect between latent/observed variables. | Affirmation of causal/theoretical mechanism strength. | Standardized Path Coefficients | Multivariate, Causal, Structural |
| **Bayesian Statistics** | Posterior Probability | $P(\theta|X) \propto P(X|\theta)P(\theta)$ | Updated belief about a parameter after observing data. | Affirmation of data-informed parameter state. | Posterior Mean; Posterior Variance; Log Posterior Density | Bayesian, Inferential, Updating |
| **Bayesian Statistics** | Marginal Likelihood Estimate | $P(X) = \int P(X|\theta)P(\theta)d\theta$ | Probability of data under the model. | Affirmation of overall model evidence. | None | Bayesian, Model Selection, Evidence |
| **Bayesian Statistics** | Hierarchical Shrinkage Coefficient | $\tau$ in $\beta_j \sim N(0, \tau^2)$ | Group-level variance controlling parameter pooling. | Affirmation of cross-group regularization strength. | Random Effects Variance | Bayesian, Hierarchical, Regularization |
| **Time Series & Forecasting** | Autocorrelation Function (ACF) | $\rho(k) = \gamma(k) / \gamma(0)$ | Correlation of series with its lagged self. | Affirmation of temporal dependency structure in the generator. | Partial Autocorrelation Function (PACF); Autocovariance Function; Partial Autocovariance Function; Residual Autocorrelation Coefficient | Time Series, Dependence, Lag |
| **Time Series & Forecasting** | Cross-Correlation Function | $\rho_{XY}(k) = \gamma_{XY}(k) / (\sigma_X \sigma_Y)$ | Correlation between two series at various lags. | Affirmation of inter-series lead/lag relationships. | Cross-Covariance Function | Time Series, Bivariate, Lag |
| **Time Series & Forecasting** | Volatility Forecast Statistic | $\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$ | Predicted time-varying variance. | Affirmation of localized uncertainty magnitude in the generator. | ARCH Coefficient; GARCH Coefficient; EGARCH Coefficient; IGARCH Coefficient | Time Series, Volatility, Forecasting |
| **Time Series & Forecasting** | Cointegration Residual Variance | $\text{var}(u_t)$ where $Y_t - \beta X_t = u_t$ | Variance of stationary residual from a non-stationary relationship. | Affirmation of long-run equilibrium stability. | None | Time Series, Equilibrium, Stationarity |
| **Time Series & Forecasting** | Vector Autoregression Coefficients | $Y_t = c + \sum A_i Y_{t-i} + u_t$ | Interdependent lagged effects across multiple time series. | Affirmation of system-wide temporal dynamic mechanisms. | None | Time Series, Multivariate, System Dynamics |
| **Time Series & Forecasting** | Impulse Response Function | $\partial Y_{t+h} / \partial \epsilon_t$ | Reaction of system variables to a shock over time. | Affirmation of temporal shock propagation pathways. | None | Time Series, Causality, Shock |
| **Time Series & Forecasting** | Variance Decomposition | Proportion of MSE from specific shocks | Contribution of structural shocks to forecast error. | Affirmation of exogenous source importance over time. | None | Time Series, Forecasting, Attribution |
| **Spectral & Signal** | Power Spectral Density (PSD) | $S(f) = \lim_{T \to \infty} \frac{1}{T}|\hat{X}(f)|^2$ | Power distribution across frequencies. | Affirmation of frequency-domain energy distribution of the generator. | Spectral Density Estimate; Periodogram; Welch’s Method Estimate; Multi-Taper Spectral Estimate | Spectral, Frequency, Energy |
| **Spectral & Signal** | Coherence Function | $C_{xy}(f) = |S_{xy}(f)|^2 / (S_{xx}(f)S_{yy}(f))$ | Frequency-domain correlation between two signals. | Affirmation of frequency-specific linear relationship strength. | Coherency; Canonical Spectral Correlation | Spectral, Bivariate, Frequency |
| **Spectral & Signal** | Wavelet Energy Spectrum | $\int |W(a, b)|^2 db$ | Energy localized in time and frequency. | Affirmation of non-stationary time-frequency power. | Hilbert-Huang Transform Statistic; Empirical Mode Decomposition Residuals; Principal Oscillation Pattern Coefficients | Spectral, Time-Frequency, Non-Stationary |
| **Spectral & Signal** | Signal-to-Noise Ratio (SNR) | $SNR = P_{signal} / P_{noise}$ | Relative power of signal versus background noise. | Affirmation of information dominance over generative noise. | Signal-to-Interference Ratio (SIR); Peak-to-Average Power Ratio (PAPR) | Signal Processing, Quality, Ratio |
| **Spectral & Signal** | Phase Locking Value | $PLV = \frac{1}{N}|\sum e^{i(\phi_x - \phi_y)}|$ | Consistency of phase difference between signals. | Affirmation of frequency-specific coupling/synchronization. | None | Spectral, Phase, Synchronization |
| **Spectral & Signal** | Mel-Frequency Cepstral Coefficients (MFCCs) | DCT of log mel-spectrum | Representation of spectral envelope timbre. | Affirmation of perceptually relevant spectral shape. | Cepstrum Coefficients | Signal Processing, Feature Extraction, Acoustic |
| **Spectral & Signal** | Spectral Entropy | $H = -\sum p(f) \log p(f)$ | Flatness/uniformity of the power spectrum. | Affirmation of spectral complexity or unpredictability. | Energy Entropy | Spectral, Complexity, Information |
| **Spectral & Signal** | Spectral Shape Descriptors | Moments/Cumulants of $S(f)$ | Statistical summarization of the spectral shape. | Affirmation of spectral mass, brightness, and distribution. | Spectral Centroid; Spectral Bandwidth; Spectral Rolloff; Spectral Skewness; Spectral Kurtosis; Instantaneous Frequency | Spectral, Descriptive, Shape |
| **Spectral & Signal** | Intrinsic Mode Function (IMF) Variance | $\text{var}(c_i(t))$ | Variance of a specific oscillatory mode in HHT. | Affirmation of energy encapsulated in specific adaptive scales. | Signal Complexity Index | Signal Processing, Adaptive, Decomposition |
| **Information Theory** | Entropy (Shannon) | $H(X) = -\sum p(x) \log p(x)$ | Expected information content/uncertainty. | Affirmation of average generative unpredictability. | Renyi Entropy; Tsallis Entropy; Cross-Entropy; Conditional Entropy; Interaction Information; Total Correlation; Multivariate Mutual Information; Multi-Information; Entropy Rate; Pointwise Mutual Information (PMI); Normalized PMI | Information, Uncertainty, Fundamental |
| **Information Theory** | Kullback-Leibler Divergence | $D_{KL}(P|Q) = \sum p(x) \log(p(x)/q(x))$ | Relative entropy between two distributions. | Affirmation of information loss when approximating a generator. | Relative Fisher Information | Information, Divergence, Asymmetric |
| **Information Theory** | Mutual Information | $I(X;Y) = H(X) - H(X|Y)$ | Shared information between two variables. | Affirmation of nonlinear statistical dependency. | None | Information, Dependency, Symmetric |
| **Information Theory** | Transfer Entropy | $T_{X \to Y} = H(Y_{t+1}|Y_t) - H(Y_{t+1}|Y_t, X_t)$ | Directed information transfer between time series. | Affirmation of predictive causal influence in the generator. | Local Transfer Entropy; Active Information Storage | Information, Causality, Directional |
| **Information Theory** | Approximate Entropy | $ApEn = \lim_{N \to \infty} [\Phi^m - \Phi^{m+1}]$ | Measure of sequential data regularity/predictability. | Affirmation of the presence of structured patterns in generation. | Sample Entropy; Permutation Entropy; Lempel-Ziv Complexity; Lempel-Ziv Entropy; Kolmogorov Complexity Estimate | Complexity, Regularity, Sequential |
| **Spatial Statistics** | Moran’s I | $I = \frac{N}{\sum w_{ij}} \frac{\sum \sum w_{ij}(x_i - \bar{x})(x_j - \bar{x})}{\sum (x_i - \bar{x})^2}$ | Global spatial autocorrelation. | Affirmation of spatial clustering or dispersion in the generator. | Geary’s C; Local Indicators of Spatial Association (LISA); Local G Statistic; Global G Statistic; Moran Scatterplot Slope | Spatial, Autocorrelation, Global |
| **Spatial Statistics** | Getis-Ord Gi* | $G_i^* = \frac{\sum_j w_{ij}x_j - \bar{x}\sum_j w_{ij}}{s\sqrt{[n\sum_j w_{ij}^2 - (\sum_j w_{ij})^2]/(n-1)}}$ | Local spatial hot/cold spot statistic. | Affirmation of localized spatial extreme clustering. | None | Spatial, Cluster, Local |
| **Spatial Statistics** | Ripley’s K-function | $K(r) = \lambda^{-1} E[\text{points within } r]$ | Spatial dependence of point patterns across scales. | Affirmation of spatial aggregations relative to a Poisson generator. | L-function (Besag); Pair Correlation Function (g(r)) | Spatial, Point Pattern, Scale |
| **Spatial Statistics** | Variogram | $2\gamma(h) = E[(Z(x) - Z(x+h))^2]$ | Spatial variance as a function of distance. | Affirmation of spatial continuity or decay of dependence. | Semivariogram; Covariogram; Cross-Variogram; Spatial Covariogram; Range of Spatial Autocorrelation | Spatial, Continuity, Interpolation |
| **Spatial Statistics** | Spatial Lag Coefficient | $\rho$ in $y = \rho W y + X\beta + \epsilon$ | Effect of neighboring spatial values on a target. | Affirmation of magnitude of spatial spillover in the generator. | Spatial Error Coefficient | Spatial, Regression, Dependence |
| **Spatial Statistics** | Geographically Weighted R² | Local $R^2$ estimated at spatial coordinates. | Spatially varying model fit. | Affirmation of spatial non-stationarity in explanatory power. | Geographically Weighted Residuals | Spatial, Regression, Non-Stationary |
| **Event/Timing & Fractal** | Fano Factor | $F = \text{Var}(N) / E[N]$ | Variance-to-mean ratio of event counts. | Affirmation of event over/under-dispersion in a counting generator. | Burstiness Index; Inter-Event Time Coefficient of Variation; Coefficient of Variation of Inter-Event Times | Event, Dispersion, Counting |
| **Event/Timing & Fractal** | Allan Variance | $\sigma_y^2(\tau) = \frac{1}{2} \langle(y_{k+1} - y_k)^2\rangle$ | Frequency stability over averaging times. | Affirmation of underlying noise type and long-term generative drift. | None | Timing, Stability, Noise |
| **Event/Timing & Fractal** | Hurst Exponent | $H$ derived from $R/S = c \cdot n^H$ | Long-term memory of a time series. | Affirmation of trend-reinforcing (persistent) or mean-reverting behavior. | Detrended Fluctuation Analysis Statistic; Fractal Dimension Estimate | Fractal, Memory, Scaling |
| **Event/Timing & Fractal** | Lyapunov Exponent Estimate | $\lambda = \lim_{t \to \infty} \lim_{\delta_0 \to 0} \frac{1}{t} \ln|\delta(t)/\delta_0|$ | Rate of separation of infinitesimally close trajectories. | Affirmation of the presence of chaotic generative dynamics. | None | Chaos, Sensitivity, Nonlinear |

## References

- [Function](../mathematical/function.md)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- https://en.wikipedia.org/wiki/Decile
- https://en.wikipedia.org/wiki/Metric
- https://en.wikipedia.org/wiki/Rating
- https://en.wikipedia.org/wiki/Ranking
- https://en.wikipedia.org/wiki/Mean
- [Metric Space](../mathematical/metric-space.md)
- https://en.wikipedia.org/wiki/Cosine_similarity
- https://en.wikipedia.org/wiki/Similarity_measure
