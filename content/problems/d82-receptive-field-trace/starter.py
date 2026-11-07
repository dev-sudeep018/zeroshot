import numpy as np


def receptive_fields(kernels, strides, dilations):
    """Trace theoretical receptive-field span and input-space jump after every layer."""
    # The previous jump converts a kernel offset to input-space distance.
    # Expand the field before applying the current layer’s stride.
    raise NotImplementedError("Implement the operation and validate its inputs")
