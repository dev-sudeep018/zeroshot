import numpy as np


def regression_fit_score(targets, predictions):
    """Compute residual and total sums of squares and R-squared with an explicit constant-target convention."""
    # First: Measure squared error of the model and of the constant mean predictor separately.
    # Then: Handle constant targets before division, and do not clip a legitimate negative score.
    raise NotImplementedError("Complete the calculation and input checks")
