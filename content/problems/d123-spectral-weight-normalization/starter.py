import numpy as np


def spectral_normalize(weights, bound):
    """Scale a nonzero weight matrix so its largest singular value equals a requested positive bound."""
    # The leading singular value measures operator gain, while Frobenius norm measures all squared entries.
    # A zero matrix has no direction to normalize and is rejected.
    raise NotImplementedError("Implement the operation and validate its inputs")
