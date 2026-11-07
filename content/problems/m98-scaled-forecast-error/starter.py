import numpy as np


def scaled_forecast_error(training, actual, predicted, lag):
    """Normalize evaluation absolute error by training seasonal-naive absolute error with an explicit zero-scale policy."""
    # First: Estimate the naive-error scale only from the training series.
    # Then: Measure evaluation MAE separately, then apply the documented zero-scale convention.
    raise NotImplementedError("Complete the calculation and input checks")
