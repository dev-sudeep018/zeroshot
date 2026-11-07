import numpy as np


def causal_convolution_chunk(chunk, kernel, state):
    """Compute outputs for the new chunk and return the history needed for the next call."""
    # Join the stored history to the new chunk before applying backward-looking windows.
    # A chunk shorter than the kernel still leaves some old history in the next state.
    raise NotImplementedError("Implement the operation and validate its inputs")
