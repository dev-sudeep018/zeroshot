# Measure Binned Population Shift

The PSI compares two discrete distributions on shared bins. A positive pseudocount prevents division by zero, and every contribution is nonnegative because its two factors have matching signs.

Results depend on binning and smoothing. The implementation reports the statistic and its contributions without attaching universal severity thresholds.
