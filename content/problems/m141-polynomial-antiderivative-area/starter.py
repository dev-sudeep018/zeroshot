import numpy as np


def polynomial_integrals(coefficients, lower, upper):
    """Build antiderivative coefficients and evaluate signed definite integrals for paired bounds."""
    # First: An exponent k becomes k+1 in the antiderivative, so divide its coefficient by k+1.
    # Then: Evaluate the same antiderivative at upper and lower bounds, then subtract in that order.
    raise NotImplementedError("Complete the calculation and input checks")
