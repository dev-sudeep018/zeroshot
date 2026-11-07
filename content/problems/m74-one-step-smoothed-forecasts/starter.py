import numpy as np


def smoothed_forecasts(values, alpha, initial):
    """Produce one-step exponential-smoothing forecasts and the final level without leaking the current observation."""
    # First: Store the old level before reading the observation into the update.
    # Then: The forecast array has n entries; the final updated level is a separate output.
    raise NotImplementedError("Complete the calculation and input checks")
