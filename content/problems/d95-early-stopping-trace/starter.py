import numpy as np


def early_stopping(losses, patience, min_delta):
    """Replay early stopping and return the best epoch, stopping epoch, and observed stall counts."""
    # Keep separate state for the remembered best loss and the consecutive stall count.
    # Equality at the min_delta boundary is a stall under this contract.
    raise NotImplementedError("Implement the operation and validate its inputs")
