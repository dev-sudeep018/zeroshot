# Differentiate a Spatial Cross-Correlation

An interior pixel influences several outputs, so its derivative sums their contributions. A kernel coefficient likewise influences every valid output location.

The single-channel contract exposes the adjoint calculation directly. Finite differences check both operands independently.
