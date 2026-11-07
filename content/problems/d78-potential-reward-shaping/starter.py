import numpy as np

def shape_rewards(rewards, potentials, next_potentials, terminated, discount):
    """Add the potential-based shaping term to each reward. Inspect why the current-state potential is subtracted even on a terminal transition."""
    raise NotImplementedError("Begin with the worked examples")
