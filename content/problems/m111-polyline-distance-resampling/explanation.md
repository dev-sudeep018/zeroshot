# Sample a Path by Traveled Distance

Equal spacing in vertex index is not equal spacing along a path when segments have different lengths. Cumulative geometric distance provides the coordinate needed for uniform travel.

Repeated vertices add no distance and should not create division by zero. Endpoint handling and right-sided segment lookup make such repetitions harmless while preserving the original path geometry.
