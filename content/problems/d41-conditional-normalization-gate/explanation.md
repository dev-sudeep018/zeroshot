# Control a Normalized Branch with a Gate

A gate of zero closes this branch even if the conditioning shift is nonzero. A constant token has zero normalized features and therefore exposes only gate\*shift.

This adapts the upstream modulation equation to supplied parameters. It is not an entire AdaLN-Zero transformer block, and it does not include the upstream conditioning projection.
