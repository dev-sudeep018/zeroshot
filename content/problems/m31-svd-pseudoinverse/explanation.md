# Solve Rank Deficiency with a Pseudoinverse

The pseudoinverse reverses each retained singular direction and leaves discarded directions at zero. Multiplying it by a target gives the minimum-norm least-squares solution under that cutoff.

The cutoff is relative to the largest singular value, so multiplying a matrix by a common nonzero scale preserves which directions survive. Equality with the threshold is deliberately discarded.
