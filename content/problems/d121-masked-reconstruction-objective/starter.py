import numpy as np


def masked_reconstruction(prediction, target, masked):
    """Return the mean squared error over masked patch features and its gradient with respect to the prediction."""
    # Expand the patch mask along the feature axis.
    # The denominator is selected patch count multiplied by feature width.
    raise NotImplementedError("Implement the operation and validate its inputs")
