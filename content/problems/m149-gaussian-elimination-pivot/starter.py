import numpy as np


def pivoted_linear_solve(matrix, target):
    """Perform elimination and back substitution with row pivoting and a documented singularity threshold."""
    # First: Choose a pivot row from the still-unprocessed rows before eliminating below it.
    # Then: Carry row swaps and elimination into the target vector, then solve from the last equation upward.
    raise NotImplementedError("Complete the calculation and input checks")
