import numpy as np


def centered_smoothing(values, radius):
    """Average centered windows with shrinking boundaries and return the contributing counts."""
    # First: Work out valid left and right boundaries before taking each window.
    # Then: Divide by the actual window size rather than the nominal width 2*radius+1.
    raise NotImplementedError("Complete the calculation and input checks")
