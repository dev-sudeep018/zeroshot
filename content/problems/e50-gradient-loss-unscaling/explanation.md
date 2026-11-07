# Unscale Gradients and Skip Overflowed Steps

Scaling is useful only if gradients are restored before the optimizer consumes them. Applying an optimizer to scaled gradients changes the effective update size.

This function demonstrates a finite-check gate with an explicit skip signal. It does not simulate low-precision hardware, maintain master weights, or silently turn an overflowed step into a partial parameter update.

Concept references (original code and prose):

- [PyTorch Automatic Mixed Precision examples](https://docs.pytorch.org/docs/2.14/notes/amp_examples.html) — Sample-weighted supplied gradients and finite-check/unscale gate; no autograd or optimizer implementation.
