import numpy as np


def median_outliers(values, threshold):
    """Compute a median center and median absolute deviation, then flag strict threshold exceedances including a zero-MAD policy."""
    # First: Find the median twice: first on values, then on absolute distances from that center.
    # Then: Compare distances directly with threshold times MAD so the zero-MAD case needs no division.
    raise NotImplementedError("Complete the calculation and input checks")
