import numpy as np


def linear_resample(times, values, queries):
    """Interpolate queries on a strictly increasing grid with constant endpoint extension and preserved query order."""
    # First: Locate the two sample times surrounding each query before forming a fraction.
    # Then: Interpolate values with that fraction and handle outside-domain queries using endpoint extension.
    raise NotImplementedError("Complete the calculation and input checks")
