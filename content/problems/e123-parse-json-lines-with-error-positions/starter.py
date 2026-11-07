def parse_json_lines(text):
    """Read one JSON object per nonblank line and return valid objects plus rejected line numbers."""
    # Catch parsing errors per line so one bad record does not discard later
    # records.
    raise NotImplementedError("Implement the transformation")
