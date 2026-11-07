import numpy as np


def mixture_variance(weights, means, variances):
    """Combine mixture weights, conditional means and variances into a total mean and variance."""
    # First: First compute the overall weighted mean.
    # Then: Average the within-group variances and separately measure the spread of group means.
    raise NotImplementedError("Complete the calculation and input checks")
