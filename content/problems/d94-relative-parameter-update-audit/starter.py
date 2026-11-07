import numpy as np


def update_ratios(weights, updates, epsilon):
    """Return parameter norms, update norms, and stabilized update-to-weight ratios for each row."""
    # Reduce within each block and preserve the block axis.
    # A small denominator needs an explicit floor; do not add epsilon to every norm.
    raise NotImplementedError("Implement the operation and validate its inputs")
