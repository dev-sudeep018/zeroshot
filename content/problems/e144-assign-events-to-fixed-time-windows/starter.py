def fixed_windows(timestamps, width, origin):
    """Aggregate event counts into half-open integer windows anchored at a supplied origin."""
    # Floor division handles negative offsets correctly; truncation toward zero
    # does not.
    raise NotImplementedError("Implement the transformation")
