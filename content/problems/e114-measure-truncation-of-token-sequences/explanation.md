# Measure Truncation of Token Sequences

Truncation makes variable-length examples fit a bounded model input. Recording what was dropped helps audit whether important context is systematically lost.

The metadata is aligned with input rows, so empty sequences remain visible. A zero limit is meaningful: it removes every token while preserving the batch structure.
