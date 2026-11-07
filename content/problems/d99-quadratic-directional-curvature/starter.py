import numpy as np


def quadratic_probe(hessian, point, direction):
    """Return the objective value, directional slope, directional curvature, and unconstrained minimizing step along the direction."""
    # Expand q(x+t*d) as a quadratic in the scalar t.
    # Only positive curvature along this direction is required; the matrix need not be positive definite in every direction.
    raise NotImplementedError("Implement the operation and validate its inputs")
