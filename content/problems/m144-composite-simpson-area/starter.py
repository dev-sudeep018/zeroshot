import numpy as np


def simpson_samples(values, spacing):
    """Validate odd sample count and apply alternating interior weights to a fixed-spacing sample vector."""
    # First: Use separate slices for odd and even interior sample indices.
    # Then: Apply endpoint weights only once, then multiply the entire weighted sum by spacing/3.
    raise NotImplementedError("Complete the calculation and input checks")
