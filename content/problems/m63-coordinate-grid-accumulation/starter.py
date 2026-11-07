import numpy as np


def accumulate_grid(rows, cols, coordinates, values):
    """Scatter repeated integer grid coordinates into separate sum and count grids."""
    # First: Allocate separate sum and count grids so zero-valued measurements are still counted.
    # Then: Visit each coordinate-value pair and add to the existing cell rather than overwrite it.
    raise NotImplementedError("Complete the calculation and input checks")
