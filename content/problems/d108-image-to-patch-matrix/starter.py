import numpy as np


def image_patch_matrix(image, kernel_size, stride):
    """Extract valid image patches as flattened rows and return their top-left coordinates."""
    # A valid top-left coordinate leaves the entire kernel inside the image.
    # Row-major flattening visits adjacent columns before the next patch row.
    raise NotImplementedError("Implement the operation and validate its inputs")
