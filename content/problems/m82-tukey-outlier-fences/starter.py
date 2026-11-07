import numpy as np


def tukey_fences(values, multiplier):
    """Compute linear-interpolated quartiles and Tukey fences, and classify lower and upper outliers separately."""
    # First: Compute the IQR from interpolated quartiles before expanding the fences.
    # Then: Apply lower and upper strict comparisons separately to preserve the direction of each flag.
    raise NotImplementedError("Complete the calculation and input checks")
