# Build Deterministic Holdout by ID Hash

Stable holdout assignment helps preserve evaluation membership as a dataset grows. Every ID is classified independently, so reordering a file cannot change its membership.

Hash buckets approximate a requested proportion; they do not guarantee exact split sizes. Identical subjects must share an ID if leakage between their records must be prevented.
