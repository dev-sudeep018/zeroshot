# Fit Median Imputation on Training Rows

Fit and transform are distinct operations. The feature statistics depend only on observed training entries, and the transform reuses those statistics on any aligned matrix.

A separate boolean mask avoids overloading a numeric sentinel such as zero or NaN. Zero can be a valid observation, and arbitrary masked placeholders must not influence the median.
