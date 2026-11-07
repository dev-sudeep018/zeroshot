import numpy as np


def symmetric_percentage_errors(actual, predicted):
    """Compute symmetric absolute percentage errors with a both-zero convention and their mean."""
    # First: Build an absolute-magnitude denominator from both observations in each pair.
    # Then: Write zero for the both-zero case before averaging the bounded per-item errors.
    raise NotImplementedError("Complete the calculation and input checks")
