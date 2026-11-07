import numpy as np


def point_line_projection(point, normal, offset):
    """Return signed distance and perpendicular foot for a nondegenerate implicit 2D line."""
    # First: Evaluate the line equation at the point to obtain an unnormalized signed offset.
    # Then: Normalize by the normal length, then move the point against the unit normal by that distance.
    raise NotImplementedError("Complete the calculation and input checks")
