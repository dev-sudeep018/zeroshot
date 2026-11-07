# Construct a Transposed Convolution by Scattering

Segments can reinforce or cancel where they overlap. Assignment instead of addition silently loses earlier contributions.

The shape follows the transpose of a valid strided cross-correlation matrix. It cannot generally recover information lost in the forward operation.
