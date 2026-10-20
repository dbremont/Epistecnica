---
tags: [text-format]
---

# Unicode

- [UTF-8](note.html?n=technica/computation/representation/conceptual-model-computational-representation/utf-8.md), [Font Format](note.html?n=technica/computation/representation/conceptual-model-computational-representation/font-format.md)

> Unicode is a **universal character encoding standard** that provides a unique numeric identifier (code point) for every character, symbol, and script used in written languages across the world. It is designed to encompass all modern and historical scripts, as well as technical symbols, punctuation, and other textual elements. Unicode supports a vast range of characters, currently defining over 1.1 million code points in its repertoire, organized into 17 planes, each comprising 65,536 code points.
> 

QA:

- **Can X11 render the Unicode charset?** X11  itself does not handle font rendering directly; this is the 
responsibility of the client applications. The ability to render Unicode  characters depends on the fonts, libraries, and toolkits used by the 
client.
- **Which clients are capable of displaying the Unicode charset in X11?** Modern X11 clients that use libraries like **Xft**, **FreeType**, **Pango**, or **HarfBuzz** can render Unicode characters. Examples include applications built with toolkits like **GTK**, **Qt**, or **wxWidgets**.  These clients rely on Unicode-aware font systems and proper  configuration (e.g., UTF-8 locales and appropriate fonts) to display  Unicode text correctly.
- How the length of a string is computed?

## Typograhy Taxonomy

| **Category** | **Subcategory** | **Concept** | **Description** |
| --- | --- | --- | --- |
| **Glyph System** | Character Representation | Glyph | Visual form of a character in a font. |
|  |  | Character | Abstract textual unit mapped to one or more glyphs. |
|  | Encoding & Rendering | Unicode Mapping | Digital character encoding standard. |
|  |  | Hinting | Algorithmic fine-tuning for pixel alignment in rasterized text. |
| **Type Design** | Typeface Structure | Typeface | A set of glyphs sharing a visual identity. |
|  |  | Font | A specific instantiation of a typeface with defined weight, style, and size. |
|  | Typographic Anatomy | X-Height | The height of lowercase letters, relative to the baseline. |
|  |  | Ascender | The part of a letter that extends above the x-height. |
|  |  | Descender | The part of a letter that extends below the baseline. |
|  |  | Cap Height | The height of uppercase letters. |
| **Typographic Variation** | Structural Variants | Serif | Typefaces with small strokes at character ends. |
|  |  | Sans-serif | Typefaces without serifs, often modern or minimalist. |
|  |  | Monospace | Fonts where all characters have equal width. |
|  |  | Proportional | Fonts where character widths vary for readability. |
|  | Style Variants | Italic | Cursive-like typeface variation. |
|  |  | Oblique | Mechanically slanted variant of a typeface. |
|  |  | Bold | A heavier-weight variation of a typeface. |
| **Typography & Space** | Spacing | Kerning | Adjusting space between specific character pairs. |
|  |  | Tracking | Uniform letter-spacing across text. |
|  |  | Leading | Line spacing, measured from baseline to baseline. |
|  | Layout Control | Justification | Text alignment to both left and right margins. |
|  |  | Baseline Grid | A consistent horizontal alignment guide for text. |
|  |  | Dynamic Flow | Responsive text adjustment based on viewport or container. |
| **Rendering & Display** | Digital Typography | Subpixel Rendering | Exploiting pixel substructure for enhanced clarity. |
|  |  | Anti-Aliasing | Smoothing the jagged edges of text on screens. |
|  | Print Typography | DPI & Print Resolution | The density of printed characters per inch. |
|  |  | Ink Trapping | Adjustments to compensate for ink spread in print. |
| **Readability & Legibility** | Legibility Factors | Contrast | Difference in stroke weight and background color. |
|  |  | Optical Adjustments | Typeface refinements for enhanced perception. |
|  | Readability Factors | Line Length | Optimal text width for reading efficiency. |
|  |  | Typographic Hierarchy | Differentiation of text elements via weight, size, or style. |

## List of Components

The Unicode Standard specifies the following key components:

1. **Code Points**: Each character is assigned a unique numerical value, typically represented in hexadecimal format (e.g., U+0041 for the Latin capital letter "A").
2. **Encoding Forms**: Unicode defines several encoding forms to represent code points in binary format, including:
    - **UTF-8**: A variable-width encoding that uses 1 to 4 bytes per code point, backward-compatible with ASCII.
    - **UTF-16**: A variable-width encoding that uses 1 or 2 16-bit code units per code point.
    - **UTF-32**: A fixed-width encoding that uses exactly 32 bits per code point.
3. **Character Properties**: Unicode includes metadata for each character, such as its category (e.g., letter, number, punctuation), case, directionality, and other attributes.
4. **Normalization**: Unicode provides algorithms for normalizing text to ensure consistent representation of equivalent character sequences, which is critical for text comparison, searching, and storage.
5. **Collation**: Unicode defines rules for sorting and comparing strings in a language-sensitive manner.
6. **Bidirectional Text**: Unicode supports scripts written in both left-to-right (e.g., Latin) and right-to-left (e.g., Arabic) directions, enabling proper rendering of mixed-direction text.

## References

- https://home.unicode.org/
- https://en.wikipedia.org/wiki/Unicode
- https://www.unicode.org/main.html
- - [Representation Problem: Text (String)]
- [**Computational Typography**](note.html?n=technica/computation/miscelanea/computational-typography.md)
- https://www.youtube.com/watch?v=MijmeoH9LT4
- [Internationalization and Localization](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/internationalization-and-localization.md)
- https://en.wikipedia.org/wiki/UTF-16