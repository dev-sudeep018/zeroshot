# Compose Residual Attention across Layers

Multiplying mixing matrices accumulates indirect token routes across layers. Adding the identity includes a simplified residual route that preserves a token’s own representation.

Rollout is an attention-based attribution approximation. It ignores nonlinearities, value projections, and gradient effects, so it should not be presented as a complete causal explanation of model output.
