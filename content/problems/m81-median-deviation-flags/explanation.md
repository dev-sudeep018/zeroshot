# Flag Outliers Using Median Deviations

The median resists a minority of extreme values, and the median distance measures a similarly robust spread. A raw MAD is a distance in the same units as the observations.

Dividing by MAD creates a zero-denominator problem for repeated values. Comparing distances with the scaled MAD both avoids that division and implements a clear policy for constant or nearly constant samples.
