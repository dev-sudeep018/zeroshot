# Refine a Gaussian Mixture with Soft Assignments

The expectation step normalizes component joint densities into responsibilities. The maximization step treats those responsibilities as fractional membership weights for new means and variances.

The likelihood belongs to the parameters supplied at the start of the step. A variance floor prevents collapse to zero width; numerically empty components require a policy and are rejected here.
