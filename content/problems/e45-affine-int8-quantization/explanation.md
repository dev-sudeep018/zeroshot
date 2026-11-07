# Quantize with an Affine Zero Point

Affine quantization separates the spacing between representable real values from the integer code assigned to real zero. This supports asymmetric real ranges.

Saturation is distinct from rounding error: once a value crosses the representable range, changing it further leaves its integer code fixed. The lesson uses supplied calibration parameters rather than fitting them.
