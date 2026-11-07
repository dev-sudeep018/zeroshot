import numpy as np


def neuron_contributions(features, weights, bias):
    """Return each feature contribution and the resulting affine score for every example."""
    # Multiply matching feature coordinates before reducing the feature axis.
    # A negative input multiplied by a negative weight contributes positively.
    raise NotImplementedError("Implement the operation and validate its inputs")
