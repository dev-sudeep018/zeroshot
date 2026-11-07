import numpy as np


def expected_distinct(probabilities, draws):
    """Compute per-category appearance probabilities and expected distinct categories after independent draws."""
    # First: Use the complement: a category is unseen only if every draw avoids it.
    # Then: Add appearance probabilities using linearity of expectation; their indicator variables need not be independent.
    raise NotImplementedError("Complete the calculation and input checks")
