import numpy as np


def markov_steps(initial, transition, steps):
    """Propagate a probability row vector through a stochastic matrix for a fixed number of steps."""
    # First: A transition row describes where probability leaves its starting state.
    # Then: Save the initial row, then repeatedly multiply on the right and append each resulting distribution.
    raise NotImplementedError("Complete the calculation and input checks")
