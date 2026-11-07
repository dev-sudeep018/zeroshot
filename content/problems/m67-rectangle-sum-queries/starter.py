import numpy as np


def rectangle_sums(grid, rectangles):
    """Use a summed-area table to answer half-open rectangular grid queries, including empty rectangles."""
    # First: Pad the cumulative-sum table with a zero row and column.
    # Then: Combine bottom-right minus top strip minus left strip plus their overlap.
    raise NotImplementedError("Complete the calculation and input checks")
