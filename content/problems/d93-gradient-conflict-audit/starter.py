import numpy as np


def gradient_conflicts(gradients):
    """Return cosine similarities and a boolean matrix identifying strictly negative cosine similarity."""
    # Normalize nonzero rows, then form their Gram matrix.
    # Opposite vectors conflict, while perpendicular and zero vectors do not.
    raise NotImplementedError("Implement the operation and validate its inputs")
