import numpy as np


def epsilon_insensitive_loss(predictions, targets, epsilon):
    """Compute mean epsilon-insensitive absolute loss and its prediction subgradient with zero derivative at the boundary."""
    # First: Compute signed residuals, then use their absolute values to decide which observations leave the band.
    # Then: Only outside observations contribute a sign gradient, scaled by the number of observations.
    raise NotImplementedError("Complete the calculation and input checks")
