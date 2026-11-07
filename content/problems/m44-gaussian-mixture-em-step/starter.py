import numpy as np


def gaussian_em_step(values, weights, means, variances, variance_floor=1e-6):
    """Perform one full univariate Gaussian-mixture expectation and maximization step, returning updated parameters and the old total log likelihood."""
    raise NotImplementedError("Implement the documented operation")
