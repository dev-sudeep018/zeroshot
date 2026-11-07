import numpy as np


def collision_probability(categories, draws):
    """Compute collision probability for uniform independent labels using the no-collision product."""
    # First: Condition on each earlier draw having used a different label.
    # Then: The next draw avoids all k occupied labels with probability 1-k/categories.
    raise NotImplementedError("Complete the calculation and input checks")
