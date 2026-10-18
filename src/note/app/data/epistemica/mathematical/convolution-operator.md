---
tags: [operator]
---

# Convolution Operator

 : Function Space (Function%20Space%201d6c0f5171ec80b5b311fe52e4fa23b8.md), Operator (Operator%2096b9329acc2b493388cda715c8e66caa.md)

> A **convolution is a mathematical operation** that combines two functions (or signals) to produce a third function, describing **how the shape of one is modified by the other**.
> 

> The **convolution operator** is a bilinear, shift-invariant integral transform defined for functions f, g $\in L^1(\mathbb{R}^n)$  by  $(f * g)(x) = \int_{\mathbb{R}^n} f(x - t)g(t)\, dt$, producing a third function that represents the weighted overlap of ff and a time- or space-reversed and shifted version of $g$, and serves as the foundational operation in linear time-invariant systems and convolutional neural networks.
> 

## Continuous Formulation

For two functions $f(t)$ and $g(t)$, their convolution is: $(f * g)(t) = \int_{-\infty}^{\infty} f(\tau)\, g(t - \tau)\, d\tau$

- $f(\tau)$: the "input" signal.
- $g(t-\tau)$: a flipped-and-shifted version of the other signal, often called the **kernel** or **impulse response**.
- The integral accumulates how much overlap there is between the two as one slides over the other.
- $\tau$ is an integration variable.

Observations:

- **The goal of the kernel is to define how you want to process or transform the signal** — it encodes the feature, pattern, or effect you want to extract.
- Convolution is **linear** and **shift-invariant**, making it a fundamental tool in signal processing, probability, and systems analysis.

## **Discrete Case Formulation**

> For sequences $f[n]$ and $g[n]$:  $(f * g)[n] = \sum_{k=-\infty}^{\infty} f[k] \, g[n - k]$
> 

> This is common in digital signal processing and computer science.
> 

## **Property**

- **Commutative:** $fg = gf$
- **Associative:** $(fg)h = f(gh)$
- **Distributive:** $f*(g+h) = fg + fh$
- **Identity:** $f * \delta = f$ (where $\delta$ is the Dirac delta or Kronecker delta).

## **Intuition**

- Think of convolution as "sliding" one function across another and computing the overlap at each position.
- In signals: it shows how an input signal is modified by a system’s response.
- In probability: convolution of two probability distributions gives the distribution of their sum.
- In image processing: convolution applies filters (like blurring, sharpening, edge detection).

## Use

| **Domain** | **Use** | **Case** |
| --- | --- | --- |
| **Mathematics (Geometry)** | Measure similarity or correlation between two functions or curves. | Comparing similarity of two curves by shifting one against the other. |
| **Signal Processing** | Modify or extract features from signals by combining with a kernel. | Image blur (kernel averages neighbors), edge detection (kernel emphasizes changes). |
| **Probability & Statistics** | Find the distribution of the sum of independent random variables. | Distribution of $X+Y$ = convolution of distributions of $X$ and $Y$. |
| **Physics / Engineering** | Compute system responses to inputs, especially linear time-invariant systems. | Clap in a concert hall → convolution gives the full echo/reverb pattern. |
| **Heat (Diffusion Equations)** | Model how quantities spread over time. | Heat distribution after some time is convolution with a Gaussian kernel. |
| **Optics** | Describe how light is spread by lenses or apertures. | Blurring effect of imperfect lenses modeled as convolution. |
| **Machine Learning (CNNs)** | Automatically detect patterns and features in data. | Detecting edges, corners, or textures in an image via learned kernels. |
| **Time-Series Analysis** | Smooth data or detect trends by combining nearby observations. | Moving average filter for financial trend detection. |

## References

- Functional Analysis
[https://nptel.ac.in/courses/111105037](https://nptel.ac.in/courses/111105037)
- [Functional analysis](https://en.wikipedia.org/wiki/Functional_analysis)
- [Operator Theory](https://en.wikipedia.org/wiki/Operator_theory)
- [List of Functional Analysis Topics](https://en.wikipedia.org/wiki/List_of_functional_analysis_topics)
- [Operator (mathematics)](https://en.wikipedia.org/wiki/Operator_(mathematics))
- [C*-algebra](https://en.wikipedia.org/wiki/C*-algebra)
- An interactive guide to Fourier series (2022) ([injuly.in](http://injuly.in/))
[https://news.ycombinator.com/item?id=39509414](https://news.ycombinator.com/item?id=39509414)
- [List of functional analysis topics](https://en.wikipedia.org/wiki/List_of_functional_analysis_topics)
- [Schwartz space](https://en.wikipedia.org/wiki/Schwartz_space)
- https://en.wikipedia.org/wiki/Convolution_power
- https://en.wikipedia.org/wiki/Convolution_theorem
- [https://www.youtube.com/watch?v=KuXjwB4LzSA](https://www.youtube.com/watch?v=KuXjwB4LzSA)
