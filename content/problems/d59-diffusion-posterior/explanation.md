# Recover the Conditional Diffusion Posterior

Conditioning on the clean endpoint produces a different update from a denoiser prediction. The posterior variance vanishes at the first forward step.

The two mean coefficients need not add to one. They come from Gaussian conditioning rather than an ordinary convex interpolation.
