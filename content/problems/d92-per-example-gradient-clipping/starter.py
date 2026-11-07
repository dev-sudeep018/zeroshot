import numpy as np


def clip_example_gradients(gradients, max_norm):
    """Clip every gradient row by its own L2 norm, then return the clipped rows, scale factors, and mean gradient."""
    # Compute a norm per row instead of one norm for the entire batch.
    # Clipping and averaging generally do not commute.
    raise NotImplementedError("Implement the operation and validate its inputs")
