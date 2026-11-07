import numpy as np


def fold_batchnorm(weights, bias, mean, variance, gamma, beta, epsilon):
    """Return folded weights and bias for batch normalization applied to x@weights+bias."""
    # Each output column has its own normalization scale.
    # The original bias participates before subtracting the running mean.
    raise NotImplementedError("Implement the operation and validate its inputs")
