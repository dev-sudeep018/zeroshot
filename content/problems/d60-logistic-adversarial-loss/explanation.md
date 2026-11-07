# Separate Discriminator and Generator Objectives

The discriminator pushes real scores upward and fake scores downward. The non-saturating generator objective pushes fake scores upward without changing real logits.

These forward losses do not imply a complete training loop. During actual updates the appropriate model parameters and gradient routes must be selected.
