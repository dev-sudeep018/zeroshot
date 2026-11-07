# Separate Within-Group Scatter from Group Means

Pooling within-group variances combines scatter around each group mean. It intentionally excludes differences between the group means themselves.

Weighting by group size would be slightly wrong because each estimated mean consumes one degree of freedom. Groups with identical sample variances retain that variance regardless of their different sizes.
