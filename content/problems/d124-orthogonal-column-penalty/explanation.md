# Differentiate an Orthogonality Penalty

The penalty treats unit length and independence as one matrix objective. Its gradient moves columns in response to both their norms and their pairwise correlations.

When columns outnumber the ambient dimension, they cannot all be orthonormal. The function still provides a well-defined optimization objective rather than rejecting the rectangular matrix.
