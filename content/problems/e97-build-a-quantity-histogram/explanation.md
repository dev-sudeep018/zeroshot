# Build a Quantity Histogram

Explicit bucket boundaries turn raw quantities into a stable reporting schema. Keeping empty bins means reports remain comparable even when some ranges have no observations.

Boundary equality belongs to the lower indexed bucket under this contract. A conservation check is that the sum of counts equals the number of input values.
