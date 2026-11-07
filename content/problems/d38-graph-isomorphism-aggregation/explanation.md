# Distinguish Graph Neighborhoods with Sum Aggregation

The self coefficient 1+epsilon controls how the node’s own features enter the aggregate. The zero-diagonal contract prevents accidental double counting through the adjacency matrix.

Changing a sum to a mean removes neighborhood-count information. This lesson demonstrates the layer calculation; it does not claim every parameter choice distinguishes every pair of graphs.

Ported the upstream GIN sum-and-MLP equation to NumPy with explicit edge direction, supplied weights and strict shapes. Kept the final output linear and epsilon unrestricted in sign.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/gin_layer.py
