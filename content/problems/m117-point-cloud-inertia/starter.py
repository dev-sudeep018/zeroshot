import numpy as np


def planar_mass_moments(points, masses):
    """Compute mass-weighted center and second-moment inertia components around that center."""
    # First: Compute the mass-weighted center before evaluating any squared distances.
    # Then: Moment about the x axis uses squared y distance, while the cross term carries a minus sign.
    raise NotImplementedError("Complete the calculation and input checks")
