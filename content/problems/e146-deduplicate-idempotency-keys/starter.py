def idempotent_accepts(keys, capacity):
    """Replay request keys with a bounded seen-key history and return accepted indices."""
    # Only accepted requests enter the FIFO history.
    raise NotImplementedError("Implement the transformation")
