# Distribute Average-Pooling Gradients

Center pixels of overlapping windows receive more contributions than corners. The pattern follows coverage rather than pixel values.

This adjoint does not need the original image because averaging has a constant derivative within each window.
