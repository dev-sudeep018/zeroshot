import numpy as np


def plane_from_points(a, b, c):
    """Normalize a cross product into a plane normal and compute its offset, rejecting collinear points."""
    # First: Construct two edge vectors lying within the plane.
    # Then: Normalize their cross product, then choose the offset that makes one given vertex satisfy the plane equation.
    raise NotImplementedError("Complete the calculation and input checks")
