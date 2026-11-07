import numpy as np


def attention_support(attention):
    """Return attention entropy in natural units, exponential effective support, and the largest weight per query."""
    # Only positive probabilities contribute to the entropy sum.
    # A uniform row over K keys has effective support K; a one-hot row has support one.
    raise NotImplementedError("Implement the operation and validate its inputs")
