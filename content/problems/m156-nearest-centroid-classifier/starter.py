import numpy as np


def nearest_centroid_predict(training, labels, queries, classes):
    """Fit centroids for each contiguous class ID and predict nearest centroid with smallest-ID tie breaking."""
    # First: Group training rows by class and average each group along the sample axis.
    # Then: Broadcast query-to-centroid differences, sum their squares over features, and take the first minimum.
    raise NotImplementedError("Complete the calculation and input checks")
