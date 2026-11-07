# Ignore Errors inside a Tolerance Band

An epsilon-insensitive loss ignores deviations that lie within a practical tolerance. Larger deviations are penalized linearly by only the amount beyond that tolerance.

The loss is nondifferentiable at the band edges. Defining the subgradient there as zero makes the implementation deterministic and separates this loss from smooth quadratic penalties.
