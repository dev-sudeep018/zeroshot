# Keep the Identity Path during Backpropagation

When all branch activations are negative, the identity path still carries upstream. Masking both routes incorrectly eliminates that gradient.

Upstream already differentiates the final objective with respect to y. This operation neither averages it nor introduces a new loss.
