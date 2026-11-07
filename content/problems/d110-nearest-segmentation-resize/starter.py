import numpy as np


def resize_segmentation(labels, output_size):
    """Resize an integer label map with the documented nearest-neighbor coordinate rule."""
    # Construct source indices independently for the two output axes.
    # Never average class identifiers, even when downsampling.
    raise NotImplementedError("Implement the operation and validate its inputs")
