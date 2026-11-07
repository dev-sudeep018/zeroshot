import numpy as np


def convolution_budget(input_channels, output_channels, kernel, groups, output_size, bias):
    """Count weight parameters, optional biases, and multiply-accumulates for one output image."""
    # Each grouped output sees only input_channels/groups input channels.
    # Output positions share parameters; multiply the operation count by area.
    raise NotImplementedError("Implement the operation and validate its inputs")
