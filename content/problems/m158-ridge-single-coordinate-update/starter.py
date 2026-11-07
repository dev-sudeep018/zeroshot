import numpy as np


def ridge_coordinate(matrix, targets, coefficients, coordinate, penalty):
    """Update one linear coefficient from the residual excluding that feature under a fixed squared-error and L2 convention."""
    # First: Remove the chosen coefficient contribution from current predictions to form its partial residual.
    # Then: The exact one-coordinate minimizer is column dot partial-residual divided by its squared norm plus the penalty.
    raise NotImplementedError("Complete the calculation and input checks")
