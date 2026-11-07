import numpy as np


def plateau_rates(losses, initial_rate, factor, patience, min_rate):
    """Return the learning rate to use after each epoch’s validation, including repeated reductions down to a floor."""
    # Track best loss, consecutive stalls, and current rate as separate variables.
    # Record the rate after processing the epoch, so the reduction appears at that index.
    raise NotImplementedError("Implement the operation and validate its inputs")
