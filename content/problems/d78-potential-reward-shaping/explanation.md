# Inspect Potential-Based Reward Shaping

Summing the shaping terms along a discounted trajectory cancels intermediate potentials. The remaining terms depend on the initial potential and the final boundary.

For a terminal trajectory with the defined zero final potential, the shaped discounted return differs from the original by minus the initial potential. This explains why terminal conventions cannot be omitted.

Conceptual reading: https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf
