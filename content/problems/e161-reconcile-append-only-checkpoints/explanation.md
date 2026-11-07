# Reconcile Append-Only Checkpoints

A checkpoint records a contiguous prefix of completed work. Concurrent workers may finish later items while an earlier item is still missing.

Keeping later acknowledgments pending allows the frontier to advance once the gap closes. Ignoring old acknowledgments makes replayed completion events harmless.
