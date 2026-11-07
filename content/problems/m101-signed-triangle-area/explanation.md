# Measure Triangle Orientation and Size

A signed area retains the order in which vertices are visited. Exchanging two vertices flips the orientation while preserving geometric size.

This cross-product calculation is useful in polygon algorithms because it distinguishes left turns, right turns and collinearity without computing angles. The sign convention must remain consistent across those algorithms.
