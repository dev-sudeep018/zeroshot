# Inspect a Clipped Policy Objective

For a positive advantage, increasing the action probability beyond the upper clip boundary stops improving this surrogate. For a negative advantage, reducing it below the lower boundary stops improving the surrogate.

The minimum chooses the less optimistic term for either sign. Simply clipping every ratio and then averaging fails on the other side of the interval.

Ported the upstream clipped surrogate to NumPy with bounded log-ratio validation. Autograd detachment and full PPO training are outside this forward-only contract.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/ppo_loss.py
