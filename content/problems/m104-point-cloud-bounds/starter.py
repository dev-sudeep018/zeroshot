import numpy as np


def point_cloud_bounds(points):
    """Compute coordinatewise bounds, center, side lengths and volume for a point cloud."""
    # First: Reduce rows independently for each coordinate to find the lower and upper limits.
    # Then: Derive midpoint, lengths and volume from those limits rather than from the point mean.
    raise NotImplementedError("Complete the calculation and input checks")
