# Pool an Image into a Requested Grid

Adaptive pooling summarizes variable input sizes with a fixed output shape. Floor and ceiling boundaries can create overlapping bins when dimensions do not divide evenly.

The result is an average over each region rather than a resampled value at one coordinate. Consequently it behaves differently from bilinear interpolation and from disjoint block pooling.
