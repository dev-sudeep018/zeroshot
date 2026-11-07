# Predict from Ordered Regression Bins

Piecewise-constant regression represents a numeric function by intervals and one prediction per interval. Boundary conventions are part of the model and must be consistent during evaluation.

A right-sided split convention makes equal-to-threshold values move into the next interval. Separating returned indices from predictions helps diagnose routing errors even when adjacent bins share a value.
