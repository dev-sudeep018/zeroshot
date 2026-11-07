# Fit a Monotone Sequence

When two adjacent block means decrease, their unconstrained estimates violate monotonicity. Combining them at their joint weighted mean is the least-squares compromise for that pooled block.

A merge may create a new violation with the preceding block, so checking backward is essential. Sorting the observations would solve a different problem and discard their original order.
