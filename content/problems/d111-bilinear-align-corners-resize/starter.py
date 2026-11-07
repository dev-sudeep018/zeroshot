import numpy as np


def bilinear_resize(image, output_size):
    """Resize a single-channel image using bilinear interpolation with aligned corners."""
    # Interpolate horizontally in two source rows, then vertically between those results.
    # A source axis of length one contributes the same coordinate everywhere.
    raise NotImplementedError("Implement the operation and validate its inputs")
