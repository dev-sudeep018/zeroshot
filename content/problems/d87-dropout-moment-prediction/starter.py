import numpy as np


def dropout_moments(activations, keep_probability):
    """Return elementwise mean, variance, and second moment under independent inverted dropout."""
    # List the two possible outcomes for a single coordinate.
    # Squared values determine variance, so negative activations still have nonnegative variance.
    raise NotImplementedError("Implement the operation and validate its inputs")
