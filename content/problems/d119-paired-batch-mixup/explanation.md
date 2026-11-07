# Interpolate Training Examples and Their Labels Together

Pairwise interpolation encourages the model to behave smoothly between training examples. Soft labels express the same mixture used to construct the input.

Pair selection and coefficient sampling are separate policies. Supplying them explicitly makes this operation deterministic and lets tests catch mismatches between feature and label pairing.
