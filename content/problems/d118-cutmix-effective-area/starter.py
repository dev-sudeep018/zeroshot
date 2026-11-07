import numpy as np


def cutmix_pair(image_a, image_b, label_a, label_b, rectangle):
    """Replace a clipped rectangle of the first image with the second image and return the area-correct soft label."""
    # Compute label mixing from clipped dimensions, not the requested dimensions.
    # A patch outside the image has zero area and must leave the first label unchanged.
    raise NotImplementedError("Implement the operation and validate its inputs")
