import numpy as np


def regression_bins(splits, values, queries):
    """Assign numeric queries to right-sided split intervals and return their piecewise constant predictions and bin indices."""
    # First: A bin index equals the number of split values less than or equal to the query.
    # Then: Use those indices to gather predictions from the bin-value vector.
    raise NotImplementedError("Complete the calculation and input checks")
