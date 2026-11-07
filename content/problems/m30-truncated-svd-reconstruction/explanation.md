# Compress a Matrix with Singular Values

The truncated singular-value expansion is a best rank-k approximation in squared Frobenius error. Its discarded squared singular values equal the residual energy.

Singular-vector signs cancel during reconstruction. A tie exactly at the truncation boundary is different: several reconstructed matrices can be equally good, so this contract rejects that ambiguous case.
