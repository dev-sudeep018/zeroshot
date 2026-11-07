def schema_issues(records, required, allowed):
    """Report missing and unexpected fields per record without dropping rows."""
    # Compare key sets; required-field presence does not depend on value
    # truthiness.
    raise NotImplementedError("Implement the transformation")
