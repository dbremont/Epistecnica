---
tags: [analytical, discrete]
qa:
  - "Why does one extra bit buy about 6 dB of signal-to-quantization-noise ratio?"
  - "Why does dithering help when it only adds noise?"
  - "Is quantizing a neural network's weights the same operation as quantizing a signal?"
---

# Quantization

> **Quantization** replaces a value drawn from a continuum — or from any set finer than the one that must carry it — by a representative drawn from a finite set of **levels**, chosen by a declared partition rule.

> It is the irreversible step in the analog-to-digital chain: sampling fixes *when*, quantization fixes *how coarsely*. What is gained is a finite alphabet that can be stored, compared, and transmitted exactly; what is lost is resolution, and the loss is not free — it appears as **quantization error**, whose size trades against the number of levels.

## Formulation

### What is this epistemic instance?

> The **quantization instance** is the organized practice of replacing a magnitude by one of finitely many representatives. Formally, a quantizer is a map
>
> $$Q : X \to C, \qquad X \subseteq \mathbb{R}^n, \qquad C = \{c_1, \dots, c_L\}, \qquad L < \infty,$$
>
> together with the **partition** it induces, $R_i = \{x \in X : Q(x) = c_i\}$, whose cells cover $X$ and meet only on their boundaries. The two components are independent design choices: a **partition rule** assigns each source value to a cell, and a **codebook** (the set $C$) names the representative of each cell. Scalar quantization takes $n = 1$ and $L = 2^b$ for a nominal $b$ bits per sample; vector quantization takes $n > 1$ and quantizes whole blocks against a codebook of vectors.
>
> The scalar case is where the arithmetic lives. A **uniform** quantizer of step $\Delta$ has $c_i = i\Delta$, granular error bounded by $|x - Q(x)| \leq \Delta/2$ under nearest-level assignment, and — under the high-resolution assumption that the error is uniform inside a cell — error variance $\sigma_e^2 = \Delta^2/12$. Outside the represented range the error is no longer granular but **overload**: the value clips to an end level.

> Quantization is not its neighbours, and the distinctions are load-bearing:

| Construct | What is made discrete | Result |
| --- | --- | --- |
| **Quantization** | the range of values (the codomain) | finitely many representatives for uncountably many values |
| **Sampling** | the domain (time, space) | values known at discrete instants, still continuous in magnitude |
| **Discretization** | either or both, as a modelling move | a discrete model of a continuum — the umbrella term |
| **Rounding** | one value, by a rule | the nearest admissible representative — a component of the quantizer, not the whole |
| **Encoding** | levels → symbols | a bit string or index — lossless once the levels are fixed |
| **Approximation** | the structure of a function or model | a simpler function, with error measured in function space |
| **Quantization in physics** | a classical theory | a quantum theory — a different construct, not this one |

> The composition matters: an analog-to-digital converter **samples** (band-limits, holds, then reads at instants), **quantizes** each reading, and **encodes** the resulting level as a code word. Only the middle step is lossy in amplitude.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Aggregate`** — the **quantization practice** as an epistemic whole: an orientation (a resolution gap and a purpose), a target (a magnitude range), an access path (the sampler), a representation (the quantized code), operations (encoding and decoding), an evaluation (distortion under a rate budget), and conditions (noise floor, dynamic range). The practice is the coherent collection of these elements, not any one of them.

> `readable as` an **`Epistemic Operation`** when attention falls on the quantizing act itself — assigning a value to its cell's representative. `readable as` an **`Epistemic Representation`** when attention falls on the quantized code — the finite alphabet and its code words as a representational system. The note decomposes the practice because the operation alone leaves its partition, its error, and its rate budget outside the tree.

> The magnitude quantized is read in the **Ontic Order**; the code that carries it is epistemic.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in four ways the decomposition keeps apart. First, **which aspect**: "quantization" names the act (mapping a value), the code (the finite alphabet), and the apparatus (the quantizer: partition plus codebook). The note types the practice and keeps the act and the code as `readable as` prose. Second, **which sense**: the signal-processing and information-theoretic sense — replacing amplitudes by levels — is not the physicist's quantization of a classical theory into a quantum one (canonical, geometric, deformation). The shared word is a false friend; the physics construct is a theory-construction, not a value substitution, and it is not decomposed here (see [Geometric Quantization](note.html?n=epistemica/science/geometric-quantization.md)). Third, **where the boundary with sampling lies**: the step is quantized in the codomain and sampled in the domain, and a chain that does both is not thereby a single construct. Fourth, **what the input is**: quantizing a signal, a model's parameters, and a table of measurements are the same operation applied to different relata — the practice is portable, the apparatus differs.

> The ambiguity is resolved by declaring `Aggregate` primary and typing the branches as the practice's elements: the code under `Epistemic Representation`, the acts under `Epistemic Operation`, the distortion and its budget under `Epistemic Evaluation`. Calling quantization a representation would erase its lossy act; calling it an operation would erase the codebook it produces.

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — the quantization practice — into its orientation, target, access, representation, operations, evaluation, and conditions. Adjacent constructs (sampling, encoding, the physics quantization) are named but not decomposed.
>
> **Stopping rule.** A row is terminal when it names a concrete purpose, question, observable, element, property, convention, rule, act, method, standard, constraint, or error; the theory of rate–distortion is not decomposed here (see [Signal](note.html?n=epistemica/mathematical/signal.md)).
>
> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique.
>
> **Typing.** The root type is `Aggregate`, declared once; every branch is typed by its nearest enclosing grouping segment.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Quantization | The organized practice of replacing a continuum of values by a finite set of representatives. |
| `Aggregate` → Quantization → `Epistemic Orientation` | Grouping: orientation of the practice. |
| `Aggregate` → Quantization → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of quantizing. |
| `Aggregate` → Quantization → `Epistemic Orientation` → `Epistemic Purpose` → Bounded-Representation Purpose | Telos: carry a magnitude in a finite alphabet — trade resolution for a representation that can be stored, compared, and transmitted exactly. |
| `Aggregate` → Quantization → `Epistemic Orientation` → `Epistemic Question` | Grouping: questions directing the choice of representative. |
| `Aggregate` → Quantization → `Epistemic Orientation` → `Epistemic Question` → Representative-Choice Question | Which level $c_i$ should stand for the value $x$, and how much error does that choice commit? |
| `Aggregate` → Quantization → `Epistemic Orientation` → `Epistemic Gap` | Grouping: gaps motivating quantizing. |
| `Aggregate` → Quantization → `Epistemic Orientation` → `Epistemic Gap` → Resolution Gap | Deficiency of the carrier: a finite register cannot hold a continuum, and an exact magnitude cannot be reproduced from it. |
| `Aggregate` → Quantization → `Epistemic Target` | Grouping: targets of the practice. |
| `Aggregate` → Quantization → `Epistemic Target` → `Observable` | Grouping: registrable features of the target. |
| `Aggregate` → Quantization → `Epistemic Target` → `Observable` → Magnitude Range | The continuous magnitude to be represented, together with the dynamic range it occupies. |
| `Aggregate` → Quantization → `Epistemic Access` | Grouping: the path by which the magnitude enters the practice. |
| `Aggregate` → Quantization → `Epistemic Access` → `Observation Interface` | Grouping: coupling of the source to the quantizer. |
| `Aggregate` → Quantization → `Epistemic Access` → `Observation Interface` → Sampler | The instrument registering the magnitude at discrete instants — upstream of quantization, and never part of it. |
| `Aggregate` → Quantization → `Epistemic Representation` | Grouping: the discrete code the practice produces. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` | Grouping: the sign system carrying the levels. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code | The finite alphabet of levels and the map assigning each level a code word. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Representation Element` | Grouping: combinable constituents of the code. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Representation Element` → Quantization Level | One of the $L$ representatives $c_i$; the only values the code can express. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Representation Element` → Quantization Cell | The set $R_i$ of source values assigned to one level — a Voronoi cell under nearest-neighbor assignment. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Representation Element` → Step Size | The spacing $\Delta$ between adjacent uniform levels; the parameter a non-uniform quantizer varies. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Representation Element` → Code Word | The symbol or bit pattern indexing a level — the output of encoding, not of quantization. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` | Grouping: rules and properties constituting the code. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Property` | Grouping: properties carried by the code. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Property` → Quantization Error | The residual $e = x - Q(x)$: the difference between the source value and its representative. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Property` → Distortion | The expected error magnitude under a declared measure — mean squared error for the squared-error reading. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Property` → Resolution | The smallest distinguishable increment, fixed by the number of levels spread over the range. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Property` → Signal-to-Quantization-Noise Ratio | Error power against signal power; grows by about 6.02 dB per added bit. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Convention` | Grouping: stabilized choices about the code. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Convention` → Rounding Rule | Nearest, floor, ceiling, or truncation — the policy that resolves values inside a cell. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Convention` → Mid-Rise Versus Mid-Tread | Whether a level sits at zero: the two uniform layouts, differing in error at the origin and in the presence of a zero code. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Convention` → Nominal Bit Depth | The declared $b$ bits per sample, hence $2^b$ levels; a budget, not a property of the source. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Formation` | Grouping: rules of well-formed assignment. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Formation` → Partition Rule | How source values are assigned to cells — nearest level, or a declared threshold layout. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Formation` → Level Assignment Rule | How a cell's representative is fixed — midpoint for uniform steps, centroid for the Lloyd–Max optimum. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Interpretation` | Grouping: meaning assignments carried by the code. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Interpretation` → Reconstruction Reading | Reading a level back as the cell's representative value on output — the decoder's interpretation. |
| `Aggregate` → Quantization → `Epistemic Representation` → `Representational System` → Quantized Code → `Constitutive Substrate` → `Interpretation` → Codebook Reading | Reading a level as an index into a table of vectors rather than as a magnitude — the vector-quantization reading. |
| `Aggregate` → Quantization → `Epistemic Operation` | Grouping: operations of the practice. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Action` | Grouping: direct transformations. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Action` → Quantizing Act | Assigning a source value to the representative of the cell that contains it. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Action` → `Procedure` | Grouping: ordered routines. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Action` → `Procedure` → Encode Stage | Mapping the sampled value to a level and the level to a code word. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Action` → `Procedure` → Decode Stage | Mapping the code word back to its level, and the level to the reconstructed value. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` | Grouping: coordinated routines. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized ways of quantizing. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Uniform Quantization | One step size across the range: simple, fast, and optimal only for a uniform source density. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Non-Uniform Quantization | Step size tuned to the source density — the Lloyd–Max quantizer alternating nearest-neighbor cells with centroid levels. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Companding | A compressive law applied before a uniform step and inverted after it — μ-law and A-law approximating logarithmic spacing for speech. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Vector Quantization | Levels replaced by codebook vectors in $\mathbb{R}^n$, cells by their Voronoi regions; better rate–distortion at the price of complexity exponential in dimension. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Product Quantization | The vector space split into subspaces, each quantized with its own codebook — a tractable approximation to vector quantization. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Dithering | Noise added before the step so the error decorrelates from the signal instead of tracking it. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Method` → Error Diffusion | The residual of each sample pushed forward to later samples instead of discarded — the imaging counterpart of noise shaping. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Principle` | Grouping: rules guiding the design. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Principle` → Nearest-Neighbor Principle | A source value belongs to the cell of the closest level. |
| `Aggregate` → Quantization → `Epistemic Operation` → `Organization` → `Principle` → Centroid Principle | A level should be the centroid of the values assigned to its cell. |
| `Aggregate` → Quantization → `Epistemic Evaluation` | Grouping: assessments of the practice. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards judging a quantizer. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Standard` → Distortion Standard | A quantizer stands only if its distortion stays within budget at the declared rate. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Criterion` → Granular Error Bound | The in-cell error bound — $\Delta/2$ for uniform nearest-level assignment. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Constraint` | Grouping: limits on the practice. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Constraint` → Rate Constraint | The bit budget per sample or per vector, setting how many levels the code may have. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Epistemic Constraint` → Dynamic Range Limit | The span the code must cover; values outside it become overload, a strictly worse failure than granular error. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Error` | Grouping: deviations of the representative from the source value. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Error` → Overload Error | The clipping of out-of-range values — unbounded error at the edges of the range. |
| `Aggregate` → Quantization → `Epistemic Evaluation` → `Error` → Granular Noise | The in-cell error of values inside the range — bounded, and signal-dependent unless dithered. |
| `Aggregate` → Quantization → `Epistemic Context` | Grouping: conditions of the practice. |
| `Aggregate` → Quantization → `Epistemic Context` → `Epistemic Condition` | Grouping: surrounding conditions. |
| `Aggregate` → Quantization → `Epistemic Context` → `Epistemic Condition` → Noise Floor Condition | Quantization is useful only while granular error stays under the ambient noise of the channel or sensor. |
| `Aggregate` → Quantization → `Epistemic Context` → `Epistemic Condition` → Source Density Condition | The distribution of the source decides whether uniform steps are efficient or wasteful. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The instance is well identified once sampling, discretization, rounding, encoding, approximation, and the physicist's quantization are separated: **pass**. Its definition is clear in the signal-processing and information-theoretic setting and equivocal outside it, where "quantization" names model compression, a theory-construction, or mere rounding: **partial**. Its determinacy is carried by the declared partition and codebook — without them the term names no particular map: **partial**. It is internally consistent: partition, codebook, error, and rate budget are stated as one construction whose trade-offs agree: **pass**. Its representational adequacy covers scalar uniform and non-uniform, companding, vector and product quantization, dithering, and the two error regimes: **pass**. Its purpose adequacy is high for bounded representation under a rate budget, and nil for exactness: **pass**.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note separates quantization from sampling (domain vs codomain), discretization (umbrella), rounding (one component), encoding (lossless after the levels), approximation (structure), and the physics quantization (a different construct). |
| **Definitional Clarity** | Partial | The map, partition, and codebook are formalized and the error bound is stated; ordinary usage applies the word to any lossy reduction and to the construction of quantum theories, which no single definition covers. |
| **Conceptual Determinacy** | Partial | Membership is decided by a quantizer's declared partition and codebook, not by the word; a scheme that merely reduces precision without a fixed level set — pruning, truncation — is a borderline case the definition excludes. |
| **Internal Consistency** | Pass | Partition, level assignment, error bound, and rate budget are mutually compatible; the overload and granular regimes are distinguished rather than conflated, and the resolution of the code is not confused with the resolution of the source. |
| **Representational Adequacy** | Pass | Uniform and non-uniform scalar schemes, companding, vector and product quantization, dithering, and error diffusion are covered, together with the properties (error, distortion, resolution, SQNR) and the two readings of a level. |
| **Purpose Adequacy** | Pass | Serves bounded representation, transmission, storage, and parameter compression; it is explicitly inadequate where exactness is required, and the note does not claim exactness. |

## QA

### Why does one extra bit buy about 6 dB of signal-to-quantization-noise ratio?

> Because each added bit **halves the step** and the error power falls with the square of the step. With $L = 2^b$ levels over a fixed range, $\Delta \propto 2^{-b}$, and for a uniform quantizer $\sigma_e^2 = \Delta^2/12 \propto 2^{-2b}$. Twice the levels, a quarter of the error power: $10 \log_{10} 4 \approx 6.02$ dB. A full-scale sinusoid against a uniformly spaced quantizer lands at $\mathrm{SQNR} \approx 6.02b + 1.76$ dB; the constant depends on the source distribution and the loading, the slope does not.

### Why does dithering help when it only adds noise?

> Because it replaces an error that is **correlated with the signal** by one that is not. Deterministic rounding makes the quantization error a function of the input — audible as distortion, visible as banding, and able to lock an otherwise stable feedback loop into a limit cycle. Dithering adds a small random component before the step; the resulting error is randomized and, when the dither is right, its first and second moments no longer depend on the signal. The total error power rises slightly, but it becomes noise instead of distortion — a favourable trade wherever the ear or the estimator is more tolerant of noise than of structure.

### Is quantizing a neural network's weights the same operation as quantizing a signal?

> The operation is the same — replace values by finitely many representatives under a declared partition and codebook — but the apparatus and the budget differ. A signal quantizer is designed against a source density over a fixed dynamic range, at a fixed rate per sample, and judged by distortion. A weight quantizer is designed against a weight distribution that is learned, with **scales** chosen per tensor or per channel, often at rate 8 or 4 bits, and judged by downstream task loss rather than by reconstruction error — which is why it accepts large per-weight distortion when the loss is flat in that direction. See [Quantization](note.html?n=technica/ais/inference/quantization.md) for the engineering treatment.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Discretization](note.html?n=epistemica/mathematical/discretization.md)
- [Rounding](note.html?n=epistemica/mathematical/rounding.md)
- [Signal](note.html?n=epistemica/mathematical/signal.md)
- [Scale](note.html?n=epistemica/mathematical/scale.md)
- [Measurement Theory](note.html?n=epistemica/measurement/measurement-theory.md)
- [Geometric Quantization](note.html?n=epistemica/science/geometric-quantization.md)
- [Quantum Framework](note.html?n=epistemica/science/quantum-framework.md)
- [Quantization (engineering treatment)](note.html?n=technica/ais/inference/quantization.md)
- [Quantization (signal processing)](https://en.wikipedia.org/wiki/Quantization_(signal_processing))
- [Vector quantization](https://en.wikipedia.org/wiki/Vector_quantization)
- [Dither](https://en.wikipedia.org/wiki/Dither)
- [Rate–distortion theory](https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory)
- [Lloyd's algorithm](https://en.wikipedia.org/wiki/Lloyd%27s_algorithm)
- Gray, R. M., & Neuhoff, D. L. (1998). Quantization. *IEEE Transactions on Information Theory*, 44(6), 2325–2383.
- Gersho, A., & Gray, R. M. (1992). *Vector Quantization and Signal Compression*. Kluwer.
- Jayant, N. S., & Noll, P. (1984). *Digital Coding of Waveforms: Principles and Applications to Speech and Video*. Prentice-Hall.
- Widrow, B., & Kollár, I. (2008). *Quantization Noise: Roundoff Error in Digital Computation, Signal Processing, Control, and Communications*. Cambridge University Press.
- Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.), ch. 10 — rate–distortion theory.
- Jégou, H., Douze, M., & Schmid, C. (2011). Product quantization for nearest neighbor search. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 33(1), 117–128.
- Jacob, B., et al. (2018). Quantization and training of neural networks for efficient integer-arithmetic-only inference. *CVPR 2018*.
