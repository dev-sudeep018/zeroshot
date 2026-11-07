# Turn Distances into Radial Similarities

The exponential maps zero distance to one and large distance toward zero. Multiplying squared distance by gamma sets the length scale of that decay.

A kernel matrix is not an attention probability matrix: its rows need not sum to one. Keeping cross-set shape explicit makes the same operation usable for training and evaluation rows.
