def downstream_impact(dependencies, changed):
    """Return all downstream components affected by changed IDs, excluding seeds from results."""
    # Propagate impact along prerequisite-to-dependent edges, not in the reverse
    # direction.
    raise NotImplementedError("Implement the transformation")
