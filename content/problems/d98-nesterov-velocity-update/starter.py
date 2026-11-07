import numpy as np


def nesterov_step(weights, velocity, lookahead_gradient, momentum, learning_rate):
    """Return the lookahead point, new velocity, and updated parameters using the velocity-as-displacement convention."""
    # The stored velocity includes the sign and scale of previous movements.
    # The lookahead point is where the supplied gradient was evaluated; it is not the final updated point.
    raise NotImplementedError("Implement the operation and validate its inputs")
