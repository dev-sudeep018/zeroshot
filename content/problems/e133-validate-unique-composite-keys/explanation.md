# Validate Unique Composite Keys

Composite keys identify rows using several fields together. A repeated value in one column is acceptable when the full combination remains unique.

Tuple keys preserve component boundaries. String concatenation with a delimiter can produce collisions when that delimiter already occurs in source values.
