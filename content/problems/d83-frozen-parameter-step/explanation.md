# Respect Frozen Parameters during SGD

Freezing is an optimizer choice, separate from gradient computation. Keeping masked coordinates unchanged supports transfer learning and staged training.

The delta output makes the choice observable. Zero learning rate and an all-frozen mask both give zero changes without modifying the original arrays.
