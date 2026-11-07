import numpy as np


def anova_partition(values, labels, groups):
    """Compute grand mean, between-group and within-group sums of squares from labeled numeric observations."""
    # First: Compute each group count and mean before its contribution to between-group variation.
    # Then: Subtract the corresponding group mean from each observation to isolate within-group variation.
    raise NotImplementedError("Complete the calculation and input checks")
