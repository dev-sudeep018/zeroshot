import numpy as np


def temperature_nll(logits, targets, temperature):
    """Return mean negative log likelihood and the derivative with respect to temperature."""
    # Differentiate each scaled logit z/T with respect to T.
    # Subtracting a common constant from every class in a row should change neither result.
    raise NotImplementedError("Implement the operation and validate its inputs")
