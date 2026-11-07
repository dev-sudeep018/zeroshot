import numpy as np


def attention_rollout(attention, residual_weight):
    """Return layer-by-layer cumulative token mixing matrices after residual addition and row normalization."""
    # The newest mapping multiplies on the left because it maps current tokens to previous tokens.
    # Normalize after adding identity so every cumulative row still sums to one.
    raise NotImplementedError("Implement the operation and validate its inputs")
