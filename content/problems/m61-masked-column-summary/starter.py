import numpy as np


def observed_column_summary(values, observed, fallback):
    """Compute column counts and means under an explicit observation mask, with a defined empty-column fallback."""
    # First: Keep the observation mask separate from the numeric measurements.
    # Then: Sum only selected cells and divide only columns whose count is positive.
    raise NotImplementedError("Complete the calculation and input checks")
