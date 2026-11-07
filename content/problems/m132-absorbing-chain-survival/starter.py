import numpy as np


def absorption_trace(initial, transient, steps):
    """Propagate transient mass through a substochastic matrix and report per-step absorption probabilities."""
    # First: Missing mass in a transition row represents leaving the transient state space permanently.
    # Then: Compare total mass before and after each multiplication, and retain the unnormalized state vector.
    raise NotImplementedError("Complete the calculation and input checks")
