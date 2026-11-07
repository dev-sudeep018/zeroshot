import numpy as np


def three_event_regions(a, b, c, ab, ac, bc, abc):
    """Compute union and exactly-one/exactly-two probabilities from all intersections and validate nonnegative atomic regions."""
    # First: Subtract the triple region from every pairwise intersection to get exactly-two regions.
    # Then: Remove pairwise overlaps from each single event, adding the triple region back once.
    raise NotImplementedError("Complete the calculation and input checks")
