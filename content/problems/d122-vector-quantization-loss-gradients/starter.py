import numpy as np


def vq_losses(encoder, codes, commitment):
    """Compute mean codebook and commitment losses with their separate gradients for already matched code vectors."""
    # The scalar squared residual can be reused, but the two gradient destinations cannot.
    # At zero commitment only the codebook is updated by these losses.
    raise NotImplementedError("Implement the operation and validate its inputs")
