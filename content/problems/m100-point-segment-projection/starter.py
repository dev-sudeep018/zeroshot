import numpy as np


def nearest_on_segment(point, start, end):
    """Project a point onto a finite 2D segment, clamp the parameter and return squared distance."""
    # First: Project onto the infinite line using a dot product divided by squared segment length.
    # Then: Clamp the projection parameter so the nearest point cannot lie beyond either endpoint.
    raise NotImplementedError("Complete the calculation and input checks")
