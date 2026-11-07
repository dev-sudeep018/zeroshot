import numpy as np


def weight_effective_size(weights):
    """Normalize nonnegative weights and compute inverse squared-mass effective sample size and maximum weight share."""
    # First: Normalize the weights before measuring concentration.
    # Then: Squaring increases the influence of large shares; invert the sum of squares to express it as a count.
    raise NotImplementedError("Complete the calculation and input checks")
