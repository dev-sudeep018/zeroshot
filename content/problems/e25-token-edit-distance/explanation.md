# Measure Token Edit Distance

Each dynamic-programming cell stores the best cost for two prefixes. Optimal edit sequences can be extended from one of three shorter prefix pairs.

Two rows are sufficient because the recurrence only uses the current row and the previous row. The runtime is O(LR), and memory can be kept linear.
