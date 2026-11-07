import numpy as np


def weighted_density(values, weights, edges):
    """Accumulate nonnegative sample weights into uneven bins and divide by total weight and bin widths."""
    # First: Assign interior-edge values to the bin on their right, with a special inclusive final endpoint.
    # Then: Normalize weighted counts into masses before dividing by each bin width.
    raise NotImplementedError("Complete the calculation and input checks")
