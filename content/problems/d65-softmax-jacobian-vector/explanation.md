# Apply a Softmax Jacobian without Building It

The Jacobian is diag(p)-p\*p.T. Distributing its product gives an elementwise expression with one weighted reduction per row.

Every output direction sums to zero because the original probabilities must continue to sum to one. The Jacobian is symmetric, so the same formula also applies a vector-Jacobian product.
