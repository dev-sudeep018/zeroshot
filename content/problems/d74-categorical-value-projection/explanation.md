# Project a Distributional Value Target

Projection preserves total probability and the clipped transformed expectation. Support clipping can change the unbounded Bellman expectation, so the support is a modeling choice.

Terminal updates collapse the future distribution to the reward, but a reward between two support points still occupies two bins. This is the categorical projection used by distributional methods, with an arbitrary support size.

Conceptual reading: https://arxiv.org/abs/1707.06887
