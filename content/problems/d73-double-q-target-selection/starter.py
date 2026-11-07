import numpy as np

def double_q_targets(rewards, online_next, target_next, terminated, discount):
    """Select actions using the online estimates, then look up those actions in the target estimates to construct a batch of bootstrap targets."""
    raise NotImplementedError("Begin with the worked examples")
