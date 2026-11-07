import numpy as np


def leave_one_out_mean(values):
    """Compute omitted-observation means and the jackknife mean estimate without refitting each sample."""
    # First: A shared total sum lets you omit one value without rebuilding each sample.
    # Then: Measure variation among the leave-one-out estimates using the specified jackknife scaling.
    raise NotImplementedError("Complete the calculation and input checks")
