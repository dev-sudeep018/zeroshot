import numpy as np


def clip_segment_box(start, end, lower, upper):
    """Compute the visible parameter interval of a 2D segment inside a closed axis-aligned rectangle."""
    # First: Each coordinate imposes an allowed interval for the segment parameter.
    # Then: Intersect those intervals, taking care with directions equal to zero before dividing.
    raise NotImplementedError("Complete the calculation and input checks")
