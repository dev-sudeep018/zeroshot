import numpy as np


def pixel_tile_locations(height, width, tile_height, tile_width, indices):
    """Convert flat pixel indices into tile coordinates and within-tile coordinates for uneven image boundaries."""
    # First: First decode flat indices using image width, not tile width.
    # Then: Then divide and take remainders of row and column separately by tile dimensions.
    raise NotImplementedError("Complete the calculation and input checks")
