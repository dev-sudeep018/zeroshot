import numpy as np

def n_step_targets(rewards, values, terminated, discount, steps):
    """Construct a target for every starting transition. Keep track of how many rewards were consumed so the bootstrap receives the correct discount power."""
    raise NotImplementedError("Begin with the worked examples")
