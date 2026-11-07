# Reverse One Deterministic Diffusion Step

The earlier diffusion state has at least as much retained signal as the current state. Reversing that ordering would move toward more noise, outside this lesson’s update contract.

An exact predicted noise reconstructs the clean signal used in a synthetic forward process. A real denoiser can be wrong; the formula does not guarantee clean predictions.

Ported the upstream eta-zero DDIM equation and exposed its clean estimate alongside the previous sample. Added an explicit positive retention floor and direction checks.

Adapted code source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/ddim_step.py
