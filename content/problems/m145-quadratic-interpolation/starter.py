import numpy as np


def quadratic_interpolate(nodes, values, queries):
    """Solve three-point Lagrange interpolation for distinct nodes and evaluate a batch of queries."""
    # First: Each basis polynomial is one at its own node and zero at the other two nodes.
    # Then: Multiply each basis value by its corresponding sample and sum all three contributions.
    raise NotImplementedError("Complete the calculation and input checks")
