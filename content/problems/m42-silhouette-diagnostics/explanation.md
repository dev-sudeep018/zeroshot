# Diagnose Cluster Separation

A silhouette compares the average distance within the assigned group with the best competing group. Values near one indicate favorable separation; negative values indicate a closer alternative.

A singleton lacks a within-group comparison, so this exercise assigns it zero. Including self-distance in a larger group would artificially reduce a and inflate the score.
