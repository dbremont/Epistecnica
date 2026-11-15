---
tags: [note, guia]
---

# A Guide to Image Processing


> Image Processing..
> 

## Index

## How to create an image from a piece of text?

```python
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
img = Image.new('RGB', (500, 200), color='white')

# Initialize ImageDraw
d = ImageDraw.Draw(img)

# Define the text and font
text = "Hello, this is a text-to-image example!"
font = ImageFont.load_default()

# Position of the text
text_position = (10, 90)

# Text color
text_color = (0, 0, 0)  # Black

# Add text to image
d.text(text_position, text, font=font, fill=text_color)

# Save the image
img.save('text_image.png')
```

## How to convert a `.webp` Image to PNG Icons of different sizes?

> Tool: `sudo apt-get install imagemagick`
> 

```bash
convert input.webp -resize 16x16 icon16.png
convert input.webp -resize 48x48 icon48.png
convert input.webp -resize 128x128 icon128.png
```

## How to remove the background of an Image?

> https://www.pixelcut.ai/ai-image-editor?tool=removeBackground
> 

## How to optimize an image?

> Image optimization aims to reduce **file size**, **loading time**, and **bandwidth usage** while maintaining **visual quality** and **semantic integrity**.
> 

### Factor

| Factor | Description | Guidance |
| --- | --- | --- |
| **Format** | Choice of image encoding standard | Prefer **WebP** or **AVIF** over JPEG/PNG for web use |
| **Resolution** | Pixel dimensions relative to display size | Resize to match target device (e.g. 1200×800 for web, not 4000×3000) |
| **Compression** | Algorithmic reduction of image data | Use lossy compression (JPEG/WebP) or lossless (PNG, AVIF lossless) |
| **Color Depth** | Bits per channel / palette complexity | Reduce 24-bit → 8-bit where appropriate (e.g., logos) |
| **Metadata** | Embedded EXIF, thumbnails, ICC profiles | Strip unnecessary data to save space |
| **Transparency** | Alpha channel handling | Use PNG/WebP/AVIF only when transparency is needed |
| **Usage Context** | Web, print, mobile, ML preprocessing | Adjust compression and format to task requirements |
| **Caching & Delivery** | CDN, lazy loading, responsive sources | Optimize network-level delivery too |

### Technique

| Technique | Description | Case |
| --- | --- | --- |
| **Resize** | Reduce dimensions proportionally | `convert input.jpg -resize 1600x1200 output.jpg` |
| **Compress** | Adjust quality level | `jpegoptim --max=80 file.jpg` |
| **Strip Metadata** | Remove EXIF and other data | `convert input.jpg -strip output.jpg` |
| **Convert Format** | Re-encode to modern format | `cwebp -q 80 input.jpg -o output.webp` |
| **Quantize Colors** | Reduce color palette for flat graphics | `pngquant 256 image.png` |
| **Batch Processing** | Automate optimization for multiple images | Bash/Python scripts using ImageMagick or `rembg` |
| **Progressive Loading** | Enable incremental rendering for web | `convert input.jpg -interlace Plane output.jpg` |
| **Lazy Loading (Web)** | Load images only when visible | `<img loading="lazy">` in HTML |

### **Format Guidelines**

| Format | Type | Strength | Best For |
| --- | --- | --- | --- |
| **JPEG** | Lossy | Compact, high compatibility | Photos |
| **PNG** | Lossless | Transparency support | Graphics, UI elements |
| **WebP** | Lossy/Lossless | Small, modern, fast | Web |
| **AVIF** | Lossy/Lossless | Best compression ratio | Modern browsers |
| **SVG** | Vector | Infinite scalability | Logos, icons, diagrams |

## webp

> **WebP** is a modern image format developed by Google that provides superior lossless and lossy compression for images on the web.
> 

### Install

```bash
sudo apt update
sudo apt install webp
```

This installs:

```
cwebp → convert images to WebP
dwebp → decode WebP to PNG/JPEG
webpinfo → inspect metadata
```

## References

- [Image Procesing](https://app.notion.com/p/Image-Procesing-196c0f5171ec80899ce8e56b3e91edf7?pvs=21)
- [Representation Problem: Image (Data)](https://app.notion.com/p/Representation-Problem-Image-Data-6fbd34e8c0e94ea7bac58b83cda8725a?pvs=21)
