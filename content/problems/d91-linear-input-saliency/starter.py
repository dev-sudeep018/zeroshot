import numpy as np


def linear_saliency(features, weights, classes):
    """Return selected class scores, input gradients, and input-times-gradient attributions."""
    # The derivative of a weighted sum with respect to one input is its coefficient.
    # Gather weight columns per example, then transpose the gathered result.
    raise NotImplementedError("Implement the operation and validate its inputs")
