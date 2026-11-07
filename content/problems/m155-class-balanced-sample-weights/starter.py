import numpy as np


def balanced_sample_weights(labels, classes):
    """Compute inverse-frequency sample weights scaled to mean one from integer class labels."""
    # First: Count class occurrences before looking up weights for individual samples.
    # Then: A class with fewer observations needs larger individual weights to reach the same class-total weight.
    raise NotImplementedError("Complete the calculation and input checks")
