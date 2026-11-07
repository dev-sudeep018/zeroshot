# Estimate How Many Boxes Stay Empty

Empty boxes are not independent: placing an item into one box changes the composition of the remaining empty-box count. Summing only individual variances would ignore this dependence.

Pairwise empty probabilities supply the covariance correction. Deterministic edge cases, such as no placements or one placement, are useful checks on the cancellation in the variance formula.
