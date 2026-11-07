# Normalize Scores over Every Label Sequence

The log partition includes all paths, even those with poor scores. Replacing log-sum-exp with max computes a best-path score and loses normalization mass.

Transition orientation is part of the model. Transposing it changes the score of an asymmetric chain.
