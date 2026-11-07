# Remove Correlation with Symmetric Whitening

A covariance eigendecomposition identifies orthogonal directions and their variances. Scaling each direction by the inverse square root and rotating back gives a symmetric transform.

With regularization, W(C+epsilon I)W.T equals identity up to numerical error. W C W.T instead retains a small regularization-dependent shrinkage, so it should not be claimed to equal identity exactly.
