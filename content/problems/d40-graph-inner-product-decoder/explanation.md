# Reconstruct Edge Probabilities from Node Embeddings

The score matrix is symmetric, so this decoder cannot independently represent two directions of an edge. Orthogonal node embeddings produce probability one half, not zero.

Every diagonal score is a squared norm. The resulting self-pair probability is at least one half; applications that omit self-edges must handle that in their data or loss rather than silently altering this decoder.

Extracted and ported the upstream graph-autoencoder inner-product decoder to NumPy with stable sigmoid branches. The upstream randomly initialized two-layer encoder is deliberately outside this supplied-embedding contract.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/gae.py
