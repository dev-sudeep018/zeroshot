import numpy as np


def decoupled_decay(weights, direction, learning_rate, decay):
    """Return the proposed parameters and separate optimization and decay changes."""
    # Compute both changes from the same starting parameter state.
    # Applying decay to the already updated weights introduces a different cross term.
    raise NotImplementedError("Implement the operation and validate its inputs")
