import numpy as np


def pooled_variance(sizes, variances):
    """Combine group sizes and sample variances using residual degrees of freedom without adding between-group variation."""
    # First: A sample variance represents its residual sum of squares divided by size minus one.
    # Then: Recover those sums of squares and divide their total by total residual degrees of freedom.
    raise NotImplementedError("Complete the calculation and input checks")
