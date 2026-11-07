---
tags: [note, nature, ontology, process]
qa:
  - Is a change an event, a process, or a relation between two states?
  - Does change require an enduring bearer, or can it be read as a difference between configurations alone?
  - At which level of organization does a change exist — the state transition, the bearer, or a pattern over many transitions?
  - How much of a change is ontic and how much is the observer's cut (sampling, granularity, scale)?
---

# Change

> **Change** is a difference in the state of a bearer between two configurations: the aspect that takes different values, the prior and posterior states, the interval over which the difference obtains, and the region where the bearer's state differs.

> It is the transition itself — not its cause and not the noticing of it. Causality explains why a change occurs; observation registers that it did; both are decomposed elsewhere and cross-linked here.

> A single change is discrete and delimited, an `Event`; a run of changes extended in time is a `Process`, and a regularity predicated over such a run is a `Phenomenon`.

## Formulation

### What natural element type does this natural instance belong to?

> `Event` at the meso level of organization. The guide defines an `Event` as a discrete, delimited change marking a transition between states, so a change is an event whose content is the state difference and whose extent is the transition interval. Read as extended change the same segment is a `Process` (`Process` `(→ Generation)` `Event`); read as a regularity across repeated transitions it is a `Phenomenon`.

### What is this natural instance?

> A **change**: the difference between two configurations of one bearer, taken as one delimited occurrence. The segment includes the bearer that changes, the aspect whose value differs (position, temperature, composition, phase), the prior and posterior states, the magnitude of the difference, the interval over which it obtains, the locus at which it obtains, and the constraints that bound it.

> Excluded: the causes of the transition (decomposed under causality and cross-linked), the act of observing or measuring it (an epistemic construction, not an ontic element), and any purpose the change serves (technical or social).

> The worked binding is a **cooling body**: a bounded system whose temperature field passes from one configuration to another over one night, at the body's own locus, under conservation and rate bounds. The same tree relocates to a migrating dune, a germinating seed, or a folding protein.

### Which limitation factors bound this description?

> The bound instance exhibits four of the checklist's factors; the rest apply only where a concrete instance shows them, and are recorded per instance rather than assumed.

- **Partial Observability** — only samples of the prior and posterior fields are available; the states are reconstructed from the record, not seen whole.
- **Non-Repeatability** — this transition happens once; a rerun is a different instance, not the same change.
- **Uncertainty** — the magnitude, the interval, and the locus are estimated with error, and a change too small to separate from noise is undecidable from the record.
- **Scale** — the same bearer changes at micro and macro scales; a same-named change at another level is a second node with its own path.

### What is the recursive instance decomposition of this natural instance?

> The bound bearer sits at the meso level; the transition is held over one interval. Grouping types are `` `code` ``, instances are Title Case, every link names its relation, and each row carries its level.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change | The element under study: one delimited transition of a bearer's state — in the worked binding, the cooling of one body over one night. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `Variable Aspect` | Grouping: the dimension whose value differs between the two states. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `Variable Aspect` `(→ Instance)` Changed Aspect | The concrete dimension carrying the difference — temperature here: what the change is a change *of*. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `State` | Grouping: the configurations on either side of the transition. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `State` `(→ Instance)` Prior State | The configuration before the difference obtains: the initial temperature field. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `State` `(→ Instance)` Posterior State | The configuration after it: the field once the body has cooled. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `Property` | Grouping: determinable features of the transition itself. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Attribute)` `Property` `(→ Instance)` Difference Magnitude | The size of the state difference — ΔT here — the quantity that ranks one change above another. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Situation)` `Time` | Grouping: the temporal situation of the transition. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Situation)` `Time` `(→ Instance)` Transition Interval | The interval, or instant, over which the difference obtains: the event's temporal extent. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Situation)` `Space` | Grouping: the spatial situation of the transition. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Situation)` `Space` `(→ Instance)` Locus of Change | The region where the bearer's state differs — the body's volume, not the room around it. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Substrate)` `Substrate` | Grouping: the bearer the change is borne on. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Substrate)` `Substrate` `(→ Instance)` Changed Bearer | The material particular or system whose state differs: the cooling body. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Constraint` | Grouping: bounds on what the transition may do. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Constraint` `(→ Instance)` Conservation Constraint | Invariants the transition cannot violate: the heat leaves the body, it is not destroyed. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Constraint` `(→ Instance)` Rate Bound | Limits on how fast the difference may accumulate: the cooling rate set by conduction, surface area, and surroundings. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Limitation Factor` | Grouping: description-bounding properties of the segment. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Limitation Factor` `(→ Instance)` Partial Observability | Only samples of the prior and posterior fields are recorded; the states are inferred, not observed whole. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Limitation Factor` `(→ Instance)` Non-Repeatability | The transition is one-off: reproducing it yields another instance with its own path, never the same change twice. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Limitation Factor` `(→ Instance)` Uncertainty | Magnitude, interval, and locus carry estimation error; changes below the noise floor cannot be separated from constancy. Meso. |
| `Ontic Element` `(→ Kind)` `Event` `(→ Instance)` Change `(→ Bound)` `Limitation Factor` `(→ Instance)` Scale | The bearer also changes at micro and macro levels; each is a separate node, decomposed separately and linked. Meso. |

> Limitation checklist (ontic properties of the segment, not method failures): the four factors above are bound as rows; Complexity (coupled conduction, radiation, evaporation), Nonlinearity (phase-change and failure thresholds), Chaos (sensitive dependence), Emergence, Irreducibility, Measurement Disturbance, Data Availability, Computational Complexity, and Many-Body coupling apply only where the concrete instance shows them — record them per instance, never assume them.

> Secondary readings (kept as prose, never merged into the tree above): readable as `Process` — the extended run of changes whose events are these transitions, decomposed with `Process` `(→ Generation)` `Event`; readable as `Phenomenon` — a regularity predicated over a trajectory of states, such as a cooling curve; readable as epistemic — detecting, measuring, or missing a change (difference thresholds, change blindness) belongs to the epistemicarum grammar; readable as technique — actuating a change or holding it back belongs to the technicarum grammar. The instrument technically, the transition naturally.

## References

- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) — the schema, the permitted links, and the limitation checklist this note follows.
- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) — how inquiry targets the described element.
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) — the concept-evaluation grammar.
- [Event](/note.html?p=notes/nature/theory/event.md) — the epistemic note on the event concept.
- [State](/note.html?p=notes/epistemica/epistemic/theory/state.md) — the state a transition leaves and enters.
- [Causality](/note.html?p=notes/epistemica/causality/causality.md) — why the transition occurs, decomposed separately.
- Aristotle. (c. 350 BCE). *Physics*, III.1–3. https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0084:book=3:chapter=1
- Arp, R., Smith, B., & Spear, A. D. (2015). *Building ontologies with Basic Formal Ontology*. MIT Press.
- Casati, R., & Varzi, A. (n.d.). Events. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy*. https://plato.stanford.edu/entries/events/
- Sider, T. (2001). *Four-dimensionalism: An ontology of persistence and time*. Oxford University Press.
- Whitehead, A. N. (1929). *Process and reality: An essay in cosmology*. Macmillan.
