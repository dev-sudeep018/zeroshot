# Fold Evaluation Batch Normalization into a Linear Layer

Fixed normalization is an affine transform, so composing it with a linear layer gives another affine transform. Folding avoids a separate normalization operation during evaluation.

The equivalence depends on fixed statistics. Recomputing mean and variance from each input batch would make the transform input-dependent and would not permit this same fold.
