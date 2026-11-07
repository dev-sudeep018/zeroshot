import numpy as np


def trimmed_summary(values, trim):
    """Sort observations, trim a fixed count from both tails, and report the retained mean and count."""
    # First: Sort before deciding which observations belong to each tail.
    # Then: Slice from trim to n-trim and compute both the mean and retained count.
    raise NotImplementedError("Complete the calculation and input checks")
