import numpy as np


def bernoulli_log_scores(features, priors, likelihoods):
    """Compute class log scores from priors and conditional feature probabilities, including absent features."""
    # First: Use one log-probability term for feature presence and another for absence.
    # Then: Matrix multiplication can sum those contributions for every sample-class pair before adding log priors.
    raise NotImplementedError("Complete the calculation and input checks")
