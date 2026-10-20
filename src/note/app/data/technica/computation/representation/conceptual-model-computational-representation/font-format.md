---
tags: [font-format, text-format]
---

# Font Format

- [Unicode](note.html?n=technica/computation/representation/conceptual-model-computational-representation/unicode.md)

> The **representation problem of fonts** in digital typography refers to the challenge of accurately encoding, storing, and rendering font data across diverse platforms, resolutions, and rendering systems while ensuring consistency, scalability, and fidelity to the original typeface design.
> 

> A **font format** is a standardized digital file structure (e.g., `.ttf`, `.otf`, `.woff`) that encodes glyph data, metadata, and rendering instructions to enable the storage, distribution, and display of a typeface across various platforms and devices.
> 

QA:

- ….

---

| **Font Format** | **Description** | **File Extension** | **Key Features** |
| --- | --- | --- | --- |
| **Bitmap Fonts** | Fonts represented as grids of pixels, typically used in low-resolution displays. | `.bdf`, `.pcf` | Fixed size, not scalable, lightweight. |
| **TrueType (TTF)** | Outline font format using quadratic Bézier curves, developed by Apple and Microsoft. | `.ttf` | Scalable, supports hinting for improved rendering at small sizes. |
| **OpenType (OTF)** | Extension of TrueType, supporting advanced typographic features and Unicode. | `.otf`, `.ttf` | Scalable, supports ligatures, alternate glyphs, and multiple scripts. |
| **PostScript (Type 1)** | Outline font format using cubic Bézier curves, commonly used in professional printing. | `.pfb`, `.pfm` | High-quality rendering, widely used in print media. |
| **Web Open Font Format (WOFF)** | Compressed font format optimized for web use, based on TrueType/OpenType. | `.woff`, `.woff2` | Efficient for web delivery, supports metadata and compression. |
| **SVG Fonts** | Fonts defined using Scalable Vector Graphics (SVG), often used for icons and symbols. | `.svg` | Scalable, supports color and gradients, used in web and graphic design. |
| **Embedded OpenType (EOT)** | Compact font format for web embedding, developed by Microsoft. | `.eot` | Compressed, designed for legacy web browsers (e.g., Internet Explorer). |
| **DFont** | A Mac-specific font format that stores font data in the Mac OS resource fork. | `.dfont` | Used in older Mac systems, less common today. |
| **CID-Keyed Fonts** | Used in PostScript for handling large character sets, particularly in Asian languages. | `.cid` | Optimized for CJK (Chinese, Japanese, Korean) fonts. |
| **Multiple Master Fonts** | A deprecated font format that allowed dynamic interpolation between font styles. | N/A | Supported variable font styles, precursor to modern variable fonts. |
| **Sfnt (Spline Font)** | A container format for fonts, used as the basis for TrueType and OpenType. | N/A | Generic format for storing font data in tables. |
| **PFR (Portable Font Resource)** | A compact font format designed for embedded systems and low-bandwidth environments. | `.pfr` | Used in devices like e-book readers and set-top boxes. |
| **FNT (Windows Bitmap Font)** | A legacy bitmap font format used in older versions of Windows. | `.fnt` | Fixed-size, pixel-based, used in early Windows systems. |
| **TeX Fonts** | Fonts used in the TeX typesetting system, often in Metafont format. | `.mf`, `.pk` | Designed for high-quality typesetting in academic and scientific publishing. |
| **Graphite Fonts** | A font format designed for complex script rendering, particularly for minority languages. | N/A | Supports advanced typographic features for non-Latin scripts. |
| **Color Fonts** | Fonts that include color information, such as emoji or decorative fonts. | `.sbix`, `.cbdt`, `.colr` | Supports multi-color glyphs, used in modern applications. |

## References

- - [Representation Problem: **Font**]
- [**Computational Typography**](note.html?n=technica/computation/miscelanea/computational-typography.md)