---
tags: [system]
---

# Design Token

- [Beauty](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/beauty.md)

> A **design token** is a **named, platform-agnostic value** that represents a design decision such as a color, spacing, typography, or other visual style property. Design tokens are used to **ensure consistency** and **enable scalability** across different platforms and products by centralizing design choices in a **machine-readable format** (usually JSON, YAML, or SCSS variables).
> 

## Case Study

```json
{
  "color.primary": {
    "value": "#1E90FF"
  },
  "spacing.small": {
    "value": "8px"
  }
}
```

## Why Use Design Tokens?

- ✅ Consistency across web, mobile, and other platforms.
- 🔁 Reusability of design values in multiple components or themes.
- 🧪 Themability, enabling easy switching between light/dark modes.
- 🔧 Automation, integrating design into the build pipeline (e.g., using tools like Style Dictionary).

## References

- https://atlassian.design/tokens/design-tokens
- https://spectrum.adobe.com/page/design-tokens/