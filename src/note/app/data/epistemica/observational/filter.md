---
tags: [filter, state-estimation]
---

# Filter

 : State Estimation (State%20Estimation%2018ec0f5171ec80b997b6c78fc4b3be89.md), Wiener Filter (Wiener%20Filter%209ccf83502d7d42f581e2c3330671fbdf.md), Particle Filter (Particle%20Filter%20717c4959d29f4f3097d7c45f9577b934.md), Kalman Filter (Kalman%20Filter%2016d5cde028354320ba60d35aaa2a4a38.md), Savitzky–Golay (S–G) Filter (Savitzky%E2%80%93Golay%20(S%E2%80%93G)%20Filter%2027ac0f5171ec80109902e5f65ce28868.md)

> 

## Formulation

> What is the epistemic function of  a filter? Which other elements - can serve that function?
> 

> What is the limit of filters?
> 

### What is a filter?

> A **filter** is an operator $F : \mathcal{X} \rightarrow \mathcal{Y},$ that transforms an input signal into an output signal by **selectively** preserving, suppressing, or transforming certain properties of the input.
> 

The "selection" may occur in many domains:

- frequency
- time
- scale
- probability
- geometry
- information
- latent state

A filter is therefore **a selective transformation operator**.

### What is the most abstract way to conceptualize a filter?

A filter can be viewed as a member of a larger class of epistemic operators: $\mathcal{E} : \mathcal{R} \rightarrow \mathcal{R}',$

where:

- $\mathcal{R}$ is a representation of observations,
- $\mathcal{R}'$ is a representation with greater utility for a specified inference, prediction, or decision task.

From this perspective:

- a moving average is an epistemic operator,
- a Kalman filter is an epistemic operator,
- a Fourier transform is an epistemic operator (changing representation rather than discarding information),
- principal component analysis is an epistemic operator,
- Bayesian updating is an epistemic operator.

A **filter** is the subclass of epistemic operators whose defining role is **selective transformation**: retaining information deemed relevant while attenuating information deemed irrelevant according to an explicit criterion or model. This places filters within a broader theory of information-processing operations rather than treating them as isolated signal-processing tools.

### What is the epistemic function of a filter?

> The epistemic purpose of a filter is **not merely smoothing**.
> 

Its purpose is:

> **to increase the epistemic utility of an observation by reducing components considered less informative while preserving components considered more informative for a given task.**
> 

> The filter changes the representation, not necessarily the underlying reality.
> 

A filter may perform one or more of:

| Operation | Purpose |
| --- | --- |
| Denoising | Remove random fluctuations |
| Smoothing | Reveal long-term structure |
| Enhancement | Increase visibility of desired features |
| Separation | Isolate components |
| Compression | Remove redundancy |
| Projection | Keep only relevant dimensions |
| Estimation | Infer latent quantities |
| Regularization | Reduce overfitting and instability |
| Normalization | Improve comparability |
| Feature extraction | Produce informative variables |

Notice that not all filters smooth.

A derivative operator, for example, **enhances high frequencies** rather than suppressing them.

### Which other elements can serve the same epistemic function?

> Filtering is only one member of a broader family of **epistemic transformation operators**.
> 

| **Method** | **Primary epistemic function** |
| --- | --- |
| Filter | Remove or suppress unwanted information |
| Estimator | Infer unknown quantities |
| Predictor | Infer future quantities |
| Classifier | Assign categories |
| Detector | Decide whether a phenomenon exists |
| Compressor | Remove redundancy |
| Encoder | Change representation |
| Feature extractor | Produce informative variables |
| Optimizer | Select the best hypothesis |
| Interpolator | Infer missing observations |
| Aggregator | Summarize many observations |
| Bayesian updater | Revise beliefs with evidence |
| Dimensionality reduction | Reveal intrinsic structure |

### Which are the limits of filters?

> A filter cannot create information that is absent.
> 

Therefore, filters can:

- suppress noise,
- reorganize information,
- expose hidden structure,
- improve signal-to-noise ratio,
- estimate latent variables (given a model),

but they cannot recover information that was never observed.

Every filter involves trade-offs.

| **Limitation** | **Consequence** |
| --- | --- |
| Information loss | Some signal may be removed with the noise |
| Model dependence | Results depend on assumptions (e.g., Gaussian noise, smooth trends) |
| Resolution trade-off | Better smoothing usually reduces temporal or spatial resolution |
| Bias | Filters may systematically distort estimates |
| Delay (causal filters) | Real-time filters often introduce lag |
| Endpoint effects | Non-causal filters (e.g., HP filter) are unreliable near the boundaries |
| Identifiability | Different latent signals can produce the same observations, making unique recovery impossible |
| Task dependence | There is no universally optimal filter; usefulness depends on the objective |

## Filter Space

> Which are the filters?
> 

| **Filter** | **Description** | **Typical Usage** |
| --- | --- | --- |
| Identity Filter | Returns the input unchanged | Baseline/reference |
| Moving Average (SMA) | Local averaging operator | Noise reduction, trend estimation |
| Exponential Moving Average (EMA) | Recursive weighted average | Online smoothing, finance |
| Gaussian Filter | Convolution with a Gaussian kernel | Image processing, signal denoising |
| Median Filter | Replaces each sample with the neighborhood median | Removing impulsive (salt-and-pepper) noise |
| Wiener Filter | Minimum mean-square-error linear estimator | Signal restoration under Gaussian noise |
| Kalman Filter | Recursive Bayesian state estimator for linear Gaussian systems | Tracking, navigation, economics |
| Extended Kalman Filter (EKF) | Linearization of nonlinear systems | Robotics, aerospace |
| Unscented Kalman Filter (UKF) | Nonlinear state estimation using sigma points | Autonomous systems |
| Particle Filter | Monte Carlo approximation of posterior distributions | Nonlinear, non-Gaussian state estimation |
| Hodrick–Prescott (HP) Filter | Penalized optimization producing a smooth trend | Macroeconomics, financial trend extraction |
| Baxter–King Filter | Finite band-pass filter | Business cycle extraction |
| Christiano–Fitzgerald Filter | Approximate ideal band-pass filter | Macroeconomic cycle analysis |
| Butterworth Filter | Maximally flat frequency response | Signal processing |
| Chebyshev Filter | Sharp frequency cutoff with ripple | Communications |
| Elliptic (Cauer) Filter | Very sharp frequency cutoff | Electronics |
| Bessel Filter | Maximally flat phase response | Audio, control systems |
| Low-Pass Filter | Removes high-frequency components | Smoothing |
| High-Pass Filter | Removes low-frequency components | Edge detection, detrending |
| Band-Pass Filter | Keeps only a frequency band | Spectral analysis |
| Band-Stop (Notch) Filter | Removes a frequency band | Noise removal (e.g., 50/60 Hz) |
| Matched Filter | Maximizes SNR for a known signal | Radar, communications |
| Savitzky–Golay Filter | Local polynomial regression | Spectroscopy, preserving peaks |
| Bilateral Filter | Edge-preserving nonlinear smoothing | Computer vision |
| Total Variation Filter | Optimization-based denoising | Image reconstruction |
| Wavelet Filter | Removes wavelet coefficients at selected scales | Denoising, multiscale analysis |
| Fourier Filter | Modifies Fourier coefficients | Frequency-domain filtering |
| Morphological Filter | Uses dilation/erosion operators | Image morphology |
| Adaptive Filter (LMS/RLS) | Parameters adapt over time | Echo cancellation, adaptive control |
| Recursive Least Squares (RLS) Filter | Adaptive least-squares estimator | Online system identification |

## QA

### Which are is the relation with Filtration, Filter and State Estimation?

> 

### Which are the others related ideas?

> 

### What is the relation with ‘Information Theory’?

> Information theory is not a theory of meaning or knowledge; it is a mathematical theory of data representation, uncertainty, communication, and compression.
> 

> A filter (a re-representation of data) cannot increase the amount of information in data; it can only transform the distribution of information, removing irrelevant variation and making relevant structure easier to detect.
> 

> How much information about the original source is preserved after the transformation?
> 

> By large science, and epistemic practices are fundamentally compression - that is human attention - remove the irrelevant - only signal  - not noise.
> 

## References

- [**Operator**](../mathematical/operator.md)
