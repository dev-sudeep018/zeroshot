import numpy as np


def cohen_agreement(first, second, classes):
    """Compute observed agreement, marginal chance agreement and Cohen's kappa for paired categorical labels."""
    # First: Build one empirical label-frequency vector for each rater.
    # Then: Compare actual agreement with the agreement implied by independent draws from those two marginal distributions.
    raise NotImplementedError("Complete the calculation and input checks")
