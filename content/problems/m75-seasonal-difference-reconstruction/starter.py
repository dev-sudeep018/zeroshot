import numpy as np


def seasonal_differences(values, lag):
    """Compute lagged differences and reconstruct the signal from its initial season and differences."""
    # First: Keep the first full season; differences alone cannot recover the starting level.
    # Then: During reconstruction, add each difference to the value one full lag earlier.
    raise NotImplementedError("Complete the calculation and input checks")
