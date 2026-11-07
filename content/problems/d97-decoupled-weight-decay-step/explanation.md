# Apply Weight Decay Separately from the Optimizer Direction

Decoupling makes the parameter shrinkage independent of the optimizer’s transformation of the gradient. The direction could already include momentum or adaptive scaling.

In plain SGD this expression can coincide with an L2-gradient update. That equivalence does not generally hold after nonlinear or coordinate-dependent gradient transformations.
