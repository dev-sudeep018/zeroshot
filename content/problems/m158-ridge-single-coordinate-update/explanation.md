# Minimize One Ridge Coordinate Exactly

Coordinate descent reduces a multivariate optimization problem to one variable at a time. For a squared-error objective with L2 regularization that one-dimensional minimizer has a closed form.

The factor conventions in the objective determine the denominator. Removing the old coordinate contribution avoids double-counting it, and an exact update cannot increase this objective.
