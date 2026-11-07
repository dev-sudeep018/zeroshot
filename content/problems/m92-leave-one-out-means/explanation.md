# Compute Every Leave-One-Out Mean

Leave-one-out estimates reveal how sensitive a statistic is to each observation. For the mean, subtracting an observation from the total gives every refitted estimate in linear time.

The estimates are highly dependent because their samples overlap. The jackknife standard-error factor accounts for that structure; taking their ordinary standard deviation would use the wrong scale.
