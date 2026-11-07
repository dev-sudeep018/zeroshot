import numpy as np


def orthogonality_penalty(weights):
    """Return the squared Frobenius penalty on W.T@W-I and its gradient with respect to W."""
    # The diagonal of the Gram matrix measures squared column norms; off-diagonal entries measure inner products.
    # The derivative receives equal contributions from both appearances of W.
    raise NotImplementedError("Implement the operation and validate its inputs")
