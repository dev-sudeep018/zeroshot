# Give Each Class Equal Total Training Weight

Frequency-balanced sample weights change the contribution of each class without duplicating observations. Scaling the weights to mean one keeps their overall magnitude interpretable.

Requiring every declared class to appear prevents division by zero. Equal total weight across classes is the defining invariant, not equal weight across samples.
