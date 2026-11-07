import numpy as np


def wilson_interval(successes, trials, z):
    """Compute a Wilson score interval from successes, trials and a supplied positive z value."""
    # First: Compute the shared denominator and adjusted center before the half-width.
    # Then: The adjustment changes both center and width, especially near zero or one observed proportion.
    raise NotImplementedError("Complete the calculation and input checks")
