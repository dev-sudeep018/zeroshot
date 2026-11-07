import numpy as np


def ensemble_audit(probabilities):
    """Average model probabilities and measure the fraction of votes outside the majority class."""
    # Average the model axis while retaining batch and class axes.
    # Averaged probabilities and majority votes can favor different classes.
    raise NotImplementedError("Implement the operation and validate its inputs")
