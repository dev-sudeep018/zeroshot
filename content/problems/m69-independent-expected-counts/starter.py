import numpy as np


def independence_baseline(counts):
    """Derive expected cell counts from observed row and column totals and report observed-minus-expected residuals."""
    # First: Compute the row totals and column totals once.
    # Then: Their outer product is too large by one factor of the grand total, so divide by that total.
    raise NotImplementedError("Complete the calculation and input checks")
