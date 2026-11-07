import numpy as np


def calibrate_channels(readings, gains, offsets, lower, upper):
    """Broadcast channel gains and offsets over readings, then clip each channel to its physical range."""
    # First: Represent channel parameters as vectors matching the second matrix axis.
    # Then: Compute calibrated values first, then compare with both bounds before clipping.
    raise NotImplementedError("Complete the calculation and input checks")
