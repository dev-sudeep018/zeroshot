import numpy as np


def secant_polynomial(coefficients, first, second, steps):
    """Apply a fixed number of secant iterations with clear zero-denominator handling."""
    # First: Reuse the last two estimates and their function values to form a secant slope.
    # Then: Check the denominator before division and retain both old estimates until the new one is computed.
    raise NotImplementedError("Complete the calculation and input checks")
