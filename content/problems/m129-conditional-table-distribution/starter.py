import numpy as np


def condition_joint_columns(joint, selected):
    """Restrict a joint probability table to an event and return event probability and conditional row distribution."""
    # First: Sum the selected cells separately within each row.
    # Then: Normalize these row totals by their combined event mass, not by each original row sum.
    raise NotImplementedError("Complete the calculation and input checks")
