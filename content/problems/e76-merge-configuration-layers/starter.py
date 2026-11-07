def merge_config(layers):
    """Apply ordered shallow overrides while treating None as deletion."""
    # Replay layers in order and treat None as an operation, not a stored value.
    raise NotImplementedError("Implement the transformation")
