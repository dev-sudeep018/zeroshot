import numpy as np


def frozen_sgd(weights, gradients, trainable, learning_rate):
    """Apply SGD only to trainable coordinates and report their changes."""
    # Mask the proposed update.
    # Zeroing a frozen weight would destroy the value you intended to preserve.
    raise NotImplementedError("Implement the operation and validate its inputs")
