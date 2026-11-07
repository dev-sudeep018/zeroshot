import numpy as np


def logit_margins(logits):
    """Return the winning class, runner-up class, and logit margin for every example."""
    # Stable descending sorting preserves index order for tied scores.
    # Common score offsets cannot change either the ranking or the margin.
    raise NotImplementedError("Implement the operation and validate its inputs")
