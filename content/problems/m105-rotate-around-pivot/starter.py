import numpy as np


def rotate_points(points, pivot, angle):
    """Translate to a pivot, apply a 2D rotation in radians and translate back without modifying inputs."""
    # First: Subtract the pivot so the rotation can be performed around the origin.
    # Then: With row-stored points, multiply by the transpose of the usual column-vector rotation matrix.
    raise NotImplementedError("Complete the calculation and input checks")
