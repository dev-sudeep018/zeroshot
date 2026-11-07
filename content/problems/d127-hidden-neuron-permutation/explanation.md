# Reorder Hidden Neurons without Changing a Network

This parameter symmetry creates multiple parameter arrays for the same network function. Equality of predictions therefore does not imply equality of individual hidden-neuron weights.

The argument relies on applying the same elementwise nonlinearity to every hidden coordinate. A coordinate-specific operation would need its own parameters permuted as well.
