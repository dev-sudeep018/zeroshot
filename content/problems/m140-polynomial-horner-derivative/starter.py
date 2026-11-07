import numpy as np


def horner_value_slope(coefficients, points):
    """Apply a coupled Horner recurrence to descending coefficients at a batch of query points."""
    # First: Keep the value and slope accumulators as arrays matching the query vector.
    # Then: Update the slope using the old value before replacing the value accumulator.
    raise NotImplementedError("Complete the calculation and input checks")
