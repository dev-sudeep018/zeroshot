# Turn Image Windows into Matrix Rows

The patch matrix makes local receptive fields explicit. Multiplying its rows by flattened kernel weights produces the corresponding valid convolution outputs.

Overlapping patches duplicate image values in this representation. That duplication can increase memory use even though a direct convolution could reuse the original pixels.
