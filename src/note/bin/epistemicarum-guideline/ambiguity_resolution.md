# Ambiguity Resolution: Readings and Multi-Root Notes

> Some instances answer to more than one grammar: a technique may be technical in
> means but epistemic in goal; a retail operation may be technical in apparatus,
> epistemic in forecasting, and social in phenomenon. This note states how such
> cases are typed and decomposed without compromise typing — in dual readings,
> and in single multi-root notes that carry one tree per space.

## Formulation

### When is a technique epistemic in goal?

> A technique is epistemic in goal when its desired difference is a reduction of
> ignorance rather than a transformed state of the world: the intervention succeeds
> when it yields warranted belief about reality, and it is judged by validation
> standards (confirmation, predictive yield, reproducibility) rather than by
> transformation performance (throughput, tolerance, uptime).

### What is the canonical dual-reading case?

> **Well logging**: drilling a borehole and lowering wireline sondes and sensors to
> measure the geological formations around it. The means are thoroughly technical —
> drilling, actuation, transduction, encoding — but the end is formation evaluation:
> knowledge of what lies underground. The operation is validated the way epistemic
> artifacts are validated (do later observations and extractions confirm the reading?),
> not the way a production process is evaluated.

### How is such an instance decomposed?

> Twice — once per reading, following the multi-root forest rule ("How to decompose
> an instance that belongs to multiple element types?" in Philosophia Artium
> Technicarum et Operis): one tree binding `<<Technical Element>>` for the means
> (Technical Acts, Technical Interface & Actuation, Technical Configurations), one tree
> binding `<<Epistemic Element>>` for the end (Observation Interface, Concrete Epistemic
> Artifacts such as the log curves, Epistemic Standards judging them). The two roots
> are cross-linked; no row ever carries both types.

### What must not be done?

> Do not merge the readings into a compromise type ("epistemic technique" as a single
> category), and do not file the whole instance under technique merely because its
> means are technical. Type the means technically, the end epistemically; when the
> reading is contested, record the default root explicitly with secondary readings
> kept as `readable as …` prose.

### When is a note multi-root?

> A note is multi-root when its instance answers the dominant questions of two or
> more spaces (technique, nature, social, epistemic, moral — cf. the
> [topic placement strategy](topic_placement.md), step 1). The multi-root forest
> rule ("How to decompose an instance that belongs to multiple element types?" in
> each philosophia) already multiplies trees across *types within one space*; a
> multi-root note multiplies trees across *spaces for one instance*.

### What is a multi-root note?

> One note, N trees: one well-formed tree per confirmed reading, each typed by
> its own space's grammar. Declare a **primary reading** — the dominant question
> that anchors the instance — and record it explicitly in the note's first
> Formulation answer ("This instance's primary belonging is `X` (…space);
> readable as …"). The primary reading sets the note's home: the note lives in
> the primary space's section and is titled after the instance, never after the
> space.
>
> Secondary readings are full trees in the same note, never prose-only
> summaries; no row ever carries two types, and no reading is merged into a
> hybrid type. Contrast with the default-root fallback above: that fallback
> applies when the reading is contested and unanswered; a multi-root note is
> the positive case, built only from confirmed readings.
>
> For operative instances the trees close the loop `Reality → Knowing → Acting
> → Reality`: the epistemic tree's feedback (validation, residuals, censored
> observations) feeds the technical tree's next acts, and the social tree's
> phenomenon frames both.

### What is the multi-root note schema?

> Per-reading blocks plus a readings table naming each space, root type, and
> tree.

```bash
# (Instance — multi-root)

> (Intro: one instance; declared primary reading)

## Formulation

### Which readings does this instance carry?

| Space | Root type | Tree |
| --- | --- | --- |
| (primary space) | (root type) | (tree) |
| (secondary space) | (root type) | (tree) |

### What is the recursive instance decomposition of this instance under <primary space>?
### What is the recursive instance decomposition of this instance under <secondary space>?

(one decomposition section per confirmed reading, each typed by its own grammar)

## References

- ...
```

### What must not be done in a multi-root note?

> Do not merge readings into a hybrid type ("socio-technical demand entity");
> do not split the instance into one note per space (the note documents one
> instance — the single-home rule governs nodes and datasets, not readings);
> do not let a secondary space own the primary's nodes; do not reduce a
> confirmed secondary reading to `readable as …` prose.

### What is the canonical multi-root note?

> **Retail supply–demand matching**, primary technical. As a system it is
> primarily operative — it acts on stocks, orders, routes, and prices — so it
> reads as a `Technical Practice` (demand planning and replenishment) with its
> tasks, techniques, acts, and ensemble (`Technical Element Set`). It carries
> two further confirmed readings. Read socially, the phenomenon is a `Social
> Compound` (retailer, distribution center, store, supplier; procurement roles;
> service-level norms; prices and assets as coordinators; stockout,
> substitution, and bullwhip as dynamics) under the economic facet. Read
> epistemically, its forecasting subsystem is an `Observation Interface`
> (POS/EDI feeds, censored sales) feeding a `Concrete Epistemic Artifact`
> (demand estimate, substitution model), judged by `Epistemic Standards` and
> corrected through `Epistemic Feedback` (stockout censoring, forecast error).
> The material substrate (goods, cold chain) stays a cross-link to the natural
> decomposition, not a fourth tree.
>
> In the note these are three trees: the technical tree primary, the social
> and epistemic trees secondary, each typed by its own grammar and
> cross-linked; the feedback from the epistemic tree (validation, residuals)
> feeds the technical tree's next replenishment acts, closing
> `Reality → Knowing → Acting → Reality`.

## QA

### Is measurement then never a technical matter?

> Measurement is technical in execution and epistemic in purpose. Calibration
> procedures, sensor design, and sampling regimes belong to the technical tree;
> what the measurement warrants believing belongs to the epistemic tree. The
> boundary runs between executing the observation and warranting its product.

### Does a multi-root note violate the single-home rule?

> No. The single-home rule governs nodes and datasets: every node lives in
> exactly one owning dataset. A multi-root note documents one instance; its
> home is the primary space's section, and the secondary trees are
> decompositions of the same instance, not second homes. Nodes are still
> created only in their owning space.

### Why not one note per reading?

> Because the object of documentation is the instance, not the space.
> Separate notes would scatter one system's phenomenon, its knowledge, and
> its apparatus across three places and hide the feedback loop that makes it
> intelligible as a whole.

## References

- https://en.wikipedia.org/wiki/Well_logging
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
- [Philosophia Artium Epistemicarum et Operis](note.html?n=meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Philosophia Naturalis et Operis](note.html?n=meta/philosophia-naturalis-et-operis.md)
- [Topic placement strategy](topic_placement.md)
