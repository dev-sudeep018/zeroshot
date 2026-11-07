# Route Tokens into a Mixture of Expert Outputs

With k=1 the selected output is returned exactly. With larger k, each token receives a convex combination of its selected expert vectors, and unselected expert outputs cannot affect it.

Stable index-order ties keep the routing deterministic. This contract chooses an exact count even when several experts share the boundary score.

Adapted the upstream top-k gate and weighted expert mixture to NumPy using supplied expert outputs. Removed learned router/expert layers and made exact index-order tie handling explicit.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/moe.py
