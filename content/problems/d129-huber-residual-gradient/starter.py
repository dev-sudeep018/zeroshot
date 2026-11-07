import numpy as np


def huber_residuals(residuals, delta):
    """Return each residual’s Huber loss and derivative, plus the mean loss and the gradient of that mean."""
    # Both branches agree in value and slope at the threshold.
    # The derivative points in the residual’s direction but its magnitude stops growing beyond delta.
    raise NotImplementedError("Implement the operation and validate its inputs")
