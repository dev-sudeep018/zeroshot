import numpy as np


def jacobi_iterations(matrix, target, initial, steps):
    """Compute a fixed number of Jacobi iterations from an initial vector and return the residual."""
    # First: Separate the diagonal from all off-diagonal coefficients once.
    # Then: Compute a complete new vector at each iteration so no coordinate sees another coordinate from the same update.
    raise NotImplementedError("Complete the calculation and input checks")
