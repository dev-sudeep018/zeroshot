import numpy as np


def crest_summary(signal):
    """Compute RMS amplitude, peak absolute amplitude, and crest factor with an explicit all-zero convention."""
    # First: Square every sample before averaging so positive and negative amplitudes cannot cancel.
    # Then: Compute peak from absolute values and define the zero-energy case before dividing.
    raise NotImplementedError("Complete the calculation and input checks")
