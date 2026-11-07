import numpy as np


def event_probabilities(probabilities, event_a, event_b):
    """Use probability masses and two event masks to compute union, intersection and conditional probability."""
    # First: Treat each mask as a selection of outcomes, and combine masks with AND and OR.
    # Then: Compute the probability of B before division; conditioning is undefined when that mass is zero.
    raise NotImplementedError("Complete the calculation and input checks")
