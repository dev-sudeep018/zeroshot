import numpy as np


def resample_polyline(points, distances):
    """Interpolate positions at cumulative path distances while skipping zero-length segments."""
    # First: Use cumulative segment lengths to locate the segment containing each traveled distance.
    # Then: Subtract the distance before that segment and divide by its positive length to get the local interpolation fraction.
    raise NotImplementedError("Complete the calculation and input checks")
