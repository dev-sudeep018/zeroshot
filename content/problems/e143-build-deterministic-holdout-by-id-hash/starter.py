def hash_holdout(ids, holdout_buckets):
    """Assign each distinct string ID to a stable split using a documented SHA-256 bucket."""
    # Hash each ID separately so adding a new ID cannot move an old one.
    raise NotImplementedError("Implement the transformation")
