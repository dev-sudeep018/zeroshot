import numpy as np


def weighted_median(values, weights):
    """Sort value-weight pairs and return the smallest value whose cumulative weight reaches half the total."""
    # First: Sort values while keeping their weights paired, then remove zero-weight entries.
    # Then: Find the first cumulative weight at or above half the total, using a left-sided search.
    raise NotImplementedError("Complete the calculation and input checks")
