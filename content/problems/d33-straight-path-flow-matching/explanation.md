# Follow a Straight Noise-to-Data Path

Changing time moves the point along the segment, but it does not change the target velocity for fixed endpoints. A model prediction would usually depend on that point and time; here it is supplied explicitly.

The mean includes both the batch and feature axes. Summing feature errors before averaging the batch introduces an extra factor of D.

Adapted the upstream velocity MSE and added an inspectable straight-path interpolation. Inputs and outputs are NumPy arrays, and no trained generative model is implied.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/flow_matching.py
