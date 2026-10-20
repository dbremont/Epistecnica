---
tags: [compression, problema, tool]
---

# Compression


> 

- **Technique Space** (How can information be compressed?)
- **Constitutive Technical Objects** (Which tools can be embedded in or connected to a larger system to enable compression?)
- **Evaluation** (How should a compression method be evaluated?)
- **Implementation Forms** (Which forms can a compression technique take in practice?)
    - **Trade-Offs** (What trade-offs are inherent in these forms?)
- Which are the **limits of compression**?

## Technical  Object Space

> Which are the tools used to compress things?
> 

| **Tool** | **Description** | **File Extensions** |
| --- | --- | --- |
| **gzip** | A popular compression tool that reduces file sizes using the DEFLATE algorithm. Often used in conjunction with `tar` for compressing archives. | `.gz` |
| **bzip2** | Provides better compression than `gzip` but is slower. It uses the Burrows-Wheeler algorithm and is also commonly used with `tar` for archiving. | `.bz2` |
| **xz** | Offers high compression ratios, better than `gzip` and `bzip2`, using the LZMA algorithm. It is slower but produces smaller files. | `.xz` |
| **zip** | A widely-used compression and archiving tool that creates compressed archive files, compatible with other systems like Windows. Supports multiple files in one archive. | `.zip` |
| **7z (7-Zip)** | A high-compression tool using the LZMA algorithm, supporting multiple file formats and offering strong compression. | `.7z` |
| **tar** | Primarily used for archiving multiple files into a single file, often combined with other compression tools like `gzip`, `bzip2`, or `xz` for compressed archives. | `.tar`, `.tar.gz`, `.tar.bz2`, `.tar.xz` |
| **compress** | An older Unix compression tool that uses the LZW algorithm. It is less commonly used today, but still available on many systems. | `.Z` |
| **ar** | A tool used to create and manipulate archives, mainly used in the creation of Debian package files (`.deb`). | `.a` |
| **lzma** | An older compression tool that also uses the LZMA algorithm. It has largely been replaced by `xz`, which provides similar compression with more features. | `.lzma` |
| **lzop** | A fast compression tool that uses the LZO algorithm, offering less compression, but faster speeds compared to `gzip` and `bzip2`. | `.lzo` |
| **zstd** | A fast compression tool providing high compression ratios, developed by Facebook. It is becoming increasingly popular due to its speed and efficiency. | `.zst` |
| **tar.gz** | A combination of `tar` and `gzip` used to create compressed archive files. | `.tar.gz`, `.tgz` |
| **tar.bz2** | A combination of `tar` and `bzip2` for compressed archiving, offering better compression at the cost of speed. | `.tar.bz2`, `.tbz2` |
| **tar.xz** | A combination of `tar` and `xz` for high-compression archiving, producing smaller files but with slower compression times. | `.tar.xz`, `.txz` |

## References

- [Coding](https://app.notion.com/p/Coding-21b82ffc9433484ca5e7a8aa98f32825?pvs=21)
- [Information](https://app.notion.com/p/Information-17ac0f5171ec813d813ff6055c98fe7d?pvs=21)
- https://en.wikipedia.org/wiki/Bzip2
- [Huffman Coding](https://app.notion.com/p/Huffman-Coding-198c0f5171ec807cabf9e059541c655f?pvs=21)
- https://en.wikipedia.org/wiki/Data_compression
- https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm