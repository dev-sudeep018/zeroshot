# Choose a Gini Decision Split

Each candidate is judged by the impurity remaining after the split, weighted by child sample counts. An unweighted average could overvalue a tiny pure child.

Thresholds inside a gap create the same partition, so midpoints give a reproducible representative. Ties are resolved explicitly to keep training deterministic.
