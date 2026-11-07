def canonical_json(value):
    """Produce deterministic compact JSON with sorted object keys and finite numbers only."""
    # Sort keys recursively through the serializer, but never sort array items.
    raise NotImplementedError("Implement the transformation")
