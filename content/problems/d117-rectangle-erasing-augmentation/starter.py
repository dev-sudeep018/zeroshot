import numpy as np


def erase_rectangle(image, rectangle, fill):
    """Replace the pixels in a half-open rectangle with a fill value and return an erased-position mask."""
    # Clip boundaries before constructing the region; negative Python slice indices would mean something different.
    # Half-open coordinates make erased area equal to height times width after clipping.
    raise NotImplementedError("Implement the operation and validate its inputs")
