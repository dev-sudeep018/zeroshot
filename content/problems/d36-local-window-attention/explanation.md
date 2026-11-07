# Limit Attention to a Local Window

Locality can make a distant change invisible to a single layer. Multiple stacked layers can propagate information farther, but this exercise evaluates one attention operation.

The reference processes each local slice directly. The lesson tests the neighborhood and normalization semantics and makes no measured runtime claim.

Ported the upstream bidirectional radius mask to NumPy local slices, avoiding a full score matrix in the reference. Kept the source’s two-sided window rather than silently adding causality.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/sliding_window.py
