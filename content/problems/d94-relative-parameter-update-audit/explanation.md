# Compare Update Size with Parameter Scale

Relative update size provides a scale-aware training diagnostic. It can reveal blocks that move disproportionately even when their raw gradients look similar.

The floor makes zero-weight blocks finite and exposes the selected reference scale. A large ratio is a prompt for investigation, not a universal rule that the update is incorrect.
