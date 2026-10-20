---
tags: [development]
---

# Beauty

- [Design System](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/design-system.md), [Design Token](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/design-token.md)

> Basically attention to the last detail.
> 

> UI Designer …
> 

A beautiful UI feels intuitive *and* emotionally satisfying. It's not just how it looks — it's how it *feels* to use. Key elements:

1. **Visual Hierarchy** – Clear prioritization of elements via size, contrast, spacing, and typography.
2. **Consistency** – Styles, layouts, icons, and spacing that reinforce coherence.
3. **Whitespace** – Proper use of negative space to let the interface breathe and avoid clutter.
4. **Alignment & Rhythm** – Grid-based layouts, consistent padding/margin, and visual rhythm.
5. **Typography** – Readable, elegant fonts with good line spacing and size balance.
6. **Color Use** – Harmonious palettes with good contrast and emotional tone.
7. **Microinteractions** – Subtle animations and feedback that make the UI feel alive.
8. **Affordances** – Clear indicators of what is clickable, draggable, etc.
9. **Responsiveness** – Smooth transitions, quick feedback, no jank.
10. **Emotional Tone** – A mood that fits the product: warm, professional, playful, calm, etc.

## Benchmarks

There are **some tools and frameworks** that try to *automatically benchmark UI quality*, but full automation is limited because UI beauty is partly subjective. Still, you can automate **certain measurable aspects** of UI quality — particularly usability, performance, accessibility, and consistency.

| Category | Tools / Metrics | What It Evaluates |
| --- | --- | --- |
| **Accessibility** | Lighthouse, axe-core, Pa11y, WAVE | Color contrast, alt text, focus order, ARIA roles, keyboard nav |
| **Performance** | Lighthouse, WebPageTest, Chrome DevTools, SpeedCurve | Load time, interactivity, rendering speed |
| **Usability (Partial)** | Session replay + heuristics (e.g., Hotjar, Smartlook, Clarity) | Rage clicks, dead clicks, scroll depth, interaction delays |
| **Consistency / Visual Regression** | Percy, Chromatic, Applitools Visual AI | Pixel-perfect diffs across builds (for design drift detection) |
| **Design System Compliance** | Stylelint, Figma plugins, Storybook rules | Use of tokens, spacing units, font sizes from design system |
| **Responsiveness** | BrowserStack, LambdaTest, Responsive Design Mode in DevTools | Layout stability across breakpoints/devices |

🔬 **Experimental or Research-Grade Approaches**

Some academic or ML-based approaches try to *score visual appeal*:

1. **Aesthetic Score Prediction Models**
    - Neural nets trained on user-rated UIs (e.g., [CUIs dataset](https://github.com/ubc-cs/CUIs))
    - Output a score from 0–10 based on visual layout features.
2. **Automated Heuristic Evaluations**
    - Research systems that map design to Nielsen’s heuristics.
    - Still limited in practical use outside specific lab setups.
3. **Design Linting:** Tools like **DesignLint for Figma** flag inconsistent spacing, color contrast, non-grid alignment.

📉 **What Can’t Be Fully Automated Yet**

- **Visual harmony / beauty** (balance, rhythm, mood)
- **Emotional tone** (e.g., "playful vs. professional")
- **Context appropriateness** (e.g., is the UI suitable for doctors or kids?)
- **Branding alignment** (Does it feel like *your* product?)

## References

- https://lawsofux.com/
- https://uxarchive.com/
- https://atlassian.design/
- https://www.awwwards.com/
- https://news.ycombinator.com/item?id=33047199
- http://bokardo.com/principles-of-user-interface-design/