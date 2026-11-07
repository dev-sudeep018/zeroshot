# Split Time-Ordered Data with an Embargo

A temporal split tests predictions on later observations. The embargo discards a band around the cutoff, which can reduce overlap between temporally adjacent examples.

The exact inequalities matter: the lower embargo boundary belongs to the gap, while the upper boundary belongs to test. This convention yields disjoint and exhaustive row sets.
