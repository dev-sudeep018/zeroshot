# Classify by Learned Class Means

Nearest-centroid classification compresses each class into its mean feature vector. It provides a simple learned baseline whose fitted state is easy to inspect.

Queries must not alter the centroids; that would leak evaluation information into training. Stable class ordering also makes tie behavior reproducible.
