import numpy as np


def rolling_origin_splits(length, initial, horizon, stride):
    """Produce expanding-window training and validation index boundaries with a fixed horizon and stride."""
    # First: Track the training endpoint and derive each validation endpoint from the fixed horizon.
    # Then: Stop before a horizon would cross the dataset length instead of truncating the last validation fold.
    raise NotImplementedError("Complete the calculation and input checks")
