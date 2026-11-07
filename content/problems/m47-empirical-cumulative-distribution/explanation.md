# Read Probability from an Empirical CDF

Each sample contributes mass 1/n. The empirical CDF adds those masses up through a threshold and therefore includes every tied value at that threshold.

Sorting once permits binary-search queries. The result is a step function rather than the interpolation used by the earlier quantile exercise.
