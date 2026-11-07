import numpy as np


def permute_hidden(input_weights, hidden_bias, output_weights, order):
    """Apply a hidden-neuron permutation to both sides of a two-layer network."""
    # Incoming connections are columns; outgoing connections are rows.
    # The same order is needed on both sides, rather than the inverse on one side.
    raise NotImplementedError("Implement the operation and validate its inputs")
