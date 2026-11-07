import numpy as np


def lag_products(values, max_lag, normalization):
    """Compute raw lag products with biased or overlap-count normalization and return counts."""
    # First: Slice two overlapping portions separated by the requested lag.
    # Then: Keep the normalization choice explicit because overlap shrinks as lag grows.
    raise NotImplementedError("Complete the calculation and input checks")
