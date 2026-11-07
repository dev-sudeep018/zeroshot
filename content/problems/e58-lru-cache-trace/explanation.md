# Trace Least-Recently-Used Eviction

LRU approximates temporal locality: recently accessed keys are retained in preference to older ones. A hit must refresh recency or the policy becomes insertion-order eviction.

This list-based implementation makes state transitions transparent and has linear lookup cost. A production cache can combine a dictionary with a linked order structure for constant-time operations.
