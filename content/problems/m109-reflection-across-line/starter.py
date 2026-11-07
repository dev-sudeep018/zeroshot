import numpy as np


def reflect_points(points, normal, offset):
    """Use signed line offsets to reflect a batch of 2D points across a nonzero-normal line."""
    # First: Calculate the offset of each point from the line equation.
    # Then: A reflection travels twice the displacement needed to reach the perpendicular foot.
    raise NotImplementedError("Complete the calculation and input checks")
