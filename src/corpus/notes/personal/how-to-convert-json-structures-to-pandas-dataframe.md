---
tags: [note, como]
---

# How to convert json structures to pandas dataframe?


```python
data = <some json>
df = pd.json_normalize(data['results'])
```
