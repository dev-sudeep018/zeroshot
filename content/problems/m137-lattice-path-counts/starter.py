import numpy as np


def blocked_grid_paths(blocked):
    """Use dynamic programming to count right/down lattice routes while respecting blocked endpoints."""
    # First: A reachable cell receives paths from the cell above and the cell to its left.
    # Then: Carry one row of exact counts; a blocked cell must reset its count to zero.
    raise NotImplementedError("Complete the calculation and input checks")
