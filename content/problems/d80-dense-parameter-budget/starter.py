import numpy as np


def dense_budget(widths, biases):
    """Return per-layer weight, bias, and total counts, plus the total network parameter count."""
    # Adjacent widths describe a parameter block; the input layer has none.
    # Disabling bias removes one parameter per output neuron.
    raise NotImplementedError("Implement the operation and validate its inputs")
