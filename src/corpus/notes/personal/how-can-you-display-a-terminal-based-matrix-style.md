---
tags: [note, como]
---

# How can you display a terminal-based matrix-style animation in Linux?


`cmatrix`

```bash
autoreconf -i  # skip if using released tarball
./configure
make
make install

# If problems try

sudo apt-get install libncursesw5-dev
gcc -o cmatrix cmatrix.c -lncursesw
```
