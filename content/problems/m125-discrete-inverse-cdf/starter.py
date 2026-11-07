import numpy as np


def categorical_inverse_cdf(probabilities, draws):
    """Build a categorical CDF and choose the first cumulative mass strictly above each supplied draw."""
    # First: Cumulative masses divide [0,1) into half-open category intervals.
    # Then: A right-sided search moves past equal cumulative boundaries and zero-width intervals.
    raise NotImplementedError("Complete the calculation and input checks")
