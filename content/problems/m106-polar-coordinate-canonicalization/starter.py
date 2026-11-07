import numpy as np


def canonical_polar(points):
    """Compute radii and angles in [0,2*pi), using zero angle at the origin."""
    # First: Use both coordinates in atan2 so the quadrant is preserved.
    # Then: Wrap angles into one fixed interval and treat radius zero as a separate canonical case.
    raise NotImplementedError("Complete the calculation and input checks")
