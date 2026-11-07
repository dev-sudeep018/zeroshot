def advance_checkpoint(committed, acknowledged):
    """Advance a contiguous completed offset only across gap-free acknowledged sequence IDs."""
    # Membership in a set handles duplicate and out-of-order acknowledgments.
    raise NotImplementedError("Implement the transformation")
