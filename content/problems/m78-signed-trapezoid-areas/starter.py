import numpy as np


def trapezoid_integral(times, values):
    """Return each signed trapezoidal area and cumulative integral for timestamped measurements."""
    # First: Compute a separate width for every neighboring timestamp pair.
    # Then: Multiply each width by the average endpoint height, then prefix the running total with zero.
    raise NotImplementedError("Complete the calculation and input checks")
