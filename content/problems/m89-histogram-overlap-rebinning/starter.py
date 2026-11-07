import numpy as np


def rebin_histogram(old_edges, masses, new_edges):
    """Redistribute piecewise-uniform bin mass according to interval overlaps between two edge grids."""
    # First: Compute the intersection length between each old interval and each new interval.
    # Then: Divide each intersection by the old interval width before multiplying by its mass.
    raise NotImplementedError("Complete the calculation and input checks")
