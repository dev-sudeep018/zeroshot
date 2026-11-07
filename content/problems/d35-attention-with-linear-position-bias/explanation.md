# Bias Attention toward Nearby Positions

With zero content scores, the attention weights depend only on distance and the supplied slope. At an edge, fewer positions exist on one side, so normalization still uses the available keys.

A zero slope recovers ordinary bidirectional scaled dot-product attention. The distance bias does not prevent future-token access; a causal model would need an additional mask.

Adapted the upstream bidirectional ALiBi attention to explicit head-shaped NumPy arrays and caller-provided slopes. Removed learned projections and the fixed upstream slope schedule.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/alibi.py
