import numpy as np


def segmentation_boundaries(labels):
    """Return a boolean map marking pixels with at least one differently labeled four-connected in-bounds neighbor."""
    # Compare adjacent rows and adjacent columns, marking both members of each unequal pair.
    # Do not wrap around the image when checking an edge.
    raise NotImplementedError("Implement the operation and validate its inputs")
