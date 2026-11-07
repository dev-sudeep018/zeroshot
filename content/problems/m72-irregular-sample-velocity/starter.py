import numpy as np


def interval_velocities(times, positions):
    """Compute interval velocities and their midpoint timestamps from strictly increasing sample times."""
    # First: Compute each elapsed time separately because spacing may change.
    # Then: Pair each difference quotient with the average of its two timestamps.
    raise NotImplementedError("Complete the calculation and input checks")
