# Advance a Diagonal State-Space Memory

Restricting decay to nonpositive values prevents exponential growth of the retained memory. The input term still depends linearly on the time step.

The port exposes state and readout arrays directly. It follows the upstream exp(delta*A), delta*B convention rather than an exact zero-order-hold input integral.
