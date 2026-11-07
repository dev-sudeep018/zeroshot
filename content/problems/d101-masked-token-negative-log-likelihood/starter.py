import numpy as np


def masked_token_nll(logits, targets, mask):
    """Return per-token negative log likelihood with zeros at masked positions and its mean over valid positions."""
    # Subtract each vocabulary row’s maximum before exponentiating.
    # Sum the masked losses and divide by the number of valid tokens.
    raise NotImplementedError("Implement the operation and validate its inputs")
