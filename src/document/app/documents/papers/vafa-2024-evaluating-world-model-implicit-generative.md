---
tags: [ml, cognition, epistemology]
---

# Vafa, K., Chen, J. Y., Rambachan, A., Kleinberg, J., & Mullainathan, S. (2024). Evaluating the World Model Implicit in a Generative Model. https://arxiv.org/abs/2406.03689


```python
@misc{vafa2024evaluatingworldmodelimplicit,
  title={Evaluating the World Model Implicit in a Generative Model},
  author={Keyon Vafa and Justin Y. Chen and Ashesh Rambachan and Jon Kleinberg and Sendhil Mullainathan},
  year={2024},
  eprint={2406.03689},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2406.03689}
}
```

## Notes

---

## QA

### How do we test whether a model has learned a world model?

The key is to test the model against the **true state of the world**, rather than
simply checking whether it predicts the next token correctly. The approach
constructs a world whose underlying structure is known, generates sequences in
that world, and then asks whether the model's behaviour respects the
distinctions made by the true structure.

There are two separate tests:

- **Equivalence (sequence compression):** if two sequences lead to the same true
  state, does the model treat them as equivalent?
- **Discrimination (sequence distinction):** if two sequences lead to different
  true states, does the model distinguish them?

### What are the limits of this approach? Is the term *world model* even appropriate, given that we live in a chaotic world?

> ...

## References

- Vafa, K., Chen, J. Y., Rambachan, A., Kleinberg, J., & Mullainathan, S. (2024). *Evaluating the World Model Implicit in a Generative Model*. arXiv:2406.03689. https://arxiv.org/abs/2406.03689
- Shalizi, C. R., & Crutchfield, J. P. (2001). *Computational Mechanics: Pattern and Prediction, Structure and Simplicity*. Journal of Statistical Physics, 104, 817–879.
- [Generative Model](../note/note.html?n=epistemica/observational/generative-model.md)
- [Computational Learning](../note/note.html?n=epistemica/observational/computational-learning.md)
- [Active Inference](../note/note.html?n=epistemica/dynamical-intelligence/active-inference.md)
