import numpy as np


def poisson_counts(rate, counts):
    """Compute probabilities for requested integer counts and the expected count for a bounded positive rate."""
    # First: The logarithm of k! is lgamma(k+1), including the k=0 case.
    # Then: Evaluate each requested count separately and preserve its original position.
    raise NotImplementedError("Complete the calculation and input checks")
