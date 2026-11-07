def sessionize(timestamps, timeout):
    """Start a new session only when the sorted timestamp gap strictly exceeds a timeout."""
    # Compare consecutive events rather than measuring from the first event in a
    # session.
    raise NotImplementedError("Implement the transformation")
