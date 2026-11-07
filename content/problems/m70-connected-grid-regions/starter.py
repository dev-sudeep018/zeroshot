import numpy as np


def connected_grid_regions(mask):
    """Label true-cell components in row-major discovery order and report their sizes and exposed-edge perimeters."""
    # First: Scan row-major for unlabeled true cells; each becomes a flood-fill seed.
    # Then: Mark a neighbor when adding it to the work list, and count any edge that cannot enter a true cell.
    raise NotImplementedError("Complete the calculation and input checks")
