# Accumulate Unequal Microbatch Gradients

The full-batch mean is a sample-weighted combination of microbatch means. Equal averaging is correct only when microbatches have equal example counts.

This is an algebraic accumulation lesson with supplied gradients. Stateful layers, stochastic masks, and loss normalization can make actual microbatch training differ from a single large-batch forward pass.

Concept references (original code and prose):

- [PyTorch Automatic Mixed Precision examples](https://docs.pytorch.org/docs/2.14/notes/amp_examples.html) — Sample-weighted supplied gradients and finite-check/unscale gate; no autograd or optimizer implementation.
