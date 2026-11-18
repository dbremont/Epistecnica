---
tags: [note, como]
---

# ¿Cómo remover los primeros x bytes de un archivo?


¿Cómo remover los primeros x bytes de un archivo?

```bash
dd bs=1 skip=87 if=ARC_ARCHIVO of=trimed
```
