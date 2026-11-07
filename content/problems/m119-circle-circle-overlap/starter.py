import numpy as np


def disk_overlap(radius_a, radius_b, distance):
    """Handle disjoint, contained and partial-overlap circles with the lens-area formula."""
    # First: Handle disjointness and containment before the lens formula, which divides by center distance.
    # Then: In the partial-overlap case, use each radius for its own sector and subtract the shared triangle contribution.
    raise NotImplementedError("Complete the calculation and input checks")
