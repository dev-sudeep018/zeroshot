def normalize_resource_path(path):
    """Resolve dot and dot-dot path segments while rejecting traversal above the root."""
    # Treat segments as a stack; .. removes the most recent normal segment.
    raise NotImplementedError("Implement the transformation")
