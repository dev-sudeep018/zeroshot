# Average Loss over Real Tokens Only

A token-level mean gives each observed token equal weight even when sequence lengths differ. Dividing by padded area would make loss artificially smaller for batches with more padding.

Stable log-sum-exp avoids overflow and protects confidently wrong predictions from probability underflow. The result remains finite even for large positive and negative logits.
