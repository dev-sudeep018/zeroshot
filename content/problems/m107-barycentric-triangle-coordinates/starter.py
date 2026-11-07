import numpy as np


def barycentric_location(point, vertices):
    """Solve barycentric weights and test inclusive membership for a nondegenerate 2D triangle."""
    # First: Use vertex zero as the origin and solve for coefficients of its two edge vectors.
    # Then: The remaining coefficient is one minus the two solved coefficients; all three determine membership.
    raise NotImplementedError("Complete the calculation and input checks")
